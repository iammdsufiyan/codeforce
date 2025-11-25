import math

def reflect_over_line(x0, y0, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    a = dy
    b = -dx
    c = dx*y1 - dy*x1
    d = (a*x0 + b*y0 + c)/(a**2 + b**2)
    xr = x0 - 2*a*d
    yr = y0 - 2*b*d
    return (xr, yr)

def side_of_line(x0, y0, x1, y1, x2, y2):
    val = (x2-x1)*(y0-y1) - (y2-y1)*(x0-x1)
    if val > 1e-8:
        return "left"
    elif val < -1e-8:
        return "right"
    else:
        return "on"

# Input
A = float(input())
x1, y1, x2, y2 = map(float, input().split())
side_len = math.sqrt(A)

# Original square corners
square = [(0,0), (0,side_len), (side_len,side_len), (side_len,0)]

# Set to hold points
points = set()

for x, y in square:
    points.add((round(x,2), round(y,2)))
    if side_of_line(x, y, x1, y1, x2, y2) == "left":
        xr, yr = reflect_over_line(x, y, x1, y1, x2, y2)
        points.add((round(xr,2), round(yr,2)))

# Remove duplicates automatically with set
points = list(points)
points.sort(key=lambda p: (p[0], p[1]))

# Output
for px, py in points:
    print(f"{px:.2f} {py:.2f}")