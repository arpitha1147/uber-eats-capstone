import pandas as pd
import numpy as np
from faker import Faker
import os

fake = Faker('en_IN')
Faker.seed(42)
np.random.seed(42)

NUM_CUSTOMERS = 2000
NUM_RESTAURANTS = 200
NUM_ORDERS = 10000

# 1. Customers
customers = pd.DataFrame({
    'customer_id': range(1, NUM_CUSTOMERS + 1),
    'age': np.random.randint(18, 60, NUM_CUSTOMERS),
    'segment': np.random.choice(['Student', 'Professional', 'Family'], NUM_CUSTOMERS)
})

# 2. Restaurants
restaurants = pd.DataFrame({
    'restaurant_id': range(1, NUM_RESTAURANTS + 1),
    'category': np.random.choice(['North Indian', 'South Indian', 'Chinese', 'Biryani', 'Fast Food'], NUM_RESTAURANTS),
    'rating': np.random.uniform(2.5, 5.0, NUM_RESTAURANTS).round(1)
})

# 3. Orders & Deliveries
orders = pd.DataFrame({
    'order_id': range(1, NUM_ORDERS + 1),
    'customer_id': np.random.choice(customers['customer_id'], NUM_ORDERS),
    'restaurant_id': np.random.choice(restaurants['restaurant_id'], NUM_ORDERS),
    'order_timestamp': [fake.date_time_between(start_date='-1y', end_date='now') for _ in range(NUM_ORDERS)],
    'order_amount': np.random.uniform(150, 1500, NUM_ORDERS).round(2),
    'num_items': np.random.randint(1, 8, NUM_ORDERS),
    'distance_km': np.random.uniform(1.0, 15.0, NUM_ORDERS).round(2),
    'weather': np.random.choice(['Clear', 'Rain', 'Fog'], NUM_ORDERS, p=[0.7, 0.2, 0.1]),
    'traffic': np.random.choice(['Light', 'Moderate', 'Heavy'], NUM_ORDERS, p=[0.4, 0.4, 0.2]),
    'prep_time_min': np.random.randint(10, 35, NUM_ORDERS),
    'status': np.random.choice(['Delivered', 'Cancelled'], NUM_ORDERS, p=[0.92, 0.08])
})

orders['delivery_time_min'] = (orders['distance_km'] * 2.5) + np.where(orders['traffic'] == 'Heavy', 15, 0) + np.where(orders['weather'] == 'Rain', 10, 0) + np.random.randint(5, 12, NUM_ORDERS)
orders['delivery_time_min'] = orders['delivery_time_min'].round(0)
orders['tip_amount'] = np.where(orders['status'] == 'Delivered', (orders['order_amount'] * np.random.uniform(0, 0.15, NUM_ORDERS)).round(2), 0)

# 4. Reviews
delivered_orders = orders[orders['status'] == 'Delivered'].copy()
delivered_orders['review_score'] = np.random.choice([1, 2, 3, 4, 5], len(delivered_orders), p=[0.1, 0.1, 0.2, 0.3, 0.3])
delivered_orders['review_text'] = np.where(
    delivered_orders['review_score'] >= 4,
    np.random.choice(["Great food", "Fast delivery", "Loved it", "Nice packaging"], len(delivered_orders)),
    np.random.choice(["Cold food", "Late delivery", "Bad taste", "Missing items"], len(delivered_orders))
)
reviews = delivered_orders[['order_id', 'customer_id', 'restaurant_id', 'review_score', 'review_text']]

# Save datasets
os.makedirs('data', exist_ok=True)
customers.to_csv('data/customers.csv', index=False)
restaurants.to_csv('data/restaurants.csv', index=False)
orders.to_csv('data/orders.csv', index=False)
reviews.to_csv('data/reviews.csv', index=False)

print("Data generated successfully in the 'data' folder.")