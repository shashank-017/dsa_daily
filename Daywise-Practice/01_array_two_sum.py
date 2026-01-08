"""Day 1 Problem: Two Sum 
Problem statement (simple words)
You are given:
a list of numbers
a target number
You must find two different positions (indexes) such that:

number at index i + number at index j = target


Example:

nums = [2, 7, 11, 15]
target = 9

👉 2 + 7 = 9
👉 indexes are 0 and 1
👉 answer = [0, 1]
"""


# Brute Force Approach:

def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

nums,target = [2, 7, 11, 15], 9
print(two_sum_brute_force(nums, target))

#Complexity Analysis:
# Time Complexity: O(n^2) where n is the number of elements in the list
# Space Complexity: O(1) as we are not using any extra space


# Optimised Approach using Hash Map:
'''
Human logic:
Look at a number
Calculate needed = target - current_number
Ask:
👉 “Have I already seen this needed number before?”
If yes → answer found
If no → store current number for future

'''

def two_sum_optimized(nums, target):
    seen = {}
    for i in range(len(nums)):
        current = nums[i]
        needed = target - current

        if needed in seen:
            return [seen[needed], i]
            break

        seen[current] = i

nums,target = [2, 7, 11, 15], 9
print(two_sum_optimized(nums, target))

#Complexity Analysis:
# Time Complexity: O(n) where n is the number of elements in the list
# Space Complexity: O(n) as we are using extra space for the hash map