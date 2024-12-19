**3 Signet Limited Internship Repository**
# **Student Dropout Prediction Project**

## **Project Overview**
This project focuses on predicting student dropouts using machine learning techniques. By identifying students at risk of dropping out, the project aims to provide actionable insights to improve retention rates. The model has been deployed as a user-friendly Streamlit application that allows users to input student data and receive dropout predictions.

---

## **Dataset**
- **Description:** The dataset contains information about students, including demographic, academic, and behavioral features. Key features include:
  - **Demographics:** Age, gender, location, etc.
  - **Academics:** Grades, attendance, study hours, etc.
  - **Behavioral Patterns:** Participation in extracurricular activities, behavioral warnings, etc.
- **Preprocessing Steps:**
  - Handled missing values and normalized the data.
  - Encoded categorical features using one-hot encoding or label encoding.
  - Scaled numerical features for model compatibility.

---

## **Model Architecture**
- **Algorithm:** Random Forest Classifier.
- **Key Steps:**
  - Initially trained using all features in the dataset.
  - Feature selection identified the 10 most important features to optimize the model's performance.
  - Hyperparameter tuning was performed to enhance accuracy.
- **Evaluation Metrics:**
  - Accuracy
  - Precision, Recall, and F1-score
  - ROC-AUC score to assess the model's ability to separate classes.

---

## **Training Process**
- **Training:** 
  - Data was split into training and test sets (e.g., 80-20 split).
  - Applied cross-validation to ensure the model's robustness.

---

## **Results**
- **Accuracy:** Achieved a high accuracy on the test set.
- **Key Observations:**
  - The model effectively identifies high-risk students but may occasionally misclassify borderline cases.
- **Feature Importance:** Attendance, grades, and behavioral warnings were among the most impactful features.

---

## **Deployment**
- **Platform:** The model is deployed as a web application using **Streamlit**.
- **Functionality:** 
  - Users can input student data through the app interface.
  - The app predicts whether the student is at risk of dropping out, along with a probability score.

---

*This is the link to the deployed model: https://studentdropoutrateprediction.streamlit.app/

*This is the link to the visualization dashboard: https://my-viz.streamlit.app/

---

## **Key Features**
1. **Feature Selection:** Reduced the dataset to the top 10 impactful features to improve efficiency.
2. **Interactive App:** Allows real-time predictions with a simple user interface.
3. **Visualization:** Displays feature importance and prediction probabilities for transparency.

---

## **Recommendations**
1. **Enhanced Features:** Include additional data such as parental engagement or socioeconomic status for improved predictions.
2. **Deployment at Scale:** Deploy the app on a cloud platform like AWS or Azure for handling larger datasets and multiple users.

---

## **Limitations**
1. **Data Collection:** The dataset's scope is limited to specific institutions, which may reduce generalizability.
2. **Behavioral Bias:** Model performance may vary if certain features (e.g., attendance) are biased or inaccurately recorded.
3. **Real-Time Updates:** The model doesn't account for dynamic, real-time changes in student behavior.

---

## **Future Work**
- Incorporate additional features such as parental involvement or teacher feedback for richer predictions.
- Deploy the model on cloud platforms for scalability and integrate a dashboard for administrators.
- Implement explainable AI techniques to provide interpretable predictions for stakeholders.

---


