class Solution:
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #we may cut down the possible solutions by applying a constraint to the nums
        
        pos_val = {}
        pos_val_lis = []
        for n in nums:
            if n <= target:
                pos_val_lis.append(n)
                pos_val[n] = nums.index[n]
                
        #try all possible combinations
        print(pos_val)
        for i in range(len(pos_val)):
            strt = pos_val[i]
            for s in range(i+1, len(pos_val)):
                sec = pos_val[s]
                val = strt + sec
                if val == target:
                    x = nums.index[strt]
                    y = nums.index[sec]
                    return [x, y]
                
r = Solution.twoSum([0, 4, 3, 0], 3)
print(r)
