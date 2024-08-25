def palindrome(s):
    return s[::-1] == s

while True:
    s = input("Enter a palindrome: ");
    print(s,"is palindrome!" if palindrome(s) else "not a palindrome!");