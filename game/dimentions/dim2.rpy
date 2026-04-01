############
# GLUTTONY #
############

# Characers
define smk = Character("[smoker_name]")

label gluttony:
    $ coming_from_wrath = False
    $ coming_from_pride = False
    $ coming_from_gluttony = True
    $ coming_from_sloth = False

    smk "GIMME THOSE DALMATIONS"

    return
