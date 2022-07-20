def sumNum(num):
    tmpNum = num
    while tmpNum > 9:
        tmpRes = 0
        while tmpNum > 9:
            tmpRes += tmpNum % 10
            tmpNum //= 10
        tmpNum += tmpRes
    return tmpNum


print(sumNum(56)) 

