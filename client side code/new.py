import PyPDF2 
import os
import re
from datetime import datetime
import time
import json
import requests

def parse_diagnosis(data,page):
    dates = re.findall(r"\d\d.\d\d.\d\d\d\d", data)
    return_data = []
    for k, day_data in enumerate(re.split(r"\d\d.\d\d.\d\d\d\d", data)):
        times = re.findall(r"\d\d:\d\d:\d\d", day_data)
        rows = re.split(r"\d\d:\d\d:\d\d", day_data)
        rows.pop(0)
        for i in range(len(rows)):
            row = rows[i].split("  ")
            row = [col.strip() for col in row if col.strip() != '']
            rows[i] = [times[i]] + row 
            rows[i][0] = datetime.strftime(datetime.strptime(dates[k-1],'%m/%d/%Y'),'%Y-%m-%d') + ' ' + rows[i][0]
            return_data.append(rows[i])
    return return_data


def parse_change(data,page):
    operations = ['Change of run', 'Operator', 'Set value', 'Others', 'Control']
    return_data =[]
    dates = re.findall(r"\d\d.\d\d.\d\d\d\d", data)
    for k, day_data in enumerate(re.split(r"\d\d.\d\d.\d\d\d\d", data)):
        times = re.findall(r"\d\d:\d\d:\d\d", day_data)
        rows = re.split(r"\d\d:\d\d:\d\d", day_data)
        rows.pop(0)          
        for i in range(len(rows)):
            for o in operations:
                if o.lower() in str(rows[i]).lower():
                    rows[i] = [times[i]] + [o] + [rows[i][re.search(o.lower(), rows[i].lower()).span()[1]:]]
                    rows[i][0] = datetime.strftime(datetime.strptime(dates[k-1],'%m/%d/%Y'),'%Y-%m-%d') + ' ' + rows[i][0]
                    rows[i][-1] = rows[i][-1].strip()
                    return_data.append( rows[i])
    return return_data

def parse_production(data, page):
    dates = re.findall(r"\d\d.\d\d.\d\d\d\d", data)
    return_data = []
    #print(data)
    for k, day_data in enumerate(re.split(r"\d\d.\d\d.\d\d\d\d", data)):
        times = re.findall(r"\d\d:\d\d:\d\d", day_data)
        rows = re.split(r"\d\d:\d\d:\d\d", day_data)
        rows.pop(0)
        for i in range(len(rows)):
            row = rows[i].split("  ")
            row_temp = [col.strip() for col in row if col.strip() != '']
            row = []
            for x in [ [i[0],i[1:-10],i[-10:-6],i[-6:-3],i[-3:]] for i in row_temp ]:
                for y in x:
                    row.append(y)
            rows[i] = [times[i], *row]
            rows[i][0] = datetime.strftime(datetime.strptime(dates[k-1],'%m/%d/%Y'),'%Y-%m-%d') + ' ' + rows[i][0]
            return_data.append(rows[i])
            #print(row)
    return return_data

def parse_result(data, page):
    delimeter = "Station [0-9]*SetMeanMinMaxSreln>T2>T1<T1<T2"
    stations = re.findall(delimeter, data)
    delimeters = ["Main compr. force[kN]", "Pre compr. force [kN]", "Weight [mg]", "Thickness [mm]", "Diameter [mm]", "Hardness [N]"]
    rows = []
    print(rows)
    return_data = []
    for k, station_data in enumerate(re.split(delimeter, data)):
        station_data = re.split("[\sa-zA-Z0-9\[\.]*\]", station_data)
        print(station_data)
    
def read_report(pdfFileObj):
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    diagnosis_data = []
    change_final = []
    production_data = []
    result_data = []
    for page in range(pdfReader.numPages):
        data = pdfReader.getPage(page).extractText()
        product = re.split("Batch:", re.split("Product:", data)[1].strip())[0].strip()
        batch = re.split("Batch:", data)[1].strip()[:7]
        if "Trial" in batch:
            batch = "Trial"
        if 'change report' in data.lower():
            change_final += parse_change(data, page)
        elif 'diagnosis report' in data.lower():
            diagnosis_data += parse_diagnosis(data, page)
        elif 'production report' in data.lower():
            production_data += parse_production(data, page)
        # elif 'result report' in data.lower():
        #     result_data += parse_result(data, page)
    diagnosis_data = list(filter(None, diagnosis_data))
    change_final = list(filter(None, change_final))
    production_data = list(filter(None, production_data))
    #print(production_data)
    return {
        'product': product,
        'batch': batch,
        'diagnosis':diagnosis_data,
        'change': change_final,
        'production':production_data,
    }

def ls(data_folder_path):
	l = os.listdir(data_folder_path)
	return l

if __name__ == '__main__':
	osdir = []
	data_folder_path = os.getcwd() + '\\data_folder'
	while True:
		osdir = set(ls(data_folder_path))
		for file_path in set(osdir):
			final_path = data_folder_path + "\\" + file_path
			pdf_file = open(final_path, 'rb')
			data_to_db = read_report(pdf_file)

			try:
				print(data_to_db)
				print("Sending data to remote server...")
				r = requests.post("http://192.168.43.191:8000/api/", data=json.dumps(data_to_db))
				print("Success!")
			except Exception as e:
				print("Cannot connect to server..." + e)
		time.sleep(5)	