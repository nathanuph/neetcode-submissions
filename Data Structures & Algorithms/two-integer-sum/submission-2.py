class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nested for loop brute forcing each combination 
        for i in range (len(nums)):
            for j in range(len(nums)):
                #skip duplicates
                if i == j:
                    continue
                #check if they sum to the target
                if (nums[i]+nums[j]) == target:
                    #order smallest index first and return
                    if i < j:
                        return [i,j]
                    else:
                        return [j,i]
