
import colors_terminal
def print_cell(iteration_count: int, max_value_in_data : int, character_to_print : str) -> str:
    val = (iteration_count/max_value_in_data)*255
    if iteration_count != -1:
        return f"{colors_terminal.RGB(0, round(val), 0)}{character_to_print}{colors_terminal.reset}"
    else:
        return character_to_print

