# financial-analysis

This is a simple project to practice concepts of:
- Web scraping;
- Working with APIs;
- Json objects;
- Database objects; and
- Extract, transform and load (ETL) process.

The goal is to find the top 50 banks by market capitalization, and read it in EUR$. In order to do that, web scraping is used to gather data from wikipedia, and an API call is used to get currency conversion values. The first file is saved as a .json file, and the second as .csv.

ETL process then begins, and is logged throughout its course. The result dataset is then saved as a .csv file.

## Usage

In order to reproduce results, one must execute the bash script "setup.sh" in a linux environment. This script will be responsible for creating and activating a virtual environment, installing dependencies, and also for executing required files to obtain desired results.
