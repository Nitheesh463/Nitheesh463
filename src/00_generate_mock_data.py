import csv
import random
from datetime import datetime, timedelta
import os

def generate_mock_sales_data(num_rows=10000):
    # Set up the path to save the CSV
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_dir = os.path.join(base_dir, "data", "raw")
    output_file = os.path.join(raw_dir, "raw_sales.csv")
    
    # Ensure the directory exists
    os.makedirs(raw_dir, exist_ok=True)
    
    # Define 30 diverse base records to rotate through
    base_records = [
        {"customer_id": 5001, "category": "Electronics", "quantity": 1, "price": 899.99},
        {"customer_id": 5002, "category": "Clothing", "quantity": 2, "price": 25.50},
        {"customer_id": 5003, "category": "Home", "quantity": 4, "price": 15.00},
        {"customer_id": 5004, "category": "Clothing", "quantity": 1, "price": 45.00},
        {"customer_id": 5005, "category": "Sports", "quantity": 2, "price": 120.00},
        {"customer_id": 5006, "category": "Home", "quantity": 1, "price": 250.00},
        {"customer_id": 5007, "category": "Electronics", "quantity": 3, "price": 15.99},
        {"customer_id": 5008, "category": "Clothing", "quantity": 5, "price": 10.00},
        {"customer_id": 5009, "category": "Sports", "quantity": 1, "price": 450.00},
        {"customer_id": 5010, "category": "Home", "quantity": 2, "price": 45.50},
        {"customer_id": 5011, "category": "Beauty", "quantity": 3, "price": 12.99},
        {"customer_id": 5012, "category": "Toys", "quantity": 1, "price": 59.99},
        {"customer_id": 5013, "category": "Electronics", "quantity": 1, "price": 1200.00},
        {"customer_id": 5014, "category": "Sports", "quantity": 4, "price": 18.50},
        {"customer_id": 5015, "category": "Beauty", "quantity": 2, "price": 35.00},
        {"customer_id": 5016, "category": "Clothing", "quantity": 1, "price": 85.00},
        {"customer_id": 5017, "category": "Toys", "quantity": 5, "price": 9.99},
        {"customer_id": 5018, "category": "Home", "quantity": 1, "price": 199.99},
        {"customer_id": 5019, "category": "Electronics", "quantity": 2, "price": 45.00},
        {"customer_id": 5020, "category": "Sports", "quantity": 1, "price": 89.00},
        {"customer_id": 5021, "category": "Beauty", "quantity": 1, "price": 110.00},
        {"customer_id": 5022, "category": "Clothing", "quantity": 3, "price": 22.50},
        {"customer_id": 5023, "category": "Toys", "quantity": 2, "price": 15.00},
        {"customer_id": 5024, "category": "Home", "quantity": 4, "price": 12.50},
        {"customer_id": 5025, "category": "Electronics", "quantity": 1, "price": 350.00},
        {"customer_id": 5026, "category": "Sports", "quantity": 2, "price": 65.00},
        {"customer_id": 5027, "category": "Beauty", "quantity": 4, "price": 8.99},
        {"customer_id": 5028, "category": "Clothing", "quantity": 1, "price": 120.00},
        {"customer_id": 5029, "category": "Toys", "quantity": 1, "price": 145.00},
        {"customer_id": 5030, "category": "Home", "quantity": 2, "price": 75.00}
    ]
    
    start_date = datetime(2023, 1, 1)
    
    print(f"Generating {num_rows} rows of mock data by rotating {len(base_records)} base records...")
    
    data = []
    
    for i in range(1, num_rows + 1):
        # Rotate through the base records using the modulo operator
        base_record = base_records[i % len(base_records)]
        
        # Generate random date
        random_days = random.randint(0, 365)
        order_date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
        
        customer_id = base_record["customer_id"]
        category = base_record["category"]
        quantity = base_record["quantity"]
        price = base_record["price"]
        
        # Intentionally inject some NULL/Empty values (about 3% of the time) to test silver layer cleaning
        if random.random() < 0.03:
            price = ""
        if random.random() < 0.02:
            category = ""
            
        row = [i, order_date, customer_id, category, quantity, price]
        data.append(row)
        
        # Intentionally inject duplicates (about 2% of the time) to test dropDuplicates()
        if random.random() < 0.02:
            data.append(row)
            
    # Write to CSV
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['order_id', 'order_date', 'customer_id', 'product_category', 'quantity', 'price'])
        writer.writerows(data)
        
    print(f"Successfully generated {len(data)} rows and saved to: {output_file}")

if __name__ == "__main__":
    generate_mock_sales_data(10000)