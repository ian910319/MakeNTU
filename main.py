from typing import Dict
from data_analysis import *
import pandas as pd
import warnings                     ## ignore warning owing to version difference ##
warnings.filterwarnings("ignore")   ## not a big deal, just didn't want to see it ##
pd.options.mode.chained_assignment = None

################### open data from sensorTile box ######################
try:
    raw_data = pd.read_csv('E:\output.csv').values
    f = open("raw_data/Raw_data.csv","w", newline ='')
    title =["time", "accx", "accy", "accz"]
    writer = csv.DictWriter(f, fieldnames = title)
    writer.writeheader()
    for event in raw_data:
        event = {"time":event[0],"accx":event[1],"accy":event[2],"accz":event[3]}
        event["accx"] -= 981
        event["accx"] /= 100
        event["accy"] /= 100
        event["accz"] /= 100
        writer.writerow(event)
except:
    pass
########################################################################

#################### transfer raw data to test data ####################
dimentionName =["maxAmpl", "avgAmpl", "maxSlope", "peakAboveRate", "stdDiviation"]
    
    
scatterAnalysis("raw_data/Raw_data.csv", "unknown")          #分析

dimentionName.append("situation")      #存成 .csv
dimentionName.append("time")
saveData(fileName =whereDataGoes, fieldnames =dimentionName, dataList =attributeVectorList)      #存成 .csv
########################################################################

#################### start machine learning ############################
train_data = pd.read_csv('Trained.csv')
test_data = pd.read_csv('processed_data_to_be_trained/test.csv')

X = train_data[['maxAmpl','avgAmpl','maxSlope','peakAboveRate','stdDiviation']]
Y = train_data[['situation']]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=100)
Y_train['situation'] = Y_train['situation'].map({'rest':0, 'walk':1, 'active':2, 'fall':3})
Y_test['situation'] = Y_test['situation'].map({'rest':0, 'walk':1, 'active':2, 'fall':3})

from xgboost import XGBClassifier
xgbc = XGBClassifier(use_label_encoder =False, eval_metric='mlogloss')
xgbc.fit(X_train, Y_train)
print(xgbc.score(X_test,Y_test))

import xgboost as xgb
from sklearn.model_selection import RandomizedSearchCV

# Create the parameter grid: gbm_param_grid 
gbm_param_grid = {
    'n_estimators': range(8, 20),
    'max_depth': range(6, 10),
    'learning_rate': [.4, .45, .5, .55, .6],
    'colsample_bytree': [.6, .7, .8, .9, 1]
}

# Instantiate the regressor: gbm
gbm = XGBClassifier(eval_metric='mlogloss',n_estimators=10)

# Perform random search: grid_mse
xgb_random = RandomizedSearchCV(param_distributions=gbm_param_grid, 
                                    estimator = gbm, scoring = "accuracy", 
                                    verbose = 1, n_iter = 50, cv = 4)


# Fit randomized_mse to the data
xgb_random.fit(X, Y)

# Print the best parameters and lowest RMSE
print("Best parameters found: ", xgb_random.best_params_)
print("Best accuracy found: ", xgb_random.best_score_)

############################### above is learning ##################################

############################### output learning result #############################
time = test_data.time
test_data.drop(['situation','time'], axis = 1, inplace=True)

xgb_pred = xgb_random.predict(test_data)

submission = pd.concat([pd.DataFrame(xgb_pred),time], axis = 'columns')
submission.columns = ["situation","time"]
submission.to_csv('situation.csv', header = True, index = False)
####################################################################################

############################### save fall time into text for warning ###############
f =open("flutter/health_monitoring_app/assets/text/warning.txt", "w")

for event in pd.read_csv("situation.csv").values:
    if event[0] == "fall":
        f.write(str(event[1]))
        f.write(" Patient Falled!!")
        f.write('\n')

f.close()
####################################################################################

from graph import *
radialHeatMap("situation.csv")