enemies = 1
def increase_enemies():
    # global enemies # modify global score
    # enemies +=1
    
    # without modifying global score
    print(f'inside {enemies}')
    return enemies + 1
    

increase_enemies()
print(f'outside: {enemies}')