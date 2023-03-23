from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

def IFRC_data_downloader(url="https://go.ifrc.org/reports/all"):
    # Specify the download directory
    dir = os.getcwd()
    len_dir = len([f for f in os.listdir('.') if os.path.isfile(f)])
    new_filename = "IFRC-data.csv"

    #remove the file if it already exists so that it can be replaced/updated
    if os.path.exists(dir + "/" + new_filename):
        os.remove(new_filename)

    # Create Chrome webdriver options
    options = Options()
    options.add_experimental_option("prefs", {"download.default_directory": dir})

    # Create a new Chrome webdriver instance
    driver = webdriver.Chrome(options=options)

    # Load the reports page
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    # Click the "Export Table" button
    export_button = driver.find_element(By.CSS_SELECTOR, "button.button.button--primary-bounded.button-small.styles_export-button__1oWc-")
    export_button.click()

    # Wait for the download to complete
    while not any(filename.startswith("field") for filename in os.listdir(dir)):
        time.sleep(1)

    #rename the file    
    if len([f for f in os.listdir('.') if os.path.isfile(f)]) > len_dir:
        temp_dir =[f for f in os.listdir('.') if os.path.isfile(f)]
        for f in temp_dir:
            if f.startswith("field"):
                os.rename(f, new_filename)
                break
            
    # Close the browser
    driver.quit()
