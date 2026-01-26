import csv
import json

def csvconverter(filename):
    with open(filename,'r') as f:
    
        reader=csv.DictReader(f)
        rows=list(reader)

    
    with open('data.json','w') as outfile:
        json.dump(rows,outfile,indent=2)
csvconverter(r"C:\Users\vicha\OneDrive\Desktop\git-intials\Vichakshna-s-Rep1\Hello  - Sheet1.csv")
print("CSV converted to JSON successfully!")
