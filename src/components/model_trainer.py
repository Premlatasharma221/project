import os
import sys
from dataclasses import dataclass

from catboost import CatBoostClassifier
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from src.utils import evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split traning and test input data")
            x_train,y_train,x_test,y_test=(train_array[:,:-1],
                                           train_array[:,-1],
                                           test_array[:,:-1],
                                           test_array[:,-1] 
                                           )
            models={
                "Random Forest":RandomForestRegressor(),
                "Decision Tree":DecisionTreeRegressor(),
                "Gradient Boosting":GradientBoostingRegressor(),
                "Linear Regression":LinearRegression(),
                "K-Neighbors Classifier":KNeighborsRegressor(),
                "XGBRegressor":XGBRegressor(),
                "Catboosting Regressor":CatBoostRegressor(verbose=False),
                "Adaboost Regressor":AdaBoostRegressor(),
            }

            model_report:dict=evaluate_models(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,
                                        models=models)
            ## to get the best models score from dict
            best_model_score=max(sorted(model_report.values()))

            ## To get the best model name from dict
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info("Best found model on both training and testing dataset")

            preprocessing_obj=
            
        except:
            pass

