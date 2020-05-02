import os
import flask
#import import_ipynb
import tesseract1
import xlwt 
from xlwt import Workbook

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>DATA EXTRACTION FROM INVOICE</h1>
<p>An API for passing foloder location in variable <b>base_path<b> and receiving info in json format.</p>'''

@app.route('/api/v1/', methods=['GET'])
def api_extract():
    
    # Workbook is created 
    wb = Workbook() 
  
    # add_sheet is used to create sheet. 
    sheet1 = wb.add_sheet('Sheet 1') 
    sheet1.write(0, 0, 'FILENAME') 
    sheet1.write(0, 1, 'DATE OF INVOICE')
    sheet1.write(0, 2, 'INVOICE NUMBER')
    sheet1.write(0, 3, 'CUSTOMER NUMBER')
    sheet1_index = 1;

    base_path = r'C:\Users\INH8KOR\Desktop\api\Invoices';

    list_of_invoices = os.listdir(base_path);
    for invoice in list_of_invoices:
        #print(invoice)
        #inp1 = input("enter any value to continue")
        tesseract1.read_image(base_path,invoice,sheet1,sheet1_index)
        sheet1_index +=1
        
    wb.save(r'C:\Users\INH8KOR\Desktop\api\results.xls')
    print('Completed')
    return '<p>Extraction completed</p>'

if(__name__=='__main__'):
    app.run()