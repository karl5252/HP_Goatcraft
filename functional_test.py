from selenium import webdriver

browser = webdriver.Firefox(executable_path="C:\\Users\\karlm\\Documents\\Browser_Drivers\\geckodriver.exe")
browser.get('http://localhost:8000')
# naglowek zawiera slowo listy
assert 'Listy' in browser.title, 'Browser title is: ' + browser.title
# uzytkownik zostaje zachecony aby wpisac rzecz doz robienia
# w polu tekstoowym wpisal 'kupic pawie piora'
# po nacisnieicu klawisza enter storna zostala uaktualniona i wyseietla
# "1.kupic prawie piora"

# Na stronie nadal znajduje sie pole tekstowe zachecajca eo dodania kolejnego zadania
# uzytkownik wpisal 'uzyc pior do stowrzenia przynety"

# strona zostala znowu uaktualniona

# Uzytkownik potrzebuje aby strona zapamietala jego liste
# zosal wygenerowany unikatowy adres url wraz z testekm z wyjasnieniem

# pod podanym adresem zostaje wyswietlona lista reczy do zrobienia

browser.quit()