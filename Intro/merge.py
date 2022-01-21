from re import L, S


class Solution(object):
    def mergeSort(self, arr):
        "split arr into 2 list"
        arr_len = len(arr)
        midpoint = arr_len // 2

        left = arr[:midpoint]
        right = arr[midpoint:]

        "merge sorted lists"
        if len(left) == 0:
            return right

        elif len(right) == 0:
            return left
        index_left = index_right = 0
        list_merged = []
        list_len_target = len(left) + len(right)

        while len(list_merged) < list_len_target:

            if left[index_left] <= right[index_right]:
                list_merged.append(left[index_left])
                index_left += 1
            else:
                list_merged.append(right[index_right])
                index_right += 1

            if index_right == len(right):
                list_merged += left[index_left:]
                break
            elif index_left == len(left):
                list_merged += right[index_right:]

        
        return list_merged

nums = [1,5,10,6,9,11]
s = Solution()
print(s.mergeSort(nums))