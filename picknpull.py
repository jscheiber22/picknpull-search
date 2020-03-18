from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
import re

class PickNPull:
    # This initializes the instance with the specified make and model along with the zip code and search radius defaulted to 95648 and 50 respectively.
    def __init__(self, model, startYear = None, endYear = None, zipcode = "95648", searchRadius = "50", verbose = False):
        # At this point, this is simply an arbitrary determination of the values Pick N Pull has assigned to the makes and models and uses for their searching feature.
        # I figured that most model names are unique to their makes, so simply searching for the model would make the searching process simpler.
        if model == "IS300":
            self.makeValue = 170
            self.modelValue = 3320
        elif model == "WRX":
            self.makeValue = 226
            self.modelValue = 4155
        elif model == "IMPREZA":
            self.makeValue = 226
            self.modelValue = 4153
        elif model == "ACCORD":
            self.makeValue = 145
            self.modelValue = 2366
        else: # Defaults the values to IS300 because it is by far the coolest
            self.makeValue = 170
            self.modelValue = 3320

        self.zipcode = zipcode
        self.searchRadius = searchRadius

        # Adding the headless option allows the browser to open without a GUI. This makes the program far more user friendly.
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

        # COMMENT OUT THE ABOVE THREE LINES AND UNCOMMENT THIS ONE IF YOU WANT TO SEE THE BROWSER WINDOW
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())

        if startYear == None or endYear == None:
            self.yearSearch = ""
            if verbose:
                print("Searching for " + model + "s within " + str(self.searchRadius) + " miles of " + str(self.zipcode) + ".")
        else:
            self.yearSearch = str(startYear) + "-" + str(endYear)
            if verbose:
                print("Searching for " + model + "s between years " + self.yearSearch + " within " + str(self.searchRadius) + " miles of " + str(self.zipcode) + ".")

        # Updates the page before it gets called and whanot
        self.updatePage()

    # This method does the search for the results found in the page parsed above.
    def search(self):
        self.driver.get(self.page)
        findings = self.driver.find_elements_by_xpath("//*[contains(text(), 'Displaying')]")
        originalFindingsCount = 0

        for finding in findings:
            # The HTML uses a template of "Displaying x vehicles" per site that it finds. This bit of code removes everything except that 'x' value and adds them all together.
            # The main point of this would be to keep a running list of the number of found vehicles to update the user when a new one is posted.
            number = re.search(r'\d', finding.text)
            originalFindingsCount += int(number.group())


        # Pick N Pull plays rude and still shows the results for all years if you input a specified year range, fucking up all my data. So this fixes that.
        if self.yearSearch != "":
            self.yearSearch = ""
            self.updatePage()
            self.driver.get(self.page)
            findings = self.driver.find_elements_by_xpath("//*[contains(text(), 'Displaying')]")
            allYearsFindingsCount = 0

            for finding in findings:
                number = re.search(r'\d', finding.text)
                allYearsFindingsCount += int(number.group())

            # If there was a difference, it will return that difference rather than the loser fake value pick n pull gave us because they suck >:(
            return str(originalFindingsCount - allYearsFindingsCount)

        # After adding all of these values together and possibly removing some, it returns the value so that it can be addressed however the user so desires.
        return str(originalFindingsCount)

    # A cute little splice for all of the information that was provided to the class when it was initialized.
    def updatePage(self):
        self.page = "https://www.picknpull.com/check_inventory.aspx?Zip=" + str(self.zipcode) + "&Make=" + str(self.makeValue) + "&Model=" + str(self.modelValue) + "&Year=" + self.yearSearch + "&Distance=" + str(self.searchRadius)