# Arrivals and Departutres

def MaxConcurrent(n, timesAndIDs):
    # Write your code here
    # Sort the list by timestamp
    timesAndIDs.sort(key=lambda x: (x[0]))
    # Variables for current and max occupancy
    current_occupancy = 0
    max_occupancy = 0
    # Track whether ID has arrived
    arrival_id = {}
    # Iterate for the number of events
    for i in range(n):
        current_time = timesAndIDs[i][0]
        # Process all events with current time
        arrivals = 0
        departures = 0
        # Check current time is equal to position
        while i < n and timesAndIDs[i][0] == current_time:
            time, id_num = timesAndIDs[i]
            # Check if its a departure
            if id_num in arrival_id:
                departures += 1
                # Remove from list
                del arrival_id[id_num]
            else:
                # Must be arrival
                # Add to arrival_list
                arrival_id[id_num] = True
                arrivals += 1
            i += 1

        net_change = arrivals - departures
        current_occupancy += net_change
        if current_occupancy > max_occupancy:
            max_occupancy = current_occupancy
    
    return max_occupancy
    
    
        
        

n = 10
timesAndIDs = [[5, 11209], [6, 59752], [8, 11209], [13, 39712], [19, 39013], [4, 39013], [3, 66310], [11, 39712], [17, 59752], [14, 66310]]
MaxConcurrent(n, timesAndIDs)