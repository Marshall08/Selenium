from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import time

CHROMEDRIVER_PATH = "/Users/egormarsavin/Downloads/chromedriver-mac-x64/chromedriver"

def setup_driver():
    service = Service(CHROMEDRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def comnews():
    driver = setup_driver()
    try:
        driver.get("https://www.comnews.ru/news")
        time.sleep(5)
        headlines = []
        elements = driver.find_elements(By.CSS_SELECTOR, "div.title a")

        for element in elements:
            title = element.text.strip()
            if title:
                headlines.append({"Заголовки статей": title})

        with open("comnews_headlines.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Заголовки статей"])
            writer.writeheader()
            writer.writerows(headlines)

        print("Done")

    finally:
        driver.quit()

if __name__ == "__main__":
    comnews()

