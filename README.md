
# Uber Eats Operational & Customer Intelligence System

An end-to-end operational and customer intelligence analytics platform built to extract actionable business insights, profile behavioral cohorts, and classify real-time sentiment from customer feedback.

---

## Project Architecture & Directory Structure

```text
uber-eats-capstone/
├── data/
│   ├── customers.csv              # Customer demographics and base profiles
│   ├── orders.csv                 # Transactional order logs
│   ├── restaurants.csv            # Restaurant partner profiles
│   ├── reviews.csv                # Customer feedback ratings and textual reviews
│   └── data_dictionary.md         # Schema and metadata definitions
├── notebooks/
│   ├── 01_customer_segmentation.ipynb   # Day 2: K-Means, DBSCAN & PCA Persona Clustering
│   └── 02_sentiment_analysis.ipynb      # Day 3: NLP Text Cleaning, TF-IDF, SVM & VADER
├── src/
│   └── data_generation.py         # Synthetic data generation engine
└── README.md