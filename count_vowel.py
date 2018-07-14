vowels = 'aeiou'
str1 = raw_input("Enter a string: ")
str1=str1.lower()
count = {}.fromkeys(vowels,0)
for char in str1:
   if char in count:
       count[char] += 1

print(count)
