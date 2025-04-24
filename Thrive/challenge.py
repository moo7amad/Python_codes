#import libraries
import json
import pandas as pd

# Load and convert JSON files to DataFrames
try:
    companies = pd.read_json('companies.json')
except Exception as e:
    print(f"Error reading companies.json: {e}")
    companies = pd.DataFrame()

try:
    users = pd.read_json('users.json')
except Exception as e:
    print(f"Error reading users.json: {e}")
    users = pd.DataFrame()

if not companies.empty and not users.empty:
    try:
        #Filter on active users and sort by company id and last name
        active_users = users[users["active_status"] == True].sort_values(by=['company_id', 'last_name'])

        # Merge the dataframes by company id
        company_lines = pd.merge(companies, active_users, right_on='company_id',left_on='id', how='right', suffixes=('_com', '_usr'))

        #Write the output file
        with open('output.txt', 'w') as file:
            for company_id, group in company_lines.groupby('company_id'):
                file.write("\n") 
                data = group.iloc[0] #put the data in an array
                user_count = len(group) #gives us the number of users by company
                
                #to handle in case top_up value is null or non mumeric
                top_up = data['top_up']
                if (pd.to_numeric(top_up, errors='coerce') == True):
                    top_up = 0
                
                total_top_up = top_up * user_count
                
                file.write(f"    Company Id: {company_id}\n")
                file.write(f"    Company Name: {data['name']}\n")

                #separate emailed users and non emailed users
                emailed_users = group[group['email_status_usr'] == True]
                non_emailed_users = group[group['email_status_usr'] == False]

                if(data['email_status_com'] == False):
                    file.write("    Users Emailed:\n")
                    file.write("    Users Not Emailed:\n")
                    users_list = group #to print the whole group list
                else:
                            file.write("    Users Emailed:\n")
                            for _, row in group.iterrows():
                                    #to handle in case token value is null or non mumeric
                                    tokens = row['tokens']
                                    if (pd.to_numeric(tokens, errors='coerce') == True):
                                        tokens = 0
                                    if(row['email_status_usr'] == True):
                                        file.write(f"       {row['last_name']} , {row['first_name']}, {row['email']}\n")
                                        file.write(f"           Previous Token Balance, {tokens}\n")
                                        new_balance = top_up+tokens
                                        file.write(f"           New Token Balance {new_balance}\n")

                            file.write("    Users Not Emailed:\n")
                            users_list = non_emailed_users #print only non emailed users
                
                for _, row in users_list.iterrows():
                    #to handle in case token value is null or non mumeric
                    tokens = row['tokens']
                    if (pd.to_numeric(tokens, errors='coerce') == True):
                        tokens = 0
                    file.write(f"       {row['last_name']}, {row['first_name']}, {row['email']}\n")
                    file.write(f"           Previous Token Balance, {tokens}\n")
                    file.write(f"           New Token Balance {tokens + top_up}\n")
                
                file.write (f"       Total amount of top ups for {data['name']}: {total_top_up}\n")
    except Exception as e:
        print(f"Error processing data: {e}")
else:
    print("DataFrames are empty, check input files.")
