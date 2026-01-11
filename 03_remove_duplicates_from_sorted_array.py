'''
Day 3 — Remove Duplicates from a Sorted Array
(Two Pointers Pattern)


Problem statement (simple words)

You are given a sorted list of numbers.
Example:
nums = [1, 1, 2, 2, 3, 3, 3]


You must:
remove duplicates in-place
keep only one occurrence
return how many unique elements are left

Final array (first part):

[1, 2, 3, _, _, _, _]

Return:
3
'''

# Solution

"""
First: think like a human
Because the array is sorted, duplicates are next to each other.
So naturally:
Keep the first occurrence
Skip all repeated ones
Move forward only when you see a new value

Enter: Two Pointers (plain English)
We’ll use:
i → slow pointer (where to place next unique value)
j → fast pointer (scans the array)
Think:
j explores
i builds the answer
"""

def remove_duplicates(val):
    i = 0
    for j in range(1, len(val)):
        if val[j] != val[i]:
            i += 1
            val[i] = val[j]
    return i+1

remove_duplicates([1, 1, 2, 2, 3, 3, 3])  # [1, 2, 3, _, _, _, _]