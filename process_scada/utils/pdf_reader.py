import PyPDF2
import requests
import re
import json 
def munde_camelcase(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1\n\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1\n\2', s1).lower()

def format_str(string):
    string = munde_camelcase(string)
    dates_split = re.split(r'(\d\d.\d\d.\d\d\d\d)', string)
    time_split = [re.split(r'(\d\d:\d\d:\d\d)',i) for i in dates_split]

    time_split = list(filter(None, time_split))
    return time_split

def remove_n(data):
    data_dup=''
    for i in range(len(data[2])):
        data_dup += "\n"+data[2][i]
    data = data_dup.split("\n")
    data = list(filter(None, data))
    return data

# for i in range(count):
#     page = pdfReader.getPage(i)
#     data =page.extractText()
#     data = format_str(data)
#     print(data)
#     data = remove_n(data)
#     print(json.dumps(data,indent=2))
# print(date)
# for i in range(len(data)):
#     pass
    

if __name__ == "__main__":
    pdfdoc = open('temp.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfdoc)
    for page in [pdfReader.getPage(i) for i in range(pdfReader.numPages)]:
        pass

