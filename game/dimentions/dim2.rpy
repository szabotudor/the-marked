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
                jump kill_smk

            "{color=#ff0000}KILL [smoker_name]{/color}":
                jump kill_smk
    else:
        smk "Back for more?"

        menu:
            "TRAVEL":
                jump start

            "{color=#ff0000}KILL [smoker_name]{/color}":
                jump kill_smk

    return

label smk_who_are_you:
    "And who might you be?"

    smk "You can call me Ed."

    $ smoker_name = "Ed"

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
    "{color=#22ff33}The scent of vanity draws me elsewhere...{/color}{w}\nYou've unlocked another world"
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
        "{color=#22ff33}The scent of consumption draws me elsewhere...{/color}{w}\nYou've unlocked another world"
        jump gluttony

label kill_smk:
    return
