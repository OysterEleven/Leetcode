class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 :
            return 0
        profit = 0
        min = prices[0]
        for i in range(len(prices)):
            if prices[i] < min :
                min = prices[i]
            elif prices[i] - min > profit :
                profit = prices[i] - min
        return profit

    def MaxProfit(self, Prices):
        margin = 0
        profit = 0
        if len(Prices) == 0 :
            return 0
        for i in range(len(Prices)):
            margin = max()


    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 :
            return 0
        maxsum = nums[0]
        middle = 0
        for i in range(len(nums)):
            if middle < 0 :
                middle = nums[i]
            #elif nums[i] + middle > maxsum :
            else:
                middle += nums[i]
            if maxsum < middle :
                maxsum = middle
        return maxsum



if __name__ == '__main__':
    a = Solution()
    #print(a.maxProfit( [ 2,6,1,4,8 ] ))
    print(a.maxSubArray( [-2,1,-3,4,-1,2,2,-5,4] ))
