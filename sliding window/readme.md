In many problems that involve:
* finding shortest, longest substrings with specific constraints
* in arrays or linked lists, when asked to find or calculate something among all the contiguous subarrays (or sublists) of a given size

Sliding windows can be fixed or variable length:
* When asked to find min, max subarray given a constraint - usually a variable window problem
* When asked to find shortest, longest substring given a contraint - usually a variable window problem
* When given an explicit size of the subarray, k - fixed window problem 

Lookout for problems that may appear like sliding window problem, but actually involve lookbacks, e.g.
* [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
