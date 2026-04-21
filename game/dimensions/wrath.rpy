#########
# WRATH #
#########

# Characters
define dad = Character("[dad_name]")
define kid = Character("[kid_name]")

default wrath_first_time = True

label wrath:
    $ coming_from_wrath = True
    $ coming_from_pride = False
    $ coming_from_gluttony = False
    $ coming_from_sloth = False

    if wrath_first_time:
        $ wrath_first_time = False
        "This world has a foul smell"

        "This apartment probably hasn't been cleaned in weeks"

        dad "Watch your mouth, buddy!"

        dad "I've got enough on my mind already."

        menu:
            "What is your name?":
                jump wrath_dad_introduce

            "What is on your mind?":
                jump wrath_work0

            "{color=[kill_color]}KILL [dad_name]{/color}":
                jump kill_dad
    else:
        dad "Whaddaya want?"

        menu:
            "TRAVEL":
                jump start

            "{color=[action_color]}Look around{/color}" if (unlock_kid and not unlock_kid_2):
                jump dad_look_around

            "Who are you hiding?" if (unlock_kid_2):
                jump dad_hiding

            "{color=[kill_color]}KILL [dad_name]{/color}":
                jump kill_dad


label wrath_dad_introduce:
    $ dad_name = "Darrel"
    dad "Name's Darrel."

    dad "And I'm doing fine by the way, not that you asked."

    dad "Now whaddaya want?{w} I've had a long enough day already."

    menu:
        "What do you do for work?":
            jump dad_do_for_work
        "Planning to relax?":
            jump dad_plans_for_night

    return

label dad_do_for_work:
    "What do you do for work?"

    dad "Construction."

    dad "Ain't pretty work, but I gotta put food on the table, and beer in the fridge."

    "You sure have a lot of it in there."

    dad "Sure do.{w} Gotta have enough for the game tonight."

    $ unlock_gluttony = True
    "{color=[new_smell_color]}The scent of consumption draws me elsewhere...{/color}{w}\nYou've unlocked another world"
    jump wrath

label dad_plans_for_night:
    "How do you plan on spending tonight then?"

    dad "I'm watching the game, what else?"

    dad "Don't need no hobbies.{w} Football's fun enough."

    "You do that often?"

    dad "Every night."

    $ unlock_sloth = True
    "{color=[new_smell_color]}The scent of lethargy draws me elsewhere...{/color}{w}\nYou've unlocked another world"
    jump wrath


label wrath_work0:
    dad "Tired."

    dad "Had a long day at work. Just like yesterday... {w} And the day before... {w} And every day for that matter."

    dad "Ain't got no time for a good time."

    $ dad_name = "Darrel"
    dad "And name's Darrel by the way, not that you asked."

    menu:
        "Didn't ask your name.":
            jump i_didnt_ask_name
        "Was curious about you.":
            jump curiour_about_dad

label i_didnt_ask_name:
    "Your name doesn't matter.{w} I can still talk with you, name or no name."

    dad "Well I don't wanna talk to you, I got a game to catch!"

    menu:
        "Anything besides the game?":
            jump anything_besides_game
        "Go watch your game.":
            jump go_watch_game

label curiour_about_dad:
    "I only wanted to talk to you.{w} We don't need formalities."

    dad "Well I don't wanna talk to you, I got a game to catch!"

    menu:
        "Anything besides the game?":
            jump anything_besides_game
        "Go watch your game.":
            jump go_watch_game

label anything_besides_game:
    "Do you do anything besides watch the game?"

    dad "Do what? Ain't got no hobbies."

    dad "And football's fun enough."

    dad "I can sip my beer and sit at the TV.{w} What more can a man ask for?"

    "And you do that every day?"

    dad "Sure do."
    
    $ unlock_sloth = True
    "{color=[new_smell_color]}The scent of lethargy draws me elsewhere...{/color}\n{w}You've unlocked another world"
    jump wrath

label go_watch_game:
    "Then go watch your game. We'll talk later."

    dad "Ugh, I'll wait for you to interupt me again then."

    "{i}He walks to the fridge and picks up a six pack.{/i}"
    "{i}Judging by the state of this place, this is a common occurence.{/i}"

    $ unlock_gluttony = True
    "{color=[new_smell_color]}The scent of consumption draws me elsewhere...{/color}{w}\nYou've unlocked another world"
    jump wrath

label dad_look_around:
    "{i}You look around the kitchen.{/i}"
    "{i}You take a whiff.{/i}"
    "{i}There is something else here... Someone else.{/i}"
    $ unlock_kid_2 = True
    jump wrath

label dad_hiding:
    jump kill_dad

label kill_dad:
    return
