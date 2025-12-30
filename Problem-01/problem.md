# Problem 01 – Palindrome Number

## 📌 Problem Summary
Determine whether an integer is a palindrome.  
A palindrome is a number that reads the same forward and backward (e.g., 121 is a palindrome, but -121 is not because of the negative sign).

## 💡 Approach
- Convert the number to a string and check if it’s the same when reversed.  
- Alternatively, solve it mathematically without converting to a string (by reversing half the number).  

For simplicity, the string approach is straightforward and efficient for interviews.  

## 🧩 Pseudocode
if number < 0:
return False
convert number to string
check if string == reversed string

## ⏱️ Complexity Analysis
- **Time Complexity**: O(n), where n is the number of digits.  
- **Space Complexity**: O(1) if done mathematically, O(n) if using string conversion.  

## 📝 Notes
- Negative numbers can never be palindromes (because of the "-" sign).  
- Numbers ending with 0 are not palindromes unless the number is 0 itself.  
