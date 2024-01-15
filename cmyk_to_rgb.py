"""
The purpose of this program was to create a function that received user input to cast inside a dictionary of CMYK colors(Cyan, Magenta, Yellow, Key/Black). 
The function would then convert the dictionary to RGB colord (Red, Green, Blue) values and print them
The program is used to represent how printing software conevrts between the two color models.

"""

#The colors are the keys of the dictionary while user input are values
#CMYK values range from 0 - 100
c = int(input("Enter the Cyan Color Value: "))
m = int(input("Enter the Magenta Color Value: "))
y = int(input("Enter the Yellow Color Value: "))
k = int(input("Enter the Key Color Value: "))

#Function to convert CMYK to RGB
def CMYK_to_RGB():
    #The user inputs were added to the empty dictionary CMYKdict
    CMYKdict = {}
    CMYKdict["Cyan"] = c
    CMYKdict["Magenta"] = m
    CMYKdict["Yellow"] = y
    CMYKdict["Key"] = k
    #print(CMYKdict)
    
    #Formulas to convert the CMYK values to RGB
    R = (255 * (1 - c / 100) *  (1 - k /100))
    #print(f'{R:.1f}')

    G = 255 * (1- m / 100) * (1 - k /100)
    #print(f'{G:.1f}')

    B = 255 * (1 - y /100) * (1 - k /100)
    #print(f'{B:.1f}')

    #New dictionary to inserts the new RGB values
    RGBdict = {}
    RGBdict["Red"] = R
    RGBdict["Green"] = G
    RGBdict["Blue"] = B
    
    #For loop that prints both the key and value from RGBdict
    for a,b in RGBdict.items():
        print(f'{a}: {b:.1f} ')
    
print()
print("RGB Values")
#Call dict here when printing
print(CMYK_to_RGB())

"""
Not included 
print(f'Red: {RGBdict["Red"]:.1f} ')
print(f'Green: {RGBdict["Green"]:.1f} ')
print(f'Blue: {RGBdict["Blue"]:.1f} ')
""" 
