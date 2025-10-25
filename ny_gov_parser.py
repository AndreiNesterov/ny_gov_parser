import requests
import pandas as pd

def display_10_records() -> None:
    '''
    Requesting the dataset 'n9v6-gdp6' from data.ny.gov and getting 10 records sorted by Date of incorporation;
    If no error, saves a table with records in an html file; if error, prints the error
    Returns none
    '''

    # Usings the dataset API; taken from:
    # (1) https://catalog.data.gov/dataset/active-corporations-beginning-1800 (Landing Page) -> 
    # (2) https://data.ny.gov/Economic-Development/Active-Corporations-Beginning-1800/n9v6-gdp6/about_data (Export -> API Endpoint -> SODA2)
    # Using SODA2 because it does not require authentication; we retrieve only 10 records, so it can be done without authentication;
    # SODA2 documentation: https://dev.socrata.com/docs/endpoints; order: https://dev.socrata.com/docs/queries/order.html; limit: https://dev.socrata.com/docs/queries/limit.html;

    updated = "No data" # default; when the data was last updated
    
    url = "https://data.ny.gov/resource/n9v6-gdp6.json"

    # retrieving the date when the records were last updated
    # in this dataset, all the records are updated at the same time; so retrieving a single record would be enough
    params_hidden = {
        "$select": ":*", # about system fields: https://dev.socrata.com/docs/system-fields.html
        "$limit": 1
    }
    response_hidden = requests.get(url, params=params_hidden)
    
    if response_hidden.status_code == 200:
        updated = response_hidden.json()[0][':updated_at']

    # retrieving 10 records
    params = {
        "$order": "initial_dos_filing_date DESC",
        "$limit": 10
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        ny_gov_data = response.json()

        # converting to df (if needed later, it can be easily converted to csv)
        # https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
        # the columns are inconsisted, there can be NaN values
        df_10_records = pd.json_normalize(ny_gov_data)

        # converting a df inti a scrollable HTML table
        html_table = df_10_records.to_html()

        with open("n9v6_gdp6_results.html", "w", encoding="utf-8") as f:
            f.write(f'<h1>Active Corporations in the state of New York</h1><p>Displaying 10 records sorted by the date of incorporation.</p><p>This data was last updated on: {updated}</p><div style="overflow-x:auto;">{html_table}</div>')
        print("The results are saved in the file 'n9v6_gdp6_results.html'. Open it in your browser.")
    else:
        print(f"Could not request the data: {response.status_code}")

    return None

if __name__ == "__main__":
    display_10_records()