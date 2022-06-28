# financial-analysis

This is a simple project to practice concepts of:
- Web scraping;
- Working with APIs;
- Json objects;
- Dadabase objects; and
- Extract, transform and load (ETL) process.

The goal is to find the top 50 banks by market capitalization, and read it in EUR$. In order to do that, web scraping is used to gather data from wikipedia, and an API call is used to get currency conversion values. The first file is saved as a .json file, and the second as .csv.

ETL process then begins, and is logged throughout its course. The result dataset is then saved as a .csv file.

## Usage

In order to reproduce results, one must execute separately files related to webscraping and API, adding its personal key to the last. Once that is done, run init and results should be as shown in the transformed_data.csv file in the data folder. The log file contains information about the ETL process.