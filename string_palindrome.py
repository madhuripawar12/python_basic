def reverse(s):
    return s[::-1]
 
def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False
 
 
str1 = raw_input("Enter String: ")
ans = isPalindrome(str1)
 
if ans == 1:
    print("String is Palindrome.",str1)
else:
    print("String is not palindrome. ",str1)


