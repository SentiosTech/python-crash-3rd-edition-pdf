cities = {
    "Madrid": {
        "country": "Spain",
        "population": "3.3 million",
        "fact": "Madrid is known for its vibrant nightlife and cultural heritage."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Tokyo is famous for its blend of traditional and modern architecture."
    },
    "New York": {
        "country": "USA",
        "population": "8.4 million",
        "fact": "New York is home to the iconic Statue of Liberty."
    }
    
}

for city, info in cities.items():
    country = info["country"]
    population = info["population"]
    fact = info["fact"]
    
    print(f"{city} is in {country}. It has a population of {population}. Fun fact: {fact}\n")