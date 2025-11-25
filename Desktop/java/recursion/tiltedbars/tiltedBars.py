import sys
from math import isclose

EPS = 1e-9

# --- Data Structures ---
class Point:
    def __init__(self, x, y):
        self.x = round(x / EPS) * EPS
        self.y = round(y / EPS) * EPS

    def __eq__(self, other):
        return isclose(self.x, other.x, abs_tol=EPS) and isclose(self.y, other.y, abs_tol=EPS)

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"{self.x:.6f},{self.y:.6f}"

class Bar:
    def __init__(self, p1, p2, idx):
        self.id = idx
        # Order points so p1.x < p2.x or if equal p1.y < p2.y for consistent representation
        if (p1.x < p2.x) or (isclose(p1.x, p2.x, abs_tol=EPS) and p1.y < p2.y):
            self.p1 = p1
            self.p2 = p2
        else:
            self.p1 = p2
            self.p2 = p1
        self.mid = Point((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)

    def __str__(self):
        return f"{self.p1}|{self.p2}"

class State:
    def __init__(self, bars, ball_pos):
        # Represent bars as sorted strings for consistent state hashing
        bars_str = []
        for b in sorted(bars, key=lambda x: x.id):
            bars_str.append(str(b))
        self.bar_config = ";".join(bars_str)
        self.ball_pos = ball_pos

    def __eq__(self, other):
        return self.bar_config == other.bar_config and self.ball_pos == other.ball_pos

    def __hash__(self):
        return hash((self.bar_config, self.ball_pos))

# --- Global Variables ---
ground_positions = set()
visited_states = set()

# --- Geometric Helpers ---
def rotate(p, c, dir):
    # Rotate point p around c by 90 degrees * dir (dir = +1 or -1)
    dx = p.x - c.x
    dy = p.y - c.y
    x_prime = c.x + dir * dy
    y_prime = c.y - dir * dx
    return Point(x_prime, y_prime)

def on_segment(p, q, r):
    # Check if point q lies on segment pr
    return (min(p.x, r.x) - EPS <= q.x <= max(p.x, r.x) + EPS and
            min(p.y, r.y) - EPS <= q.y <= max(p.y, r.y) + EPS)

def orientation(p, q, r):
    # Compute orientation of ordered triplet (p, q, r)
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if abs(val) < EPS:
        return 0  # colinear
    return 1 if val > 0 else 2  # clock or counterclock wise

def segments_intersect(p1, p2, p3, p4):
    # Check if segments p1p2 and p3p4 intersect
    o1 = orientation(p1, p2, p3)
    o2 = orientation(p1, p2, p4)
    o3 = orientation(p3, p4, p1)
    o4 = orientation(p3, p4, p2)

    if o1 != o2 and o3 != o4:
        return True

    # Special cases
    if o1 == 0 and on_segment(p1, p3, p2):
        return True
    if o2 == 0 and on_segment(p1, p4, p2):
        return True
    if o3 == 0 and on_segment(p3, p1, p4):
        return True
    if o4 == 0 and on_segment(p3, p2, p4):
        return True

    return False

def get_intersection(bar1, bar2):
    # Returns Point of intersection or None
    p1, p2 = bar1.p1, bar1.p2
    p3, p4 = bar2.p1, bar2.p2

    A1 = p2.y - p1.y
    B1 = p1.x - p2.x
    C1 = A1 * p1.x + B1 * p1.y

    A2 = p4.y - p3.y
    B2 = p3.x - p4.x
    C2 = A2 * p3.x + B2 * p3.y

    det = A1 * B2 - A2 * B1
    if abs(det) < EPS:
        return None  # parallel or coincident

    x = (B2 * C1 - B1 * C2) / det
    y = (A1 * C2 - A2 * C1) / det
    inter = Point(x, y)

    # Check if intersection lies on both segments (with EPS tolerance)
    if (min(p1.x, p2.x) - EPS <= x <= max(p1.x, p2.x) + EPS and
        min(p1.y, p2.y) - EPS <= y <= max(p1.y, p2.y) + EPS and
        min(p3.x, p4.x) - EPS <= x <= max(p3.x, p4.x) + EPS and
        min(p3.y, p4.y) - EPS <= y <= max(p3.y, p4.y) + EPS):
        # Exclude endpoints as landing points
        if inter == p1 or inter == p2 or inter == p3 or inter == p4:
            return None
        return inter
    return None

def point_below_line(p, bar):
    # Returns True if point p is strictly below line segment bar
    dx = bar.p2.x - bar.p1.x
    if abs(dx) < EPS:
        # Vertical line, compare y-coordinates
        return p.y < min(bar.p1.y, bar.p2.y) - EPS
    slope = (bar.p2.y - bar.p1.y) / dx
    y_line = bar.p1.y + slope * (p.x - bar.p1.x)
    return p.y < y_line - EPS

def ball_lands_on_bar(ball_x, bar):
    # Returns y-coordinate on bar at ball_x if ball_x within bar horizontal range, else None
    x1, x2 = bar.p1.x, bar.p2.x
    if x1 - EPS <= ball_x <= x2 + EPS:
        dx = x2 - x1
        if abs(dx) < EPS:
            return None
        slope = (bar.p2.y - bar.p1.y) / dx
        y = bar.p1.y + slope * (ball_x - x1)
        return y
    return None

def is_upper_v(bar, intersection):
    # Determine if the intersection is an upper V vertex for bar
    # For the intersection point, check the two bars form a 'V' with the intersection as vertex,
    # and ball can only land on the upper side of this V.
    # We check the directions of bars at intersection and if intersection is a 'peak' from ball's perspective.

    # Get vectors from intersection to bar endpoints
    v1 = (bar.p1.x - intersection.x, bar.p1.y - intersection.y)
    v2 = (bar.p2.x - intersection.x, bar.p2.y - intersection.y)

    # If both vectors go downward (negative y), intersection is a peak (upper V)
    # We require the intersection to be above both endpoints in y
    return v1[1] < -EPS and v2[1] < -EPS

# --- DFS Logic ---
def dfs(current_bars, ball_pos):
    current_state = State(current_bars, ball_pos)
    if current_state in visited_states:
        return
    visited_states.add(current_state)

    # If ball is on or below ground, record and stop
    if ball_pos.y <= EPS:
        ground_positions.add(round(ball_pos.x))
        return

    # Find next bar to land on:
    # Among all bars, find the one with highest y below ball at ball_pos.x
    landing_bar = None
    landing_y = -float('inf')
    landing_intersection = None

    for bar in current_bars:
        y_on_bar = ball_lands_on_bar(ball_pos.x, bar)
        if y_on_bar is None:
            continue
        if y_on_bar >= ball_pos.y - EPS:
            # bar is above or at ball, cannot land
            continue
        if y_on_bar <= landing_y + EPS:
            # lower than current landing candidate
            continue

        # Check intersections of bar with others to identify upper V constraints
        upper_v_intersection = None
        for other_bar in current_bars:
            if other_bar.id == bar.id:
                continue
            inter = get_intersection(bar, other_bar)
            if inter is not None:
                # Intersection must be below the bar at ball_x to block landing
                if inter.y < y_on_bar - EPS:
                    # Check if intersection is upper V vertex for bar
                    if is_upper_v(bar, inter):
                        if upper_v_intersection is None or inter.y > upper_v_intersection.y:
                            upper_v_intersection = inter

        # If there is an upper V intersection below landing y, ball cannot land here
        if upper_v_intersection is not None:
            continue

        # Update landing bar candidate
        landing_bar = bar
        landing_y = y_on_bar
        landing_intersection = upper_v_intersection

    if landing_bar is None:
        # No bar to land on, ball falls to ground
        ground_positions.add(round(ball_pos.x))
        return

    landing_spot = Point(ball_pos.x, landing_y)
    # Check if landing spot is exactly at bar endpoint
    is_endpoint = landing_spot == landing_bar.p1 or landing_spot == landing_bar.p2

    if is_endpoint:
        # Slide ball slightly down and continue dfs
        dfs(current_bars, Point(landing_spot.x, landing_spot.y - EPS))
        return

    # Tilt bar around intersection if exists, else midpoint
    pivot = landing_intersection if landing_intersection else landing_bar.mid

    for direction in [1, -1]:  # clockwise and counterclockwise
        new_bars = []
        for b in current_bars:
            if b.id == landing_bar.id:
                p1_rot = rotate(b.p1, pivot, direction)
                p2_rot = rotate(b.p2, pivot, direction)
                new_bars.append(Bar(p1_rot, p2_rot, b.id))
            else:
                new_bars.append(b)
        # After tilt, ball slides to both endpoints of rotated bar
        rotated_bar = next(b for b in new_bars if b.id == landing_bar.id)
        dfs(new_bars, rotated_bar.p1)
        dfs(new_bars, rotated_bar.p2)

# --- Main Execution ---
def solve():
    N = int(sys.stdin.readline().strip())
    bars = []
    for i in range(N):
        x1, y1, x2, y2 = map(float, sys.stdin.readline().split())
        bars.append(Bar(Point(x1, y1), Point(x2, y2), i))
    x0, y0 = map(float, sys.stdin.readline().split())
    drop_pos = Point(x0, y0)

    global ground_positions, visited_states
    ground_positions = set()
    visited_states = set()

    dfs(bars, drop_pos)

    for x in sorted(ground_positions):
        print(f"{x} 0")

if __name__ == "__main__":
    solve()