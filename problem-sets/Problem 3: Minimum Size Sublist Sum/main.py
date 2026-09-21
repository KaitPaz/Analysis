# Given a list of of positive integers nums and a positive integer target return the minimum
# length of a sublist whose sum is greater than or equal to target. If there is no such sublist 
# return 0 instead.

# Recall that a sublist is a contiguous, non-empty sequence of elements within the list.

def min_sublist_len(nums, target):
    # Since a sublist is continguous, sliding window technique

    # Compare elements indivudually
    # if no individual element is not greater than or equal target, compare two at a time then three (use slicing?)

    for num in nums:
        if num >= target:
            return 1 

    window_frame = 2

    while(window_frame <= len(nums)):

        window_sum = sum(nums[:window_frame])
        if window_sum >= target:
            return window_frame

        for start in range(1, len(nums) - window_frame + 1):
            window_sum = sum(nums[start:start + window_frame])

            if window_sum >= target:
                return window_frame

        window_frame += 1

    return 0

print(min_sublist_len([2,3,5,7,11,13,17,19], 76))


