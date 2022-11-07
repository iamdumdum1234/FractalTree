import turtle as tu

roo = tu.Turtle()
wn = tu.Screen()
wn.bgcolor("black")
wn.title("Fractal Tree Pattern")
roo.speed(20)

def rotate(angle: int):
    # Quay ngược lại so với đường tròn lượng giác
    if angle < 0:
        print("rotating left bro", abs(angle))
        roo.left(abs(angle))
        return
    roo.right(angle)


_color_idx = 0
_colors = [
    "yellow",
    "magenta",
    "red",
    "#FFF8DC",
    "lightgreen",
    "red",
    "yellow",
    "#FFF8DC",
    "cyan",
    "yellow",
    "magenta",
    "#FFF8DC",
]


def get_color(): # Chọn màu theo thứ tự từ list _colors ở trên
    global _color_idx
    color = _colors[_color_idx]
    _color_idx += 1
    if _color_idx >= len(_colors):
        _color_idx = 0
    return color


pen_size = 2


def change_pensize(): # Thay đổi độ dày của nét vẽ
    global pen_size
    match pen_size:
        case 2:
            pen_size = 3
        case 3:
            pen_size = 2


def draw(l: int, color: str, line_thiccness: int): # Vẽ cây
    if l < 10:
        return
    roo.pensize(pen_size)
    roo.pencolor(color)
    roo.forward(l)
    roo.left(30)
    draw(line_thiccness * l / (line_thiccness + 1), color, line_thiccness)
    roo.right(60)
    draw(line_thiccness * l / (line_thiccness + 1), color, line_thiccness)
    roo.left(30)
    roo.pensize(pen_size)
    roo.backward(l)


draw_len = 20
line_thiccness = 3
rotate(90)
while True: # Lặp lại vẽ cây
    for i in range(0, 4):
        rotate(90)
        draw(draw_len, get_color(), line_thiccness)
    roo.speed(2000)
    line_thiccness += 1
    draw_len += 20
    change_pensize()

