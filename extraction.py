import requests
import json
import logging
import csv
def extract_data():
        with open('./source_and_target/config.json') as config_file:
            config = json.load(config_file)
        
        
# Fetch data
        response = requests.get(config['source'])
        if response.status_code == 200:
            data = response.json()
            logging.info("Data fetched successfully")
        logging.info("Data fetched successfully")
        with open('customers.csv','w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            logging.info("Data written to customers.csv successfully")
        return './customers.csv'
