import os
from julia_plotter import get_julia
import color_scheme
import time
import random

wait_time = 0.025
step_size = 0.025
min_c = -1.0
max_c = 1.0

def change_c(c: complex, change_type : int):
    if change_type == 0:
        new_x = c.real + random.uniform(-step_size, step_size)
        new_y = c.imag + random.uniform(-step_size, step_size)
    elif change_type == 1:
        new_x = c.real+step_size
        new_y = c.imag
        if abs(new_x) > max_c:
            new_x = min_c
            new_y= c.imag-step_size
        if new_y<min_c:
            new_y = max_c


    x = min(max(min_c, new_x), max_c)
    y = min(max(min_c, new_y), max_c)
    return complex(x, y)


def draw_to_terminal(c : complex, character_to_print="."):
    terminal_size = os.get_terminal_size()  # Doesn't work in IDE
    data = get_julia(terminal_size.columns, terminal_size.lines, c)
    max_val = max([max(x) for x in data])
    if max_val == 0:
        max_val = 1
    str_to_draw = ""
    for row in data:
        for cell in row:
            #color_scheme.print_cell(cell, max_val)
            str_to_draw+=color_scheme.print_cell(cell, max_val, character_to_print)
        #print("\n")
        str_to_draw +="\n"
    print(str_to_draw)


if __name__ == "__main__":
    c = 0.355 + 0.355
    while True:
        print("\033[H\033[xJ", end="")
        print('\033[?25l', end="")  # Hide cursor
        draw_to_terminal(c, "#")
        c = change_c(c, 1)
        time.sleep(wait_time)
