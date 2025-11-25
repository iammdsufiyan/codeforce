import sys

def movement_cost(degrees, direction_cost, low_cost, high_cost):
    """Calculate cost for moving a hand with tiered pricing."""
    if degrees <= 90:
        return degrees * low_cost * direction_cost
    else:
        return 90 * low_cost * direction_cost + (degrees - 90) * high_cost * direction_cost

def minimal_cost_stepwise(h_angle, m_angle, target_angle, A, B, P, Q, X, Y):
    """
    Compute minimal cost to form target_angle between hands,
    with hour hand moving one step (30°) at a time.
    """
    from math import ceil

    min_cost = float('inf')
    best_h = h_angle
    best_m = m_angle

    # If current angle already matches target, no movement needed
    curr_angle = abs(h_angle - m_angle) % 360
    if curr_angle > 180:
        curr_angle = 360 - curr_angle
    if curr_angle == target_angle:
        return 0, h_angle, m_angle

    # Hour hand can move stepwise, up to ±6 hours (180°)
    for h_steps in range(-6, 7):
        # Compute target hour angle by moving stepwise
        new_h = (h_angle + h_steps * 30) % 360
        # Two possible minute angles to form target
        possible_m = [
            (new_h + target_angle) % 360,
            (new_h - target_angle + 360) % 360
        ]

        for new_m in possible_m:
            # Compute hour movement degrees stepwise
            if h_steps >= 0:
                h_total_deg = h_steps * 30
                h_dir_cost = A  # CW
            else:
                h_total_deg = -h_steps * 30
                h_dir_cost = B  # CCW

            # Minute movement degrees
            m_cw = (new_m - m_angle + 360) % 360
            m_ccw = (m_angle - new_m + 360) % 360

            # Two scenarios: Hour CW + Minute CCW or Hour CCW + Minute CW
            # 1. Hour CW, Minute CCW
            cost1 = movement_cost(h_total_deg, h_dir_cost, P, Q) + movement_cost(m_ccw, B, X, Y)
            if cost1 < min_cost:
                min_cost = cost1
                best_h = new_h
                best_m = new_m

            # 2. Hour CCW, Minute CW
            h_total_deg_ccw = 360 - h_total_deg if h_total_deg > 0 else 0
            cost2 = movement_cost(h_total_deg_ccw, B if h_dir_cost == A else A, P, Q) + movement_cost(m_cw, A, X, Y)
            if cost2 < min_cost:
                min_cost = cost2
                best_h = new_h
                best_m = new_m

    return min_cost, best_h, best_m

def solve():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    hours, minutes = map(int, input_lines[idx].split(':'))
    idx += 1
    N = int(input_lines[idx]); idx += 1
    A, B = map(int, input_lines[idx].split()); idx += 1
    P, Q = map(int, input_lines[idx].split()); idx += 1
    X, Y = map(int, input_lines[idx].split()); idx += 1
    queries = [int(input_lines[idx + i]) for i in range(N)]

    # Initial angles
    current_h = (hours % 12) * 30 + (minutes / 60) * 30
    current_m = minutes * 6
    total_cost = 0

    for angle in queries:
        cost, current_h, current_m = minimal_cost_stepwise(
            current_h, current_m, angle, A, B, P, Q, X, Y
        )
        total_cost += cost

    print(int(total_cost))

if __name__ == "__main__":
    solve()