
def convert(T):
    tempC = (T - 32) * (5/9)
    return tempC


def find_windchill(T, W):
    windchill = 35.74 + (0.6215 * T) - (35.75 * W**0.16) + (0.4275 * T * W**0.16)
    return windchill


data = {31:15, 27:18, 25:20, 24:22}
for i in data:
    print("T(F)= ",i, " T(C)= ", convert(i), " wind speed= ", data[i], " wind chill= ",find_windchill(i, data[i])),


