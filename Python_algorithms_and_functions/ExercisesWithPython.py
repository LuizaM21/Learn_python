from pprint import pp


# Write a function that takes a list of response times and returns a tuple (count, total, maximum),
# using a loop only (no len, sum or max).
def stats(times: list[int]) -> tuple[int, int, int]:
    if not times:
        return 0, 0, 0

    count = 0
    total = 0
    maximum = times[0]

    for ms in times:
        count += 1
        total += ms
        if ms > maximum:
            maximum = ms

    return count, total, maximum

# Write low_and_avg(times) that returns (minimum, average) using one loop.
def low_and_avg(values: list[int])-> tuple[int, float] | tuple[int, float | int]:
    if not values:              # 1. handle empty list FIRST
        return 0, 0.0
    low = values[0]             # 2. start from a real item
    total = 0
    for item in values:
        total += item
        if item < low:          # 3. compare with the smallest so far
            low = item

    return low, total / len(values)   # 4. safe: a list isn't empty here

# Write slowest_endpoint(results) that takes the (endpoint, ms) tuples and returns the endpoint name with the highest response time.
def slowest_endpoint(result: list[tuple[str, int]]) -> str | None:
    if not result:
        return None
    best_endpoint, best_ms = result[0]
    for endpoint, ms in result:
        if ms > best_ms:
            best_endpoint, best_ms = endpoint, ms
    return best_endpoint

# Write max_per_endpoint(results) that returns a dict mapping each endpoint to its highest response time.
def max_per_endpoint(result: list[tuple[str, int]]) -> dict[str, int]:
    if not result:
        return {}
    max_ms_per_endpoint = {}
    for endpoint, ms in result:
        if endpoint not in max_ms_per_endpoint or ms > max_ms_per_endpoint[endpoint]:
            max_ms_per_endpoint[endpoint] = ms
    return max_ms_per_endpoint

# Write count_and_total(results) that returns, per endpoint, its count and total time.
def count_and_total(result: list[tuple[str, int]]) -> dict[str, dict[str,int]]:
    if not result:
        return {}
    stats_results = {}
    for endpoint, ms in result:
        if endpoint not in stats_results:
            stats_results[endpoint] = {'count': 1, 'total': ms}
        else:
            stats_results[endpoint]['total'] +=ms
            stats_results[endpoint]['count'] +=1
    return stats_results

# Return {endpoint: {"count", "avg" (2 decimals), "max"}} from (endpoint, ms) tuples; empty input -> {}.
def summarize(results_api: list[tuple[str, int]]) -> dict[str, dict]:
    stats_result = {}
    if not results_api:
        return {}

    for endpoint, ms in results_api:
        if endpoint not in stats_result:
            stats_result[endpoint] = {'count': 1, 'total': ms, 'max': ms}
        else:
            s = stats_result[endpoint]
            s['count'] += 1
            s['total'] += ms
            s['max'] = max(s['max'], ms)

    for s in stats_result.values():
        s['avg'] = round(s['total'] / s['count'], 2)
        del s['total']
    return stats_result


if __name__ == '__main__':
    print(stats([100, 200, 300]))
    print(low_and_avg([120, 80, 100]))  # (80, 100.0)
    print(low_and_avg([]))  # (0, 0.0)

    results = [("/login", 120), ("/accounts", 500), ("/login", 80)]
    print(slowest_endpoint(results))  # "/accounts"
    print(slowest_endpoint([]))  # None

    results = [("/login", 120), ("/accounts", 300), ("/login", 80), ("/accounts", 500)]
    print(max_per_endpoint(results))    # {'/login': 120, '/accounts': 500}
    print(max_per_endpoint([]))     # {}

    results = [("/login", 120), ("/accounts", 300), ("/login", 80)]
    print(count_and_total(results))        # {'/login': {'count': 2, 'total': 200}, '/accounts': {'count': 1, 'total': 300}}

    results = [("/a", 10), ("/a", 10), ("/b", 10), ("/b", 10), ("/b", 10), ("/a", 10), ("/b", 20)]
    print(count_and_total(results))     # expected: {'/a': {'count': 3, 'total': 30}, '/b': {'count': 3, 'total': 30}}

    results = [("/login", 120),
               ("/accounts", 300),
               ("/login", 80),
               ("/accounts", 500),
               ("/login", 100)]

    pp(summarize(results))
    # {'/login':    {'count': 3, 'avg': 100.0, 'max': 120},
    #  '/accounts': {'count': 2, 'avg': 400.0, 'max': 500}}
    pp(summarize([]))  # {}
