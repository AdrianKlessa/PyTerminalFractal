
import check_convergence


def get_julia(columns: int, lines: int, c: complex):
    # Range between -2-2i to 2+2i
    if columns <= 0 or lines <= 0:
        return [[0.0]]
    horizontal_step = 4 / columns
    vertical_step = 4 / lines
    current_x = -2.0
    current_y = 2.0
    data = []
    for y_i in range(lines):
        data.append([])
        for x_i in range(columns):
            data[-1].append(check_convergence.check_julia_convergence(current_x, current_y, c))
            current_x = current_x + horizontal_step
        current_x = -2.0
        current_y -= vertical_step
    return data