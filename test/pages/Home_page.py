from selenium import webdriver
from selenium.webdriver.common.by import By
from lib.reporter import Reporter
from lib.selenium_extensions import (Click, findElementBy, isDisplayed,
                                     isEnabled, isSelected, sendKeys,
                                     waitUntilDisplay, waitUntilExistInDOM,
                                     waitUntilHidden,findElementsBy)
import time
from lib.dataManager import DataManager
import pyodbc
from lib.configuration import Configuration
import os
import sys
import requests

#The isDisplayed() method of WebElement interface is used to check whether the element is visible or not on the web page

class Home_Page:
    
    driver = None

    def __init__(self,driver):
        self.driver = driver
  

    ADDButton= (By.ID,'shopping_cart_container')
    ContShop=(By.CLASS_NAME,"btn_secondary")
    ADDprodBTN1=(By.XPATH, "//div[contains(text(),'Sauce Labs Bike Light')]/../../../div[@class='pricebar']/button")
    Add_Product_Btn2=()
    #  //div[contains(text(),'Sauce Labs Bike Light')]/../../../div[@class='pricebar']/button
    #//div[contains(text(),"Sauce Labs Backpack"]//following::button[1][contains(text(),"ADD TO CART")]'
    Sorting_Menu=(By.CLASS_NAME,"product_sort_container")
    RemoveBtn= (By.XPATH,'//button[contains(text(),"REMOVE")]')#//div[contains(text(),'Sauce Labs Backpack')]/../../../div[@class='pricebar']/button 
    checkoutBtn=(By.XPATH,"//a[contains(text(),'CHECKOUT')]")
    #checkoutBtn=(By.CLASS_NAME,"btn_action checkout_button")
    #checkoutBtn=(By.XPATH,"/html/body/div/div[2]/div[3]/div/div[2]/a[2]")
    F_Name=(By.ID,"first-name")
    L_Name=(By.ID,"last-name")
    zip_Code=(By.ID,"postal-code")
    Error_btn=(By.CLASS_NAME,"error-button")
    #Continue_Btn=(By.CLASS_NAME,"btn_primary cart_button")
    Continue_Btn=(By.XPATH,"//input[@value='CONTINUE']")
    Finish_Btn=(By.XPATH,"//a[contains(text(),'FINISH')]")
    CartValue = (By.CLASS_NAME, "shopping_cart_badge")
    #Cart_num=(By.XPATH,'//span[contains(text(),"1")]')
    Sorting_A_Z=(By.XPATH,"//option[contains(text(),'Name (A to Z)')]")
    Sorting_Z_A=(By.XPATH,"//option[contains(text(),'Name (Z to A)')]")
    Sorting_Low_High=(By.XPATH,"//option[contains(text(),'Price (low to high)')]")
    Sorting_High_Low=(By.XPATH,"//option[contains(text(),'Price (high to low)')]")
    Product1=(By.XPATH,"//div[@class='inventory_item_name']")
    """
    Product2=(By.XPATH,"(//div[@class='inventory_item_name'])[2]")
    Product3=(By.XPATH,"(//div[@class='inventory_item_name'])[3]")
    Product4=(By.XPATH,"(//div[@class='inventory_item_name'])[4]")
    Product5=(By.XPATH,"(//div[@class='inventory_item_name'])[5]")
    Product6=(By.XPATH,"(//div[@class='inventory_item_name'])[6]")
    """
    Price= (By.XPATH,"//div[@class='inventory_item_price']")

    #//div[contains(text(),'Sauce Labs Bike Light')]/ancestor::div[@class='cart_item']//div[@class='inventory_item_price']
  

    def Add_To_Cart_Btn(self):
        AP=self.driver.findElementBy(*Home_Page.ADDprodBTN1) 
        AP.Click()


    def Validate_Add_To_Cart_Button(self):
        Remove =self.driver.findElementBy(*Home_Page.RemoveBtn)
        if Remove.waitUntilDisplay(2):
            return True
        else:
            return False 
        
    def validate_add_to_cart_Btn(self):
    
     try:
        initial_cart_Value = self.driver.findElementBy(*Home_Page.CartValue)
        initial_value = int(initial_cart_Value.text)
     except:
         initial_value = 0

     self.Add_To_Cart_Btn()
     time.sleep(2)
    
     try:
        updated_cart_badge = self.driver.findElementBy(*Home_Page.CartValue)
        updated_value = int(updated_cart_badge.text)
     except:
        updated_value = 0
        return updated_value > initial_value  

    

    def Cart_Btn(self):
      ADDtbttn=self.driver.findElementBy(*Home_Page.ADDButton) 
      ADDtbttn.Click()
      

    def Validate_Cart_Btn(self):
        AtoZ=self.driver.findElementBy(*Home_Page.Sorting_Menu)
        if AtoZ.waitUntilHidden(1):
            return True
        else:
            return False
    
    def Continue_Shopping_Btn(self):
        counBtt=self.driver.findElementBy(*Home_Page.ContShop)
        counBtt.Click()
   
    def Validate_Continue_Shopping_Btn(self):
        AtZ=self.driver.findElementBy(*Home_Page.Sorting_Menu)
        if AtZ.waitUntilDisplay(3):
            return True
        else:
            return False

    def ChecKout_Btn(self):
        CO=self.driver.findElementBy(*Home_Page.checkoutBtn)
        CO.Click()

    def Validate_Checkout_Btn(self):
        Couninu_shoping=self.driver.findElementBy(*Home_Page.checkoutBtn)
        if Couninu_shoping.waitUntilHidden(3):
            return True
        else:
            return False
        
    def Checkout_Form(self):
        First_name=self.driver.findElementBy(*Home_Page.F_Name)
        First_name.sendKeys("shikah")
        Last_name=self.driver.findElementBy(*Home_Page.L_Name)
        Last_name.sendKeys("Mohammed")
        Zip_code=self.driver.findElementBy(*Home_Page.zip_Code)
        Zip_code.sendKeys("F1-456")

    def Validate_Checkout_Form(self):
        Error_Btn=self.driver.findElementBy(*Home_Page.Error_btn)
        if Error_Btn.isDisplayed:
            Reporter.failed("Validate CheckOut Failed {0}")
        else:
            Reporter.passed("Validate CheckOut passed") 

    def Continue_BtN(self):
        CB=self.driver.findElementBy(*Home_Page.Continue_Btn) 
        CB.Click() 

    def Validate_Continue_BtN(self):
        CB=self.driver.findElementBy(*Home_Page.Continue_Btn)
        if CB.waitUntilHidden(1):
            return True
        else:
            return False
    def Finish_BtN(self):
        FB=self.driver.findElementBy(*Home_Page.Finish_Btn)
        self.driver.execute_script("arguments[0].scrollIntoView()",FB)
        FB.Click()

    def Validate_Finish_Btn(self):
        FB=self.driver.findElementBy(*Home_Page.Finish_Btn)
        
        if FB.waitUntilHidden(1):
            return True
        else:
     
            return False
   
    def Sorting_menu(self):
        Sm=self.driver.findElementBy(*Home_Page.Sorting_Menu) 
        Sm.Click()

    def Validate_Sorting_menu(self):
        Sm=self.driver.findElementBy(*Home_Page.Sorting_A_Z)
        if Sm.waitUntilDisplay:
            return True
        else:
            return False

   
    @staticmethod
    def getDictionaryTableFromExcell(strQuery):
                dataTable=dict()
                colNmaes=dict()
                rowID = 0
                colID =0
                try:
                        Home_Page.qry=strQuery
                        cStr = Home_Page.cfg.connectionStrings["import pyodbc"].replace("[ControlFileName]",os.getcwd()+DataManager.cfg.appSettings["ControlFileName"])
                        cnxn = pyodbc.connect(cStr,autocommit=True)
                        cursor = cnxn.cursor()
                        cursor.execute(DataManager.qry)
                        # create a dictionary of column names
                        for desc in cursor.description:
                                colNmaes[colID]=desc[0]
                                colID+=1   
                        # Loop through returned data rows                                             
                        for row in cursor: 
                                colID =0   
                                dataRow=dict() 
                                #  create a dictionary using column name and value
                                for column in row:     
                                        dataRow[colNmaes[colID]]= str(column)
                                        colID+=1  
                                # Add the dictionary to the table dictionary
                                dataTable[rowID] = dataRow
                                rowID+=1     
                except:
                        print("Failed to execute query ({0}) on database for Error: {1}".format(strQuery,sys.exc_info()[1]))
                        cnxn.rollback()
                finally:                       
                        cursor.close()
                        cnxn.close()
                        return dataTable
                
    def Sorting_Name_From_A_Z(self):
        AtoZ=self.driver.findElementBy(*Home_Page.Sorting_A_Z)
        AtoZ.Click()
        time.sleep(2)      
    # for i in range(5): 0-4 
    #print(i)    
    # list = [1, 2, 3, 4, 5]
    # length_of_list = len(my_list)  //5 
        
    def Validate_Sorting_Name_From_A_Z(self):
    
     product_from_Excel = DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$]")
     print("Query Result:", product_from_Excel)
     #items = [product_from_Excel[row_id]['ProductName'] for row_id in range(len(product_from_Excel))]
     items = [product_from_Excel[row_id]['ProductName'] for row_id in product_from_Excel]
     items.sort()

     self.Sorting_Name_From_A_Z()

     products_elements = self.driver.findElementsBy(*Home_Page.Product1)
     products = [element.text for element in products_elements]
     
     if products == items:
        for item in items:
            print("Item from excel:", item)
        print(" ")
        for pro in products:
            print("Product sorted from website:", pro)
        return Reporter.passed("Validate Sorting name from A to Z passed")
     else:
        for item in items:
            print("Item from excel", item)
        print(" ")
        for pro in products:
            print("Product sorted from website:", pro)
        return Reporter.failed("Validate Sorting name from A to Z Failed for {0}")


    def Sorting_Name_From_Z_A(self):
        ZtoA=self.driver.findElementBy(*Home_Page.Sorting_Z_A)
        ZtoA.Click()
 

    def Validate_Sorting_Name_From_Z_A(self):
     product_from_Excel = DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$]")
     #items = [product_from_Excel[row_id]['ProductName'] for row_id in range(len(product_from_Excel))]
     items = [product_from_Excel[row_id]['ProductName'] for row_id in product_from_Excel]
     items.sort(reverse=True)

     self.Sorting_Name_From_Z_A()

     products_elements = self.driver.findElementsBy(*Home_Page.Product1)
     products = [element.text for element in products_elements]
     
     if products == items:
        for item in items:
            print("Item from excel:", item)
        print(" ")
        for pro in products:
            print("Product sorted from website:", pro)
        return Reporter.passed("Validate Sorting name from Z to A passed")
     else:
        for item in items:
            print("Item from excel", item)
        print(" ")
        for pro in products:
            print("Product sorted from website:", pro)
        return Reporter.failed("Validate Sorting name from Z to A Failed for {0}")
   


    def Sorting_Price_Low_High(self):
        LtoH=self.driver.findElementBy(*Home_Page.Sorting_Low_High)
        LtoH.Click()



    def Validate_Sorting_Price_Low_High(self):
     Price_from_Excel=DataManager.getDictionaryTableFromExcell('select [Price] from [Items$]')
     # Price_from_Ex=[float(Price_from_Excel[row_id]['Price'])for row_id in range(len(Price_from_Excel))]
     Price_from_Ex=[float(Price_from_Excel[row_id]['Price'])for row_id in Price_from_Excel]
     Price_from_Ex.sort()

     self.Sorting_Price_Low_High()

     price_from_website=self.driver.findElementsBy(*Home_Page.Price)
     price_from_web=[float(price.text.strip('$')) for price in price_from_website]

     if Price_from_Ex== price_from_web:
        for i in Price_from_Ex:
          print ("price from excel:",i)
        print(" ")
        for p in price_from_web:
            print("Price from website",p) 
        print(Price_from_Ex== price_from_web)    
        return Reporter.passed("Validate Sorting price from low to high passed")
     else:
        for i in Price_from_Ex:
          print ("price from excel:",i)
        print(" ")
        for p in price_from_web:
            print("Price from website",p) 
        print(Price_from_Ex== price_from_web)      
        return Reporter.failed("Validate Sorting price from low to high failed")


    def Sorting_Price_High_Low(self):
        HtoL=self.driver.findElementBy(*Home_Page.Sorting_High_Low)
        HtoL.Click()


    def Validate_Sorting_Price_High_Low(self):

     Price_from_Excel=DataManager.getDictionaryTableFromExcell('select [Price] from [Items$]')
     #Price_from_Ex=[float(Price_from_Excel[row_id]['Price'])for row_id in range(len(Price_from_Excel))]
     Price_from_Ex=[float(Price_from_Excel[row_id]['Price'])for row_id in Price_from_Excel]

     Price_from_Ex.sort(reverse=True)

     self.Sorting_Price_High_Low()

     price_from_website=self.driver.findElementsBy(*Home_Page.Price)
     price_from_web=[float(price.text.strip('$')) for price in price_from_website]

     if Price_from_Ex== price_from_web:
        for i in Price_from_Ex:
          print ("price from excel:",i)
        print(" ")
        for p in price_from_web:
            print("Price from website",p) 
        print(Price_from_Ex== price_from_web)   
        Price_from_Ex_str = ' '.join([str(s) for s in Price_from_Ex])
        price_from_web_str = ' '.join([str(s) for s in price_from_web])
        Reporter.info(price_from_web_str +' '+ Price_from_Ex_str) 
        return Reporter.passed("Validate Sorting price from High to low passed")
     else:
        for i in Price_from_Ex:
          print ("price from excel:",i)
        print(" ")
        for p in price_from_web:
            print("Price from website",p) 
        print(Price_from_Ex== price_from_web)      
        return Reporter.failed("Validate Sorting price from high to low failed")




    def HomePage(self,tdr=dict()):
         self.Cart_Btn()
         self.Continue_Shopping_Btn()
         self.Add_To_Cart_Btn()
        
    def ADDTocartValidatopn(self,tdr=dict()):
         self.Add_To_Cart_Btn()
         self.Cart_Btn()

    def Validate_CheckOut(self,tdr=dict()):
         self.validate_add_to_cart_Btn()
         #self.Add_To_Cart_Btn()
         #self.validate_add_to_cart_btn()
         #self.Validate_Add_To_Cart_Btn()
         self.Cart_Btn()
         self.Validate_Cart_Btn()
         self.ChecKout_Btn()
         self.Validate_Checkout_Btn()
         self.Checkout_Form()
         self.Validate_Checkout_Form()
         self.Continue_BtN()
         self.Validate_Continue_BtN()
         self.Finish_BtN()
         self.Validate_Finish_Btn()

    def Validate_Sorting_Name_From_A_to_Z1(self,tdr=dict()):
        self.Sorting_menu()
        self.Sorting_Name_From_A_Z()
        self.Validate_Sorting_Name_From_A_Z()

    def Validate_Sorting_Name_From_Z_to_A1(self,tdr=dict()):
         self.Sorting_menu()
         self.Sorting_Name_From_Z_A()
         self.Validate_Sorting_Name_From_Z_A()

    def Validate_Sorting_Price_Low_High1(self,tdr=dict()):
        self.Sorting_menu()
        self.Sorting_Price_Low_High()
        self.Validate_Sorting_Price_Low_High()

    def Validate_Sorting_Price_High_Low1(self,tdr=dict()):
        self.Sorting_menu()
        self.Sorting_Price_High_Low()
        self.Validate_Sorting_Price_High_Low()
            




#//a[contains(text(),"CANCEL")]
#how to remove case sensetive 
#make seprate validation on each function suing if else
#learning more about Xpath
#test senario make it for try catch



"""
p1=self.driver.findElementBy(*Home_Page.Product1)
        p2=self.driver.findElementBy(*Home_Page.Product1)
        p3=self.driver.findElementBy(*Home_Page.Product1)
        p4=self.driver.findElementBy(*Home_Page.Product1)
        p5=self.driver.findElementBy(*Home_Page.Product1)
        p6=self.driver.findElementBy(*Home_Page.Product1)


        
     items = []
     row_id = 1
     while True:
        try:
          item = DataManager.getDictionaryTableFromExcell(f"select [ProductName] FROM [Items$] WHERE RowID={row_id}")[0]['ProductName']
          items.append(item)
          row_id += 1
        except IndexError:
         break 
     items.sort()  
     
     for ite in items:
        print("Item from Excel:", ite)
     """   


"""
def Validate_Sorting_Name_From_A_Z(self):
     
     items1= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=1")[0]['ProductName']
     items2= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=2")[0]['ProductName']
     items3= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=3")[0]['ProductName']
     items4= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=4")[0]['ProductName']
     items5= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=5")[0]['ProductName']
     items6= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=6")[0]['ProductName']
     items = [items1, items2, items3, items4, items5, items6]
     items.sort()
     

     self.Sorting_Name_From_A_Z()

     product1=self.driver.findElementBy(*Home_Page.Product1).text
     product2=self.driver.findElementBy(*Home_Page.Product2).text
     product3=self.driver.findElementBy(*Home_Page.Product3).text
     product4=self.driver.findElementBy(*Home_Page.Product4).text
     product5=self.driver.findElementBy(*Home_Page.Product5).text
     product6=self.driver.findElementBy(*Home_Page.Product6).text
     products = [product1, product2, product3, product4, product5, product6]

     is_sorted = (products == items)
     for item in items:
        print("Item from Excel:", item)

     print(" ")

     for pro in products:
       print("Sorted Products:", pro)

     if (products == items):
       return Reporter.passed("Sorting Name from A to Z passed")
       print("Is sorted:", is_sorted)

     else:
         return  Reporter.failed("Validate Sorting Name from A to Z Failed for {0}")


"""

"""
def Validate_Sorting_Name_From_Z_A(self):
     items1= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=1")[0]['ProductName']
     items2= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=2")[0]['ProductName']
     items3= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=3")[0]['ProductName']
     items4= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=4")[0]['ProductName']
     items5= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=5")[0]['ProductName']
     items6= DataManager.getDictionaryTableFromExcell("select [ProductName] FROM [Items$] WHERE RowID=6")[0]['ProductName']
     items = [items1, items2, items3, items4, items5, items6]
     items.sort(reverse=True)
     
     self.Sorting_Name_From_Z_A()
     product1=self.driver.findElementBy(*Home_Page.Product1).text
     product2=self.driver.findElementBy(*Home_Page.Product2).text
     product3=self.driver.findElementBy(*Home_Page.Product3).text
     product4=self.driver.findElementBy(*Home_Page.Product4).text
     product5=self.driver.findElementBy(*Home_Page.Product5).text
     product6=self.driver.findElementBy(*Home_Page.Product6).text

     products = [product1, product2, product3, product4, product5, product6]

     is_sorted = (products == items)
     for item in items:
        print("Item from Excel:", item)

     print(" ")

     for pro in products:
       print("Sorted Products:",pro)

     print(" ")  

     if (products == items):
         return Reporter.passed("Sorting Name from Z to A passed")
         print("Is sorted:", is_sorted)
     else:
         return Reporter.failed("Validate Sorting Name from Z to A Failed for {0}")

"""