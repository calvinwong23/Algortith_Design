class Solution(object):
    def insertionSort(self, n):
        for j in range(1, len(n)):
            key = n[j]
            i = j - 1

            while i >= 0 and n[i] > key:
                n[i + 1] = n[i]
                i = i - 1
            
            n[i + 1] = key

        return n

nums = [5,2,4,11,6,1,3,10]
s = Solution()
print(s.insertionSort(nums)) #4