import pandas as pd
import os,logging,json
import time


FILENAME='data_dictionary.json'
OUTPUT_FILENAME='mushrooms_transformed.csv'

data_file_name='mushrooms.csv'
def read_file(filename):
    try:
        f=open(filename,'r')
        data=json.loads(f.read())
        f.close()
        return data
    except Exception as e:
        logging.error(e)
        logging.info("Please check file or fix json exiting")
        exit()

def read_data_file(filename):
    try:
        data=pd.read_csv(filename)
        return data
    except Exception as e:
        logging.error(e)
        logging.error("please ensure that %s file is present in %s",filename, os.getcwd())
        exit()


def validating_data(data, data_dictionary):

    logging.info("checking if the columns in data dictionary and data are consistent")
    columns=[col for col in data_dictionary]
    columns_in_data=list(data.columns)
    difference=list(set(columns).difference(columns_in_data))
    if len(difference)!=0:
        logging.warning("Some columns in data dictionary are not present in data file given")
        columns=list(set(columns).intersection(columns_in_data))

    if len(columns)==0:
        logging.error("Cannot process data with zero columns")
        exit()

    data=data[columns]
    for col in data.columns:
        values=list(data[col].values)
        present_in_dict=[val for val in data_dictionary[col]]
        
        key_difference=set(values).difference(set(present_in_dict))
        if (key_difference==set()):
            logging.info("Column %s successfully validated", col)
        else:
            logging.warning("Values not consistent with the data for %s", col)

    return data


def replacing_with_values(data,data_dictionary):
    try:
        for col in data.columns:
            data[col]=data[col].map(data_dictionary[col])
        return data
    except Exception as e:
        logging.error(e)
        exit()




if __name__ == "__main__":
    start_time=time.time()
    logging.basicConfig(format='%(filename)s - %(levelname)s - %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    logging.info("Reading Data Dictionary")
    data_dictionary=read_file(FILENAME)
    
    data=read_data_file(data_file_name)

    logging.info("validating and selecting required columns from data")
    data=validating_data(data, data_dictionary) 
    logging.info("Transforming Data..")
    logging.info("Replacing the keys with the values")
    
    data=replacing_with_values(data, data_dictionary)


    logging.info("Successfully Transformed")
    data.to_csv(OUTPUT_FILENAME, index=False)
    logging.info("Successfully Loaded transformed data to file %s", OUTPUT_FILENAME)

    logging.info("ETL took time: {:.2f} seconds".format(time.time()-start_time))


