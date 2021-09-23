import pickle
import numpy as np
import pandas as pd

model= pickle.load(open('model_ml7.pkl','rb'))

def predict(df):
    df=df[["Rating","Kilometers","Owner","Fuel_Type","Transmission_Type","RTO_State","Insurance_Months","Years_Old","Insr_Type","Car_Catgor"]]
    for i in range(len(df.Transmission_Type)):
        if(df.Transmission_Type[i]=='MANUAL'):
            df.Transmission_Type[i]=1
        else:
            df.Transmission_Type[i]=0
    df["First"]=df["Owner"]
    df["Second"]=df["Owner"]
    df["Third"]=df["Owner"]
    for i in range(len(df.Owner)):
        if(df.Owner[i]==1):
            df.First[i]=1
            df.Second[i]=0
            df.Third[i]=0
        elif(df.Owner[i]==2):
            df.First[i]=0
            df.Second[i]=1
            df.Third[i]=0
        elif(df.Owner[i]==3):
            df.First[i]=0
            df.Second[i]=0
            df.Third[i]=1
        else:
            df.First[i]=0
            df.Second[i]=0
            df.Third[i]=0
    df.drop('Owner',axis=1,inplace=True)
    df["Diesel"]=df["Fuel_Type"]
    df["Petrol"]=df["Fuel_Type"]
    for i in range(len(df.Fuel_Type)):
        if(df.Fuel_Type[i]=='Diesel'):
            df.Diesel[i]=1
            df.Petrol[i]=0
        elif(df.Fuel_Type[i]=='Petrol'):
            df.Diesel[i]=0
            df.Petrol[i]=1
        else:
            df.Diesel[i]=0
            df.Petrol[i]=0
    df.drop('Fuel_Type',axis=1,inplace=True)
    df["North_India"]=df["RTO_State"]
    df["South_India"]=df["RTO_State"]
    df["West_India"]=df["RTO_State"]
    for i in range(len(df.RTO_State)):
        if(df.RTO_State[i]=='North_India'):
            df.North_India[i]=1
            df.South_India[i]=0
            df.West_India[i]=0
        elif(df.RTO_State[i]=='South_India'):
            df.North_India[i]=0
            df.South_India[i]=1
            df.West_India[i]=0
        elif(df.RTO_State[i]=='West_India'):
            df.North_India[i]=0
            df.South_India[i]=0
            df.West_India[i]=1
        else:
            df.North_India[i]=0
            df.South_India[i]=0
            df.West_India[i]=0
    df.drop('RTO_State',axis=1,inplace=True)
    df["Insurance_3rd_Party"]=df["Insr_Type"]
    df["Insurance_Comprehensive"]=df["Insr_Type"]
    df["Insurane_Expired"]=df["Insr_Type"]
    for i in range(len(df.Insr_Type)):
        if(df.Insr_Type[i]=='Third_Party'):
            df.Insurance_3rd_Party[i]=1
            df.Insurance_Comprehensive[i]=0
            df.Insurane_Expired[i]=0
        elif(df.Insr_Type[i]=='Comprehensive'):
            df.Insurance_3rd_Party[i]=0
            df.Insurance_Comprehensive[i]=1
            df.Insurane_Expired[i]=0
        elif(df.Insr_Type[i]=='Expired'):
            df.Insurance_3rd_Party[i]=0
            df.Insurance_Comprehensive[i]=0
            df.Insurane_Expired[i]=1
        else:
            df.Insurance_3rd_Party[i]=0
            df.Insurance_Comprehensive[i]=0
            df.Insurane_Expired[i]=0
    df.drop('Insr_Type',axis=1,inplace=True)
    df["low"]=df["Insr_Type"]
    df["Budget"]=df["Insr_Type"]
    df["Medium"]=df["Insr_Type"]
    df["Highend"]=df["Insr_Type"]
    for i in range(len(df.Car_Catgor)):
        if(df.Car_Catgor[i]=='Luxury'):
            df.low[i]=1
            df.Budget[i]=0
            df.Medium[i]=0
            df.Highend[i]=0
        elif(df.Car_Catgor[i]=='Budget'):
            df.low[i]=0
            df.Budget[i]=0
            df.Medium[i]=0
            df.Highend[i]=1
        elif(df.Car_Catgor[i]=='Medium'):
            df.low[i]=0
            df.Budget[i]=0
            df.Medium[i]=1
            df.Highend[i]=0
        elif(df.Car_Catgor[i]=='Highend'):
            df.low[i]=0
            df.Budget[i]=1
            df.Medium[i]=0
            df.Highend[i]=0
        else:
            df.low[i]=0
            df.Budget[i]=0
            df.Medium[i]=0
            df.Highend[i]=0
    df.drop('Car_Catgor',axis=1,inplace=True)
    numpy_array = df.to_numpy()
    predictions = model.predict(numpy_array)
    output = (np.around(predictions)).tolist()
    prnt = "Predicted Pre_Owned_Car Price is: "
    output = [str(i) for i in output]
    output = ["{}{}".format(prnt , i) for i in output]
    return output
    