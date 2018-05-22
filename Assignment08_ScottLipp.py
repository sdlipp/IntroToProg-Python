'''
Title:  Assignment 08 - Working with Objects and Classes
Developer:  Scott Lipp
Created on:  5/21/2018
Class:  IT FDN 100 A: Intro to Programming (Python)
Change Log:  N/A
Purpose:    This program allows a user to import a simple list using an object class.
            A loop allows the user to enter more items until they choose to quit.
            The list is then written back to a text file in the same format it was
            read from.
'''

#Global Variables
objFileLoc = "C:\_PythonClass\ProdInventory.txt"
listInventory = []
strHeader = "ID, Name, Price\n" \
            "---------------"
strMenuOptions = "\nOptions:\n" \
                 "--------\n" \
                "1: Display Data\n" \
                "2: Add Data\n" \
                "3: Save Data\n" \
                "4: Exit Program"

class Product(object):
    """For defining rows of a list by their ID, Name and Price"""

    #Fields
    __ItemCounter = 1       #Allows the ID to be auto-generated to user unique, sequential numbering
    __ProdID = ""           #Private attribute for ProductID accessed by properties
    __ProdName = ""         #Private attribute for ProductName accessed by properties
    __ProdPrice = ""        #Private attribute for ProductPrice accessed by properties

    #Constructors
    def __init__(self, ProdName, ProdPrice):        #For defining a newly created object of the 'Product' class
        self.ProdID = str(Product.__ItemCounter)    #Creates ID using auto-counter, converts to string
        self.ProdName = ProdName                    #Creates Product Name
        self.ProdPrice = ProdPrice                  #Creates Product Price
        Product.__ItemCounter += 1                  #Increases the counter by 1 for the next entry

    #Properties
    @property                       #Public property for displaying private ProdID attribute
    def ProdID(self):
        return self.__ProdID

    @ProdID.setter                  #Public property for setting a ProdID attribute for an object in Product class
    def ProdID(self, ProdID = ""):
        self.__ProdID = ProdID

    @property                       #Public property for displaying private ProdName attribute
    def ProdName(self):
        return self.__ProdName

    @ProdName.setter                #Public property for setting a ProdName attribute for an object in Product class
    def ProdName(self, ProdName = ""):
        self.__ProdName = ProdName

    @property                       #Public property for displaying private ProdPrice attribute
    def ProdPrice(self):
        return self.__ProdPrice

    @ProdPrice.setter               #Public property for setting a ProdPrice attribute for an object in Product class
    def ProdPrice(self, ProdPrice = ""):
        self.__ProdPrice = ProdPrice

    #Methods
    def __str__(self):              #For displaying each set of product information (ID, Name, Price) as a string
        return self.ProdID + ", " + self.ProdName + ", $" + self.ProdPrice


class InputOutput(object):
    """For allowing the user to interface with the list (view, add, save)"""

    @staticmethod
    def DataLoad(fileName):
        """For loading data from a comma-separated text file into objects of the 'Product' class"""

        __listInv = []      #Empty list created so .append method can be used below

        try:
            objTxtFile = open(fileName, "r")
            #Iterate over each row of data in the text file
            for entry in objTxtFile:
                #Separate ID, Name, Price by a comma into separate components
                tplProd = entry.strip().split(",")
                #Discard ID, pass Name and Price -- absent '$' -- into Product class to create new objects
                #For consistency, '$' added in other code so needs to be removed here to avoid duplicates
                objProd = Product(str(tplProd[1]).strip(), str(tplProd[2]).strip().strip("$"))
                #Add each object into a list for storing in the run-time
                __listInv.append(objProd)
            objTxtFile.close()
            #Return the generated list to the code that called the function
            return __listInv
        except Exception as e:      #In case of error during data load/handling
            print(str(e))           #Error description displayed to user

    @staticmethod
    def DataDisplay(listName):
        """Display the list to the user in the run-time"""

        print("\n" + strHeader)
        for entry in listName:      #Extracts each object of the 'Product' class from the list
            print(entry)            #Uses the string method defined in the 'Product' class to display data

    @staticmethod
    def AddData():
        """Add new items to the list"""

        #Get input from user on Product Name.  Loop through if empty string is returned to force an entry
        while True:
            strProdName = input("Enter the name of a Product: ").strip().title()
            if strProdName == "":
                print("\nAn empty string is not a valid entry for a name.")
                continue
            else: break
        #Get input from user on Product Price.  Loop through if empty string is returned to force an entry
        while True:
            #User may enter '$' sign; strip it out since it will be added later
            strProdPrice = input("Enter the price of '" + strProdName + "': ").strip().strip("$")
            if strProdPrice == "":
                print("\nAn empty string is not a valid entry for price.")
                continue
            else: break
        objProd = Product(strProdName, strProdPrice)    #Create new object of the Product class
        return objProd                                  #Return the new object of Product class

    @staticmethod
    def SaveData(listName, fileName):
        """Save data to file in a comma separated file"""

        #Utilize 'try/except' block to catch any errors from the data-write step
        try:
            objTxtFile = open(fileName, "w")            #Open file in write mode to re-write the contents
            for entry in listName:                      #Iterates over each 'Product' object in the list
                objTxtFile.write(str(entry) + "\n")     #Writes each entry using string method in 'Product'
            objTxtFile.close()
            print("\nFile was saved here: " + objFileLoc)
        except Exception as e:                          #Catch error and code
            print(str(e))                               #Display error code to user

    @staticmethod
    def MenuLoop(listName):
        """Loop through a list of Menu options indefinitely to view, add, save list to file
         until user chooses to exit"""

        while True:
            #Display the Menu to the user
            print(strMenuOptions)
            strUserOption = input("\nPlease enter the option number followed by 'enter': ")
            #Option 1: Display list to user. Call 'DataDisplay' method
            if strUserOption == "1":
                InputOutput.DataDisplay(listName)
            #Option 2: Add new item to the list. Call 'AddData' method
            elif strUserOption == "2":
                listName.append(InputOutput.AddData())
            #Option 3: Save the list. Call 'SaveData' method
            elif strUserOption == "3":
                InputOutput.SaveData(listName, objFileLoc)
            #Option 4: Quit program. Provide options to continue program and save list prior to exiting
            elif strUserOption == "4":
                strQuit = input("Are you sure you'd like to quit? (y/n): ")
                if strQuit.lower()[0] == "y":       #Provide flexibility: look for first letter of 'y'
                    strSave = input("Would you like to save before quitting? (y/n): ")
                    if strSave.lower()[0] == "y":   #Provide flexibility: look for first letter of 'y'
                        InputOutput.SaveData(listName, objFileLoc)
                        break
                    else: break
                else: continue
            else: print("\nInvalid selection. Please enter a valid option from the menu.")

#------------Main Program----------------#

#Create the initial list from file, if it exists.
listInventory = InputOutput.DataLoad(objFileLoc)

#Dispay data to user before beginning the Menu Loop
InputOutput.DataDisplay(listInventory)

#Initiate the loop that will call the rest of the necessary methods
InputOutput.MenuLoop(listInventory)

#Pause the program so the user can view it before it closes
input("\nPress enter to close the program.")

