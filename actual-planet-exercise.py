planet_list = ["Mercury", "Mars"]
print(planet_list)
# planet_list.append("Jupiter")
# print(planet_list)

# planet_list.append("Jupiter")
# print(planet_list)

planet_list.extend(["Jupiter", "Saturn"])
print(planet_list)

planet_list.insert(1, "Earth")
print(planet_list)
planet_list.insert(1, "Venus")
print(planet_list)

planet_list.extend(["Uranus", "Neptune", "Pluto"])
print(planet_list)

rocky_planets = planet_list[0:4]
print(rocky_planets)
print (planet_list)

del planet_list[-1]
print(planet_list)