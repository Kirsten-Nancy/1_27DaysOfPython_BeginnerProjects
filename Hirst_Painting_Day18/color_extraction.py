import colorgram

colors = colorgram.extract('image.jpg', 20)
list_rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    my_color = (r, g, b)
    list_rgb_colors.append(my_color)
