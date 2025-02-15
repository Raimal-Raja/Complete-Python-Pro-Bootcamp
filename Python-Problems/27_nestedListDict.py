travel_log = [
    {
    "country": "france",
    "visited": 12, 
    "cities" : ["paris", "lille", "Diljon"]
     },
    {
    "country":"Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country['country'] = country_visited
    new_country['visits'] = times_visited
    new_country['cities'] = cities_visited
    travel_log.append(new_country)
    
add_new_country("Russia", 2, ["Moscow", "Saint Petric"])
print(travel_log)
