import ChatGPTBrowser
import time
import DigitalPDFExtractor
import os


def readDocuments(folder_path):
    # change to folder with invoices

    # ask chat GPT to keep a track of categories

    # Get all files in the folder with their full paths
    file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
                  os.path.isfile(os.path.join(folder_path, f))]

    # Get the list of file paths
    for file_path in file_paths:
        pdfdata = DigitalPDFExtractor.extract_pdf_details(file_path)
        # print("Extracting data for " + file_path)
        # print("Extracted data " ,  pdfdata["text"])
        text = pdfdata["text"] + """ . 
        Extract data from the text provided into a JSON object of the shape provided. 
        Provide the value 'UNSURE' where data is not available or you are not sure. 
        Eliminate duplicate invoice data.
        Invoices will be grouped as per bill_type later, each item can be categorised into groceries, bill_payment, electronics or miscellaneous and has to be decided by the items in the invoices by you. Track that through each invoice till the end.
    
        Shape:
        {   
        total: number // total amount due in the invoice, 
        order_number: string // order number, 
        invoice_number: string // invoice number, 
        order_Date:date //order date or date when order was placed, 
        supplier: string // sold by or supplier , 
        ship_from_address : string // address from  which order was shipped  , 
        gstin : string // GST number of the supplier,
        taxes : string // total taxes for the order or sum of total IGST, SGST and CGST,
    
            items { 
                    item_name : string // name or description or title of the item,
                    item_amount : string // total amount for the item,
                    hsn : string // HSN number for the item,
                    unit_price : string //Unit Price for the item,
                    discount : string // total discount for the item,
                    quantity : string // quantity for the item,
                    shipping_charges : string // shipping charges for the item
    
                } : array // array of items
    
    
        } . 
        The response should contain only the JSON, no conversation or explanation should be present. 
    
        """
        ChatGPTBrowser.inputRequest(text)
        print("Request complete")
        # waiting for chatgpt to print out the output on the browser, smart check has been added, but someitmes it does it in batches
        time.sleep(15)
        print(ChatGPTBrowser.getResponse())
        # waiting for 5 secs to throttle requests to avoid chat gpt blocking frequent requests
        time.sleep(5)

    # get data in PDF
    # pdfdata = DigitalPDFExtractor.extract_pdf_details("C:/bills/Aug23/invoice 7.pdf")

    # text = pdfdata["text"] + " " + ". Extract data from the text provided into a JSON object of the shape provided. Provide the value 'UNSURE' where data is not available or you are not sure. Shape:{   total: number // total amount due, invoice_number: string // invoice number, billed_to: string // name of the person that needs to pay the invoice , billing_address:string // bill to address} . The response should contain only the JSON, no conversation or explanation should be present. "
    # ChatGPTBrowser.inputRequest(text)
    # time.sleep(5)
    # print(ChatGPTBrowser.getResponse())


    time.sleep(1000)
    # closes browser after time gets over
    ChatGPTBrowser.closeBrowser()