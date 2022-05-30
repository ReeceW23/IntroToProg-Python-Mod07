# Title: Working with Error Handling and Pickling
# Dev: Reece Wonio
# Date: May 27th, 2022
# Change Log: (Who, When, What)
# (Reece Wonio, 5/27/2022, Created Script)
#----------------------------------------------------------------------------------------------------------------------#

# Working with Pickles ------------------------------------------------------------------------------------------------#
import pickle # This is imports the pickle module which is stored in python and allows us to pickle the binary data

# Data ----------------------------------------------------------------------------------------------------------------#
# Pickled Objects cannot be stored as text, they must be saved as a binary file, note the .dat
strPickleFile = 'Pickle_Data.dat'
lstPickle = []
# Processing ----------------------------------------------------------------------------------------------------------#
def save_data_to_file(pickle_file, list_of_data): # Function that will save our data to the binary data file
    file = open(pickle_file, "wb") # Note the b at the end of wb, it must be added when working w/ a binary file
    pickle.dump(list_of_data, file)
    # This references the pickle module and the .dumb function stores the data into our binary pickle file
    file.close()

def read_data_from_file(pickle_file): # Function that will read our binary data file.
    file = open(pickle_file, "rb")
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data

# Presentation --------------------------------------------------------------------------------------------------------#

# Using the Try, Except class for structured error handling. This is to catch the divide by zero error
try:
      print("Which Numbers Would you Like to Divide?")
      fltNumberOne = float(input("Enter First Number: "))
      fltNumberTwo = float(input("Enter Second Number: "))
      lstPickle = [fltNumberOne / fltNumberTwo]

      save_data_to_file(strPickleFile, lstPickle)

      print(read_data_from_file(strPickleFile))
except:
    print("There was an Error. Did you Enter a Non-Number or Divide by Zero?")


