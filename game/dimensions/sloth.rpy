#########
# SLOTH #
#########

# Characters
# TODO: Give name
define dog = Character("[dog_name]")

label sloth:
    if (coming_from_gluttony):
        $ unlock_pride = True
    else:
        $ unlock_gluttony = True

    $ coming_from_wrath = False
    $ coming_from_pride = False
    $ coming_from_gluttony = False
    $ coming_from_sloth = True

    $ visited_sloth = True

    show dog_img:
        xalign 0.5
        zoom 0.3

    dog "..."

    menu:
        "TRAVEL":
            jump start

        "How long have you been here, boy?":
            jump dog_convo

        "{color=[action_color]}Look around{/color}" if (unlock_kid):
            jump dog_look_around

        "{color=[kill_color]}KILL [dog_name]{/color}":
            jump kill_dog

    return

label dog_look_around:
    "{i}You look around the kitchen.{/i}"
    "{i}It smells like expired dog food.{/i}"
    "There's nothing of note in here."
    jump sloth

label dog_convo:
    dog "Long enough for my heart to ache."
    "Are you here all alone?"
    dog "Yes, and I deserve it. My master put me in the corner and told me to stay here."

    menu:
        "{i}Tell him his fate{/i}":
            jump yes_fate
        "{i}Keep silent{/i}":
            jump no_fate

label yes_fate:
    "When he comes back, that will be the last time you see him"
    dog "I knew he wouldn't forgive me. I have done something indefensible."
    jump after_fate

label no_fate:
    "Im sure his rage was only temporary."
    dog "..."
    "Im sure you feel guilty, and he knows that"
    dog "Yes, I did something indefensible."
    jump after_fate

label after_fate:
    "Tell me."
    dog "I bit him, I lost control of my emotions and I bit my master, my best friend, the one I should have been most loyal to."
    "..."
    dog "Aren't you going to help me?"
    "Why would I do that? Who did you expect would come?"
    dog "Someone who would rid me of this..."
    "Sin?"
    dog "Guilt."
    dog "I feel so much of it, I fear it might spill out."
    dog "It's stabbing my shoulders and dripping down into my chest. It hurts me even when I try not to think of what I did"
    "I think you are inflating the situation"
    dog "Really?"

    menu:
        "{i}Tell him the truth{/i}":
            jump tell_truth
        "{i}Lie{/i}":
            jump lie_to_him

label tell_truth:
    "No, Im sorry"
    "He will not forgive you."
    dog "I know. I am unforgivable."
    jump sloth

label lie_to_him:
    "Yes, really."
    "Your master loves you. One mistake won't mean the end of your friendship."
    "You have been loyal and loving your whole life. He knows that."
    dog "I know. He loves me, he believe that he will forgive me."
    "Dont worry, everything will be ok. The guilt you feel dripping down your ribs will drain from your body."

    jump sloth


label kill_dog:
    "I'm sorry you had to trust so deeply."
    scene bg black
    show black
    with Fade(3.0, 0.3, 0.0, color="#000")
    window hide
    window show
    "{i}Let's not describe what happens next.{/i}"
    window hide
    jump bad_ending

