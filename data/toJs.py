import csv
import json
from datetime import datetime

def convert_csv_to_js():
    CRYPTO = 'btc'
    # Input and output file paths
    input_file = f'{CRYPTO}.csv'
    output_file = f'{CRYPTO}.js'
    
    # Read CSV data
    data = []
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        
        for row in reader:
            if len(row) >= 2:
                # Extract date and price
                full_timestamp = row[0]
                price = row[1]
                
                # Parse the timestamp and extract just the date part
                try:
                    date_obj = datetime.strptime(full_timestamp, '%Y-%m-%d %H:%M:%S %Z')
                    date_only = date_obj.strftime('%Y-%m-%d')
                    
                    # Add to data array
                    data.append([date_only, float(price)])
                except (ValueError, TypeError):
                    print(f"Skipping row with invalid data: {row}")
    
    # Write to JavaScript file
    with open(output_file, 'w') as jsfile:
        jsfile.write(f'const {CRYPTO}Data = ')
        jsfile.write(json.dumps(data, indent=2))
        jsfile.write(';')
    
    print(f"Conversion complete. Data written to {output_file}")

if __name__ == "__main__":
    convert_csv_to_js()