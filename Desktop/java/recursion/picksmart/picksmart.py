import sys
import math
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 6

def round2(x):
    return float(Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def intersect(a, b, c, d):
    x1, y1 = a; x2, y2 = b
    x3, y3 = c; x4, y4 = d
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denom) < 1e-9:
        return None
    px = ((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4)) / denom

    eps = 1e-6
    if (min(x1, x2) - eps <= px <= max(x1, x2) + eps and
        min(y1, y2) - eps <= py <= max(y1, y2) + eps and
        min(x3, x4) - eps <= px <= max(x3, x4) + eps and
        min(y3, y4) - eps <= py <= max(y3, y4) + eps):
        return (round2(px), round2(py))
    return None

def polygon_area(points):
    area = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def dfs_cycle(graph, start):
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for nei in graph[node]:
            if nei == start and len(path) >= 3:
                return path
            if nei not in path:
                stack.append((nei, path + [nei]))
    return None

def main():
    data = sys.stdin.read().replace('\r', '').strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    segs = []
    total_len = 0.0

    for _ in range(n):
        x1 = float(next(it)); y1 = float(next(it))
        x2 = float(next(it)); y2 = float(next(it))
        segs.append(((x1, y1), (x2, y2)))
        total_len += distance((x1, y1), (x2, y2))

    intersections = set()
    for i in range(n):
        for j in range(i + 1, n):
            p = intersect(segs[i][0], segs[i][1], segs[j][0], segs[j][1])
            if p:
                intersections.add(p)

    if len(intersections) < 3:
        sys.stdout.write("Abandoned\n")
        return

    graph = defaultdict(list)
    for s1, s2 in segs:
        points = [s1, s2]
        v = (s2[0] - s1[0], s2[1] - s1[1])
        seg_len_sq = v[0] ** 2 + v[1] ** 2

        for p in intersections:
            vx = (p[0] - s1[0], p[1] - s1[1])
            cross = v[0] * vx[1] - v[1] * vx[0]
            if abs(cross) < 1e-9:
                dot = vx[0] * v[0] + vx[1] * v[1]
                if 0 <= dot <= seg_len_sq and p not in points:
                    points.append(p)

        points.sort(key=lambda pt: ((pt[0] - s1[0]) * v[0] + (pt[1] - s1[1]) * v[1]) / seg_len_sq)
        for i in range(len(points) - 1):
            p1, p2 = points[i], points[i + 1]
            graph[p1].append(p2)
            graph[p2].append(p1)

    polygon = None
    for pt in intersections:
        if len(graph[pt]) >= 2:
            polygon = dfs_cycle(graph, pt)
            if polygon:
                break

    if not polygon or len(polygon) < 3 or polygon_area(polygon) < 1e-6:
        sys.stdout.write("Abandoned\n")
        return

    area_k = polygon_area(polygon)
    used_len = sum(distance(polygon[i], polygon[(i + 1) % len(polygon)]) for i in range(len(polygon)))
    remaining = max(0.0, total_len - used_len)
    area_c = (remaining ** 2) / (4 * math.pi) if remaining > 0 else 0

    sys.stdout.write("Kalyan\n" if area_k > area_c else "Computer\n")

if __name__ == "__main__":
    main()