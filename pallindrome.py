def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
string = "malayalam"
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' dhanush is suspendeed for one week")