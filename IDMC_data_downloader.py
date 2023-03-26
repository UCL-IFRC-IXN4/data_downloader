from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

url = "https://www.internal-displacement.org/database/displacement-data"


regions = [
    "East Asia and Pacific",
    "Sub-Saharan Africa",
    "South Asia",
    "Europe and Central Asia",
    "Middle East and North Africa",
    "Americas",
]
countries = [
    "Abyei Area",
    "Afghanistan",
    "Albania",
    "Algeria",
    "American Samoa",
    "Angola",
    "Anguilla",
    "Antigua and Barbuda",
    "Argentina",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bangladesh",
    "Barbados",
    "Belgium",
    "Belize",
    "Benin",
    "Bermuda",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "British Virgin Islands",
    "Brunei Darussalam",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cayman Islands",
    "Central African Republic",
    "Chad",
    "Chile",
    "Colombia",
    "Comoros",
    "Congo",
    "Cook Islands",
    "Costa Rica",
    "d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Dem. People's Rep. Korea",
    "Dem. Rep. Congo",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Eritrea",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "French Guiana",
    "French Polynesia",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Greenland",
    "Grenada",
    "Guam",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hong Kong",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea",
    "Kosovo",
    "Kyrgyzstan",
    "Lao PDR",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Lithuania",
    "Luxembourg",
    "Macao",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Marshall Islands",
    "Martinique",
    "Mauritania",
    "Mauritius",
    "Mayotte",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nepal",
    "Netherlands",
    "New Caledonia",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Northern Mariana Islands",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Puerto Rico",
    "union",
    "Romania",
    "Russia",
    "Rwanda",
    "Samoa",
    "Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Slovakia",
    "Sint Maarten (Dutch part)",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "St. Kitts and Nevis",
    "St. Lucia",
    "St. Martin (French part)",
    "St. Vincent and the Grenadines",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Timor-Leste",
    "Togo",
    "Tokelau",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "rkiye",
    "Turks and Caicos Islands",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Venezuela",
    "Viet Nam",
    "Virgin Islands",
    "Yemen",
    "Zambia",
    "Zimbabwe",
    "China",
    "Slovak Republic",
]
hazard_categories = [
    "Earthquake",
    "Dry mass movement",
    "Volcanic eruption",
    "Flood",
    "Extreme temperature",
    "Wet mass movement",
    "Storm",
    "Drought",
    "Wildfire",
    "Mass movement",
    "Severe winter condition",
]


def IDMC_data_downloader(url=url):
    # Specify the download directory
    dir = os.getcwd()
    new_filename = "IDMC-data.csv"

    # remove the file if it already exists so that it can be replaced/updated
    if os.path.exists(dir + "/" + new_filename):
        os.remove(new_filename)

    len_dir = len([f for f in os.listdir(".") if os.path.isfile(f)])

    # Create Chrome webdriver options
    options = Options()
    options.add_experimental_option("prefs", {"download.default_directory": dir})

    # Create a new Chrome webdriver instance
    driver = webdriver.Chrome(options=options)

    # Load the reports page
    driver.get(url)

    # Wait for the page to load
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 100);")
    disaster_data_button = driver.find_element(By.XPATH, "//button[position()=2]")
    disaster_data_button.click()

    # gives time for the page to load
    wait = WebDriverWait(driver, 10)
    element_present = EC.presence_of_element_located(
        (By.XPATH, "//button[position()=1]")
    )
    wait.until(element_present)

    driver.execute_script("window.scrollBy(0, 100);")
    region_button = driver.find_element(By.NAME, "regions")

    # selects every possible region, country and hazard type so we download all the data
    for region in regions:
        region_button.send_keys(region)
        region_button.send_keys(Keys.ARROW_UP)
        region_button.send_keys(Keys.ENTER)
        region_button.send_keys(Keys.BACKSPACE * len(region))

    country_button = driver.find_element(By.NAME, "countries")

    for country in countries:
        country_button.send_keys(country)
        country_button.send_keys(Keys.ARROW_DOWN)
        country_button.send_keys(Keys.ENTER)
        country_button.send_keys(Keys.BACKSPACE * len(country))

    hazard_category_button = driver.find_element(By.NAME, "disasterType")

    for hazard in hazard_categories:
        hazard_category_button.send_keys(hazard)
        hazard_category_button.send_keys(Keys.ARROW_DOWN)
        hazard_category_button.send_keys(Keys.ENTER)
        hazard_category_button.send_keys(Keys.BACKSPACE * len(hazard))

    driver.execute_script("window.scrollBy(0, 600);")
    download_button = driver.find_element(By.NAME, "download")
    download_button.click()

    # # Wait for the download to complete
    while not any(filename.startswith("IDMC_GIDD") for filename in os.listdir(dir)):
        time.sleep(1)

    driver.quit()

    # rename the file
    if len([f for f in os.listdir(".") if os.path.isfile(f)]) > len_dir:
        temp_dir = [f for f in os.listdir(".") if os.path.isfile(f)]
        for f in temp_dir:
            if f.startswith("IDMC_GIDD"):
                os.rename(f, new_filename)
                break

    # removes the readme file if downloaded
    if os.path.exists(dir + "/" + "ReadMeFile_GIDD.docx"):
        os.remove("ReadMeFile_GIDD.docx")
