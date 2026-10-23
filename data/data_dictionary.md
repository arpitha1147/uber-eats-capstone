
# Uber Eats Synthetic Data Dictionary

## 1. Customers (`customers.csv`)
* **customer_id**: Unique identifier for each customer.
* **age**: Age of the customer (18-60).
* **segment**: Customer category (Student, Professional, Family).

## 2. Restaurants (`restaurants.csv`)
* **restaurant_id**: Unique identifier for each restaurant.
* **category**: Cuisine type (North Indian, South Indian, Chinese, Biryani, Fast Food).
* **rating**: Average customer rating (2.5 to 5.0).

## 3. Orders (`orders.csv`)
* **order_id**: Unique identifier for the order.
* **customer_id**: ID of the customer who placed the order.
* **restaurant_id**: ID of the restaurant.
* **order_timestamp**: Date and time the order was placed.
* **order_amount**: Total bill amount in INR.
* **num_items**: Number of items in the order.
* **distance_km**: Delivery distance in kilometers.
* **weather**: Weather condition (Clear, Rain, Fog).
* **traffic**: Traffic condition (Light, Moderate, Heavy).
* **prep_time_min**: Time taken by the restaurant to prepare the food.
* **status**: Order status (Delivered, Cancelled).
* **delivery_time_min**: Total time taken for delivery.
* **tip_amount**: Tip given by the customer.

## 4. Reviews (`reviews.csv`)
* **order_id**: Unique identifier for the order.
* **customer_id**: ID of the customer who left the review.
* **restaurant_id**: ID of the reviewed restaurant.
* **review_score**: Rating given by the customer (1 to 5).
* **review_text**: Text feedback provided by the customer.