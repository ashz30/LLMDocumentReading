

import ChatGPTBrowser


text = """Sold By: Shreyash Retail Private Limited ,
Ship-from Address: Rectangle No. 06, Rectangle No. 07, Rectangle No. 08 and Rectangle No. 13, Village- Khalikpur, Tehsil- Badli,"""

ChatGPTBrowser.inputRequest(text)
print("Request complete")
print(ChatGPTBrowser.getResponse())