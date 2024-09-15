"""
Given:
- a list representing the time taken for the 'platform' to process a message
- a list representing the time taken for a 'support device' to process a message

Return the minimum time taken to process all messages.

Support devices work simultaneously (in parallel).
The platform cannot process messages simultaneously (processes them one at a time).
"""

#
# Complete the 'getMinimumTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY platformTime
#  2. INTEGER_ARRAY supportTime
#

def getMinimumTime(platformTime, supportTime):
    # Write your code here
    
    final_min_time = max(supportTime)  # start from using support only
    
    # sort given lists in order of support time
    paired = list(zip(platformTime, supportTime))
    paired.sort(key=lambda item: item[1])
    sorted_platform, sorted_support = zip(*paired)
    
    # idea: start from using only support devices, 
    #       then slowly transfer messages from support devices with highest time taken to platform
    i = len(sorted_support) - 1  # start from the end
    total_platform_time = 0
    min_support_time = final_min_time
    # slowly transfer messages from support device over to platform
    while (i >= 0):
        # update total platform time
        total_platform_time += sorted_platform[i]  # transfer message to platform
        
        # update min support time
        if (i-1 >= 0 and sorted_support[i-1] < min_support_time):
            min_support_time = sorted_support[i-1]
        
        # update final min time
        possible_min = max(total_platform_time, min_support_time)
        final_min_time = min(possible_min, final_min_time)
        
        # check if total platform time is too high
        if total_platform_time >= min_support_time:
            # not possible to get better mins anymore
            break
             
        i -= 1
    
    return final_min_time
    
# main function to test
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     platformTime_count = int(input().strip())

#     platformTime = []

#     for _ in range(platformTime_count):
#         platformTime_item = int(input().strip())
#         platformTime.append(platformTime_item)

#     supportTime_count = int(input().strip())

#     supportTime = []

#     for _ in range(supportTime_count):
#         supportTime_item = int(input().strip())
#         supportTime.append(supportTime_item)

#     result = getMinimumTime(platformTime, supportTime)

#     fptr.write(str(result) + '\n')

#     fptr.close()
