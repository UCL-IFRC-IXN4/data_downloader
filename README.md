# data_downloader

Data downloader for DesInventar, IFRC, IDMC and EMDAT

for IFRC, IDMC and EMDAT, ensure that you have selenium installed.

## Installation

```
git clone https://github.com/UCL-IFRC-IXN4/data_downloader.git
cd data_downloader
```

## Requirements

```
pip install selenium
```

### Note for Selenium module

Ensure that you install a chrome webdriver and that its for the correct version of chrome installed on your machine.

To check the version of chrome:

[Chrome Version](chrome://settings/help)

Webdriver installation:

[Webdriver](https://sites.google.com/chromium.org/driver/)

## Usage

### Functions

```
def get_csv(country_code):
    """
    Downloads the csv file for the given country code
    :param country_code: the country code to download the csv for
    """

def clean_col(country_code):
    """
    Cleans the column names for the given country code
    :param country_code: the country code to clean the column names for
    """

def translate_file(country_code):
    """
    Translates the csv file for the given country code
    :param country_code: the country code to translate the csv for
    """
```

### Usage

to do this, run this command in terminal:

```
python3 main.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

- Dylan Penney [@DylanPenney](https://www.github.com/DylanPenney)
- Omung Bhasin [@Omung789](https://www.github.com/Omung789)
- Ryan Lock [@RyanLockQr](https://www.github.com/RyanLockQr)
- Hogan Ma [@HoganMa23](https://www.github.com/HoganMa23)
