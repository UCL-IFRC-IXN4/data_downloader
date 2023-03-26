from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

url = "https://public.emdat.be/login"

check_box = "svg-inline--fa.fa-square.fa-w-14.rct-icon.rct-icon-uncheck"


def EMDAT_data_downloader(url=url):
    # Specify the download directory
    dir = os.getcwd()
    new_filename = "EMDAT-data.csv"

    # enter your login details here
    email = ""
    password = ""

    # remove the file if it already exists so that it can be replaced/updated
    if os.path.exists(dir + "/" + new_filename):
        os.remove(new_filename)

    len_dir = len([f for f in os.listdir(".") if os.path.isfile(f)])

    # Create Chrome webdriver options
    options = Options()
    options.add_experimental_option("prefs", {"download.default_directory": dir})

    # Create a new Chrome webdriver instance
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(2)

    email_field = driver.find_element(By.ID, "user")
    email_field.click()
    email_field.send_keys(email)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    login_button = driver.find_element(By.CLASS_NAME, "button")
    login_button.click()

    # Wait for the page to load
    time.sleep(1)

    # Click the "Access Tool" button
    export_button = driver.find_element(By.CLASS_NAME, "MuiButton-label")
    export_button.click()

    # Wait for the page to load
    time.sleep(1)

    # Click on all the data we want and then click the download button,
    # there are 8 items and they use the same class name
    for i in range(8):
        button = driver.find_element(By.CLASS_NAME, check_box)
        button.click()

    # Scroll down to the download button and click it
    driver.execute_script("window.scrollBy(0, 100);")
    download_button = driver.find_element(By.CLASS_NAME, "MuiButton-label")
    download_button.click()

    # # Wait for the download to complete
    while not any(filename.startswith("emdat") for filename in os.listdir(dir)):
        time.sleep(1)

    # Close the browser
    driver.quit()

    # rename the file
    if len([f for f in os.listdir(".") if os.path.isfile(f)]) > len_dir:
        temp_dir = [f for f in os.listdir(".") if os.path.isfile(f)]
        for f in temp_dir:
            if f.startswith("emdat_public"):
                os.rename(f, new_filename)
                break
