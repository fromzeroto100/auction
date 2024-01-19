new_country = {}
country = input("Entera a name: ")
visits = int(input("Entera visited times: "))
cities = input("Entera a name with comma: ").split(", ")

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Marcel", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Frankfurt"]
    },

]

def add_new_country(name, visits, cities):
    new_country = {"country": name, "visits": visits, "cities": cities}
    travel_log.append(new_country)


add_new_country(country, visits, cities)


# new_dictionary = {
#     "country": "Brazil",
#     "visits": 2,
#     "cities": ["Rio", "Sao Paulo"]

#      }

print(travel_log)