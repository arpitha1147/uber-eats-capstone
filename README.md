
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

### Day 4: Delivery Time Prediction & Operational Regression
- **Data Pipeline**: Merged operational dimensions (restaurant prep dynamics, traffic conditions, weather impact, temporal windows) into `data/delivery_features.csv`.
- **Exploratory Data Analysis**: Analyzed target distributions, evaluated outlier spreads, and inspected multi-collinear operational relationships.
- **Model Implementations & Benchmarking**:
  - **Baseline OLS Regression**: Standard linear estimation with one-hot encoded categorical parameters.
  - **Regularized Estimators (Ridge & Lasso)**: Evaluated $L_1$ and $L_2$ shrinkage via 5-fold cross-validation.
  - **Ensemble Learning (Random Forest)**: Captured non-linear interactions between weather, congestion, and preparation time.
- **Evaluation Metrics**: Benchmarked MAE, RMSE, and $R^2$ across all models, generating actual-vs-predicted diagnostics and residual distributions.
- **Operational Insights**: Identified distance, preparation duration, and traffic severity as key drivers for dynamic ETA estimation.

## Day 5: Hourly Demand Forecasting

### 1. Overview & Objectives
- Forecasted future hourly order volume using time-series modeling to drive proactive courier staging and kitchen buffer management.
- Addressed non-stationarity, intra-day seasonality, and out-of-sample forward horizon evaluation.

### 2. Time-Series Methodology & Workflow
- **Data Aggregation**: Aggregated transactional orders into continuous hourly buckets (`data/hourly_order_demand.csv`), imputing zero-demand intervals to preserve uniform cadence.
- **Exploratory Analysis (EDA)**: Identified diurnal 24-hour cycles with sharp lunch (12:00–14:00) and dinner (19:00–21:00) peaks, alongside significant weekend demand surges.
- **Decomposition**: Implemented additive time-series decomposition ($Y_t = T_t + S_t + R_t$) using a 24-hour centered moving average to isolate long-term trend, daily periodicity, and zero-centered residual noise.
- **Stationarity & ADF Testing**: Evaluated rolling mean/variance stability and executed Augmented Dickey-Fuller (ADF) regression. Applied first-order differencing ($d=1$) to achieve statistical stationarity prior to autoregression.
- **Chronological Split**: Implemented a strict 80/20 chronological train-test split without random shuffling to prevent temporal data leakage.

### 3. Model Architectures & Benchmarks
Evaluated out-of-sample forecasting performance across MAE, RMSE, and MAPE:

| Model Architecture | Configuration / Components | MAE (orders) | RMSE (orders) | MAPE (%) |
| :--- | :--- | :--- | :--- | :--- |
| **ARIMA(3, 1, 1)** | Autoregressive Lags ($p=3$), Differencing ($d=1$), Moving Average Errors ($q=1$) | Evaluated | Evaluated | Evaluated |
| **Prophet (GAM)** | Additive Trend + Daily Fourier Harmonics ($K=3$) + Weekly Fourier Harmonics ($K=3$) + Weekend Regressor | Evaluated | Evaluated | Evaluated |

### 4. Operational & Business Impact
- **Fleet Dispatch Staging**: Position delivery couriers near high-density restaurant nodes 60–90 minutes prior to forecast peaks, reducing order pickup latency.
- **Dynamic Prep Buffers**: Provide high-volume merchants with real-time forward order projections to flatten kitchen bottlenecks.
- **Proactive Surge Pricing**: Base surge multipliers on forward-looking supply-to-demand deficit ratios rather than reactive unfulfilled order backlogs.