import gspread
import csv
import time

# Global variables
MONTH = "january"
transactions = []

# Mapping to simplify transaction names
NAME_MAPPING = {
    "microsoft": {"Microsoft"},
    "amazon purchase": {"amzn mktp", "amazon.com"},
    "coinbase": {"Coinbase"},
    "creditcard": {"INTERNET PAYMENT", "Payment Thank You-Mobile"},
    # Add more mappings...
}

# Mapping to categorize transactions
CATEGORY_MAPPING = {
    "Entertainment": {"microsoft", "example1", "example2"},
    "Subscription": {"amazon prime"},
    "shopping":{"amazon purchase"},
    # Add more categories...
}

# Process each row from the CSV file
def process_row(row, file_type):
    date = row[0]
    name = row[2]

    cleaned_name = remove_punc(name)
    simplified_name = simplify_name(cleaned_name)
    category = get_category(simplified_name)

    if simplified_name == "creditcard":
        return None

    # Process based on file type
    if file_type == "chase":
        date = row[1]
        name = row[2]
        amount = float(row[3])
        if amount > 0:
            category = "Income"
        transaction = (date, simplified_name, amount, category)
        print(transaction)
        transactions.append(transaction)

    elif file_type == "chase_credit":
        amount = float(row[5])
        transaction = (date, simplified_name, amount, category)
        print(transaction)
        transactions.append(transaction)
        if amount > 0:
            return None

    elif file_type == "discover_credit":
        amount = float(row[3]) * -1
        transaction = (date, simplified_name, amount, category)
        print(transaction)
        transactions.append(transaction)
        if amount > 0:
            return None

    return date, simplified_name, amount, category

# Remove punctuation from string
def remove_punc(string):
    punc = "*"
    for ele in string:
        if ele in punc:
            string = string.replace(ele, " ")
    return string

# Simplify transaction names based on mapping
def simplify_name(name):
    for (keyword, replacements) in NAME_MAPPING.items():
        for replacement in replacements:
            if replacement.lower() in name.lower():
                return keyword
    return name

# Get category based on mapping
def get_category(name):
    name_lower = name.lower()
    for (category, category_keywords) in CATEGORY_MAPPING.items():
        if any(keyword.lower() in name_lower for keyword in category_keywords):
            return category
    return "other"

# Process transactions from a CSV file
def process_file(file_name, process_function, file_type):
    transactions = []
    skipFirst = 0
    with open(file_name, mode="r") as csv_file:
        if skipFirst == 0:
            skipFirst = 1
        else:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                transaction = process_function(row, file_type)
                if transaction:
                    transactions.append(transaction)
    return transactions

# Insert transactions into a Google Sheets worksheet
def insert_transactions_into_sheet(sheet, transactions):
    for transaction in transactions:
        sheet.insert_row([transaction[0], transaction[1], transaction[3], transaction[2]], 8)
        time.sleep(2)

# Main function
def main():
    # Authenticate and open the spreadsheet
    sa = gspread.service_account()
    sh = sa.open("PersonalFinance")
    wks = sh.worksheet(MONTH)

    # File paths
    fileDiscoverCredit = f"discoverCredit_{MONTH}.csv"
    fileChaseCredit = f"chaseCredit_{MONTH}.csv"
    fileChase = f"chase_{MONTH}.csv"
    transactions = []
    # Process transactions from different files
    transactions += process_file(fileDiscoverCredit, process_row, "discover_credit")
    transactions += process_file(fileChaseCredit, process_row, "chase_credit")
    transactions += process_file(fileChase, process_row, "chase")

    # Insert transactions into the worksheet
    insert_transactions_into_sheet(wks, transactions)

if __name__ == "__main__":
    main()
