
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

Milestones & Implementation Progress
Day 1: System Foundation & Data Architecture
Designed relational schemas across customer profiles, restaurant partners, transaction histories, and feedback logs.

Implemented src/data_generation.py to synthesize transactional distributions, delivery durations, order values, and review score dynamics.

Verified schema consistency and documented feature dictionaries in data/data_dictionary.md.

Day 2: Customer Segmentation & Behavioral Profiling
Feature Engineering: Aggregated total spending, frequency, and average order value (AOV) per customer account.

Cluster Optimization: Evaluated inertia across k=2 to 7 via the Elbow method and validated separation using Silhouette Analysis (k=3 optimal).

Unsupervised Modeling: Applied K-Means clustering (k=3) and DBSCAN anomaly detection (eps=1.2, min_samples=5) to identify outlier spending patterns.

Dimensionality Reduction: Visualized cluster distributions in 2D space using Principal Component Analysis (PCA).

Strategic Segments:

VIP Diners: High frequency, high AOV, high lifetime value.

Occasional Diners: Moderate frequency, moderate ticket sizes.

Budget Diners: Value-focused, price-sensitive transactions.

Day 3: NLP Sentiment Analysis & Feedback Intelligence
Text Preprocessing Pipeline: Tokenization, lowercase normalization, punctuation removal, stop-word filtering, and WordNet lemmatization.

Feature Extraction: Extracted unigram and bigram n-grams (ngram_range=(1, 2)) using TF-IDF vectorization with a 1,200-feature vocabulary.

Supervised Sentiment Modeling: Benchmarked Multinomial Naive Bayes against Support Vector Machine (LinearSVC) using Accuracy, Precision, Recall, and F1-score with confusion matrix validation.

Lexicon Comparison (VADER): Analyzed raw customer text to benchmark rule-based polarity (handling emojis, slang, and exclamation intensity) against supervised ML models.

Operational Complaint Drivers: Leveraged SVM feature coefficients to isolate the primary causes of customer dissatisfaction (ETA delays, food temperature degradation, and order accuracy/missing items).

Setup & Execution
Prerequisites
Python 3.10+

Virtual environment (.venv)