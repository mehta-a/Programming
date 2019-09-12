class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        if haystack == needle:
            return 0

        j = 0
        start = -1
        i = 0
        while i < len(haystack) - len(needle) + 1:
            if haystack[i] == needle[0]:
                start = i
            while (i + j) < len(haystack) and j < len(needle) and haystack[i + j] == needle[j]:
                j += 1
            if j == len(needle):
                return start
            else:
                j = 0
                start = -1
            i += 1
        return start
