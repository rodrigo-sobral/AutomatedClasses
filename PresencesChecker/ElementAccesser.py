from msedge.selenium_tools import Edge
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from msedge.selenium_tools import EdgeOptions

class ElementAccesser:

    def __init__(self, url: str):
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument('headless')
        edge_options.add_argument('disable-gpu')
        self.driver = Edge(executable_path='msedgedriver.exe', options=edge_options)
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver,10)

    def wait4Element(self, xpath:str): 
        try: self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except: return False
    def wait4Element4Ever(self, xpath:str):
        """Wait for an element forever"""
        while True:
            try: 
                self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                return
            except: continue
    
    def findElement(self, xpath:str): 
        """Find an element, if it doesn't exist, return False"""
        element=None
        try:
            element= self.driver.find_element_by_xpath(xpath)
            return element
        except: return False
    def inputInElement(self, element:object, content:str): element.send_keys(content)
    def clickInElement(self, element:object): 
        if element==False: raise '\nelement was not found and you tried to click it'
        else: element.click()

    def checkBackgroundElement(self, element:object, color:str):
        """Compares the background of an element.
        
        color must have the following format: rgba(r, g, b, a)"""
        if str(element.value_of_css_property('background-color'))==color: return True
        else: return False

    def quitBrowser(self, quit_message:str): 
        self.driver.quit()
        return quit_message
        