class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s, low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        def allPalPartUtil(curr, start, end, s):
            print(output, curr, start, end, s)
            if start == n:
                output.append(curr)
                return
            i = start
            while i < end:
                if isPalindrome(s, start, i):
                    curr.append(s[start:i + 1])
                    allPalPartUtil(curr, i + 1, end, s)
                    curr.pop()
                i = i + 1

        output = []
        curr = []
        n = len(s)
        allPalPartUtil(curr, 0, n, s)
        return output