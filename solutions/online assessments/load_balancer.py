"""
Given:
- the number of servers n
- a list of arrival times of requests
- a list of burst times of said requests (time to process requests)

Return a list of server numbers that service each request.
Server numbers in this list should be -1 if no server is available during arrival time of request. (request is dropped)

Server numbers start from 1 to n.
"""

#
# Complete the 'getServerIndex' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arrival
#  3. INTEGER_ARRAY burstTime
#

import os

# NOT OPTIMIZED, currently runtime is O(n x m), hence timeout occurs for edge cases.
def getServerIndex(n, arrival, burstTime):
    # Write your code here
    
    # initialize each request to -1 (assume request dropped initially)
    result = [-1 for index in range(len(arrival))]
    
    # need new list to preserve request number
    request_indexes = [index for index in range(len(arrival))]
        
    # sort lists
    triplet = list(zip(arrival, burstTime, request_indexes))
    triplet.sort(key=lambda item: item[0])
    sorted_arrival, sorted_burst, sorted_request_indexes = zip(*triplet)
    
    # servers store the next available timing
    servers = [0 for index in range(n)]
    
    for arrival_index, arrival_time in enumerate(sorted_arrival):
        for server_index, server_time in enumerate(servers):
            if arrival_time >= server_time:
                # server available, update result and server available time
                # update result
                request_index = sorted_request_indexes[arrival_index]
                result[request_index] = server_index + 1  # +1 to get server number
                
                # update server available time
                servers[server_index] = arrival_time + sorted_burst[arrival_index]
                
                # stop checking servers
                break
                
    return result


# main function to test
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arrival_count = int(input().strip())

#     arrival = []

#     for _ in range(arrival_count):
#         arrival_item = int(input().strip())
#         arrival.append(arrival_item)

#     burstTime_count = int(input().strip())

#     burstTime = []

#     for _ in range(burstTime_count):
#         burstTime_item = int(input().strip())
#         burstTime.append(burstTime_item)

#     result = getServerIndex(n, arrival, burstTime)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
