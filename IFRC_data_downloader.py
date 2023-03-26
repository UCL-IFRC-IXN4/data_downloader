from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time


def IFRC_data_downloader(url="https://go.ifrc.org/reports/all"):
    # Specify the download directory
    dir = os.getcwd()
    new_filename = "IFRC-data.csv"

    # remove the file if it already exists so that it can be replaced/updated
    if os.path.exists(dir + "/" + new_filename):
        os.remove(new_filename)

    len_dir = len([f for f in os.listdir(".") if os.path.isfile(f)])

    # Create Chrome webdriver options and then make the webdriver
    options = Options()
    options.add_experimental_option("prefs", {"download.default_directory": dir})
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(5)

    # Click the "Export Table" button
    export_button = driver.find_element(
        By.CSS_SELECTOR,
        "button.button.button--primary-bounded.button-small.styles_export-button__1oWc-",
    )
    export_button.click()

    # Wait for the download to complete
    while not any(filename.startswith("field") for filename in os.listdir(dir)):
        time.sleep(1)

    driver.quit()

    # rename the file
    if len([f for f in os.listdir(".") if os.path.isfile(f)]) > len_dir:
        temp_dir = [f for f in os.listdir(".") if os.path.isfile(f)]
        for f in temp_dir:
            if f.startswith("field"):
                os.rename(f, new_filename)
                break
