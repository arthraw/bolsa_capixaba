import glob
import logging
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.utils.variables import bronze_path

logger = logging.getLogger(__name__)


def file_downloaded(file_path):
    return os.path.exists(file_path)


def remove_old_data(old_path):
    files = glob.glob(os.path.join(old_path, '*'))
    for file in files:
        try:
            os.remove(file)
        except Exception as e:
            logger.error(f"{file} not exists. Details: {e}")


def download_files(driver):
    time.sleep(2)

    download_links = driver.find_elements(By.XPATH, '//a[contains(@href, ".csv")]')
    time.sleep(2)

    for i, link in enumerate(download_links):
        href = link.get_attribute('href')
        driver.execute_script("arguments[0].click();", link)

        file_name = href.split("/")[-1]
        file_path = os.path.join(bronze_path, file_name)

        while not file_downloaded(file_path):
            time.sleep(1)

        logger.info(f"{file_name} download completed.")

        time.sleep(4)


def open_browser(url: str):
    remove_old_data(bronze_path)
    chrome_options = Options()
    prefs = {
        "download.default_directory": bronze_path,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(driver_version="136.0.7103.59").install()),
        options=chrome_options
    )
    driver.get(url)
    time.sleep(2)
    download_files(driver)
    driver.quit()
