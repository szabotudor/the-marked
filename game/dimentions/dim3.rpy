#########
# SLOTH #
#########

# Characers
# TODO: Gibe name
define dog = Character("[dog_name]")

label sloth:
    $ coming_from_wrath = False
    $ coming_from_pride = False
    $ coming_from_gluttony = False
    $ coming_from_sloth = True

    dog "Bork?"

    $ unlock_gluttony = True

    menu:
        "TRAVEL":
            jump start

        "{color=#ff0000}KILL [dog_name]{/color}":
            return

    return
