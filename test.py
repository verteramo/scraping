import re, json
from argparse import ArgumentParser, Namespace

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


DEFAULT_CONFIG_FILE = "conf.json"

# Ordered answers extraction
# Example: "a. Texto de la respuesta." -> "Texto de la respuesta."
PATTERN_MATCH_ANSWER = re.compile(r"^(?:[a-z]\.\s)?(?P<answer>.+)$")

# Right answers extraction
# Example: "Las respuestas correctas son: Respuesta 1., Respuesta 2." -> "Respuesta 1., Respuesta 2."
PATTERN_MATCH_RIGHT_ANSWER = re.compile(
    r"^(?:(?:La respuesta correcta es:?|Las respuestas correctas son:)\s)(?P<rightanswer>.+)$"
)


class Driver:
    def __init__(self, args: dict) -> None:
        self.__driver: webdriver.Edge = webdriver.Edge(**args)

    def nav(self, url: str) -> None:
        self.__driver.get(url)

    def type(self, path: str, text: str) -> None:
        self.__driver.find_element(By.XPATH, path).send_keys(text)

    def click(self, path: str) -> None:
        self.__driver.find_element(By.XPATH, path).click()

    def text(self, path: str) -> str:
        return self.__driver.find_element(By.XPATH, path).text

    def elements(self, path: str) -> list[WebElement]:
        return self.__driver.find_elements(By.XPATH, path)

    def wait(self, path: str, timeout: int = 10) -> None:
        WebDriverWait(self.__driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, path))
        )


def get_options() -> webdriver.ChromeOptions:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return dict(service=Service("drivers/msedgedriver.exe"), options=options)


def get_config() -> dict:
    parser = ArgumentParser(description="Scraps tests")
    parser.add_argument("-c", "--conf", type=str, default=DEFAULT_CONFIG_FILE)
    args = parser.parse_args()
    with open(args.config, "r") as file:
        return json.load(file)


def main():
    driver = Driver(get_options())

    


if __name__ == "__main__":
    main()
