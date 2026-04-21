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

    $ visited_sloth = True

    show dog_img:
        xalign 0.5
        zoom 0.3

    dog "Bork?"

    $ unlock_gluttony = True

    menu:
        "TRAVEL":
            jump start

        "{color=[kill_color]}KILL [dog_name]{/color}":
            return

    return
