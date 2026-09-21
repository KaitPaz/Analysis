# Write a function insert_commas(s) that takes in a String representing a positive integer and returns a string representation 
# of the same integer with commas added to appropriately separate every set of 3 digits.
# You must write this function recursively - no loops, list comprehensions, or other implicitly iterative techniques.
# You may assume that the input string represents a valid integer.

 def insert_commas(s):
   if s == "":
      return ""
   
   i = len(s)
   #Makes a group of the last three characters of a string
   group = s[max(0, i - 3): i]

   #Recursive call, assigns all of s except the last 3 characters to rest
   rest = insert_commas(s[:-3])

   if rest != "":
      return rest + "," + group

   else:
      return group
      

   pass 
