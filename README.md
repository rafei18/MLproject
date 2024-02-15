# END TO END Data Science Project project

## Student Performance Indicator Dataset 

### Approach for the project 


1. Data ingestion:
   - In this phase, the dataset is read from a CSV file.
   - Then the data is split into training and testing and saved in a file.

2. Data transformation :
   - In this phase a ColumnTransformer Pipeline is created.
   - For Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
   - For Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
   - This preprocessor is saved as pickle file.
  
3. Model training :
   - In this step, multiple models are trained while performing hyperparameter tuning using "grid search," and finaly, the best model will be saved in a pickle file.
   
4. Prediction Pipeline :
   - This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.
   
5. Flask app creation :
   - Simple Flask app is created with user interface to the performance of a given student.
      
6. AWS Deployement :
   - Using AWS Elastic Beanstalk.
 
