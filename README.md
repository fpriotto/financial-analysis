# financial-analysis

This is a simple project to practice concepts of:
- Web scraping;
- Working with APIs;
- Json objects;
- Database objects; and
- Extract, transform and load (ETL) process.

The goal is to find the top 50 banks by market capitalization, and read it in EUR$. In order to do that, web scraping is used to gather data from wikipedia, and an API call is used to get currency conversion values. The first file is saved as a .json file, and the second as .csv. A valid API key at [apilayer.com](https://apilayer.com/) is needed for the script to work.

ETL process then begins, and is logged throughout its course. The result dataset is saved as a .csv file.

## Usage

In order to reproduce results, one must install requirements running the setup script as shown:

```bash
bash setup.sh
```

Then, to reproduce results, issue the following command:

```bash
bash run.sh
```


This script will be responsible for creating and activating a virtual environment, installing dependencies, and also for executing required files to obtain desired results.
