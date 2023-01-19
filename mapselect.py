import discord
color = 0xFF6500
def pick(rando):
    if rando == 0:
        face = 'breeze'
    elif rando == 1:
        face = 'bind'
    elif rando == 2:
        face = 'ascent'
    elif rando == 3:
        face = 'icebox'
    elif rando == 4:
        face = 'fracture'
    elif rando == 5:
        face = 'haven'
    elif rando == 6:
        face = 'split'

    return face

def final_message_maps(map):
    map = map.title()
    return discord.Embed(

        title='Map',
        description=f'You rolled {map}.',

        color=color
    )
