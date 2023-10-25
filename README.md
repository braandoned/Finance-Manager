---

# Finance Manager

Welcome to the **Finance Manager** project! This tool is designed to help you manage and monitor your financial transactions with ease. It will read your CSV files, auto-categorize each transaction, and rename them to be more readable. The refined data is then posted to a dashboard on Google Sheets, allowing you to get a clear view of your financial situation.

## Features

- **CSV File Reading**: Quickly import your transaction data from CSV files.
- **Auto-Categorization**: The tool will automatically sort your transactions into categories.
- **Transaction Renaming**: All transactions are renamed to make them more understandable.
- **Google Sheets Dashboard**: All refined data is posted to a Google Sheets dashboard, giving you a real-time overview of your finances.

## Prerequisites

- **Gspread Setup**:
  - Ensure you have `gspread` located in the path: `C:\Users\YOURUSERNAME\AppData\Roaming\gspread`.
  - You should have a file named `service_account.json` within this directory to authenticate with Google services.
  - refer to [YouTube video tutorial](https://www.youtube.com/watch?v=IbdgcUqWSeo&t) for more information.

## Getting Started

1. **Clone the repository**:
   ```
   git clone https://github.com/braandoned/Finance-Manager.git
   ```

2. **Install the necessary packages**:
   ```
   pip install gspread
   ```

3. **Set up your Google Sheets Dashboard**: 
   - Create a copy of the [dashboard template](https://docs.google.com/spreadsheets/d/1nuhEEvNLrfac2Su3xNmcLQcDiln-J5D8wvZW3S8U8rk/copy).
   - Ensure that you share your copied Google Sheet with the email address found in your `service_account.json` to allow the script to access and update your sheet.

4. **Run the script**:
   ```
   python main.py
   ```

## Dashboard Template

To use the dashboard with this project, make sure you use the provided template. You can find and copy the dashboard template [here](https://docs.google.com/spreadsheets/d/1nuhEEvNLrfac2Su3xNmcLQcDiln-J5D8wvZW3S8U8rk/copy).

## References

For a deeper understanding and walkthrough, check out this [YouTube video tutorial](https://www.youtube.com/watch?v=IbdgcUqWSeo&t).

---
