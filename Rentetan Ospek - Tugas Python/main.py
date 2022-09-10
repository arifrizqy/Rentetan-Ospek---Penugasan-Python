#Create method question
def question():
    #Showing list of question
    print("\nTry again? :")
    print("1. Yes, try again \n2. No, don't try again")
    print("Please choose one from option above? \nWarning:(Please input 1 or 2)")

    #User input choise then store to variable try_again
    try_again = int(input("Your choice : "))

    """
    -) If user choise 1. Yes, try again -> So program volume calculator will running again.
    -) if user choise 2. No, try again -> So program volume calculator will ended.
    -) And Besides that, method question will stay running until user input 1. Yes, try again or 2. No, try again.
    """

    #Conditioning question
    if (try_again == 1):
        #Running method volume calculator
        volumeCalculator()
    elif (try_again == 2):
        #Program volume calculator will ended and print the text
        print("\nThanks for using my program :)\n")
    else:
        print("\nError : Invalid input! :(")
        print("Please try again.")

        question()

#Create method volume calculator
def volumeCalculator():
    #Showing list option for volume calculator
    print("\nOption volume calculator :")
    print("1. Cube \n2. Block")
    print("Please choose one from option above? \nWarning:(Please input 1 or 2)")

    #User input choise then store to variable geometry
    geometry = int(input("Your choice : "))

    """
    -) If user choise 1. Cube -> So program will running for volume cube calculator.
    -) If user choice 2. Block -> So program will running for volume block calculator.
    -) And besides that, method volume calculator will stay running until user input 1. Cube or 2. Block.
    """

    #Conditioning volume calculator
    if (geometry == 1):
        #User input length cube then store to variable length cube
        length_cube = int(input("\nEnter the length cube \t : "))

        cube_volume = length_cube**3

        print("\nCube volume with, \nLength \t\t = {} \nCube volume \t = {}\n".format(length_cube, cube_volume))

        input("Press enter to continue...")

        question()
    elif (geometry == 2):
        #User input length, width and height block then store to variable
        length_block = int(input("\nEnter the length block \t : "))
        width_block = int(input("Enter the width block \t : "))
        height_block = int(input("Enter the height block \t : "))

        block_volume = length_block * width_block * height_block

        print("\nBlock volume with, \nLength \t\t = {} \nWidth \t\t = {} \nHeight \t\t = {} \nBlock volume \t = {}\n".format(length_block, width_block, height_block, block_volume))

        input("Press enter to continue...")

        question()
    else :
        print("\nError : Volume calculator not registered! :(")
        print("Please try again.\n")

        input("Press enter to continue...")
        
        volumeCalculator()

#Running the method
volumeCalculator()