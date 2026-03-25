default unlock_pride = False

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    menu:
        "Travel to a dimension"

        "Travel to Dimention Viha":
            jump wrath

        "Travel to Dimention Ylpleys" if unlock_pride:
            jump pride

    jump dim0

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return

