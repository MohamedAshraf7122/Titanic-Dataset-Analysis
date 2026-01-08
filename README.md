📄 Project Overview

The Titanic disaster dataset is a classic dataset for binary classification problems in machine learning. The goal is to predict whether a passenger survived or not based on features like age, sex, passenger class, fare, and family connections. This project follows a structured approach to extract insights, train models, and deploy a predictive system.

🔹 Data Cleaning & Preprocessing

Data preprocessing is crucial for building accurate models. In this project, the following steps were performed:

Handling missing values: Filled or removed missing entries in columns like Age, Cabin, and Embarked.

Encoding categorical features: Converted categorical variables such as Sex and Embarked into numerical format suitable for machine learning algorithms.

Feature engineering: Created new features like FamilySize (combining SibSp and Parch) and IsAlone to capture meaningful patterns.

Scaling & normalization: Applied scaling techniques for algorithms sensitive to feature magnitude (e.g., SVM).

🔹 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed using Pandas, Matplotlib, Seaborn, and Plotly. Key insights include:

Gender Differences: Female passengers had a significantly higher survival rate than males.

Passenger Class: First-class passengers were more likely to survive, while third-class passengers had the lowest survival rate.

Age Factor: Younger passengers, especially children, had higher chances of survival.

Fare Influence: Passengers who paid higher fares tended to survive more often, indicating a correlation with passenger class.

Family Connections: Passengers traveling alone had slightly lower survival chances compared to those with family.

Visualizations included histograms, bar plots, box plots, and interactive charts to better understand data distributions and relationships.

🛠️ Tools & Libraries

Python – Core programming language

Data Manipulation: Pandas, NumPy

Visualization: Matplotlib, Seaborn, Plotly

Machine Learning: Scikit-learn (Logistic Regression, Decision Tree, Random Forest, SVM), XGBoost

Model Tuning: RandomizedSearchCV

Model Deployment: Streamlit

🔑 Model Development & Evaluation
1. Model Selection

Multiple machine learning models were tested to determine the best performing algorithm:

Model	Initial Evaluation
Logistic Regression	Good baseline
Decision Tree	Moderate performance
Random Forest	High accuracy, good generalization
XGBoost Classifier	High accuracy, slightly slower
Support Vector Machine (SVM)	Best cross-validated score
2. Model Evaluation

Used cross-validation (cross_val_score) to evaluate model stability and performance.

SVM achieved the highest cross-validated accuracy, making it the most reliable model for this dataset.

3. Hyperparameter Tuning

Applied RandomizedSearchCV to fine-tune SVM hyperparameters, including:

C (regularization parameter)

gamma (kernel coefficient)

kernel (type of SVM kernel)

Resulted in improved model performance and robustness.

🚀 Model Deployment

The tuned SVM model was deployed as an interactive web application using Streamlit, allowing users to:

Input passenger details such as age, sex, passenger class, fare, and family connections.

Get real-time predictions of survival probability.

Visualize insights and understand factors influencing survival.

This deployment demonstrates how machine learning models can be applied in real-world scenarios for interactive decision-making.

💡 Key Insights & Takeaways

Gender is a strong predictor: Females were more likely to survive than males.

Socioeconomic status matters: First-class passengers had higher survival chances.

Age effect: Children were prioritized for survival in emergency situations.

Feature engineering enhances performance: Derived features like FamilySize and IsAlone contributed to better predictions.

SVM is powerful: With proper tuning, SVM outperformed other models in accuracy and reliability.
