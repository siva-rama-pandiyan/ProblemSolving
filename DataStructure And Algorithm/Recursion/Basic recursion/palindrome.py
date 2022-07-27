def isPalindrome(word,low,length):
    if (low >= length//2):
        return True
    if word[low] != word[length-low-1]:
        return False
    return isPalindrome(word, low+1, length)
    
word = "madam"
result = isPalindrome(word,0,len(word))
if result:
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")