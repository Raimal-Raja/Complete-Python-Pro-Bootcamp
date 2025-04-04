import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states_list = data.state.to_list()

print(all_states_list)
# print(answer)

guess_list = []
missing_states = []
while len(guess_list)< 50:
    # answer = screen.textinput(title=f"{len(guess_list)}/50 Correct States", prompt="What's the next state's name").title()
    answer = screen.textinput(title=f"{len(guess_list)}/50 Correct States", prompt="What's the next state's name")
    answer =  answer.title()
    if answer in all_states_list:
        guess_list.append(answer)
        timy = turtle.Turtle()
        timy.hideturtle()
        timy.penup()
        row = data[data.state == answer]
        timy.goto(int(row.x),int(row.y))
        # timy.write(answer)

        #.item() method will extract first element
        timy.write(row.state.item())
    elif answer == 'Exit' or answer == 'Stop':

        for state in all_states_list:
            if state not in guess_list:
                missing_states.append(state)
        data_dict = {
            "correct guess":guess_list,
            "missed states":missing_states
        }


        # handling length
        max_len = max(len(guess_list), len(missing_states))
        guess_list += [""] * (max_len - len(guess_list))
        missing_states += [""] * (max_len - len(missing_states))

        new_data = pandas.DataFrame(data_dict)
        new_data.to_csv("result.csv", index=False)
        # print(missing_states)
        break

