class matrixMultiplication(object):
    def nestedLoop(self, listA, listB):
        l = []
        result = []

        for i in range(0, len(listA)):
            for j in range(0, len(listA)):
                l.append(0)
            result.append(l)
            l = []


        for i in range(0, len(listA)):
            for j in range(0, len(listB[0])):
                result[i][j] = 0
                for k in range(0, len(listB)):
                    result[i][j] += listA[i][k] * listB[k][j]

        return result

A_list = [
    [1,2],
    [3,4],
]

B_list = [
    [1,3],
    [2,5],
]

m = matrixMultiplication()
print(m.nestedLoop(A_list, B_list)) #Output: [ [5, 13], [11, 29] ]