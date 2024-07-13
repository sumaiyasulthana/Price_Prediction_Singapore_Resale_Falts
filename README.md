# Price_Prediction_Singapore_Resale_Falts
LinkedIn : https://www.linkedin.com/in/sumaiya-sulthana-906876137
Output Video Link: https://drive.google.com/file/d/1iswzhxxUA4IsNNn0PUrDdJQC9Az1fslQ/view?usp=drive_link
render deployed Link:https://price-prediction-singapore-resale-falts.onrender.com

 **Singapore  Resale Flat Prices Predicting:** The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore. This predictive model will be based on historical data of resale flat transactions, and it aims to assist both potential buyers and sellers in estimating the resale value of a flat.

**TOOLS AND LIBRARIES USED :** The process involves:

**Data Extraction:** Collect a dataset of resale flat transactions from the Singapore Housing and Development Board (HDB) for the years 1990 to Till Date.

**Data Transformation:** Using Python and Pandas to clean and structure the data.Preprocess the data for machine learning.
                         1.Appending the files.
                         2.Storing in a single file,then Read_csv

**Feature Engineering:** Extract relevant features from the dataset,DROP UNwanted once and include **town, flat type, storey range_start & end, floor area, flat model, and lease commence 
                     date,year and month** Created additional features that may enhance prediction accuracy.
                     1.**Exploratory Data Analysis**containd spliting of data,Drop Duplicates,Spell Replace
                     2. **Data Visualization** -**IN Resale_flat.ipynb file** done on floor_area and Resale_Price(target column) Histogram and Flat_model for Bar chart,Scatter plots.
                     
**Model Selection and Training:** Choosed an appropriate machine learning model for regression ( linear regression, decision trees,random forests,xgboost,gradient Boosting,Adaboost,
catboost,K-nearest neighbour). Got**RANDOM FOREST Regressor as best Score0.98** Train the model on the historical data, using a portion of the dataset for training.

**Model Evaluation:** Evaluated the model's predictive performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE),Root Mean Squared Error (RMSE) and 
                      R2 Score. on both trained and test data.
                      1.Hyperparameter tunning -Grid SearchCV on Linear Regression and achieved Best_Score_ and Best_Params_

**Dashboard Creation:** Using Streamlit to build an interactive dashboard, In an advance way to get animation effects.Utilize the trained machine learning model (Linear Regression)
                    to predict the resale price based on user inputs.

**REQUIRED LIBRARIES:**

1.Scikit-learn

2.streamlit

3.ensemble

4.numpy

5.pandas

6.seaborn

7.matplotlib.pyplot

**FEATURES of my App:** The following functions are available in my Singapore Real Estate app.

* Retrieval of data as input from user.

* Does( Label Encoder,And Standard Scaler) on input and makes it in standardized form.

* Migrate Standardized data to model.Predict on which already HYPERPARAMETER TUNINING is done and pickled.

* Loaded picked form model Deliver's the output.

* Price Predicted for the selected House model



**DOMAIN :** MACHINE LEARNING
