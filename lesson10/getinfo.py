import requests
import xml.etree.ElementTree as ET
import re

class GetInfo:
    def __init__(self):
        self.itemList = []
    
    def getInfoFromWeb(self):
        """
        Retrieve XML data from the invoice website.
        Return: Parsed list of XML items.
        """
        try:
            response = requests.get("https://invoice.etax.nat.gov.tw/invoice.xml")
            response.raise_for_status()
            tree = ET.fromstring(response.content)
            self.itemList = list(tree.iter(tag="item"))
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve data: {e}")
            self.itemList = []
        return self.itemList
    
    def DataTransform(self, itemList):
        """
        Transform web data into a structured list.
        :param itemList: List of XML items.
        :return: Simplified list containing month, winning numbers, and date.
        """
        monthPrice = []
        
        for i in range(min(3, len(itemList))):  
            monthData = []
            item = itemList[i]
            
            
            priceMonth = item.findtext("title", default="Unknown Month")
            priceNumbers = item.findtext("numbers", default="")
            openDate = item.findtext("enddate", default="113/9/25")
            
          
            getPriceNumbers = re.findall(r"\d{3,8}", priceNumbers) 
            priceMonth += "月"
            openDate = openDate[:10]  
            
        
            monthData.append(priceMonth)
            monthData.append(getPriceNumbers)
            monthData.append(openDate)
            monthPrice.append(monthData)
        
        return monthPrice
