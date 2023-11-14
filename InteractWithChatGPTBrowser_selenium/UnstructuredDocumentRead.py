import ChatGPTBrowser
import time
import DigitalPDFExtractor
import os


def readDocuments(folder_path, queryList):
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
        text = "Text based passage :" + pdfdata["text"][:2000] + """. End of passage. Provide the answers to the comma seperated questions following in the below shape :       
        
        Shape:
        {   
        question: string // question present in the list followed, 
        answer: string // Answer to the question if present in the passage else send UNSURE        
        } :array //array of question answers 
        The response should contain only the JSON, no conversation or explanation should be present. 
        """ + " Questions : " + queryList
        print("Text to be sent to chat GPT : " + text)

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

    #time.sleep(5)
    # closes browser after time gets over
    #ChatGPTBrowser.closeBrowser()