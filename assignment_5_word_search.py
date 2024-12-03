# Assignment 5: Word Search and Counting Program

# Import required library
import os

# Get current working directory and display the current working directory
currentDirectory = os.getcwd()
print("Current Directory: " + currentDirectory)

# Ask user to change current working directory for the file they want to find
getDirectory = input("Please input the pathway for the folder your file is in: ") # In this case the pathway would be: /Users/andreaalmeda/Downloads/word_search/text1_folder
os.chdir(getDirectory)

# Get the new current working directory and display the new current working directory
currentDirectory = os.getcwd()
print("Current Directory: " + currentDirectory)

# Use a for loop to list all the files and folders in the current working directory
print("Files and folders in the current directory:")
for item in os.listdir(currentDirectory):
    print(item)

# Ask user to enter the name of the file they want to search
fileName = input("Enter the name of the file to search for with the file extension (e.g., .txt): ")

# Use an if else statement to check if the file is in the current working directory
if os.path.isfile(os.path.join(currentDirectory, fileName)):
    # Ask the user to enter the word they want to search the count of
    word = input("Enter the word to search for: ")

else:
    # If the file does not exist in the current working directory, ask user to re-enter the name of the file
    fileName = input("That file was not found in the current working directory. Please re-enter the name of the file to search for with the file extension (e.g., .txt): ")
    
    # Ask user to enter the word they want to search the count of
    word = input("Enter the word to search for: ")

# Create a function that will read the user's chosen file and keep count of their chosen word
def countWords(file, wordSearch):

    # Create a counter variable
    wordCount = 0

    # Using try and except for error handling
    try:
        # Open and read the file
        with open(file, "r") as textfile:
            fileText = textfile.read()

            # Count how many times the chosen word appears in the file and convert the words from the file and user input into lower case letters
            wordCount = fileText.lower().count(wordSearch.lower())

             # If the number of times the word appears is greater than 0, return the output
            if wordCount > 0:
                return print("The word " + wordSearch + " was found " + str(wordCount) + " times in this file: " + file)
            
            # If the word was not found in the file, inform the user
            else:
                return print("The word " + wordSearch + " was not found in the file: " + file)

    # If the file entered still does not exist in the current working directory, display a "file not found" error            
    except FileNotFoundError:
        return 0

# Call countWords function to display the output
countWords(fileName, word)


