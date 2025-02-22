# namespace
# gloable scope

strong1 = 4
def matel():
    print(strong1)
    

# local scope
# def metal():
#     strong = 5
# print(strong)


play_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(play_health)
    drink_potion()
print(play_health)