def palindrome(text):
  M = len(text)
  if M <= 1:
    return True
  return (text[0] == text[M - 1]) and palindrome(text[1: M - 1])
  

mystr = "asf"
mystr1 = "asfsa"

print(palindrome(mystr))
print(palindrome(mystr1))