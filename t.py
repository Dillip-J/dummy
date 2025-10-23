# Tuple
rainfall_data = (120, 150, 180, 120, 90, 110, 130)

# 1. 
print("Length:", len(rainfall_data))

# 2.
print("Tuples are ordered, have index values, and are immutable")

# 3.
if 150 in rainfall_data:
    print("150 is present in the rainfall data")
else:
    print("150 is not present")

# 4.
rain_list = list(rainfall_data)
print("List form:", rain_list)

# 5.
for value in rainfall_data:
    print(value)

# 6 & 7
rain_list.remove(120)
rain=tuple(rain_list)
print("After removing 120:", rain)

print("Before adding 110:", rain)
rain_list.append(110)
rain_d=tuple(rain_list)
print("After adding 110:", rain_d)