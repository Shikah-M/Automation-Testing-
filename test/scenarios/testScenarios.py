
from lib.reporter import Reporter
from lib.globals import Globals
from test.pages.loginPage import LoginPage
from test.pages.Home_page import Home_Page
from test.pages.APIs_Test import APIs
from lib.browsing import Browsing
p = Browsing()
class TestScenarios:
    
    @staticmethod
    


    def Validate_Response_content_For_Get_All_ID(TestDataRow=dict()):
        APIs.Validate_response_content_Allget(TestDataRow) 

    def Validate_Response_content_For_Get_specificID(TestDataRow=dict()):   
        APIs.Validate_Response_Content_Get_specificID(TestDataRow)

    def  Validate_Creating_New_ID_Using_Post(TestDataRow=dict()):
        APIs.Validate_Using_Post(TestDataRow)  

    def Validate_Deleting_ID_Using_Delete(TestDataRow=dict()):
        APIs.validate_Using_Delete(TestDataRow)  

    def Validate_Updateing_ID_Using_Put(TestDataRow=dict()):
         APIs.Validate_Using_Put(TestDataRow)  
         
                

    def Validate_Login(TestDataRow=dict()):
        Globals.Test.Browser = p.openBrowser("chrome", Globals.Test.URL)
        try:
            login_page = LoginPage(Globals.Test.Browser)
            login_page.login(TestDataRow)
            #login_page.login_error_displayed()
        except Exception as error:            
            Reporter.failed("Validate Login Failed for {0}".format(error))
        #p.closeBrowser()    


    def Validate_Add_Item_To_Cart(TestDataRow=dict()):
        Globals.Test.Browser = p.openBrowser("chrome",Globals.Test.URL)
        login_page =LoginPage(Globals.Test.Browser)
        login_page.login(TestDataRow)
        try:
            ADDtocartVA= Home_Page(Globals.Test.Browser)
            ADDtocartVA.ADDTocartValidatopn(TestDataRow)
        except Exception as error: 
            Reporter.failed("Validate Add item to cart Failed for {0}".format(error))
        p.closeBrowser() 

    def Validate_CheckOut(TestDataRow=dict()):
        Globals.Test.Browser = p.openBrowser("chrome",Globals.Test.URL)
        login_page = LoginPage(Globals.Test.Browser)
        login_page.login(TestDataRow)
        try:
           CheckOut= Home_Page(Globals.Test.Browser)
           CheckOut.Validate_CheckOut(TestDataRow)
        except Exception as error:
            Reporter.failed("Validate CheckOut Failed for {0}".format(error))
        p.closeBrowser(TestDataRow) 

    def Validate_Sorting_Name_AtoZ(TestDataRow=dict()):
       # Globals.Test.Browser = p.openBrowser("chrome",Globals.Test.URL)
        #login_page = LoginPage(Globals.Test.Browser)
        #login_page.login(TestDataRow)
        try:
            SortingAtZ=Home_Page(Globals.Test.Browser)
            SortingAtZ.Validate_Sorting_Name_From_A_to_Z1(TestDataRow)
        except Exception as error:
            Reporter.failed("Validate Sorting Name from A to Z Failed for {0}".format(error))
            Reporter.info("here we sorting A to Z based of Excel sheet")
        #p.closeBrowser(TestDataRow) 

    def Validate_Sorting_Name_ZtoA(TestDataRow=dict()):
         # Globals.Test.Browser = p.openBrowser("chrome",Globals.Test.URL)
        #login_page = LoginPage(Globals.Test.Browser)
        #login_page.login(TestDataRow)
        try:
            SortingZtA=Home_Page(Globals.Test.Browser)
            SortingZtA.Validate_Sorting_Name_From_Z_to_A1(TestDataRow)
            #assert SortingZtA.Validate_Sorting_Name_From_Z_A.items == SortingZtA.Validate_Sorting_Name_From_Z_A.products, 'VAlidating sorting from A to Z failed'
            #if :   
        except Exception as error:
            Reporter.failed("Validate Sorting Name from Z to A Failed for {0}".format(error))
            Reporter.info("here we sorting A to Z based of Excel sheet")
        #p.closeBrowser(TestDataRow)  
    def Validate_Sorting_Price_Low_To_High(TestDataRow=dict()):
        # Globals.Test.Browser = p.openBrowser("chrome",Globals.Test.URL)
        #login_page = LoginPage(Globals.Test.Browser)
        #login_page.login(TestDataRow)
        try:
            Sorting_Price_L_H=Home_Page(Globals.Test.Browser)
            Sorting_Price_L_H.Validate_Sorting_Price_Low_High1(TestDataRow)
        except Exception as error: 
              Reporter.failed("Validate Sorting Price from Low to High Failed for {0}".format(error))
              Reporter.info("here we sorting price from low to High based of Excel sheet") 
              #p.closeBrowser(TestDataRow) 
    def Validate_Sorting_Price_High_To_Low (TestDataRow=dict()):
        # Globals.Test.Browser = p.openBrowser("chrome",Globals.Test.URL)
        #login_page = LoginPage(Globals.Test.Browser)
        #login_page.login(TestDataRow)
        try:
            Sorting_Price_H_L=Home_Page(Globals.Test.Browser)
            Sorting_Price_H_L.Validate_Sorting_Price_High_Low1(TestDataRow)
        except Exception as error: 
              Reporter.failed("Validate Sorting Price from High to Low Failed for {0}".format(error))
              Reporter.info("here we sorting price from High to Low based of Excel sheet") 
              p.closeBrowser(TestDataRow)           


    

    def conshop(TestDataRow=dict()):
        p.openBrowser("chrome",Globals.Test.URL)
        HP= Home_Page(Globals.Test.Browser)
        HP.HomePage(TestDataRow)
        p.closeBrowser()   

    def ADDpro(TestDataRow=dict()):
        p.openBrowser("chrome",Globals.Test.URL)
        AP= Home_Page(Globals.Test.Browser)
        AP.HomePage(TestDataRow)
        p.closeBrowser()      
   



