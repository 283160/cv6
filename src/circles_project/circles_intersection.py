circle_1 = {"x": 8, "y": 3, "r": 2}
circle_2 = {"x": 3, "y": 6, "r": 10}

from circles_stats import has_intersection
prunik = has_intersection(circle_1, circle_2)
if prunik["intersects"] == True and prunik["intersections_count"] == 2:
    print("Kružnice mají dva průniky.")
elif prunik["intersects"] == True and ["intersections_count"] == 1:
    print("Kružnice se dotýkají v jednom bodě.")
else:
    print("Kružnice se nedotýkají.")