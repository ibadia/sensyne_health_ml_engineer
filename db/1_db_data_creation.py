import sqlite3 as sl
import os,logging
import pandas as pd
from peewee import *


TRANSFORMED_FILENAME='mushrooms_transformed.csv'
DB_NAME='mushrooms_database.db'

db=SqliteDatabase(DB_NAME)


class BaseModel(Model):
    class Meta:
        database=db



class AllCategories(BaseModel):
    name=CharField(primary_key=True)

    class Meta:
        database=db


class Mushrooms(BaseModel):
    id=AutoField()
    cap_shape=ForeignKeyField(AllCategories)
    cap_color=ForeignKeyField(AllCategories)
    odor=ForeignKeyField(AllCategories)
    gill_size=ForeignKeyField(AllCategories)
    gill_color=ForeignKeyField(AllCategories)
    stalk_color_above_ring=ForeignKeyField(AllCategories)
    veil_color=ForeignKeyField(AllCategories)
    ring_type=ForeignKeyField(AllCategories)
    spore_print_color=ForeignKeyField(AllCategories)
    population=ForeignKeyField(AllCategories)
    habitat=ForeignKeyField(AllCategories)

#This functions takes in the whole data and gives all uniques values in all dataaset
def get_unique_categories(data):
    all_cols=list(data.columns)
    unique_cols_list=[]
    for col in all_cols:
        col_list=list(set(list(data[col].values)))

        unique_cols_list.extend(col_list)
    return list(set(unique_cols_list))

def main():

    logging.basicConfig( format='%(filename)s - %(levelname)s - %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    logging.info("Reading Data")
    data=pd.read_csv(TRANSFORMED_FILENAME)

    logging.info("Connecting to Database")
    db.connect()
    logging.info("Creating Tables")
    db.create_tables([ AllCategories, Mushrooms])

    unique_cols=get_unique_categories(data)
    unique_cols=[{'name':x} for x in unique_cols]


    logging.info("Inserting Unique Categories")
    AllCategories.insert_many(unique_cols).execute()


    logging.info("Preparing Mushrooms data")
    new_renamed_cols={}
    for x in data.columns:
        new_renamed_cols[x]=x.replace('-','_')
    data=data.rename(columns=new_renamed_cols)
    
    data_source=[]
    cols=list(data.columns)
    
    for i,x in data.iterrows():
        values=[x[col_name] for col_name in cols] 
        single_dict={}
        single_dict.update(zip(cols, values))
        data_source.append(single_dict)

    logging.info("Inserting Mushroom Data")
    Mushrooms.insert_many(data_source).execute()

if __name__ == "__main__":
    main()
