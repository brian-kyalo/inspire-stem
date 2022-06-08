#function to check if number or letter is palindrome
#ask user to select which input to check number or letter
#enter input 


 



def isPalindrome(s):
    return s == s[::-1]
 
s = "radar"
ans = isPalindrome(s)
 
if ans:
    print(f"Yes {s} is palindrome ")
else:
    print(f"No {s} is not palindrome ")
