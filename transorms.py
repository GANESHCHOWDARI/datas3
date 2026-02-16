import datetime,time
from logs import logs
import pandas as pd
def transform_data(data):
        df=pd.read_csv(data)
        df['FULL_NAME']=df['first_name'].str.strip()+' '+df['last_name'].str.strip()
        df['email']=df['email'].str.lower()
        df['phone']=df['phone'].str.replace(r'[^\d]', '', regex=True)
        df['address']=df['address'].str.strip()
        df['registered']=pd.to_datetime(df['registered'], errors='coerce')
        df['age']=df['age'].astype(int)
        df['spent']=df['spent'].astype(float)
        df.to_csv('./customers_transformed.csv',index=False)
        logs.info("Data transformed successfully")
        with open('./customers_transformed.csv','w',newline='',encoding='utf-8') as f:
            df.to_csv(f,index=False)
            logs.info("Transformed data written to customers_transformed.csv successfully")
       
        return './customers_transformed.csv'
    