import ChatGPTBrowser
import time
import DigitalPDFExtractor


pdfdata = DigitalPDFExtractor.extract_pdf_details("C:/bills/Aug23/invoice 7.pdf")
ChatGPTBrowser.inputRequest("""Extract data from the text provided later into a JSON object of the shape provided below.    
 Shape:
{ 
  total: number // total amount due,
  invoice_number: string // invoice number,
  billed_to: string // name of the person that needs to pay the invoice
}
""")
time.sleep(5)
ChatGPTBrowser.inputRequest(pdfdata["text"])
print(ChatGPTBrowser.getResponse())

time.sleep(1000)

ChatGPTBrowser.closeBrowser()