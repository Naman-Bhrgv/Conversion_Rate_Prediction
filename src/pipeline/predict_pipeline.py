import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(  self,accepts_mercadopago,available_quantity,avg_gmv_item_domain_30days,avg_qty_orders_item_sel_30days):

        self.accepts_mercadopago = accepts_mercadopago

        self.available_quantity = available_quantity

        self.avg_gmv_item_domain_30days = avg_gmv_item_domain_30days

        self.avg_qty_orders_item_sel_30days = avg_qty_orders_item_sel_30days

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "accepts_mercadopago": [self.accepts_mercadopago],
                "available_quantity": [self.available_quantity],
                "avg_gmv_item_domain_30days": [self.avg_gmv_item_domain_30days],
                "avg_qty_orders_item_sel_30days": [self.avg_qty_orders_item_sel_30days]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

