"""
1480. Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
------------------------------------------------------
---Time Complexity: O(n)
---Space Complexity O(1)
------------------------------------------------------
"""
#------Python3 Code------
# Runtime: 26ms
# Memory: 16.5 Mb
"""
Hint: Think about how we can calculate the i-th number in the running sum from the (i-1)-th number.
"""
from typing import List
class Solution():
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] +=nums[i-1]
        return nums
    
nums = [1,2,3,4]       
so = Solution()  
print(so.runningSum(nums))

#------C++ Code--------
# Runtime: 0ms
# Memory: 8.6 Mb
"""
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for(int i=1; i <nums.size(); i++)
        {
            nums[i] += nums[i-1];
        };
        return nums;
}
};
"""