def palindrome(s):
    return s[::-1] == s

while True:
    s = input("Enter a palindrome: ");
    print(s,"Yes!" if palindrome(s) else "No!", sep="\n");