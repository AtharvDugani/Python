def largestoddnumber(str):
    for i in range(len(str)-1, -1, -1):
        if int(str[i]) % 2 != 0:
            return str[:i+1]
    return ""
print(largestoddnumber("54327"))