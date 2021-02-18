from msedge.selenium_tools import Edge
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from msedge.selenium_tools import EdgeOptions


URL= 'https://ucstudent.uc.pt/login'
LOGIN_EMAIL= 'uc2018298209@student.uc.pt'
LOGIN_PASSWORD= 'coimbraEVER2000'

def test_source():
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument('headless')
    edge_options.add_argument('disable-gpu')
    driver = Edge(executable_path='msedgedriver.exe', options=edge_options)
    driver.get(URL)
    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/form/div[1]/div/input')))

    email_input= driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/form/div[1]/div/input')    
    pass_input= driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/form/div[2]/div/input')    
    email_input.send_keys(LOGIN_EMAIL)
    pass_input.send_keys(LOGIN_PASSWORD)
    
    login_button= driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/form/div[3]/button')    
    login_button.click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div/div[1]/div/div[2]/p')))
    
    try:
        enter_class_button= driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div[7]/div/div[8]/button[1]')    
        enter_class_button.click()
    
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div/div/div[4]/div/div[3]/div/button[2]')))

        online_presence= driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div[4]/div/div[3]/div/button[2]')    
        online_presence.click()

        presence_check= driver.find_element_by_xpath('/html/body/div[2]/div[2]/footer/button[2]')    
        presence_check.click()
        driver.quit()
        return 'done bro, you checked your presence, you can go back to sleep now'
    except: 
        driver.quit()
        return 'doesn\'t exist a class running right now bro'

if __name__=='__main__':
    print(test_source())