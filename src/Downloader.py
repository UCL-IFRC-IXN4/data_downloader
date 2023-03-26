from abc import ABC, abstractmethod
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Downloader(ABC):
    @abstractmethod
    def __init__(self, url, source=None):
        self.dir = os.getcwd()
        self.source = source
        self.target = None

    @abstractmethod
    def download(self):
        pass

    def specify_target_directory(self):
        """
        Helper function that tells the downloader where to download the file to.
        :param source: The source of the data
        """
        self.target = self.source + "-data.csv"

    @abstractmethod
    def srape(self):
        pass

    def remove_existing_file(self):
        """
        Helper function that removes the existing file if it already exists.
        """
        # remove the file if it already exists so that it can be replaced/updated
        if os.path.exists(self.dir + "/" + self.target):
            os.remove(self.target)

    def create_webdriver(self):
        """
        Helper function that creates a new Chrome webdriver instance.
        """
        # Create Chrome webdriver options
        options = Options()
        options.add_experimental_option("prefs", {"download.default_directory": dir})

        # Create a new Chrome webdriver instance
        self.driver = webdriver.Chrome(options=options)

    def kill_webdriver(self):
        """
        Helper function that kills the webdriver instance.
        """
        self.driver.quit()

    def wait_for_page_load(self):
        """
        Helper function that waits for the download to complete.
        """
        time.sleep(5)

    @abstractmethod
    def rename_file(self):
        pass


class IDMCDownloader(Downloader):
    def __init__(
        self,
        url="https://www.internal-displacement.org/database/displacement-data",
        source="IDMC",
    ):
        super().__init__(url)

    def remove_README_file(self):
        # removes the readme file if downloaded
        if os.path.exists(self.dir + "/" + "ReadMeFile_GIDD.docx"):
            os.remove("ReadMeFile_GIDD.docx")


class EMDATDownloader(Downloader):
    def __init__(self, url="https://public.emdat.be/login", source="EMDAT"):
        super().__init__(url)

    def login(self):
        pass


class IFRCDownloader(Downloader):
    def __init__(self, url="https://go.ifrc.org/reports/all", source="IFRC"):
        super().__init__(url)
