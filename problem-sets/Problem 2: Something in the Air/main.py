# I'm capturing data for my Air Quality tests and I need to be able to start understanding what 
# is the makeup of my data for 3 particular elements. My handy Air Quality tool tracks 
# Nitrogen ("N"), Oxygen ("O"), and Carbon ("C") as elements.
# Given a list of these elements can you develop an algorithm to sort these? 
# I have some conditions on what I need out of this algorithm:
# This must be done in place meaning only transform the array within the list.
# Do this in one pass of the list 
# The algorithm should use constant space meaning no extra lists, please!
# For correctness, the sorting order should be from least to greatest - "C" -> "N" -> "O"

def group_sort(lst):

    lowElementIndex = 0
    currElementIndex = 0
    highElementIndex = len(lst) - 1

    while(currElementIndex <= highElementIndex):
        if lst[currElementIndex] == "C":
            lst[lowElementIndex], lst[currElementIndex] = lst[currElementIndex], lst[lowElementIndex]
            lowElementIndex += 1
            currElementIndex += 1

        elif lst[currElementIndex] == "N":
            currElementIndex += 1

        else:
            lst[currElementIndex], lst[highElementIndex] = lst[highElementIndex], lst[currElementIndex]
            highElementIndex -= 1
    
    return lst

print(group_sort(["N", "N", "O", "C", "O"]))
