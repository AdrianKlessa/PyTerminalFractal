def check_julia_convergence(x: float, y: float, c: complex, iterations: int = 10, escape_radius: float = 2.0):
    z = complex(x, y)
    for i in range(iterations):
        z = z ** 2
        z = z + c
        if abs(z) > escape_radius:
            return i
    return -1

