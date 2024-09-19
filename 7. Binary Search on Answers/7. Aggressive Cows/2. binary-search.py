def canWePlace(stalls, dist, cows):
    # Size of array
    n = len(stalls)

    # Number of cows placed
    cntCows = 1

    # Position of last placed cow
    last = stalls[0]
    for i in range(1, n):
        if stalls[i] - last >= dist:
            # Place next cow
            cntCows += 1

            # Update the last location
            last = stalls[i]
        if cntCows >= cows:
            return True

    return False


def aggressiveCows(stalls, k):
    # Sort the stalls to place cows in sorted positions
    stalls.sort()

    # Binary search for the maximum minimum distance
    low = 1  # Minimum possible distance
    high = stalls[-1] - stalls[0]  # Maximum possible distance

    result = 0

    while low <= high:
        mid = (low + high) // 2  # Try this distance

        if canWePlace(stalls, mid, k):
            # If we can place cows with at least `mid` distance, try for a larger distance
            result = mid
            low = mid + 1
        else:
            # If we can't place cows with at least `mid` distance, try for a smaller distance
            high = mid - 1

    return result
