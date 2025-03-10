import colorgram

rgb_colors = []
colors = colorgram.extract('color_img.jpeg',3)
# print(colors)

# for color in colors:
#     rgb_color.append(color.rgb)
# print(rgb_color)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)