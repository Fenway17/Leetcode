# TWO POINTERS / SLIDING WINDOW
# use 2 separate pointers
# sliding window moves right pointer first, then left pointer if some condition is met
# two pointers sometimes have both pointers start at opposite ends

# Dynamic Programming 1 - Memoization
# given multiple "options", start from considering only 1 of them, and slowly add in more options into the problem
# each step should record its results, accounting for previous results
# useful for problems relating to "positions"
# -------------
# create array / table of past results

# Dynamic Programming 2 - Recurrence Relation
# find number of ways "something" can be done
# given multiple options, (sometimes) difference actions can be taken
# from taking a different action, a new version of a solution can be created
# can be used to ultimately find number of solutions or best solution for a given problem
# -------------
# define a recursive function to help solve the problem
# - create and ensure base cases are correct
# - possibly use @cache to cache results of recursive function
#   - @cache does the memoization work for the solution
#   - might not always be an optimal runtime if @cache is not usable