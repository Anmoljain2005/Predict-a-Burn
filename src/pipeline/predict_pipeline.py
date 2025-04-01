import sys
import os
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
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(self,
                 Height:float,
                 Weight:float,
                 Duration:float,
                 Heart_Rate:float,
                 Body_Temp:float,
                 Age:int,
                 Gender:str):
        
        self.Height = Height
        self.Weight = Weight
        self.Duration = Duration
        self.Heart_Rate = Heart_Rate
        self.Body_Temp = Body_Temp
        self.Age = Age
        self.Gender=Gender

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Height':[self.Height],
                'Weight':[self.Weight],
                'Duration':[self.Duration],
                'Heart_Rate':[self.Heart_Rate],
                'Body_Temp':[self.Body_Temp],
                'Age':[self.Age],
                'Gender':[self.Gender],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)