class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """

        total = len(original)

        if m*n != total:
            return []

        ans = []
        itr = 0

        for itera in range(1,m+1):
            arr = []
            while itr < itera*n :
                arr.append(original[itr])
                itr+=1
            ans.append(arr)
        return ans