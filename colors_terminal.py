import os

os.system('')


# https://stackoverflow.com/a/70599663 @Vinod Srivastav
def RGB(red=None, green=None, blue=None, bg=False):
    if (bg == False and red != None and green != None and blue != None):
        return f'\u001b[38;2;{red};{green};{blue}m'
    elif (bg == True and red != None and green != None and blue != None):
        return f'\u001b[48;2;{red};{green};{blue}m'
    elif (red == None and green == None and blue == None):
        return '\u001b[0m'


g0 = RGB()  # Reset colors
reset = g0
g1 = RGB(0, 255, 0)  # Green text (foreground)
g2 = RGB(0, 100, 0, True) + "" + RGB(100, 255, 100)  # Green background and text (different text shade)
g3 = RGB(0, 255, 0, True) + "" + RGB(0, 50, 0)  # Green background and text (different text shade)