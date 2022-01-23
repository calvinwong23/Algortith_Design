class simple(object):
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

class Recurssive(object):
    def merge_lists(self, left_sublist,right_sublist):
        i,j = 0,0
        result = []
        #iterate through both left and right sublist
        while i<len(left_sublist) and j<len(right_sublist):
            #if left value is lower than right then append it to the result
            if left_sublist[i] <= right_sublist[j]:
                result.append(left_sublist[i])
                i += 1
            else:
                #if right value is lower than left then append it to the result
                result.append(right_sublist[j])
                j += 1
        #concatenate the rest of the left and right sublists
        result += left_sublist[i:]
        result += right_sublist[j:]
        #return the result
        return result

    def merge_sort(self, input_list):
        #if list contains only 1 element return it
        if len(input_list) <= 1:
            return input_list
        else:
            #split the lists into two sublists and recursively split sublists
            midpoint = int(len(input_list)/2)
            left_sublist = self.merge_sort(input_list[:midpoint])
            right_sublist = self.merge_sort(input_list[midpoint:])
            #return the merged list using the merge_list function above
            return self.merge_lists(left_sublist,right_sublist)



nums = [1,5,10,6,9,11,3]
s = simple()
#print(s.mergeSort(nums))

r = Recurssive()
print(r.merge_sort(nums))