import sys
from pathlib import Path
import json

# ensure project root on sys.path so top-level modules can be imported
sys.path.append(str(Path(__file__).resolve().parents[1]))

import extraction
import transorms as transforms
import loads as loadings
from logs import logs

def main():
    with open('./source_and_target/config.json') as config_file:
        config = json.load(config_file)

    data = extraction.extract_data()
    logs.info("Data extraction completed successfully")
    logs.info(f"Data {len(data)} records extracted")

    transformed_data = transforms.transform_data(data)
    logs.debug("Data transformation completed successfully")
    logs.info(f"Data transformed with {len(transformed_data)} records")

    loadings.load_data(transformed_data)
    logs.info("Data loading completed successfully")

if __name__ == "__main__":
    main()