1. Project Overview : We want to know how much a customer is likely to spend in the near future, not just what they spent previously.
This project builds a regression model to predict 30-day customer spend based on historical behavior.


2. Project Problem : We want to know "How much the customer will be spending in the next thirty days. Also called short term CLV.

3. Machine Learning Problem :

Type: Supervised Regression
Input (X): Customer behavior features up to a cutoff date
Output (y): Total spend in the next 30 days after the cutoff
 
4. Dataset :Online Retail Data Set from UCI ML repo from kaggle
            Total Rows :541909
            Total Columns : 8

    key idea use :
    Key Fields Used :
                   CustomerID
                   InvoiceDate 
                   Unit Price
                   customer_id
                   Country


5. Solution Approach:
   
 1. Data Preprocessing : Remove negative/zero values
                         Remove missing customer IDs
                         Convert timestamps to datetime
                         Remove outliers

 2. 