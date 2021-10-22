from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path="C:\\Users\\karlm\\Documents\\Browser_Drivers\\geckodriver.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Uzytkownik dowiedzial sie o nowej aplikacji dostepnej pod adresem...
        # U. otwiera strone glowna aplikacji...
        self.browser.get('http://localhost:8000')

        # user zwrocil uwage ze tytul i naglowek zawiera slowo listy
        self.assertIn('Listy', self.browser.title)
        self.fail('zakonczenie testu')

    if __name__ == '__main__':
        unittest.main(warnings='ignore')

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
