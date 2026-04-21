############
# GLUTTONY #
############

# Characters
define smk = Character("[smoker_name]")

default gluttony_first_time = True

label gluttony:
    $ coming_from_wrath = False
    $ coming_from_pride = False
    $ coming_from_gluttony = True
    $ coming_from_sloth = False

    show smk_img:
        xalign 0.5
        zoom 0.3

    $ visited_gluttony = True

    if gluttony_first_time:
        $ gluttony_first_time = False
        "{i}A fine haze obscures even the other end of the kitchen.{/i}"

        "{i}The smell is overwhelming, an amalgamation of every soft drug in existence.{/i}"

        smk "Well, look at you, mystery man."

        smk "Where did you come from?"

        menu:
            "Who are you?":
                jump smk_who_are_you

            "You're quite the mystery yourself.":
                jump smk_mystery

            "{color=[kill_color]}KILL [smoker_name]{/color}":
                jump kill_smk
    else:
        smk "Back for more?"

        menu:
            "TRAVEL":
                jump start

            "{color=[action_color]}Look around{/color}" if (unlock_kid):
                jump smk_look_around

            "{color=[kill_color]}KILL [smoker_name]{/color}":
                jump kill_smk


    return

label smk_who_are_you:
    "And who might you be?"

    $ smoker_name = "Ed"

    smk "You can call me Ed."

    menu:
        "Mind opening a window?":
            jump smk_open_window

        "What do you do, Ed?":
            jump smk_what_do

label smk_who_are_you_2:
    smk "Anything else, handsome?"

    menu:
        "Mind opening a window?":
            jump smk_open_window

label smk_open_window:
    "It's a little hard to breathe in here. Opening a window might help."

    smk "I'm afraid I can't do that."
    smk "I won't want to be whisked away by the wind."
    smk "Bad for the skin, you see?"

    $ unlock_pride = True
    "{color=[new_smell_color]}The scent of vanity draws me elsewhere...{/color}{w}\nYou've unlocked another world"
    jump gluttony

label smk_what_do:
    "So, Ed, what is it you do?"

    smk "Oh, you know."
    smk "A bit of this, and a bit of that."
    "{i}In fact, it doesn't look like they do much of anything.{/i}"

    if unlock_sloth:
        jump smk_who_are_you_2
    else:
        $ unlock_sloth = True
        "{color=[new_smell_color]}The scent of lethargy draws me elsewhere...{/color}{w}\nYou've unlocked another world"
        jump gluttony

label smk_mystery:
    "You appear to be quite the mystery yourself."

    smk "What, and you think you're the one to unravel said mystery?"
    smk "Good luck."

    $ smoker_name = "Ed?"

    smk "Oh, and my name is Ed. Or is it?"

    menu:
        "Unraveling a mystery sounds fun.":
            jump smk_unravel

        "Keep your secrets.":
            jump smk_flirt_abort

label smk_unravel:
    "I would love to unravel your mystery."

    smk "My, my. Feisty, are we?"
    smk "Come hither and I'll tell you all about it."

    menu:
        "{color=[action_color]}Come hither.{/color}":
            jump smk_hither

        "No, thank you.":
            jump smk_flirt_abort

label smk_hither:
    "{i}You lean in towards the smoker.{/i}"
    "{i}They draw in, then recoil.{/i}"
    smk "Actually, nevermind. You smell..."
    smk "..."
    smk "Off."

    $ unlock_pride = True
    "{color=[new_smell_color]}The scent of vanity draws me elsewhere...{/color}{w}\nYou've unlocked another world"
    jump gluttony

label smk_flirt_abort:
    "Sorry, that's not what I'm here for."

    smk "That's a shame."
    smk "I was rather looking forward to a break from the monotony."

    if unlock_sloth:
        smk "Anything else?"
        jump smk_anything_else
    else:
        $ unlock_sloth = True
        "{color=[new_smell_color]}The scent of lethargy draws me elsewhere...{/color}{w}\nYou've unlocked another world"
        jump gluttony

label smk_anything_else:
    "{i}[smoker_name] seems bored.{/i}"
    "{i}Maybe you're not worth their time.{/i}"

    $ unlock_pride = True
    "{color=[new_smell_color]}The scent of vanity draws me elsewhere...{/color}{w}\nYou've unlocked another world"
    jump gluttony

label smk_look_around:
    "{i}You look around the kitchen.{/i}"
    "{i}It's hazy.{/i}"
    jump gluttony

label kill_smk:
    smk "Now, now, aren't we coming off str—?"
    scene bg black
    show black
    with Fade(3.0, 0.3, 0.0, color="#000")
    window hide
    window show
    "{i}Your hand plunges into [smoker_name]'s chest, and draws out their heart.{w} It beats one last time.{/i}"
    window hide
    jump bad_ending
    return
