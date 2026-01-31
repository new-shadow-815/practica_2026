import json
import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller


def human_sleep(a=1.5, b=3.5):
    time.sleep(random.uniform(a, b))


config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(config_path, encoding="utf-8") as f:
    data = json.load(f)


def test_user_scenario():
    chromedriver_autoinstaller.install()

    options = webdriver.ChromeOptions()

    # Маскировка Selenium
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Убираем navigator.webdriver
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
            """
        },
    )

    driver.get(data["url"])
    human_sleep(3, 5)

    search_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "searchInput"))
    )
    assert search_input.is_displayed()

    search_input.send_keys(data["search_query"])
    human_sleep()

    driver.find_element(By.ID, "applySearchBtn").click()
    human_sleep(4, 6)

    products = driver.find_elements(By.CLASS_NAME, "product-card")
    assert len(products) > 0

    driver.quit()
