# sensyne_health_ml_engineer
Assessment for Sensyne Health ML engineer test


STEPS TO RUN THIS PROGRAM:

## Environment Setup

```bash
pip install -r requirements.txt
```
make sure to have python 3.8.8 installed
#NOTE
PLEASE RUN ALL CODE IN HOME DIRECTLY
## ETL Code run

```bash
python etl/1_data_dictionary_creation.py
```
This will simply create a data dictionary, in word file given we have keys and values for different columns, this code will parse that and create a data dictionary which will have the value for each key like grasses=g, etc. This will create a new file on the home directory named data_dictionary.json which will be used by next program


Next is to do the transformation on the main data. Please ensure that mushrooms.csv is present in the home directory
```bash
python etl/2_etl.py
```
1. This code will parse the dictionary file (data_dictionary.json) which contains the key values for all columns
2. Then it will load the mushrooms.csv file in a pandas dataframe
3. It will then validate the data to see if there is any inconsistency between data_dictionary (keys, values) and data itself.
4. It will then transform data by replacing they keys in the data by values derived from dictionary
5. once transformed it will write all of it in mushrooms_transformed.csv file in the home dir

## Database Creation SQLITE
