#########
# SLOTH #
#########

# Characters
# TODO: Give name
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

        "{color=[action_color]}Look around{/color}" if (unlock_kid):
            jump dog_look_around

        "{color=[kill_color]}KILL [dog_name]{/color}":
            jump kill_dog

    return

label dog_look_around:
    "{i}You look around the kitchen.{/i}"
    "{i}It smells like expired dog food.{/i}"
    jump sloth

label kill_dog:
    dog "Woof :D"
    scene bg black
    show black
    with Fade(3.0, 0.3, 0.0, color="#000")
    window hide
    window show
    "{i}Let's not describe what happens next.{/i}"
    window hide
    jump bad_ending