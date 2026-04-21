default unlock_pride = False
default unlock_gluttony = False
default unlock_sloth = False

default visited_gluttony = False
default visited_sloth = False

default coming_from_wrath = False
default coming_from_pride = False
default coming_from_gluttony = False
default coming_from_sloth = False

default first_time = True
default unlock_kid = False
default unlock_kid_2 = False

default dad_name = "???"
default kid_name = "???"
default dog_name = "???"
default smoker_name = "???"
default traveler_name = "???"

default action_color = "#2233ff"
default new_smell_color = "#22ff33"
default kill_color = "#ff0000"

image bg black = "#000"
image blob = "images/blob.png"
image htr_img = "images/characters/Hunter_Clear.png"
image dad_img = "images/characters/Father_Clear.png"
image dog_img = "images/characters/Dog_Clear.png"
image smk_img = "images/characters/Smoker_Clear.png"
image adv_img = "images/characters/Traveler_Clear.png"


transform speaker:
    xalign 0.2
    yalign 0.7

label start:
    scene bg black

    if first_time:
        "..."

        window hide

        show blob:
            xalign 0.5
            yalign 0.25
            zoom 2.0
        with Fade(0.0, 0.0, 2.0)

        window show
        ""
        "It has been eons since last I've picked up the scent..."
        "..."
        "This is the place. Now to find the world..."

        window hide
        show black
        with Fade(3.0, 0.3, 0.0, color="#fff")
        $ first_time = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    window hide
    menu:
        "Remain here" if coming_from_wrath or coming_from_pride or coming_from_gluttony or coming_from_sloth:
            window show
            if coming_from_wrath:
                jump wrath
            if coming_from_pride:
                jump pride
            if coming_from_gluttony:
                jump gluttony
            if coming_from_sloth:
                jump sloth

        "Travel to World Viha" if not coming_from_wrath:
            window show
            jump wrath

        "Travel to World Ylpleys" if unlock_pride and not coming_from_pride:
            window show
            jump pride

        "Travel to World Ylensyonti" if unlock_gluttony and not coming_from_gluttony:
            window show
            jump gluttony

        "Travel to World Laiskuus" if unlock_sloth and not coming_from_sloth:
            window show
            jump sloth

    jump dim0

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return

