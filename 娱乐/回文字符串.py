def fun(string):
    """
    判断是否回文
    :param string:
    :return:
    """
    if string == string[::-1]:
        print(string, "回文")

    else:
        print(string, "非回文")


str1 = "abccba"
str2 = "abcdeg"

fun(str1)
fun(str2)
