import re
import datetime


def extract_data(path, filename, sheet1,sheet1_index):
    date =['Invoice date','Date','date','DATE','Date Invoice']
    invoice_no = ['Invoice Number','Invoice number','invoice number','Invoice No']
    customer_no = ['Customer no','Customer No','Customer Number','Vendor Number']
    date_flag = 0
    data_values=[1,1,1]
    invoice_date_regex =['(\d+\.\d+\.\d+)','(\d+\/\d+\/\d+)','(\d+\-\d+\-\d+)']
    invoice_no_regex = ['(\d{9}\s\/\s\d{4})','(\d{8})']
    customer_no_regex =['(\d{6,11})']

    with open(path + filename ) as fh:
        for line in fh:
            for word in date:
                if(re.findall(word,line)):
                    #print(word)
                    for date_regex in invoice_date_regex:
                        date_value = re.findall(date_regex,line)
                        if(date_value):
                            data_values[0]=date_value
                            #print(data_values)
                            break
            for word in invoice_no :
                if(re.findall(word,line)):
                    #print(line)
                    for invoice_regex in invoice_no_regex:
                        invoice_no_value = re.findall(invoice_regex,line)  
                        if(invoice_no_value):
                            data_values[1]=invoice_no_value
                            #print(data_values)
                            break
                    #print(invoice_no_value) 
            for word in customer_no :
                if(re.findall(word,line)):
                    #print(line)
                    for customer_regex in customer_no_regex:
                        customer_no_value = re.findall(customer_regex,line)
                        #print(customer_no_value)
                        if(customer_no_value):
                            data_values[2] =customer_no_value;
                            #print(data_values)
                            break 
                            
    print(data_values)
    
    sheet1.write(sheet1_index,0, filename)
    sheet1.write(sheet1_index,1,data_values[0])
    sheet1.write(sheet1_index,2,data_values[1])
    sheet1.write(sheet1_index,3,data_values[2])
        

