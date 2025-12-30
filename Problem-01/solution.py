class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x) #convert number to string
        return s == s[::-1] #compare with its reversed string
# ✅ Example Test
solution = Solution()
test_num = 12321  # You can change this to any number
result = solution.isPalindrome(test_num)
print(f"Number: {test_num}, Is Palindrome: {result}") 
