from selenium import webdriver

browser = webdriver.Firefox(executable_path="C:\\Users\\karlm\\Documents\\Browser_Drivers\\geckodriver.exe")
browser.get('http://localhost:8000')

assert 'The install worked successfully! Congratulations!' in browser.title