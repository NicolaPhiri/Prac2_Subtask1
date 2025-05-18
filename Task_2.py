"""
Name: Nicola
Surname: Phiri
Project Name: Task 2
Date:10 May
Term: 2
"""
# Goal: Simple project to retrieve and display components information test data
#Declare file
try:
         with open("components_data.txt", "x") as file:
             file.write("C101,3.3\n")
             file.write("A202,2.9\n")
             file.write("B303,3.1\n")
             file.write("C404,2.7\n")

# Defensive programming, making sure the program doesn't shut down because of an error.
except FileExistsError:
    file = open("components_data.txt", "r")
    print("File already exists")
    file.close()

#Step 2: Prompt the user to enter a single letter between a-z
strLetter = str(input("Please enter a letter between A - Z:" + " "))
"""Create condition to make sure they enter a letter:"""
if strLetter.isalpha() and len(strLetter)== 1: #make sure that they are entering a letter
    #Converting the entered letter into a cap
    uppercase_letter = strLetter.upper()
    # Appending the input to show up in the text file

# Request that the user enter the component ID and voltage reading
#Component ID
strCom_id = str(input("Please enter the component ID:"+" "))

# Create a condition to ensure that they enter numbers with 3 digits
if len(strCom_id)== 3:
   strVoltage = str(input("Please enter the voltage reading with 1 decimal space:" + " "))
   with open("components_data.txt", "a") as f:
       strData = (uppercase_letter + strCom_id + "," + strVoltage)
       f.write(strData + "\n")
       print(strData)

#Ask user to enter  the voltage reading
else:
    print("Please enter a 3 digit ID number.")

#Create a filter system for the entered componentes
"""Request input"""
strFilterLetter = str(input("Please enter the letter of the ID you want:"+" "))
strFilterLetter_upper =strFilterLetter.upper()

#Declaration of 'found'
found = False
"""Create filter"""
with open("components_data.txt","r") as file:
    for line in file:
        if strFilterLetter_upper in line:
            print(line.strip())
            found = True

#Message to display if no match was found
if not found:
    print(f"No component match found win an ID starting with"+ " "+ strFilterLetter+".")