cars = {"car1": "Audi", "car2": "Toyota", "car3": "Honda"}

#print(cars["car2"])

cars["car3"] = "VW"
cars["car3"]

#print(cars)

for key in cars:
    print(key)
    print(cars[key])

