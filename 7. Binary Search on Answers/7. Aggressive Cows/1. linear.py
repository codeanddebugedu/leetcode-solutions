"""Function to check if we can place 'cows' 
cows with at least 'dist' distance apart"""


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
    # Size of list
    n = len(stalls)

    # Sort the nums
    stalls.sort()

    limit = stalls[-1] - stalls[0]
    for i in range(1, limit + 1):
        if not canWePlace(stalls, i, k):
            return i - 1

    # Return the answer
    return limit
