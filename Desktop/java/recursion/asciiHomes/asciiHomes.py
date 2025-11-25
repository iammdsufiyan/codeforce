def draw_house_on_canvas(canvas, start_col, length, height, direction):
    """
    Draw a single house on the canvas starting at column start_col.
    canvas: list of list of chars (2D array)
    start_col: starting column in the canvas
    length: width of the house
    height: wall height
    direction: 'H','U','D','L','R'
    """
    total_rows = len(canvas)
    # Determine roof rows
    roof_rows = length
    base_row = total_rows - 1  # bottom row of canvas

    # Draw roof
    for i in range(roof_rows):
        row = base_row - (roof_rows + height) + i + 1
        col = start_col + (length - i - 1)
        if direction in ['L', 'R']:
            canvas[row][col + i*2] = "\\" if direction=='L' else "/"
            canvas[row][col] = "/" if direction=='L' else "\\"
        else:
            canvas[row][col] = "/"
            canvas[row][col + i*2] = "\\"

    # Draw walls
    for h in range(height):
        row = base_row - height + h
        canvas[row][start_col] = "@"
        canvas[row][start_col + length - 1] = "&"

    # Draw base
    row = base_row
    for c in range(length):
        canvas[row][start_col + c] = "#"


def ascii_homes_canvas(specs):
    # First, compute total width and max height
    house_data = []
    total_width = 0
    max_height = 0

    for spec in specs:
        lxh = spec[:-1]
        direction = spec[-1]
        length, height = map(int, lxh.split("x"))
        width_needed = max(length*2, length)  # rough width estimate
        total_width += width_needed + 2  # small spacing
        max_height = max(max_height, height + length)
        house_data.append((length, height, direction))

    # Initialize canvas
    canvas = [[' ' for _ in range(total_width)] for _ in range(max_height)]

    # Draw houses one by one
    col_pointer = 0
    for length, height, direction in house_data:
        draw_house_on_canvas(canvas, col_pointer, length, height, direction)
        col_pointer += length + 2  # spacing between houses

    # Print canvas
    for row in canvas:
        print("".join(row).rstrip())

# -----------------------
# Input
# -----------------------
input_line = input().strip()
specs = input_line.split()
ascii_homes_canvas(specs)