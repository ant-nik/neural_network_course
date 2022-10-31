import pandas
import sys
import requests

strip_chars = ' \t'

if len(sys.argv) < 3:
    raise "Error, filename or/and start number is not provided. Exiting..."
    
filename = sys.argv[1]

dataset = pandas.read_csv(filename, sep=';')
count = int(sys.argv[2])
for index, row in dataset.iterrows():
    url = row['url'].strip(strip_chars)
    tmp_file_name = f"{filename}_image_{count}"
    with open(tmp_file_name, 'wb') as file:
        file.write(requests.get(url).content)
    count = count + 1