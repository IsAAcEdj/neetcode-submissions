class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        length = rows * cols
        l = 0
        r = length - 1
        beg = 0
        end = len(matrix)
        while(l <= r):
            mid = int(l + (r - l) / 2)
            row = mid // cols
            col = mid % cols
            
            print("it")
            print(mid, "m")
            print(cols)
            if(matrix[row][col] == target):
                return True
            elif(matrix[row][col] > target):
                r = mid - 1
            else:
                l = mid + 1
        return False