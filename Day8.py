# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = []

# for i in range(rows):
#     row = []
#     for j in range(cols):
#         val = int(input(f"Enter element at position ({i},{j}): "))
#         row.append(val)
#     matrix.append(row)

# print("Matrix is:")
# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end=" ")
#     print()


# print("Maximum value from each row:")
# for i in range(rows):
#     max_val = matrix[i][0]   # assume first element is max
#     for j in range(cols):
#         if matrix[i][j] > max_val:
#             max_val = matrix[i][j]
#     print(max_val)


# class Solution(object):
#     def runningSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         list = []
#         sum = 0
#         for i in nums:
#             sum +=i
#             list.append(sum)
#         print(list)
# obj = Solution()
# obj.runningSum([1,2,3,4])
class Demo():
    def sum(self,nums,target):
        for i in range(1,len(nums)):
            for j in range(1,len(nums)):
                nums[i] + nums[j] == target
        print('target  =',target)
        
obj = Demo()
obj.sum([2,7,10,11],9)



