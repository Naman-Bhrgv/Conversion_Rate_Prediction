import sys
import os
from src.exception import CustomException
from src.logger import logging
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils import save_object
import numpy as np

class DataTransformation:

    def __init__(self):

        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):

        try:

            numerical_columns=[]

            categorical_columns=['accepts_mercadopago', 'boosted', 'free_shipping', 'fulfillment', 'health', 'is_pdp', 'listing_type_id', 'logistic_type', 'offset', 'original_price', 'price']

            cat_pipeline=Pipeline(
                steps=[
                ("LabelEncoder", LabelEncoder())
                ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("cat_pipelines",cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor


        except Exception as e:

             raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:

            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="conversion"

            train_tgt=train_df[target_column_name]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)

            input_feature_train_df=input_feature_train_df.drop(['category_id','date','deal_print_id','domain_id','etl_version','full_name','main_picture','print_server_timestamp','site_id','sold_quantity','tags','uid','warranty','item_id','platform','title'],axis=1)

            X_train, X_test, y_train, y_test = train_test_split(input_feature_train_df, train_tgt, test_size=0.33, random_state=42)
            
            input_feature_train_arr=preprocessing_obj.fit_transform(X_train)
            
            input_feature_test_arr=preprocessing_obj.transform(X_test)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]            

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )


        except:
            
            pass

        




             