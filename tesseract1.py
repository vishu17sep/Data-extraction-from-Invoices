
import pytesseract
import cv2
import glob
import os
import import_ipynb
import reg

from pdf2image import convert_from_path,convert_from_bytes

def read_image(base_path,invoice,sheet1,sheet1_index):
    #print(base_path + invoice)
    file_name = invoice.split('.pdf')[0]
    #print(file_name)
    pages = convert_from_path(base_path +'\\'+invoice,500)
    for page in pages :
        page.save(base_path + file_name + '.jpg','JPEG')
        break
    img = cv2.imread(base_path + file_name + '.jpg')

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\INH8KOR\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

    Final_Result = pytesseract.image_to_string(img, lang='eng')

#print('Data after Extraction from Tesseract tool')
#print(Final_Result)

    f = open(base_path + file_name + '.txt', 'w') 
    f.write(Final_Result)
    f.close()
    reg.extract_data(base_path,file_name + '.txt', sheet1,sheet1_index)
