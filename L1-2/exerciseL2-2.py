def S(str: str):
    S = str
    if len(str) > 5:
        S = S[0:5] + '...'
    if S[0] in 'Ll': 
        S = S.lower()
    elif S[0] in 'Uu': 
        S = S.upper()
    print(S)


S('Testing string')
S('Lux')
S('up')
S('Luxery')
