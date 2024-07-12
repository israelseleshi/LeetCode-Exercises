class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x_str = str(x)
        return x_str == x_str[::-1]

number = 121

solution = Solution()
result = solution.isPalindrome(number)

if result == True:
    print("{} is a palindrome.".format(number))
else:
    print("{} is not a palindrome.".format(number))