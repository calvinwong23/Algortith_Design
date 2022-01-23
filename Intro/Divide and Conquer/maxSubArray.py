import sys

class DivideAndConquer(object):
    def naiveSolution(self, arr):
        maxSum = 0

        for i in range(0, len(arr)):
            sum = arr[i]
            maxSum = max(sum, maxSum)

            for j in range(i + 1, len(arr)):
                sum += arr[j]
                maxSum = max(sum, maxSum)

        return maxSum

    def maxSubCrossingSubarray(self, arr, low, mid, high):
        leftSum = 1
        sum = 0

        for i in range(mid, low-1, -1):
            sum = sum + arr[i]

            if sum > leftSum:
                leftSum = sum

        sum = 0
        rightSum = -1
        for i in range(mid + 1, high + 1):
            sum = sum + arr[i]

            if sum > rightSum:
                rightSum = sum
        
        return leftSum + rightSum

    def findMaximumSubArray(self, arr, low = None, high=None):

        if low is None and high is None:
            low, high = 0, len(arr) - 1
        
        if high == low:
            return arr[low]

        mid = (low + high)//2
        maxLeft = self.findMaximumSubArray(arr,low,mid)
        maxRight = self.findMaximumSubArray(arr,mid + 1,high)
        maxCrossing = self.maxSubCrossingSubarray(arr,low, mid,high)

        return max(maxLeft,maxRight,maxCrossing)

nums = [2, -4, 1, 9, -6, 7, -3]

s = DivideAndConquer()
print(s.findMaximumSubArray(nums))
