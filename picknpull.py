from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re

class PickNPull:
    def __init__(self, make, model, zipcode = "95648", searchRadius = "100"):
        if make == "Lexus":
            self.makeValue = 170
        else:
            self.makeValue = 170
        if model == "IS300":
            self.modelValue = 3320
        else:
            self.modelValue = 3320
        self.zipcode = zipcode
        self.searchRadius = searchRadius

    def search(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.page = "https://www.picknpull.com/check_inventory.aspx?Zip=" + str(self.zipcode) + "&Make=" + str(self.makeValue) + "&Model=" + str(self.modelValue) + "&Distance=" + str(self.searchRadius)
        # page = "https://www.picknpull.com/check_inventory.aspx?Zip=95648&Make=170&Model=3320&Distance=50"
        self.driver.get(self.page)
        findings = self.driver.find_elements_by_xpath("//*[contains(text(), 'Displaying')]")
        findingsCount = 0
        for finding in findings:
            number = re.search(r'\d', finding.text)
            findingsCount += int(number.group())
        return str(findingsCount)