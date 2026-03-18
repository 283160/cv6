def average_value(values, round_to=2):
    return round(sum(values) / len(values), round_to)


print(average_value([1200, 980, 1430]))       # round_to=2
print(average_value([1200, 980, 1430], 1))    # round_to=1

def convert_coins(value, from_currency, to_currency):
    if from_currency == "gold" and to_currency == "gems":
        return value / 100
    if from_currency == "gems" and to_currency == "gold":
        return value * 100
    return value


print(convert_coins(2500, "gold", "gems"))

def basic_stats(values):
    return min(values), max(values), round(sum(values) / len(values), 2)


min_v, max_v, avg_v = basic_stats([1200, 980, 1430, 1600, 890])
print(min_v, max_v, avg_v)