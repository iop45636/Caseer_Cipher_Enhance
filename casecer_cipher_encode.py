import string
ascii_list = string.ascii_lowercase

def encode_char(character):
    ans = ""
    for i, j in enumerate(character):
            count_num =  ascii_list.index(j)
            num = count_num + (i+1)
            if num >= 25:
                num = num - 26
            char = ascii_list[num]
            ans = ans + char
    return ans
def return_string(string):
    ans = ""
    char_list = string.split()
    for i in char_list:
        char = encode_char(i)
        ans = ans + char +" "
    return print(ans)

return_string("chris kristy alex john")
