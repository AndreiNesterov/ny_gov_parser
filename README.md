# Demo: A parser for the Active Corporation dataset by NY Open Data

This Python script retrieves and displays 10 records from the dataset "Active Corporations: Beginning 1800" by the New York State Department of State using [the dataset API](https://data.ny.gov/d/n9v6-gdp6).

> [!Important note on "the last 10 additions to the register"]

> When this dataset is updated by the publisher, all its records are created and updated at the same time, as the system SODA fields **:updated_at** and **:created_at** show (see [the SODA documentation](https://dev.socrata.com/docs/system-fields.html)). It results in all records having the same timestamp. So, it is impossible to determine what records were "the latest".

> Among the API fields of this dataset, there is only one containing a timestamp, which is **initial_dos_filing_date** (Initial DOS Filing Date), indicating when a company was incorporated. The script sorts the records by this field in descending order (from newest to oldest) and requests the first 10. 

> For example, in the version of the dataset from 22.10.2025, there were 1001 records with the same value of **initial_dos_filing_date**. So, the script displays the first 10 of these 1001 records sorted by this field. How exactly these records are sorted by default is unclear.

## Instructions

You can run the script using different tools. Here are 2 possible ways, depending on your preferences. To begin, clone this repository (save it locally on your machine). Make sure you have Python and dependencies (see requirements.txt) installed.

### Jupyter Notebook

If you have Jyputer Notebook installed, open ny_gov_parser.ipynb and run the cells.

### Terminal

1. Navigate to your local script directory

```
cd **here goes your full path to ny_gov_parser**
```

2. Run the script

```
python ny_gov_parser.py
```

The 10 records will be saved in the file **n9v6_gdp6_results.html**, which is in the same directory as the script. Open it in your browser. To get an updated version of the records, run the script again. The file will be overwritten.

### Sample of screen output

See n9v6_gdp6_results.html.

### References

* [Documentation of the dataset API](https://dev.socrata.com/foundry/data.ny.gov/n9v6-gdp6)
* [General SODA API documentation](https://dev.socrata.com/docs/queries/limit.html)