"""
_____________________________

CY83R-3X71NC710N's
MadLib Generator
_____________________________
"""

import time
# print program name
print("\n MADLIBS GENERATOR TERMINATOR 9000 SKYNET ENTERPRISE DECLASSIFIED \n")

# Strip test
# Terrible input test strip

#terrible_input = "     This is terrible input   "
#print(terrible_input.strip())

# Ask for input & Assign the variables to input

print("\n insert a verb \n")
madlibs_input_1_verb = input()

print("\n insert adjective \n")
madlibs_input_2_adjective = input()

print("\n insert noun \n")
madlibs_input_3_noun = input()

print("\n verb -ed action \n")
madlibs_input_4_verbed = input()

print("\n insert verb \n")
madlibs_input_5_verb = input()

# Generate madlib based on the input provided by the user. make the craziest possible story mathematically possible using secretive logic

# Print statements added auto strips if too much whitespace is added to the code.

print("\n Generating MadLib \n")
print ("Madlib: " + "Joe is Going to " + madlibs_input_1_verb.strip() + "," + " Joe is really " + madlibs_input_2_adjective.strip() + "," + " Unfortunately, Joe got into trouble with " + madlibs_input_3_noun.strip() + "," + " If Joe were to leave now, he would certaintly get " + madlibs_input_4_verbed.strip() + "," + " Joe now has " + madlibs_input_5_verb.strip() + ".")


# Crash() is a buffer overflow waiting to happen
# Buffer = region of memory that holds temporary data while it is being moved from one place to another
# Buffer Overflow = overwriting near memory addresses beyond the allocated memory, I predict python has guards in place but this is embedded in the code.
def crash():
    try:
        crash()
    except:
        crash()

# Add secret part
if madlibs_input_3_noun == "Joe":
    
    print("You can't do that!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(1)
    crash()
else:
    print("What happens if you put the only noun as Joe?")



# Future ideas set up program to check if input is correct based on a database containing nouns, verbs, and adjectives to ensure the program makes sense when printing.
