def commonStrSet4(str1: str, str2):
    return ''.join([ch if ch.isalpha() 
    else '' for ch in set(str1).intersection(set(str2))])
print(commonStrSet4('god \tday', 'good \t morning')) 
