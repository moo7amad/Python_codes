This script reads company and user data from JSON files, processes it, and generates a detailed report of token top-ups for active users within each company.

Features:
- Loads and merges company and user data (companies.json and users.json)
- Filters for active users only
- Groups users by their associated company
- Calculates token top-ups per user and totals per company
- Differentiates between users who have been emailed and those who haven’t
- Writes a structured report to output.txt
- Includes error handling for file loading and processing steps

File Structure:
- companies.json: Contains company information including id, name, top_up, and email_status
- users.json: Contains user details such as first_name, last_name, email, company_id, tokens, active_status, and email_status
- output.txt: The generated report file listing company details, user email statuses, and updated token balances

Requirements:
- Python 3.x
- pandas

Install required packages using:
pip install pandas

To get the output, simply run the script:
python challenge.py

P.S Ensure that companies.json and users.json are in the same directory as the script.
