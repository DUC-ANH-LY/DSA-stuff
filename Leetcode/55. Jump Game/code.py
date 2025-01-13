from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # TC: O(n^n) -> cache O(n*n)  
        # SC: O(n) -> stack space
        def f(i=0):
            if i >= len(nums)-1:
                return True
            if nums[i] == 0:
                return False

            for j in range(1, nums[i]+1):
                if f(i+j):
                    return True
            return False
        return f()


        # TC: O(n^2)
        # SC: O(n+n) -> stack space + memo array
        @cache
        def f(i=0):
            if i >= len(nums)-1:
                return True
            if nums[i] == 0:
                return False

            for j in range(1, nums[i]+1):
                if f(i+j):
                    return True
            return False
        return f()



        # tabulation 
        # TC: O(n^2) 
        # SC: O(n)
        n = len(nums)
        dp = [False for _ in range(n)] 
        dp[n-1] = True

        for i in range(n-2,-1,-1):
            # if nums[i] == 0:
            #     dp[i] = False
            for j in range(1, min(n,i+nums[i]+1)):
                if dp[j]:
                    dp[i] = True
                    # must have to reduce necessary loop
                    break
        return dp[0]


        # kadane method (for each element's idx compare with the previous max reachable)
        # TC: O(n)
        # SC: O(1) 
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if max_reach < i: 
                return False
            max_reach = max(max_reach, i+nums[i])
        return True
        