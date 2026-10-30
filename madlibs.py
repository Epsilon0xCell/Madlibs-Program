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

def read_input():
    try:
        return input()
    except EOFError:
        print("\n Input closed, ending program \n")
        raise SystemExit(0)

print("\n insert a verb \n")
madlibs_input_1_verb = read_input()

print("\n insert adjective \n")
madlibs_input_2_adjective = read_input()

print("\n insert noun \n")
madlibs_input_3_noun = read_input()

print("\n verb -ed action \n")
madlibs_input_4_verbed = read_input()

print("\n insert verb \n")
madlibs_input_5_verb = read_input()

# Generate madlib based on the input provided by the user. make the craziest possible story mathematically possible using secretive logic

# Print statements added auto strips if too much whitespace is added to the code.

print("\n Generating MadLib \n")
print ("Madlib: " + "Joe is Going to " + madlibs_input_1_verb.strip() + "," + " Joe is really " + madlibs_input_2_adjective.strip() + "," + " Unfortunately, Joe got into trouble with " + madlibs_input_3_noun.strip() + "," + " If Joe were to leave now, he would certainly get " + madlibs_input_4_verbed.strip() + "," + " Joe now has " + madlibs_input_5_verb.strip() + ".")


# Add secret part
if madlibs_input_3_noun.strip() == "Joe":
    
    print("You can't do that!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(1)
else:
    print("What happens if you put the only noun as Joe?")



# Future ideas set up program to check if input is correct based on a database containing nouns, verbs, and adjectives to ensure the program makes sense when printing.
