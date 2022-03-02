# to sing a song ten time
#Jingbo Wang
def verse(number, action):
    # this function shall print the entire 9 lines of each output
    # this function should call the functions march and hurrah
    print(march(number) + hurrah())
    print(march(number) + hurrah())
    print(march(number))
    # this function should call the function little_one()
    print(little_one(action))
    # this function should call the function refrain()
    refrain()

def march(number):
    # this function returns the line 1 and 2 output with proper number
    return "The ant go marching " + number + " by " + number + ", " 

def hurrah():
    # this function returns the hurrah parts of line 1 and 2
    return "hurrah! hurrah!"

def little_one(action):
    # this function returns line 4 output with proper action
    return "The little one stops to " + action + ","

def refrain():
    # this function prints line 5 through line 9
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! " * 3)
    
# main is already defined for you, don’t edit the main function
def main():
    actions = [ ("one", "suck his thumb"),
    ("two", "tie his shoe"),
    ("three", "climb a tree"),
    ("four", "shut the door"),
    ("five", "take a dive"),
    ("six", "pick up sticks"),
    ("seven", "talk to Kevin"),
    ("eight", "jump the gate"),
    ("nine", "swing on a vine"),
    ("ten", "say 'The End'") ]
    for n,a in actions:
        verse(n,a)
        print()
    input("Press <Enter> to Quit")
main()
