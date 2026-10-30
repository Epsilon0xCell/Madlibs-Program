"""
_____________________________

CY83R-3X71NC710N's
MadLib Generator
_____________________________
"""

import time

# This printed banner is the long form of the title in my docstring
# above. I know the name is over the top. That was the joke when I
# wrote it and I kept it.
print("\n MADLIBS GENERATOR TERMINATOR 9000 SKYNET ENTERPRISE DECLASSIFIED \n")

# I do not strip answers when I read them. I strip each one where it
# is used, in the story line and in the Joe check at the bottom, so a
# padded answer like "  run  " prints as "run" and still triggers
# nothing it should not. Early on I tested strip() on a padded string
# by hand before trusting it here; that test is long gone, but the
# habit of stripping at the point of use is what stayed.

# Every prompt goes through this one helper because EOF can hit at any
# of the five reads, not just the first. I raise SystemExit instead of
# returning a marker value: with a marker, each of the five call sites
# would need its own check, and a missed one would feed a fake answer
# into the story. Raising from here ends the whole program at once,
# with status 0, because closing the input is not an error.
def read_input():
    try:
        return input()
    except EOFError:
        print("\n Input closed, ending program \n")
        raise SystemExit(0)

# The prompt order below is load bearing. The story template near the
# bottom has five fixed slots and fills them from these variables in
# this exact order, so swapping two prompts would swap what lands in
# the story even though every line still runs.
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

# The story is one fixed template about Joe. Only the five words
# change. I never check that a verb really is a verb or a noun really
# is a noun, so the story takes whatever I type, including empty
# answers, and prints it as is.

# This print is where the stripping happens: each answer is stripped
# as it goes into the template, not when it was read above.
print("\n Generating MadLib \n")
print ("Madlib: " + "Joe is Going to " + madlibs_input_1_verb.strip() + "," + " Joe is really " + madlibs_input_2_adjective.strip() + "," + " Unfortunately, Joe got into trouble with " + madlibs_input_3_noun.strip() + "," + " If Joe were to leave now, he would certainly get " + madlibs_input_4_verbed.strip() + "," + " Joe now has " + madlibs_input_5_verb.strip() + ".")


# The easter egg. It keys on the noun only, stripped, and the case has
# to match exactly: "Joe" triggers it, "joe" does not, and I left that
# as a choice rather than normalizing the case. An older version of
# this branch called a crash function that recursed on itself and hung
# the program for good. Now it prints the warning, pauses, and ends.
if madlibs_input_3_noun.strip() == "Joe":
    
    print("You can't do that!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # The one second pause is the whole effect. time is imported at
    # the top for this line and nothing else. After it, the program
    # just ends; there is no replay.
    time.sleep(1)
else:
    # Every run that misses the egg ends on this hint instead, so the
    # egg is findable without reading the code.
    print("What happens if you put the only noun as Joe?")



# An idea I had for later and never built: check each answer against
# word lists for nouns, verbs, and adjectives, so the program could
# refuse a word that does not fit the slot it was typed into. As the
# code stands there is no such check, and the comment above the story
# says so plainly.
