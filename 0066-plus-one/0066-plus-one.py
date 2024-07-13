class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits = str(int(''.join(map(str, digits))) + 1)
            return [int(digit) for digit in digits]    
        
digits = [1, 2, 3]
solution = Solution()

result = solution.plusOne(digits)
print(result)