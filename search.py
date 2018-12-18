from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import initScrap
import sys


def locationSearch(inputList, outPutFile):
    browser = webdriver.Chrome('C:/Users/Garre/Downloads/chromedriver_win32/chromedriver')
    outList = []

    for i in inputList:
        browser.get('https://google.com')
        searchBar = browser.find_element_by_name('q')
        searchBar.send_keys(i)
        searchBar.send_keys(Keys.ENTER)

        try:
            button = browser.find_element_by_class_name('cMjHbjVt9AZ__button')
            button.send_keys(Keys.ENTER)
        except Exception:
            continue

        try:
            elems = browser.find_element_by_class_name('yYlJEf').get_attribute('href')
            print(elems)
            if elems.find('maps') == -1:
                outList.append(elems)

        except Exception:
            continue

    browser.close()
    emailList = []

    for i in outList:
        print(i)
        emailList.append(initScrap.grabEmail(i))

    writeOut(emailList,outPutFile)


def genericSearch(inputList, outPutFile):
    browser = webdriver.Chrome('C:/Users/Garre/Downloads/chromedriver_win32/chromedriver')
    outList = []

    for i in inputList:
        browser.get('https://google.com')
        searchBar = browser.find_element_by_name('q')
        searchBar.send_keys(i)
        searchBar.send_keys(Keys.ENTER)

        try:
            button = browser.find_element_by_class_name('cMjHbjVt9AZ__button')
            button.send_keys(Keys.ENTER)
        except(Exception):
            continue

        try:
            elem = browser.find_elements_by_class_name('yYlJEf').get_attribute('href')
            if(elem.find('maps') == -1):
                outList.append(browser.find_element_by_class_name('yYlJEf').get_attribute('href'))
        except(Exception):
            continue

    browser.close()

    for i in outList:
        initScrap.grabEmail(i, outPutFile)


def writeOut(email, outFile):
    file = open('emailList.txt', 'a')
    if not email:
        return
    print(email)
    for i in email:
        file.write(i)
    file.write('\n')
    file.close()


def parseInputFile(inputFile):
    outList = []
    file = open(inputFile, 'r')
    currElem = ''
    for i in file.read():
        if i.isalnum():
            currElem += i
        elif i == '\n':
            outList.append(currElem)
            currElem = ''

    return outList


def handleInput():
    if len(sys.argv) > 4:
        print('Too many command arguments')
        exit(1)
    elif len(sys.argv) < 4:
        print('Too little command arguments')
        exit(1)

    inputFile = sys.argv[1]
    outPutFile = sys.argv[2]
    typeOfSearch = sys.argv[3]

    inputList = parseInputFile(inputFile)

    if typeOfSearch == '1':
        locationSearch(inputList, outPutFile)
    elif typeOfSearch == '2':
        genericSearch(inputList, outPutFile)
    else:
        print("type of search not found")
        exit(1)

handleInput()