import PyPDF2 
import os
import re

pdfFileObj = open(os.getcwd() + '\\PDF\\test\\temp3.pdf', 'rb') 

pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

operations = ['change of run', 'operator', 'set value', 'others', 'control']
for page in range(pdfReader.numPages):
    data = pdfReader.getPage(page).extractText()
    #print(data)
    for day_data in re.split(r"\d\d.\d\d.\d\d\d\d", data):
        times = re.findall(r"\d\d:\d\d:\d\d", day_data)
        rows = re.split(r"\d\d:\d\d:\d\d", day_data)
        rows.pop(0)
        for i in range(len(rows)):
            for o in operations:
                if o in str(rows[i]).lower():
                    rows[i] = [times[i]] + [o] + [rows[i][re.search(o, rows[i].lower()).span()[1]:]]
                    rows[i][-1] = rows[i][-1].strip()
                    print(rows[i])

pdfFileObj.close() 