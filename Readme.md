1. **Project Overview**: We want to know how much a customer is likely to spend in the near future, not just what they spent previously.
This project builds a regression model to predict 30-day customer spend based on historical behavior.


2. **Project Problem** : We want to know "How much the customer will be spending in the next thirty days. Also called short term CLV.

3. **Machine Learning Problem** :

Type: Supervised Regression
Input (X): Customer behavior features up to a cutoff date
Output (y): Total spend in the next 30 days after the cutoff
 
4. **Dataset** :Online Retail Data Set from UCI ML repo from kaggle
            Total Rows :541909
            Total Columns : 8

    key idea use :
    Key Fields Used :
                   CustomerID
                   InvoiceDate 
                   Unit Price
                   customer_id
                   Country


5. **Solution Approach**:
   
### **1.Data Preprocessing** :
 - Remove negative/zero values
 - Remove missing customer IDs
 - Convert timestamps to datetime
 - Remove outliers


  ### **2. Feature Engineering**
Created customer-level features:
- **Recency:** Days since last purchase
- **Frequency:** Number of purchases in past 90 days
- **Amount Value:** Average transaction value

### **3. Model Development**
Tested multiple regression models:
- Linear Regression (baseline)
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor 
---

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Download Dataset**
- Go to [https://www.kaggle.com/datasets/jihyeseo/online-retail-data-set-from-uci-ml-repo]


### **Option 2: Web Interface**
1. Open the localhost
2. Enter Recency, Frequency & Amount value
3. Click "Predict"
4. View predicted spend + explanation

---

## **Key Features**
- ✅ Predicts 30-day customer spend
- ✅ RESTful API for integration
- ✅ Simple web interface
- ✅ Feature importance visualization
- ✅ Model evaluation metrics

---

## **Technologies Used**
- **Python 3.8+**
- **pandas** - Data manipulation
- **scikit-learn** - Machine learning
- **Streamlit** -  development
- **Matplotlib/Seaborn** - Visualizations

---
### **Result **
- Accuracy Score:
  Linear Regression (baseline) - (Acuracy : 29%)
  Decision Tree Regressor - (Acuracy : 53 )
  Random Forest Regressor(Acuracy : 64.8 )
  XGBoost Regressor (Acuracy : 52.9 )
---
   

## **Future Improvements**
-  Add seasonality features (holidays, weekends)
-  Include customer demographics
-  Try deep learning models (LSTM for time series)
-  Deploy to cloud (AWS/Azure)
-  Add real-time prediction updates

---

## **Team**
- [Harsh] - Data Preprocessing
- [Suraj] - Modelling & Evaluation
- [Madhu] - UI Design

---

## **License**
This project is for educational purposes.
---

**Questions?** Contact: [nainmadhu1316@email.com]
---
