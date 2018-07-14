pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str1 =raw_input("Enter Sentence: ")

res= "  "
for char in str1:
   if char not in pun:
        res=res + char

print(res)
