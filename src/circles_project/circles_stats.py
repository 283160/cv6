import math
def radius_sum(r1, r2): #součet poloměrů
    return r1 + r2

def euclid_distance(x1, y1, x2, y2): #euklidovská vzdálenost
    x = (x2 - x1) ** 2
    y = (y2 - y1) ** 2
    d = (x + y) ** 0.5
    return d

def has_intersection(circle_1, circle_2):
    slo = {"intersects": False, "intersections_count": 0}
    x1 = circle_1['x']
    y1 = circle_1['y']
    r1 = circle_1['r']
    x2 = circle_2['x']
    y2 = circle_2['y']
    r2 = circle_2['r']
    d = euclid_distance(x1, y1, x2, y2)
    radius = radius_sum(r1, r2)
    if d > radius:
        return slo
    elif d < radius:
        slo["intersects"] = True
        slo["intersections_count"] = 2
    elif math.isclose(d, radius):
        slo["intersects"] = True
        slo["intersections_count"] = 1
    else:
        print("Nesprávné zadání kružnic")
    return slo


