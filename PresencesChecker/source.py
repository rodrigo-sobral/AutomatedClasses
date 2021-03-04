from ElementAccesser import *
from json import load

def loadJSONData() -> dict:
    with open('./DataFile.json', encoding='utf-8', mode='r') as json_reader: return load(json_reader)

def main():
    data= loadJSONData()
    #   Access Login Page
    accesser= ElementAccesser(data['url'])
    accesser.wait4Element('//*[@id="app"]/div/div/div/div[2]/div/div/form/div[1]/div/input')
    
    email_input= accesser.findElement('//*[@id="app"]/div/div/div/div[2]/div/div/form/div[1]/div/input')
    pass_input= accesser.findElement('//*[@id="app"]/div/div/div/div[2]/div/div/form/div[2]/div/input')
    login_button= accesser.findElement('//*[@id="app"]/div/div/div/div[2]/div/div/form/div[3]/button')    
    
    #   Input Login Data
    accesser.inputInElement(email_input, data['email'])
    accesser.inputInElement(pass_input, data['pass'])
    accesser.clickInElement(login_button)

    #   Failed Login
    if accesser.findElement('//*[@id="app"]/div/div/div/div[2]/div/div/form/article/section/div/div/div/div[1]/p')!=False: return '\nyou have configured a wrong email or password'
    #   Not Having Classes
    if accesser.wait4Element('//*[@id="app"]/div/div[1]/div/div/div/div/div[7]/div')==False:  return accesser.quitBrowser('\nbro, you dont even are having a class, get a life nerd!')
             
    try:
        #   Iterate All Classes of Today
        class_id, presences_checked= 6, 0
        while True:
            #   get the class div
            class_div= accesser.findElement('//*[@id="app"]/div/div[1]/div/div/div/div/div[{}]/div'.format(class_id))
            
            #   when we iterated all the classes and the presences are checked
            if not class_div: return '\ndone bro, you checked {} presences, you can go back to sleep now'.format(presences_checked)
            
            #   if the class div has green background means it is running
            if accesser.checkBackgroundElement(class_div, 'rgba(3, 164, 121, 1)'): 
                
                #   get the button to enter in the class
                enter_class_button= accesser.findElement('//*[@id="app"]/div/div[1]/div/div/div/div/div[{}]/div/div[8]/button[1]'.format(class_id))
                accesser.clickInElement(enter_class_button)
                
                online_presence= accesser.findElement('//*[@id="app"]/div/div[1]/div/div/div/div/div/div[4]/div/div[3]/div/button[2]')
                #   waits until the checking button appears, if doesn't, means that the class is closed and go to the main menu
                if online_presence==False:
                    accesser.clickInElement(accesser.findElement('//*[@id="app"]/div/div[1]/div/div/div/div/div/div[4]/button'))
                    class_id+=1
                    continue

                #   otherwise, checks the presence
                if not accesser.checkBackgroundElement(online_presence, 'rgba(3, 164, 121, 1)'):
                    accesser.clickInElement(online_presence)
                    accesser.wait4Element4Ever('/html/body/div[2]/div[2]/footer/button[2]')
                    accesser.clickInElement(accesser.findElement('/html/body/div[2]/div[2]/footer/button[2]'))
                    presences_checked+=1

                #   and we go back to the main menu
                accesser.clickInElement(accesser.findElement('//*[@id="app"]/div/div[1]/div/div/div/div/div/div[5]/button'))
            class_id+=1
    except: return accesser.quitBrowser('\ndoesn\'t exist a class running right now bro')

if __name__=='__main__': print(main())