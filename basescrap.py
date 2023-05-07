from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)

class ComponentsTest(BaseCase):
    def test_basic(self):
        self.open("https://www.google.com")
