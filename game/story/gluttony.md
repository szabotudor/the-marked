# Gluttony

Description:

_A fine haze obscures even the other end of the kitchen. The smell is overwhelming,  an amalgamation of every soft drug in existence._

Smoker:
> "Well, look at you, mystery man. Where did you come from?"

Us:
- "Who are you?"
    > "You can call me Ed."
     - "Mind opening a window?"
        > "As a matter of fact, I do. I won't want to be whisked away by the wind."
        [[unlock pride]]
     - "What do you do, Ed?"
        > "Oh, a bit of this, and a bit of that."
        If sloth is unlocked:
            > "Now leave me be."
            go back to last question and remove "What do you do, Ed?" option.
        Else:
            [[unlock sloth]]

 - "You're quite the mystery yourself."
    > "What, and you think you're the one to unravel said mystery? Good luck."
     - "Unraveling a mystery sounds fun."
        > "My, my. Feisty, are we? Come hither and I'll tell you all about it."
            [[unlock pride]]
     - "Keep your secrets."
        > "That's a shame. I was rather looking forward to a break from the monotony."
        If sloth is unlocked:
            > "Now leave me be."
            go back to last question and remove "Keep your secrets." option.
        Else:
            [[unlock sloth]]


At every option:
 - [Kill ???/Ed]
    