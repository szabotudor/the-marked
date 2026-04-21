#########
# WRATH #
#########

# Characters
define dad = Character("[dad_name]")
define kid = Character("[kid_name]")

default wrath_first_time = True
default kid_first_time = True

label wrath:
    $ coming_from_wrath = True
    $ coming_from_pride = False
    $ coming_from_gluttony = False
    $ coming_from_sloth = False

    show dad_img:
        xalign 0.5
        zoom 0.3

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

            "I'd like to talk to the kid" if (unlock_kid_3):
                jump dad_talk_kid

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
    "Sir, I know you're not alone in here."

    dad "The hell are you on about?"

    menu:
        "Nevermind.":
            jump wrath
        "Step aside.":
            jump dad_step_aside
        "{color=[action_color]}Push [dad_name] aside.{/color}":
            jump dad_push_aside

label dad_step_aside:
    "I need you to step aside."

    dad "You don't get to tell me what to do.{w} This is {i}my{/i} house, fucker."

    "{i}You swear you can hear a soft whine from behind [dad_name].{/i}"

    menu:
        "Alright.":
            jump wrath
        "Who's that behind you?":
            jump dad_behind
        "{color=[action_color]}Push [dad_name] aside.{/color}":
            jump dad_push_aside

label dad_behind:
    "I know there's someone behind you."

    "{i}[dad_name] lets out a frustrated sigh.{/i}"

    dad "Fine. You got me. Meet the kid."

    jump kid_appear

label dad_push_aside:
    "{i}You shove the burly man aside.{/i}"

    dad "HEY, keep your hands off me, you {i}fuck{/i}er!"

    jump kid_appear

label dad_talk_kid:
    "I'd like to talk to the kid, please."

    dad "I'll be watching."

    jump kid_appear

label kid_appear:
    scene bg black
    show kid_img:
        xalign 0.5
        zoom 0.3
    if (kid_first_time):
        with Fade(3.0, 0.3, 0.0, color="#000")
    else:
        with Fade(1.0, 0.3, 0.0, color="#000")
    window hide
    window show

    "{i}[kid_name] backs up against the kitchen counter.{/i}"
    kid "Stay away from me!"

    jump kid_start

label kid_start:
    $ unlock_kid_3 = True

    "{i}The kid looks terrified.{/i}"

    menu:
        "TRAVEL" if (not kid_first_time):
            jump start

        "What's your name?" if (kid_first_time):
            $ kid_first_time = False
            jump kid_name

        "{color=[kill_color]}KILL [kid_name]{/color}":
            jump kill_kid

label kid_name:
    "What's your name, kid?"

    "{i}The kid just stares at you.{/i}"

    $ kid_name = "Billy"
    dad "Billy's a little timid."

    jump kid_start

label kill_dad:
    dad "What the—?"

    scene bg black
    show black
    with Fade(3.0, 0.3, 0.0, color="#000")
    window hide
    window show
    "{i}Your hand plunges into the man's chest, and draws out his heart.{w} It beats one last time.{/i}"
    "{i}You hear the faint sound of sobbing as the world vanishes.{/i}"
    window hide
    jump bad_ending

label kill_kid:
    "{i}The kid screams.{/i}"

    scene bg black
    show black
    with Fade(3.0, 0.3, 0.0, color="#000")
    window hide
    window show
    dad "NO!"
    window hide
    window show
    "{i}Your hand plunges into the kid's chest, and draws out his heart.{w} It beats one last time.{/i}"
    "{i}Nothing but rage and desperation can be seen [dad_name]'s eyes, as he jumps at you.{w} Just before he reaches you, however, the world vanishes.{/i}"
    window hide
    jump good_ending