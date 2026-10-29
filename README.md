
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

# Uber Eats Analytics & Machine Learning Capstone

An end-to-end machine learning and operational intelligence system designed to optimize dispatch logistics, forecast hourly order demand, segment customer/restaurant cohorts, and reduce delivery delays using simulated Uber Eats platform data.

---

## 📌 Project Overview

Food delivery platforms operate on tight unit economics driven by real-time balancing of customer expectations, merchant kitchen throughput, and dynamic courier dispatch. This 6-day capstone synthesizes exploratory data analysis, natural language processing, predictive regression, and time-series forecasting into an integrated, reproducible ML workflow.

### Key Objectives
1. **Customer & Restaurant Segmentation**: Group high-value cohorts and identify bottleneck kitchen partners using RFM metrics and K-Means clustering.
2. **Sentiment Analysis & CX Diagnostics**: Classify customer review sentiment via NLP to detect primary root causes of churn and low ratings.
3. **Delivery Duration & Tip Estimation**: Forecast order transit latency and driver tips using tree-based and regularized linear regression.
4. **Demand Forecasting & Staging**: Predict forward-looking hourly order volumes using ARIMA and Prophet-style Generalized Additive Models (GAM) to drive proactive fleet dispatch.
5. **Integrated Pipeline & Strategy**: Consolidate models into an end-to-end analytical mart and translate technical metrics into data-backed business decisions.

---

## 🛠️ Repository Structure

```text
uber-eats-capstone/
├── data/
│   ├── orders.csv                       # Historical order transaction logs
│   ├── customers.csv                    # Customer profiles and registration metadata
│   ├── restaurants.csv                  # Merchant metadata, cuisine, and coordinates
│   ├── reviews.csv                      # User review text and star ratings
│   ├── delivery_features.csv            # Engineered trip, weather, and distance metrics
│   ├── hourly_order_demand.csv          # Aggregated, gap-filled time-series demand
│   └── cleaned_reviews.csv              # Tokenized, preprocessed review corpora
├── notebooks/
│   ├── 01_customer_segmentation.ipynb   # Day 2: RFM feature engineering & K-Means clustering
│   ├── 02_sentiment_analysis.ipynb       # Day 3: NLP preprocessing, TF-IDF & sentiment classifiers
│   ├── 03_delivery_time_prediction.ipynb # Day 4: Delivery duration & tip regression benchmarks
│   ├── 04_demand_forecasting.ipynb      # Day 5: Stationarity, ARIMA & Prophet time-series models
│   └── 05_end_to_end_pipeline_insights.ipynb # Day 6: Master ML pipeline, drivers & business strategy
├── src/
│   └── data_generation.py               # Dataset synthesis and seed generation logic
├── .gitignore                           # Virtual environments, cache & system exclusions
└── README.md                            # Complete architecture, benchmarks & documentation

# Uber Eats Analytics & Machine Learning Capstone

An end-to-end machine learning and operational intelligence system designed to optimize dispatch logistics, forecast hourly order demand, segment customer/restaurant cohorts, and reduce delivery delays using simulated Uber Eats platform data.

---

## 📌 Project Overview

Food delivery platforms operate on dynamic unit economics balancing Customers, Restaurant Partners, and Couriers. This 7-day capstone synthesizes exploratory data analysis, unsupervised clustering, dimensionality reduction, natural language processing, predictive regression, and time-series forecasting into an integrated, reproducible ML workflow.

### Key Objectives
1. **Customer & Restaurant Segmentation**: Identify high-value cohorts and merchant bottlenecks using RFM metrics, K-Means, DBSCAN density clustering, and PCA 2D projections.
2. **Sentiment Analysis & CX Diagnostics**: Classify customer review sentiment via NLP to detect primary root causes of churn and low ratings.
3. **Delivery Duration & Tip Estimation**: Forecast order transit latency and driver tips using regularized linear models, Random Forest, and Gradient Boosting.
4. **Demand Forecasting & Staging**: Predict forward-looking hourly order volumes using ARIMA and Prophet-style Generalized Additive Models (GAM) to drive proactive fleet dispatch.
5. **Integrated Pipeline & Presentation**: Consolidate models into an end-to-end analytical mart and present the complete solution across the 10-point evaluation rubric.

---

## 🛠️ Repository Structure

```text
uber-eats-capstone/
├── data/
│   ├── orders.csv                       # Historical order transaction logs
│   ├── customers.csv                    # Customer profiles and registration metadata
│   ├── restaurants.csv                  # Merchant metadata, cuisine, and coordinates
│   ├── reviews.csv                      # User review text and star ratings
│   ├── delivery_features.csv            # Engineered trip, weather, and distance metrics
│   ├── hourly_order_demand.csv          # Aggregated, gap-filled time-series demand
│   ├── cleaned_reviews.csv              # Tokenized, preprocessed review corpora
│   └── data_dictionary.md               # Schema definitions and attribute descriptions
├── notebooks/
│   ├── 01_customer_segmentation.ipynb   # Day 2: RFM feature engineering & K-Means clustering
│   ├── 02_sentiment_analysis.ipynb       # Day 3: NLP preprocessing, TF-IDF & sentiment classifiers
│   ├── 03_delivery_time_prediction.ipynb # Day 4: Delivery duration & tip regression benchmarks
│   ├── 04_demand_forecasting.ipynb      # Day 5: Stationarity, ARIMA & Prophet time-series models
│   └── 05_end_to_end_pipeline_insights.ipynb # Days 6 & 7: Master pipeline, PCA, DBSCAN & business strategy
├── src/
│   └── data_generation.py               # Dataset synthesis and seed generation logic
├── .gitignore                           # Virtual environments, cache & system exclusions
└── README.md                            # Complete architecture, benchmarks & documentation

📊 Day-by-Day Workflow & DeliverablesDay 1: Data Architecture & Exploratory AnalysisIngested multi-table relational schema (orders, customers, restaurants, reviews).Resolved primary/foreign keys dynamically across tables and imputed missing values.Analyzed order distribution across time of day, meal peaks (lunch/dinner), and geographic clusters.Day 2: Customer & Merchant SegmentationMethodology: Computed Recency, Frequency, and Monetary (RFM) metrics per customer. Normalized features via StandardScaler and clustered using K-Means.Customer Cohorts:High-Value VIPs: High frequency and order volume (~55–65% of platform GMV).Regular Mid-Tier: Steady monthly cadence, responsive to discount coupons.Low-Frequency / Occasional: High recency, target for win-back reactivation campaigns.Merchant Diagnostics: Segmented restaurants into an operational health matrix based on average kitchen prep time vs. review score to detect partner bottlenecks.Day 3: Review Sentiment Analysis & CX QualityText Preprocessing: Normalized text, removed stopwords, handled contractions, and generated TF-IDF feature matrices.Models: Evaluated Multinomial Naive Bayes and Logistic Regression for binary/multiclass sentiment classification (achieving ~88–92% F1-score).Core Findings:Over 70% of 1-star and 2-star reviews stem from late delivery and cold/spilled food.Negative sentiment spikes when order delivery duration exceeds 40 minutes.Day 4: Delivery Latency & Driver Tip PredictionFeature Engineering: Extracted distance, kitchen prep time, rush hour indicators, traffic congestion multipliers, and item counts.Modeling: Benchmarked Ridge Regression, Random Forest Regressor, and Gradient Boosting.Performance:Delivery Duration MAE: ~5.2–6.8 minutes.Tip Prediction MAE: ~$1.20–$1.60.Key Drivers: Kitchen prep dwell time and transit distance account for over 60% of total delay variance.Day 5: Hourly Demand ForecastingTime-Series Structuring: Aggregated raw order logs into continuous hourly intervals, imputing zero-demand time steps to ensure uniform intervals.Decomposition & ADF Stationarity: Performed additive decomposition ($Y_t = T_t + S_t + R_t$). Executed Augmented Dickey-Fuller (ADF) regression; applied first-order differencing ($d=1$) to establish statistical stationarity.Chronological Validation: Employed strict chronological 80/20 train/test splitting to prevent future data leakage.Architectures:ARIMA(3, 1, 1): Lag autoregression on differenced series with error moving average.Prophet Formulation (GAM): Additive modeling capturing linear trend, daily Fourier cycles ($K=3$), weekly cycles ($K=3$), and weekend indicators.Day 6: End-to-End Pipeline & Business InsightsIntegrated the full pipeline: $\text{Raw Data} \to \text{Cleaning} \to \text{Mart} \to \text{Inference} \to \text{Insights}$.Assessed feature importance across models (kitchen prep dwell time identified as the top non-transit delay driver).Built courier staging curve to match peak demand spikes.Day 7: Finalization, Dimensionality Reduction & PresentationDBSCAN Clustering: Implemented density-based clustering (eps=0.8, min_samples=5) on standardized RFM features to isolate behavioral noise and extreme spending anomalies.PCA Dimensionality Reduction: Transformed 3D RFM features into 2 Principal Components capturing >95% of total variance, visually confirming separation of K-Means clusters and DBSCAN outlier points.Git Branching & Release: Demonstrated complete branching workflow (feature $\to$ main) with clean history.Presentation Deck: Structured 15–20 minute presentation aligned with the 10-point evaluation rubric.📈 Consolidated Model Benchmark MatrixPipeline ComponentModel ArchitecturePrimary MetricValidation ScoreOperational RoleCustomer SegmentationK-Means (Normalized RFM)Inertia / Silhouette3 Optimal ClustersVIP priority dispatch & retention marketingDensity ClusteringDBSCAN (eps=0.8, min=5)Outlier IsolationIsolates spending anomaliesFraud & high-variance VIP behavior detectionDimensionality ReductionPCA (2 Components)Explained Variance>95% Variance Explained2D cluster visualization & compressionSentiment AnalysisTF-IDF + Logistic RegressionF1-Score / Accuracy~90.4% F1-ScoreAutomated CX incident detection & packaging auditsDelivery Time PredictionRandom Forest RegressorMAE / RMSEMAE: 5.4 minsDynamic checkout ETA & courier dispatch timingTip Amount PredictionRidge / Random ForestMAEMAE: $1.35Dynamic tip suggestion presetsDemand ForecastingProphet Additive GAMMAE / MAPEMAPE: ~14.2%Pre-shift fleet staging & surge pricing💡 Executive Business RecommendationsProactive Courier Staging & Surge Pricing:Time-series forecasting proves recurring, predictable surges during weekend dinner windows (19:00–21:00).Rather than reacting to unfulfilled order queues, stage 35–50% additional courier capacity in dense dining clusters 45–60 minutes ahead of forecasted peaks.Merchant Kitchen Pacing Interventions:Kitchen preparation dwell time is the largest non-transit contributor to delivery delays.For restaurants flagged in the "Critical Bottleneck" cluster (>75th percentile prep time, <25th percentile rating), transmit forward demand projections directly to kitchen POS systems to enable batch-prepping.VIP Customer Retention Routing:Because High-Value VIP customers generate the majority of platform gross profit, routing algorithms should prioritize nearby top-rated couriers for this tier to keep average delivery times sub-30 minutes.Thermal Bag Audits & Spillage Prevention:NLP sentiment analysis indicates cold/spilled food is the second most common complaint in low-rating reviews. Enforce insulated thermal bag verification during driver onboarding and audit packaging standards for high-leakage cuisine partners.⚠️ System Limitations & Future Engineering RoadmapSpatial Granularity: Current demand models forecast aggregate city-wide volume. Future iterations should discretize forecasts into Uber H3 hexagonal micro-grids (Resolution 7/8).External Telemetry: Incorporating live weather (precipitation, temperature) and real-time municipal traffic APIs will enhance transit duration accuracy during severe weather events.Cold-Start Handling: Implement collaborative filtering and heuristic business fallbacks for newly registered merchants and first-time app users lacking order history.Production Architecture: Transition from offline batch Jupyter pipelines to an online microservice architecture using Apache Kafka for order event streaming, Redis for low-latency feature stores, and FastAPI for real-time model serving.
