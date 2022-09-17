import csv
import json

import helper


def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines


def read_airports(filename='airports.dat'):
    airports = {}  # Return a map of code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1] 
    return airports


def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    routes = {}  # Map from source -> list of dests
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            source, dest = line[2], line[4]
            if source not in routes:
                routes[source] = []  # if a new source, start as empty dest
            routes[source].append(dest)  # otherwise add the new dest
    return routes
    


def find_paths(routes, source, dest, max_segments):
    # Run a graph search algorithm to find paths from source to dest.
    # Run the BFS search
    frontier = {source}
    seen = {source: {(source, )}}
    for steps in range(max_segments):
        next_frontier = set()
        for airport in frontier:
            for target in routes.get(airport, ()):
                if target not in seen:
                    next_frontier.add(target)
                    seen[target] = set()
                for path in seen[airport]:
                    if len(path) != steps + 1:
                        continue
                    seen[target].add(path + (target, ))
        frontier = next_frontier
    return seen[dest]



def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    output = {}  # Build a collection of output paths!

    for path in paths:
        segments = len(path) - 1
        if segments not in output:
            output[segments] = []
        output[segments].append(rename_path(path, airports))

    # Write the output to JSON!
    with open(f"{source}->{dest} (max {max_segments}).json", 'w') as f:
        json.dump(output, f, indent=2, sort_keys=True)
    


if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)


# test/see my functions
#airlines = read_airlines()
#print(airlines)
# => {'N/A': 'Private flight', 'GNL': '135 Airways', 'RNX': '1Time Airline', 'WYT': '2 Sqn No 1 Elementary Flying Training School', 'TFU': '213 Flight Unit', 'CHD': '223 Flight Unit State Airline', 'TTF': '224th Flight Unit', 'TWF': '247 Jet Ltd', 'SEC': '3D Aviation', 'MLA': '40-Mile Air', 'QRT': '4D Air', 'THD': '611897 Alberta Limited', 'AAA': 'Ansett Australia', '': 'Worldspan',...}

#airports = read_airports()
#print(airports)
# => {'GKA': 'Goroka Airport', 'MAG': 'Madang Airport', 'HGU': 'Mount Hagen Kagamuga Airport', 'LAE': 'Nadzab Airport', 'POM': 'Port Moresby Jacksons International Airport', 'WWK': 'Wewak International Airport', 'UAK': 'Narsarsuaq Airport', 'GOH': 'Godthaab / Nuuk Airport', 'SFJ': 'Kangerlussuaq Airport', 'THU': 'Thule Air Base', 'AEY': 'Akureyri Airport',...}

#routes = read_routes()
#print(routes)
# => {'AER': ['KZN', 'DYU', 'KIV', 'MSQ', 'TAS', 'TZX', 'EVN', 'KRR', 'DME', 'EVN', 'IST', 'KRR', 'LED', 'OMS', 'SVO', 'SVX', 'TAS', 'LBD', 'IST', 'DME', 'LBD', 'SVX', 'DME', 'VKO', 'DME', 'KJA'], 'ASF': ['KZN', 'MRV', 'DME', 'LED', 'SCO', 'DME', 'SVO', 'SAW'],...}
