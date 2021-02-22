from json import *
from ListScreen import *

def main():
    with open('./URLDatabase.json', mode='r', encoding='utf-8') as jsonfile: database= load(jsonfile)
    screen= CoursesWindow(database)
    screen.listingBox()
    screen.window.mainloop()

if __name__=='__main__': main()