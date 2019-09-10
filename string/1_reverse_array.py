# this is a pretty interesting and efficient solution. takes o(N) for space and O(N)
class Solution:
    def reverseOnlyLetters(self, S):
        alphas = [x for x in S if x.isalpha()]
        sol = []
        for ch in S:
            if ch.isalpha():
                sol.append(alphas.pop())
            else:
                sol.append(ch)
        return ''.join(sol)

    def reverseOnlyLetters2(self, S):
        if len(S) <= 1:
            return S
        arr = list(S)

        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i].isalpha() and arr[j].isalpha():
                # swap
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i = i + 1
                j = j - 1
            else:
                if not arr[i].isalpha():
                    i = i + 1
                if not arr[j].isalpha():
                    j = j - 1
        return ''.join(arr)

if __name__=="__main__":
    print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))