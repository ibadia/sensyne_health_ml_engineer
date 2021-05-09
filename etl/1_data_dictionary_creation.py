from pathlib import Path
import os,logging,json
import time


start_time=time.time()

logging.basicConfig(format='%(filename)s - %(levelname)s - %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


current_dir=Path(os.getcwd())

OUTPUT_FILENAME='data_dictionary.json'
word_string='''cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s 
cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y 
odor: almond=a,anise=l,creosote=c,fishy=y,foul=f, musty=m,none=n,pungent=p,spicy=s 
gill-size: broad=b,narrow=n 
gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e, white=w,yellow=y 
stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y 
veil-color: brown=n,orange=o,white=w,yellow=y 
ring-type: cobwebby=c,evanescent=e,flaring=f,large=l, none=n,pendant=p,sheathing=s,zone=z 
spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r, orange=o,purple=u,white=w,yellow=y 
population: abundant=a,clustered=c,numerous=n, scattered=s,several=v,solitary=y 
habitat: grasses=g,leaves=l,meadows=m,paths=p, urban=u,waste=w,woods=d'''

data_dictionary={}

#going through each entry in  word_string line by line
logging.info("Parsing Excerpt from WordFile")
for entry in word_string.split('\n'):
    #for each line the following two lines will split the column names and the keyvalues
    column_name, keyvalues=[item.strip() for item in entry.strip().split(':')]
    keyvalues=[x.strip().split('=') for x in keyvalues.split(',')]
    data_dictionary[column_name]={}

    for (value,key) in keyvalues:
        data_dictionary[column_name][key]=value


try:
    logging.info("Writing data_dictionary into file")
    f=open(OUTPUT_FILENAME,'w')
    f.write(json.dumps(data_dictionary, indent=2))
    f.close()
    logging.info("Successfully written data_dictionary to file %s",OUTPUT_FILENAME)
except Exception as e:
    logging.error(e)

end_time=time.time()-start_time
logging.info("Time taken for script to run: {:.5f}".format( end_time))

