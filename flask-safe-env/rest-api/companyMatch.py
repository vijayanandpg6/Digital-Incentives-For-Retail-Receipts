from csv import reader
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json

def companyMatch(company):
    company_name = company
    percent = 0
    # Load company data set
    with open('company/walmart.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        walmart_data = list(csv_reader)
    with open('company/picknpay.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        picknpay_data = list(csv_reader)
    with open('company/kroger.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        kroger_data = list(csv_reader)

    walmart = process.extract(company, walmart_data, limit=1)[0]
    walmart_val = walmart[0][0]
    walmart_percent = walmart[1]
    company_name = "Walmart"
    if(walmart_percent > 80):
        percent = walmart_percent

    picknpay = process.extract(company, picknpay_data, limit=1)[0]
    picknpay_val = picknpay[0][0]
    picknpay_percent = picknpay[1]
    if(picknpay_percent>percent and picknpay_percent > 80):
        company_name = "Pick N Pay"

    kroger = process.extract(company, kroger_data, limit=1)[0]
    kroger_val = kroger[0][0]
    kroger_percent = kroger[1]
    if(kroger_percent > percent and kroger_percent > 80):
        company_name = "Kroger"
    
    return company_name

