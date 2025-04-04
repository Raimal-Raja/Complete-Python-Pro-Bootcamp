import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states_list = data.state.to_list()

guess_list = []
missing_states = []
n = 50

while len(guess_list) < n:
    answer = screen.textinput(title=f"{len(guess_list)}/50 Correct States", prompt="What's the next state's name")
    if answer is None or answer.lower() in ['exit', 'stop']:
        missing_states = [state for state in all_states_list if state not in guess_list]
        break

    answer = answer.title()
    if answer in all_states_list and answer not in guess_list:
        guess_list.append(answer)
        timy = turtle.Turtle()
        timy.hideturtle()
        timy.penup()
        row = data[data.state == answer]
        timy.goto(int(row.x), int(row.y))
        timy.write(row.state.item())

# Save guessed states
df_guess = pd.DataFrame({"guessed state": guess_list})
df_guess.to_csv("correct_guess_states.csv", index=False)

# Save missed states
df_missing = pd.DataFrame({"missed state": missing_states})
df_missing.to_csv("missing_states.csv", index=False)
