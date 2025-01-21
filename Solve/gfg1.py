arr = [12, 35, 1, 10, 34, 1]
# sort = []
class Solution:
    def getSecondLargest(self, arr):
        # larg = arr[0]
        small = arr[0] 
        sort = []
        for i in arr:
            # if i > larg:
                # larg = i  
            if i < small:
                print(i, small)
                # sort.append(i)  
        # for j in arr:
            # if j < larg and  
        print(sort)
obj = Solution()
obj.getSecondLargest(arr)