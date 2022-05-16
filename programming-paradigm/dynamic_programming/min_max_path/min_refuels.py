"""
871. Minimum Number of Refueling Stops
"""

def min_refuels_dfs(target, stations, fuel, pos):
    """
    Naive depth first search - try all available possibilities recursively.

    Paramters
    ---------
    target : Target distance to reach.
    stations : Each station contains (position, fuel).
    fuel : The current amount of fuel.
    pos : The current position of the car in miles.
    """

    # Base case: car can travel to target in one shot.
    if fuel >= target - pos:
        return 0

    min_refuels = float('inf')

    # options refer to the list of stations the car can travel to currently.
    options = [s for s in stations if s[0] > pos and (s[0] - pos) <= fuel]

    # For each station in options,
    for i in range(len(options)):

        # Let s be the current station.
        s = options[i]

        # dist refers to the distance between the car's position and the
        # station.
        dist = s[0] - pos

        # Let rfs be the refuels needed to get from the car's current position,
        # with the current amount of fuel, to the target
        rfs = min_refuels_dfs(target, stations, fuel - dist + s[1], s[0]) + 1
        min_refuels = min(min_refuels, rfs)

    return min_refuels


def min_refuels_naive(target, stations, fuel, i):
    """
    Smarter naive solution.
    """

    stations = [(0, 0)] + stations

    # Base case: enough fuel available to reach the target.
    if fuel >= target - stations[i][0]:
        return 0

    # Last station is reached but target hasn't been reached yet. Thus, the car
    # is unable to reach the target.
    if i >= len(stations) - 1:
        return float('inf')

    refuel = no_refuel = float('inf')
    next_fuel = stations[i + 1][1]

    # Distance to next station.
    dist = stations[i + 1][0] - stations[i][0]
    
    # If next station is reacheable,
    if dist <= fuel:
        refuel = min_refuels_naive(target, stations, fuel - dist + next_fuel, i + 1) + 1
        no_refuel = min_refuels_naive(target, stations, fuel - dist, i + 1)

    return min(refuel , no_refuel)


def min_refuels(target, startFuel, stations):
    """
    Bottom-up dynamic programming solution.
    """
    
    n = len(stations)

    # dp[i][j] refers to the max. distance travelled by using 'j' stations out
    # of a total of 'i' stations.
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # If j == 0, no stations were used, thus, the maximum distance travlled is
    # startFuel.
    for i in range(n + 1):
        dp[i][0] = startFuel

    # No point in filling the first row because dp[0][j] means j stations from
    # 0 stations were used which doesn't make sense.
    for i in range(1, n + 1):

        # 1 <= j <= i stations can be used to find the maximum distance for
        # dp[i][j].
        for j in range(1, i + 1):

            # Case 1: don't refuel at current station.
            # Maximum distance car can cover is the same as the distance it
            # could cover from the previous state.
            dp[i][j] = dp[i - 1][j]

            # Case 2: refuel at the current station.
            # But check if car is able to reach this station from the pervious
            # station.
            if dp[i - 1][j - 1] >= stations[i - 1][0]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + stations[i - 1][1])

    # After dp is filled, check which dp[n][j] was the best for reaching the
    # target. i.e. minimum j used.
    for j in range(n + 1):
        if dp[n][j] >= target:
            return j

    return -1
