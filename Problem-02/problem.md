# Problem 02 – Two Sum

## 📌 Problem Summary
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.  
You may assume that each input has exactly one solution, and you may not use the same element twice.  
Return the answer in any order.

## 💡 Approach
- Use a **hash map (dictionary)** to store numbers as keys and their indices as values.  
- For each number, check if `target - num` already exists in the dictionary.  
- If yes, return the stored index and current index.  
- If not, store the number with its index in the dictionary.  

This ensures a single-pass O(n) solution.  

## 🧩 Pseudocode
initialize empty hash map
for each index, num in nums:
complement = target - num
if complement in hash map:
return [hash_map[complement], index]
store num in hash map with index


## ⏱️ Complexity Analysis
- **Time Complexity**: O(n) – we scan the list once.  
- **Space Complexity**: O(n) – in the worst case, we store all elements in the dictionary.  

## 📝 Notes
- Brute force approach would be O(n²) using nested loops.  
- Hash map reduces it to O(n) by trading space for speed.  
- Order of indices doesn’t matter (both [i, j] and [j, i] are correct).  
