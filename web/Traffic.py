
MAX_TIME = 60 # in seconds
MAX_VEHICLE = 50

def getGreenTime(n, max_time = MAX_TIME, max_vehicle = MAX_VEHICLE) -> int:
    '''
    Give the time of signal to stay green.

    n: number of vehicles
    max_time: maximum time for stay the light green
    max_vehicle: maximum expected vehicle

    return time in seconds.
    '''
    return max_time * n / max(n, max_vehicle)