#########
# PRIDE #
#########

# Characters
define adv = Character("[traveler_name]")

default pride_first_time = True

label pride:
    $ coming_from_wrath = False
    $ coming_from_pride = True
    $ coming_from_gluttony = False
    $ coming_from_sloth = False

    if pride_first_time:
        adv "Hey! I wasn't expecting guests."
        $ pride_first_time = False

        menu:
            "What are you looking at?":
                jump talk_about_map

            "What's your name?":
                jump ask_name_adv
            
            "{color=#ff0000}KILL [traveler_name]{/color}":
                jump kill_traveler

    else:
        if unlock_gluttony and unlock_sloth:
            adv "Need help getting somewhere?"

            menu:
                "I need to find someone...":
                    jump help_find_kid
                "I can do it myself":
                    jump no_help_find_kid
        else:
            adv "So many stories to tell..."

        menu:
            "TRAVEL":
                jump start

            "Anything besides traveling?" if (coming_from_gluttony or coming_from_sloth) and unlock_gluttony and unlock_sloth:
                jump talk_about_map

            "{color=#ff0000}KILL [traveler_name]{/color}":
                jump kill_traveler

    return


label help_find_kid:
    "TODO Find kid"
    return


label no_help_find_kid:
    "TODO Find kid"
    return


label talk_about_map:
    "What are you looking at over there?"

    adv "Oh this? I'm just reminiscing about old times"

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
    "{color=#22ff33}The scent of forced nostalgia draws me elsewhere...{/color}{w}\nYou've unlocked another world"

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
    "{color=#22ff33}The scent of the overwhelming need to impress draws me elsewhere...{/color}{w}\nYou've unlocked another world"

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

    "{color=#22ff33}The scent of self-pity draws me elsewhere...{/color}{w}\nYou've unlocked another world"

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

    adv "i've got to admit, I didn't expect this, but my name proceeds me."

    if unlock_gluttony:
        $ unlock_sloth = True
    elif unlock_sloth:
        $ unlock_gluttony = True

    "{color=#22ff33}The scent of self-importance draws me elsewhere...{/color}{w}\nYou've unlocked another world"

    jump pride


label kill_traveler:
    "TODO: Kill the traveler"
