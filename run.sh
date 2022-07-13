source .env/bin/activate
python3 ./src/apijson.py
python3 ./src/webscraping.py
python3 ./src/__init__.py
cat ./data/logfile.txt
deactivate