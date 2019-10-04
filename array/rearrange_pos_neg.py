class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        def rightRotate(arr, n, outOfPlace, cur):
            temp = arr[cur]
            for i in range(cur, outOfPlace, -1):
                arr[i] = arr[i - 1]
            arr[outOfPlace] = temp
            return arr

        n = len(A)
        i = 0
        outOfPlace = -1
        while i < n:
            if outOfPlace >= 0:
                if (A[i] > 0 and A[outOfPlace] < 0) or (A[i] < 0 and A[outOfPlace] >= 0):
                    A = rightRotate(A, n, outOfPlace, i)
                    if (i - outOfPlace > 2):
                        outOfPlace += 2
                    else:
                        outOfPlace = - 1
            if (outOfPlace == -1):
                if ((A[i] >= 0 and i % 2 == 0) or
                        (A[i] < 0 and i % 2 == 1)):
                    outOfPlace = i
            i += 1
        return A

if __name__=="__main__":
    s = Solution()
    print(s.solve([15, 23, 6, -2, 26, 10, -14, -8, 5, -7, 27]))