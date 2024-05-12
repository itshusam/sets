our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


common_destinations = our_routes.intersection(competitor_routes)
print("Destinations that both airlines fly to:", common_destinations)


only_us = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", only_us)


only_competitor = competitor_routes.difference(our_routes)
print("Destinations unique to the competitor airline:", only_competitor)


if not common_destinations:
    print("Neither airline shares any destinations.")
else:
    print("There are shared destinations between the airlines.")