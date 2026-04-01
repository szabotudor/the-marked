#########
# WRATH #
#########

# Characters
define dad = Character("[dad_name]")
define kid = Character("[kid_name]")

label wrath:
    $ coming_from_wrath = True
    $ coming_from_pride = False
    $ coming_from_gluttony = False
    $ coming_from_sloth = False

    dad "E"

    $ unlock_pride = True

    jump start

    return
