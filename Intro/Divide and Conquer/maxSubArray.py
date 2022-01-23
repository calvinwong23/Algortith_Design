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
        
    def maxSubCrossingSubarray(self, arr):


        return 1


nums = [2, -4, 1, 9, -6, 7, -3]

s = DivideAndConquer()
print(s.naiveSolution(nums))
