#########
# PRIDE #
#########

# Characters
define adv = Character("[traveler_name]")

default pride_first_time = True

default say_no_find_kid = False

label pride:
    $ coming_from_wrath = False
    $ coming_from_pride = True
    $ coming_from_gluttony = False
    $ coming_from_sloth = False

    scene bg kitchen:
        zoom 0.675
        yalign 0.5
    show halfblack with dissolve
    show adv_img:
        xalign 0.05
        zoom 0.21
    show htr_img:
        xalign 1.15
        yalign 0.5
        zoom 0.275

    if pride_first_time:
        adv "Hey! I wasn't expecting guests."
        $ pride_first_time = False

        if visited_gluttony and visited_sloth and not say_no_find_kid:
            adv "You seem a little lost. Need help getting somewhere?"

            menu:
                "I need to find someone...":
                    jump help_find_kid
                "I can do it myself":
                    $ say_no_find_kid = True
                    jump no_help_find_kid

        menu:
            "What are you looking at?":
                jump talk_about_map

            "What's your name?":
                jump ask_name_adv
            
            "{color=[kill_color]}KILL [traveler_name]{/color}":
                jump kill_traveler

    else:
        if visited_gluttony and visited_sloth and not say_no_find_kid and not unlock_kid:
            adv "Need help getting somewhere?"

            menu:
                "I need to find someone...":
                    jump help_find_kid
                "I can do it myself":
                    $ say_no_find_kid = True
                    jump no_help_find_kid
        else:
            adv "So many stories to tell..."

        menu:
            "TRAVEL":
                jump start

            "Anything besides traveling?":
                jump talk_about_map_but_first

            "{color=[action_color]}Look around{/color}" if (unlock_kid):
                jump adv_look_around

            "{color=[kill_color]}KILL [traveler_name]{/color}":
                jump kill_traveler

    return


label help_find_kid:
    $ unlock_kid = True
    "I am looking for someone. Do you think you could help me?"

    adv "Depends. Do they know you're coming?"

    "Yes."

    adv "Then they'll probably be hiding.{w} Maybe right under your nose..."

    "What are you trying to say?"

    adv "Come on, I basically spelled it out for you."

    "..."

    adv "Do I really have to tell you where they are hiding?"

    menu:
        "Give me a hint":
            jump yes_want_help_kid
        "I can do it myself":
            jump no_want_help_kid


label yes_want_help_kid:
    "Yes. Help me find this person."

    adv "Try going back to places you've already been.{w} You're bound to notice something you haven't before."

    menu:
        "Thank you":
            "Thank you. I will try"
            jump pride

        "More precise?":
            "Can you be more precise?"

            adv "I'm saying trust your instinct. Go back to where you started, you might find something there."

            "Thank you. I will try."
            jump pride


label no_want_help_kid:
    "No, I can handle this on my own."

    adv "Good luck in your adventure."

    "Thank you"

    jump pride


label no_help_find_kid:
    $ unlock_kid = True
    "No thank you. I can find what I'm looking for myself."

    adv "Suit yourself. Just thought you'd appreciate the help of an expert."

    jump pride


label talk_about_map_but_first:
    "Do you do anything else besides traveling?"

    adv "Nowadays I don't even do that."

    adv "But sometimes, when I'm not out on a walk, I look at things I collected along my travels."

    jump talk_about_map


label talk_about_map:
    "What are you looking at over there?"

    adv "Oh this? This is a map I've marked with travel destinations before I became an explorer."
    
    adv "I just like reminiscing about old times."

    if unlock_gluttony and not unlock_sloth:
        jump talk_about_map_a_lot
    elif unlock_sloth and not unlock_gluttony:
        jump talk_about_old_times
    
    "I'll be brief. I need help finding someone."

    adv "Really? Well you've come to the right place"

    jump help_find_kid


label talk_about_map_a_lot:
    "Do you do that a lot?{w} Reminisce I mean?"

    adv "Only thing I have left.{w} I haven't been able to travel in a long time."

    $ traveler_name = "Anderson"
    adv "The great Anderson Blevins is no more..."

    adv "I used to love adventure, exploration."

    adv "Now I'm stuck here in this apartment.{w} With these old bones."

    adv "But you should have seen me in my glory days."

    adv "You know, I once escaped Reunion Island on a life raft."

    "You seem very proud of your past as an explorer."

    adv "Yes. A pioneer, I'd say.{w} I've seen and done everything there is to see or do on this earth."

    $ unlock_sloth = True
    "{color=[new_smell_color]}The scent of forced nostalgia draws me elsewhere...{/color}{w}\nYou've unlocked another world"

    jump pride


label talk_about_old_times:
    "I see. So what did you do in the old times?"

    adv "Oh, I used to go anywhere, do anything."

    adv "There's nothing on this earth I haven't done."

    adv "When I was young, I'd just hop on a boat or a plane and see where the wind takes me."

    adv "Then, when I get there, I just let the course of a river carry me elsewhere."

    adv "I've covered the whole map.{w} I've even been off the map."

    adv "Did you know, I discovered 3 separate islands?"

    adv "Can't do that anymore, with Google or whatever."

    adv "I'm telling you, real experience is better than what the internet gives you."

    $ traveler_name = "Anderson"
    adv "But, the great Anderson Blevins is no more..."

    "Why not?"

    adv "My knees don't hold me like they used to..."

    adv "But in my youth, I really was something."

    $ unlock_gluttony = True
    "{color=[new_smell_color]}The scent of the overwhelming need to impress draws me elsewhere...{/color}{w}\nYou've unlocked another world"

    jump pride


label ask_name_adv:
    "Well, I'm here anyway. What's your name?"

    $ traveler_name = "Anderson"
    adv "I am Anderson Blevins."

    "..."

    adv "Come on, you must have heard of me?"

    adv "Anderson, the explorer?{w} The first man to walk from South Africa to Morocco on foot?"

    menu:
        "{i}stay silent{/i}":
            jump stay_silent_know_adv_first

        "I haven't heard of you":
            jump dont_know_adv

        "Yes, I know who you are":
            jump yes_know_adv


label stay_silent_know_adv:
    adv "Really? Nothing?"

    adv "Doesn't matter. It's not like I am what I used to be..."

    "Why is that?"

    adv "Look at me. I'm old now, I can't travel anymore.{w} At least not how I did before"

    adv "I only have the energy to walk around the block."

    adv "Let me tell you, I'm getting bored of suburbia."

    adv "I used to be someone, do something important.{w} I've seen every wonder, conquered every mountain..."
    adv "Now look at me..."

    if unlock_gluttony:
        $ unlock_sloth = True
    elif unlock_sloth:
        $ unlock_gluttony = True

    "{color=[new_smell_color]}The scent of self-pity draws me elsewhere...{/color}{w}\nYou've unlocked another world"

    jump pride


label stay_silent_know_adv_first:
    "..."

    adv "Ah, well what do you know anyway?"

    adv "I've been everywhere around the world. I don't imagine you've done as much."

    jump stay_silent_know_adv


label dont_know_adv:
    "No, I haven't heard of you."

    adv "Really?"

    jump stay_silent_know_adv_first


label yes_know_adv:
    "Yeah, I've heard of you. You're Anderson Blevins."

    adv "Aha, yes!{w} So you're an admirer?"

    adv "I'm guessing you've heard of my exploits?"

    adv "Which one do you like the most?"

    adv "My travel across Africa?"

    adv "My escape from Reunion Island?"

    adv "Or is it the three islands I got to name?"

    "Can't say. I prefer to stay impartial."

    adv "Hah! You just can't chose, right?"

    adv "I've got to admit, I didn't expect this, but my name precedes me."

    if unlock_gluttony:
        $ unlock_sloth = True
    elif unlock_sloth:
        $ unlock_gluttony = True

    "{color=[new_smell_color]}The scent of self-importance draws me elsewhere...{/color}{w}\nYou've unlocked another world"

    jump pride

label adv_look_around:
    "{i}You look around the kitchen.{/i}"
    "{i}It's full of souvenirs.{/i}"
    adv "It's not here, silly."
    jump pride

label kill_traveler:
    adv "H-hey, please don't, I'm not—"
    scene bg black
    show black
    with Fade(3.0, 0.3, 0.0, color="#000")
    window hide
    window show
    "{i}Your hand plunges into man's chest, and draws out his heart.{w} It beats one last time.{/i}"
    window hide
    jump bad_ending
