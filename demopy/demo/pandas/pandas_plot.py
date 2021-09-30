import pandas

# Airport, airline and route data
# https://openflights.org/data.html

airports = pandas.read_csv("airports.csv", header=None, dtype=str)
airports.columns = [
    "id", "name", "city", "country", "iata", "icao",
    "latitude", "longitude", "altitude", "timezone",
    "dst", "tz database time zone", "type", "source"
]
airlines = pandas.read_csv("airlines.csv", header=None, dtype=str)
airlines.columns = ["id", "name", "alias", "iata", "icao", "callsign", "country", "active"]

routes = pandas.read_csv("routes.csv", header=None, dtype=str)
routes.columns = [
    "airline", "airline_id", "source", "source_id",
    "dest", "dest_id", "codeshare", "stops", "equipment"
]

print(airports.head())
print(airlines.head())
print(routes.head())

# Ensures that we have only numeric data in the airline_id column.
routes = routes[routes["airline_id"] != "\\N"]

import math


def haversine(lon1, lat1, lon2, lat2):
    # Convert coordinates to floats.
    lon1, lat1, lon2, lat2 = [float(lon1), float(lat1), float(lon2), float(lat2)]
    # Convert to radians from degrees.
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # Compute distance.
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    km = 6367 * c
    return km


def calc_dist(row):
    dist = 0
    try:
        # Match source and destination to get coordinates.
        source = airports[airports["id"] == row["source_id"]].iloc[0]
        dest = airports[airports["id"] == row["dest_id"]].iloc[0]
        # Use coordinates to compute distance.
        dist = haversine(dest["longitude"], dest["latitude"], source["longitude"], source["latitude"])
    except (ValueError, IndexError):
        pass
    return dist


route_lengths = routes.apply(calc_dist, axis=1)

import matplotlib.pyplot as plt

plt.hist(route_lengths, bins=20)
plt.show()

import seaborn

seaborn.distplot(route_lengths, bins=20)
plt.show()

import numpy

route_length_df = pandas.DataFrame({"length": route_lengths, "id": routes["airline_id"]})
airline_route_lengths = route_length_df.groupby("id").aggregate(numpy.mean)
airline_route_lengths = airline_route_lengths.sort_values("length", ascending=False)
plt.bar(range(airline_route_lengths.shape[0]), airline_route_lengths["length"])


def lookup_name(row):
    try:
        # Match the row id to the id in the airlines dataframe so we can get the name.
        name = airlines["name"][airlines["id"] == row["id"]].iloc[0]
    except (ValueError, IndexError):
        name = ""
    return name


# Add the index (the airline ids) as a column.
airline_route_lengths["id"] = airline_route_lengths.index.copy()
# Find all the airline names.
airline_route_lengths["name"] = airline_route_lengths.apply(lookup_name, axis=1)
# Remove duplicate values in the index.
airline_route_lengths.index = range(airline_route_lengths.shape[0])

from bokeh.charts import Bar

showoutput_notebook()
p = Bar(airline_route_lengths, 'name', values='length', title="Average airline route lengths")
show(p)
