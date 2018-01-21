import csv
import json

csvfile = open('Verses.csv', 'r')
jsonfile = open('Verses.json', 'w')

reader = csv.DictReader( csvfile)
for row in reader:
    json.dump(row, jsonfile,indent=4, separators=(',',':'))
    jsonfile.write(','+'\n')