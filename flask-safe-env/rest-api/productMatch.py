from csv import reader
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json
import os

# print(fuzz.ratio("this is a test", "this is a test!"))
# print(fuzz.partial_ratio("this is a test", "this is a test!"))


# print(fuzz.partial_ratio("HP Notebook", "HP laptop notebook"))

# print(fuzz.ratio("HB Mango Juice", "HB"))
# print(fuzz.partial_ratio("HB Mango Juice", "HB"))
class MatchedProduct(object):
    ProductID = 0
    ProductMasterName = ""
    ProductName = ""
    ProductTerm = ""
    ProductAccuracy = 0

def productMatch(product):
    mp_id = 0
    mp_master_name = ""
    mp_product_name = ""
    mp_term = product
    mp_accuracy = 0
    os.chdir('D:/Osmosis-2020/Main/flask-safe-env/rest-api/')
    # FILE_PATH = "D:/Osmosis-2020/Main/flask-safe-env/rest-api/"
    FILE_PATH = os.getcwd() + "\\"
    #FILE_PATH = ""
    # Load products data set
    with open(FILE_PATH + 'products\\1.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        p1 = list(csv_reader)

    with open(FILE_PATH + 'products\\2.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        p2 = list(csv_reader)

    with open(FILE_PATH + 'products\\3.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        p3 = list(csv_reader)

    with open(FILE_PATH + 'products\\4.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        p4 = list(csv_reader)

    with open(FILE_PATH + 'products\\5.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        p5 = list(csv_reader)

    with open(FILE_PATH + 'products\\6.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        p6 = list(csv_reader)

    with open(FILE_PATH + 'products\\7.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        p7 = list(csv_reader)

    with open(FILE_PATH + 'products\\8.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        p8 = list(csv_reader)

    with open(FILE_PATH + 'products\\9.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        p9 = list(csv_reader)

    with open(FILE_PATH + 'products\\10.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        p10 = list(csv_reader)
 
    with open(FILE_PATH + 'products\\11.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        p11 = list(csv_reader)

    file1 = open("productsProcessing.txt","w") 
    file1.write(str(product) + "\n")

    p1_val_temp = process.extract(product, p1, limit=1)
    if(len(p1_val_temp) > 0):
        p1_val = process.extract(product, p1, limit=1)[0]
        p1_master_name = p1_val[0][0]
        p1_percent = p1_val[1]
        if(p1_percent > 85):
            mp_id = 1
            mp_master_name = "DINOSAURS Chocolate Bar"
            mp_product_name = p1_master_name
            mp_accuracy = p1_percent

    p2_val_temp = process.extract(product, p2, limit=1)
    if(len(p2_val_temp) > 0):
        p2_val = process.extract(product, p2, limit=1)[0]
        p2_master_name = p2_val[0][0]
        p2_percent = p2_val[1]
        if(p2_percent>85 and p2_percent>mp_accuracy):
            mp_id = 2
            mp_master_name = "RICH Juice Extract - Flavoured"
            mp_product_name = p2_master_name
            mp_accuracy = p2_percent

    p3_val_temp = process.extract(product, p3, limit=1)
    if(len(p3_val_temp)>0):
        p3_val = process.extract(product, p3, limit=1)[0]
        p3_master_name = p3_val[0][0]
        p3_percent = p3_val[1]
        if(p3_percent>85 and p3_percent>mp_accuracy):
            mp_id = 2
            mp_master_name = "TWIX Chocolate Cookies"
            mp_product_name = p3_master_name
            mp_accuracy = p3_percent

    p4_val_temp = process.extract(product, p4, limit=1)
    if(len(p4_val_temp)>0):
        p4_val = process.extract(product, p4, limit=1)[0]
        p4_master_name = p4_val[0][0]
        p4_percent = p4_val[1]
        if(p4_percent>85 and p4_percent>mp_accuracy):
            mp_id = 2
            mp_master_name = "FRESH FRUITS - Packaged"
            mp_product_name = p4_master_name
            mp_accuracy = p4_percent

    p5_val_temp = process.extract(product, p4, limit=1)
    if(len(p5_val_temp)>0):
        p5_val = process.extract(product, p4, limit=1)[0]
        p5_master_name = p5_val[0][0]
        p5_percent = p5_val[1]
        if(p5_percent>85 and p5_percent>mp_accuracy):
            mp_id = 2
            mp_master_name = "OREO - Original Chocalate Sandwich Biscutis"
            mp_product_name = p5_master_name
            mp_accuracy = p5_percent

    p6_val_temp = process.extract(product, p6, limit=1)
    if(len(p6_val_temp)>0):
        p6_val = process.extract(product, p6, limit=1)[0]
        p6_master_name = p6_val[0][0]
        p6_percent = p6_val[1]
        if(p6_percent>85 and p6_percent>mp_accuracy):
            mp_id = 2
            mp_master_name = "CHIVAS Regal Blended Malt Drink"
            mp_product_name = p6_master_name
            mp_accuracy = p6_percent

    p7_val_temp = process.extract(product, p7, limit=1)
    if(len(p7_val_temp)>0):
        p7_val = process.extract(product, p7, limit=1)[0]
        p7_master_name = p7_val[0][0]
        p7_percent = p7_val[1]
        if(p7_percent>85 and p7_percent>mp_accuracy):
            mp_id = 2
            mp_master_name = "GATORADE Sports Energy Drink"
            mp_product_name = p7_master_name
            mp_accuracy = p7_percent

    p8_val_temp = process.extract(product, p8, limit=1)
    if(len(p8_val_temp)>0):
        p8_val = process.extract(product, p8, limit=1)[0]
        p8_master_name = p8_val[0][0]
        p8_percent = p8_val[1]
        if(p8_percent>85 and p8_percent>mp_accuracy):
            mp_id = 2
            mp_master_name = "DR-PEPPER Chef's Need Soft Drink"
            mp_product_name = p8_master_name
            mp_accuracy = p8_percent

    p9_val_temp = process.extract(product, p9, limit=1)
    if(len(p9_val_temp)>0):
        p9_val = process.extract(product, p9, limit=1)[0]
        p9_master_name = p9_val[0][0]
        p9_percent = p9_val[1]
        if(p9_percent>85 and p9_percent>p1_percent):
            mp_id = 2
            mp_master_name = "CADBURRY - 5 Star Chocolate"
            mp_product_name = p9_master_name
            mp_accuracy = p9_percent
    
    p10_val_temp = process.extract(product, p10, limit=1)
    if(len(p10_val_temp)>0):
        p10_val = process.extract(product, p10, limit=1)[0]
        p10_master_name = p10_val[0][0]
        p10_percent = p10_val[1]
        if(p10_percent>85 and p10_percent>p1_percent):
            mp_id = 2
            mp_master_name = "PNP Beef Patties"
            mp_product_name = p10_master_name
            mp_accuracy = p10_percent
    
    p11_val_temp = process.extract(product, p11, limit=1)
    if(len(p11_val_temp)>0):
        p11_val = process.extract(product, p11, limit=1)[0]
        p11_master_name = p11_val[0][0]
        p11_percent = p11_val[1]
        if(p11_percent>85 and p11_percent>p1_percent):
            mp_id = 2
            mp_master_name = "BAKERS Lemon - Edible Cream"
            mp_product_name = p11_master_name
            mp_accuracy = p11_percent

    matched_product = MatchedProduct()
    matched_product.ProductID = mp_id
    matched_product.ProductMasterName = mp_master_name
    matched_product.ProductName = mp_product_name
    matched_product.ProductAccuracy = mp_accuracy
    matched_product.ProductTerm = mp_term
    file1.close()
    #return FILE_PATH
    return json.dumps(matched_product.__dict__) 



    # choices = ["Brand Strawberry extract", "Mango EXTRCT", "Lollipop", "Artificial essence extracts", "Mango Juice"]

    # input_val = "90JDF MNK MNGO JCE 7.8"
    # juice_val = process.extract(input_val, juice, limit=1)[0]
    # fruits_val = process.extract(input_val, fruits, limit=1)[0]

    # juice_val = process.extractOne(input_val, juice)[0]
    # fruits_val = process.extractOne(input_val, fruits)[0]
    # print(juice_val)
    # print(fruits_val)

    # print("\n\n")
    # print("JUICE CATEGORY: " + str(juice_val[0][0]) + " -- " + str(juice_val[1]) + "% \n")
    # print("FRUITS CATEGORY: " + str(fruits_val[0][0]) + " -- " + str(fruits_val[1]) + "%  \n")
    # result_val = "\n\n" + "JUICE CATEGORY: " + str(juice_val[0][0]) + " -- " + str(juice_val[1]) + "% \n" + "FRUITS CATEGORY: " + str(fruits_val[0][0]) + " -- " + str(fruits_val[1]) + "%  \n"
    # return result_val

    # print(process.extract("MNGO", juice)[0])
    # print(process.extract("MNGO", fruits)[0])
        



