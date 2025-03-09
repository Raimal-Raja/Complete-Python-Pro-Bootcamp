from turtle import Turtle
tim = Turtle()

tim.shape('turtle')

# for _ in range(4):
#     tim.forward(50)
#     for _ in range(2):
#         tim.right(45)
#         tim.forward(50)
#     tim.right(90)
#

# num_sides = 10
def draw_Shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n  in range(3, 10):
    draw_Shape(shape_side_n)