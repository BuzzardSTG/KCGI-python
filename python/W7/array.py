isRainy = True
humidity = 0.66
temperature = 21
demonstration = None
print(f"{isRainy} - {type(isRainy)}")
print(f"{humidity} - {type(humidity)}")
print(f"{temperature} - {type(temperature)}")
print(f"{demonstration} - {type(demonstration)}")

#1 var = containing many values...
weather_kyoto = ["Kyoto", True, 0.66, 21, None]
print(f"{weather_kyoto} - {type(weather_kyoto)}")
print(f"Number of items in the list: {len(weather_kyoto)}")
print(f"What is humidity (we do not want to know the rest info in Kyoto {weather_kyoto[2]}")

weather_prague = ["Prague", True, 0.77, 13, "Partly cloudy, partly sunny"]
print(f"Number of items in the list: {len(weather_prague)}")
print(f"What is humidity (we do not want to know the rest info in Kyoto {weather_prague[2]}")

weather_marrakech = ["Marrakech", False, 0.61, 21, "Sunny"]

weather = [weather_kyoto, weather_prague, weather_marrakech]
print(f"Temperarure in Kyoto {weather[0][3]}C")
for subarray in weather:
    print(f"Size of the subarray: {len(subarray)}")

print("---")
subarray_counter = 1
attribute_counter = 1
for subarray in weather:
    print(f'Subarray {subarray_counter}')
    for attribute in subarray:
        print(f'Attribute no. {attribute_counter}: {attribute}')
        attribute_counter+=1
    attribute_counter=1
    subarray_counter+=1
    print("---")

#adding
print(f'Before appending: {len(weather_kyoto)}')
print(weather_kyoto)
weather_kyoto.append(None)
print(f'After appending: {len(weather_kyoto)}')
print(weather_kyoto)



weather_vienna = weather_prague.copy()
print(f"Vienna: {weather_vienna}")
weather_vienna[0] = "Vienna"
weather_vienna[2] = 0.95
weather_vienna[3] = 16
weather_vienna[4] = "Rains cats and dogs"
weather_vienna.pop()
print(f"Vienna: {weather_vienna}")
print(f"{id(weather_prague)} vs {id(weather_vienna)}")
print(f"Prague: {weather_prague}") # just want to check if copying from prague, changes vienna did not affect the origin ...
#it does not affect the origin, so we can see that lists are mutable
print(type(weather_vienna))

print(len(weather))
weather.append(weather_vienna)
print(len(weather))
print(weather[3][0])

