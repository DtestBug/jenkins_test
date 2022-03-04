strg = "abccba"
strg1 = "abcde"


def fun(string):
    if string == string[::-1]:

        print("该宇符串是回文字符串")
    else:
        print("该字符串不是回文字符串")


fun(strg)
fun(strg1)
