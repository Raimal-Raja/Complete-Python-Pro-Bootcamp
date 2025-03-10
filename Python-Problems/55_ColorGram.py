import colorgram

rgb_color = []
colors = colorgram.extract('color_img.jpeg',3)
print(colors)

for color in colors:
    rgb_color.append(color.rgb)
print(rgb_color)