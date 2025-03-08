from lib.reporter import Reporter
import time
from lib.dataManager import DataManager
import pyodbc
from lib.configuration import Configuration
import os
import sys
from lib.globals import Globals
import requests

class APIs: 
 driver = None
 
 def __init__(self,driver):
        self.driver = driver 
     
 #hi git and hithub
 def Validate_response_content_Allget(self):
    print("welcom to validate APIs")
    response = requests.get(f"{Globals.Test.URL}/posts")   
    response_code =response.status_code
    response=response.text
    ExcelresponseCode=DataManager.getDictionaryTableFromExcell("select [State code] from [Response$] WHERE [RowID] = 1")[0]['State code']
    ExcelresponseCode=int(ExcelresponseCode)

    if  response_code==ExcelresponseCode:
            Reporter.passed("Validate State code for get all ID passed")
            Reporter.info(f"The result from get All ID: {response}")
            Reporter.info(f"The status code:{response_code}")   

    else:
            Reporter.failed("Validate State code for get all ID Failed")
            Reporter.info(f"The result from get All ID: {response.json()}")
            Reporter.info(f"The status code:{response_code}")  
 
 
 def Validate_Response_Content_Get_specificID(self):
    
    ExcelresponseText = DataManager.getDictionaryTableFromExcell("SELECT [userId], [id], [title], [body] FROM [Response$] WHERE [RowID] = 1")
    ExcelresponseText = ExcelresponseText[0] 

    ExcelresponseText['userId'] = int(ExcelresponseText['userId'])
    ExcelresponseText['id'] = int(ExcelresponseText['id'])
    ExcelresponseText['body'] = ExcelresponseText['body'].replace('\\n', '\n')
    ExcelresponseText['title'] = ExcelresponseText['title'].replace('\\n', '\n')
    print(ExcelresponseText)
   
    
    ExcelresponseCode=DataManager.getDictionaryTableFromExcell("select [State code] from [Response$] WHERE [RowID] = 1")[0]['State code']
    print(ExcelresponseCode)
    ExcelresponseCode=int(ExcelresponseCode)# when fitch status code from excel It dose not as an integer , I have to change the  type to make sure its ccompatible to compare it 
    print( )

    responseID1 = requests.get(f"{Globals.Test.URL}/posts/1")  
    APIsresponseText=responseID1.json()
    print(APIsresponseText)
    APIsresponseCode=responseID1.status_code
    print(APIsresponseCode)

    assert ExcelresponseText == APIsresponseText, f"Expected response text: {ExcelresponseText},  got: {APIsresponseText}"
    assert ExcelresponseCode == APIsresponseCode, f"Expected status code: {ExcelresponseCode},  got: {APIsresponseCode}"
    Reporter.passed("Validate Response Get specific ID Passed")
    Reporter.info(f"The result from get ID=1: {APIsresponseText}")  
    Reporter.info(f"The status code: {APIsresponseCode}") 
    

    """  if ( ExcelresponseText == APIsresponseText and ExcelresponseCode == APIsresponseCode ):
          Reporter.passed("Validate Response Get spisfic ID Pass")
          Reporter.info(f"The result from get ID=1: {APIsresponseText}")
          Reporter.info(f"The status code:{APIsresponseCode}")   
    else:
       Reporter.failed("Validate Response Get spisfic ID Faild")  
       Reporter.info(f"The result from get ID=1: {APIsresponseText}")
       Reporter.info(f"The status code:{APIsresponseCode}")     """



 def Validate_Using_Post(self):
    URL1= f"{Globals.Test.URL}/posts"
  
    Fetch_Data_From_Excel= DataManager.getDictionaryTableFromExcell("SELECT [userId], [id], [title], [body] FROM [Response$] WHERE [RowID] = 2")
    Fetch_Data_From_Excel = Fetch_Data_From_Excel[0] 

    Fetch_Data_From_Excel['userId'] = int(Fetch_Data_From_Excel['userId'])
    Fetch_Data_From_Excel['id'] = int(Fetch_Data_From_Excel['id'])
    Fetch_Data_From_Excel['body'] = Fetch_Data_From_Excel['body'].replace('\\n', '\n')
    Fetch_Data_From_Excel['title'] = Fetch_Data_From_Excel['title'].replace('\\n', '\n')
    print(Fetch_Data_From_Excel)  
    response= requests.post(URL1, json=Fetch_Data_From_Excel)
    print(response.status_code)
    print(response.json())
    response_json=response.json()
    Fetch_respnse_status_code=DataManager.getDictionaryTableFromExcell("select [State code] from [Response$] where [RowID] = 2")[0]['State code']
    print (Fetch_respnse_status_code)

    Fetch_respnse_status_code = int(Fetch_respnse_status_code)
     
 #try assertion it 
    try:
       assert response.status_code==Fetch_respnse_status_code,f"Expected status code: {Fetch_respnse_status_code},  got: {response.status_code}"
       assert response_json['userId'] == Fetch_Data_From_Excel['userId'],f"Expected User id: {Fetch_Data_From_Excel['userId']},  got: {response_json['userId']}"
       assert response_json['id'] == Fetch_Data_From_Excel['id'],f"Expected body: {Fetch_Data_From_Excel['id']},  got: {response_json['id']}"
       assert response_json['title'] == Fetch_Data_From_Excel['title'],f"Expected title: {Fetch_Data_From_Excel['title']},  got: {response_json['title']}"
       assert response_json['body'] == Fetch_Data_From_Excel['body'],f"Expected body: {Fetch_Data_From_Excel['body']},  got: {response_json['body']}"
       

       Reporter.passed("Validate the Response of post new ID Passed")
       Reporter.info(f"The result from post ID=1:{response.json()}")  
       Reporter.info(f"The status code: {response.status_code}")
    except AssertionError as e:
         Reporter.failed("Validate the  Response of post new ID Failed")  
         Reporter.info(f"TThe result from post ID=1:{response.json()}")
         Reporter.info(f"The status code: {response.status_code}") 

    """
     if response.status_code==Fetch_respnse_status_code and Fetch_Data_From_Excel== response.json():
          Reporter.passed("Validate the Response of post new ID Passed")
          Reporter.info(f"The result from post ID=1:{response.json()}")  
          Reporter.info(f"The status code: {response.status_code}")
    else:
         Reporter.failed("Validate the  Response of post new ID Failed")  
         Reporter.info(f"TThe result from post ID=1:{response.json()}")
         Reporter.info(f"The status code: {response.status_code}")  """


 def validate_Using_Delete(self):
    URL2=f"{Globals.Test.URL}/posts/1"

    r = requests.delete(URL2) 
    Fetch_StatusCode_excel=DataManager.getDictionaryTableFromExcell("select [State code] from [Response$] where [RowID] = 3")[0]['State code']
    Fetch_StatusCode_excel=int( Fetch_StatusCode_excel)

    
    if(r.status_code== Fetch_StatusCode_excel):
          Reporter.passed("Validate the Response of delete ID Passed")
          Reporter.info(f"The result from Delete ID=1: {r.json()}")
          Reporter.info(f"The status code: {r.status_code}")
         
    else:
         Reporter.failed("Validate the  Response of delete  ID Failed")  
         Reporter.info(f"The result from Delete ID=1: {r.json()}")
         Reporter.info(f"The status code: {r.status_code}")
       
    
    
 def Validate_Using_Put(self):    
    URL3=f"{Globals.Test.URL}/posts/1"

    Fetch_updatedData_fromExcel=DataManager.getDictionaryTableFromExcell("select [title],[body] from [Response$] where [RowID] = 4")[0]
    Fetch_updatedData_fromExcel['body'] = Fetch_updatedData_fromExcel['body'].replace('\\n', '\n')
    Fetch_updatedData_fromExcel['title'] = Fetch_updatedData_fromExcel['title'].replace('\\n', '\n')
    response = requests.put(URL3, json=Fetch_updatedData_fromExcel)
    print(response.json())
    response_json=response.json()
    Fetch_StatusCode_excel=DataManager.getDictionaryTableFromExcell("select [State code] from [Response$] where [RowID] = 4")[0]['State code']
    Fetch_StatusCode_excel=int( Fetch_StatusCode_excel)

    try:
       assert response.status_code==Fetch_StatusCode_excel,f"Expected status code: {Fetch_StatusCode_excel},  got: {response.status_code}"
       assert response_json['title'] == Fetch_updatedData_fromExcel['title'],f"Expected title: {Fetch_updatedData_fromExcel['title']},  got: {response_json['title']}"
       assert response_json['body'] == Fetch_updatedData_fromExcel['body'],f"Expected body: {Fetch_updatedData_fromExcel['body']},  got: {response_json['body']}"
       Reporter.passed("Validate the Response of post new ID Passed")
       Reporter.info(f"The result from post ID=1:{response.json()}")  
       Reporter.info(f"The status code: {response.status_code}")
    except AssertionError as e:
         Reporter.failed("Validate the  Response of post new ID Failed")  
         Reporter.info(f"TThe result from post ID=1:{response.json()}")
         Reporter.info(f"The status code: {response.status_code}") 





    """if response.status_code==Fetch_StatusCode_excel:
          Reporter.passed("Validate the Response of Put ID Passed")
          Reporter.info(f"The result from Put ID=1:{response.json()}") 
          Reporter.info(f"The status code: {response.status_code}") 
    else:
         Reporter.failed("Validate the  Response of Put ID Failed")  
         Reporter.info(f"The result from Put ID=1::{response.json()}")  
         Reporter.info(f"The status code: {response.status_code}")"""
 
