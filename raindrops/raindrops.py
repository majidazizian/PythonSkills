def convert(number):
    raindrops = []
    if number % 3 == 0:
        raindrops.append('Pling')
    if number % 5 == 0:
        raindrops.append('Plang')
    if number % 7 == 0:
        raindrops.append('Plong')
    if len(raindrops) == 0:
        return str(number)
    else:
        return "".join(raindrops)
