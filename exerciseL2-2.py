S = str(input('Введіть слово: '))     
print('Введене слово:')
if len(S) < 5:                
  print(S)
else: 
  print(S[0:5],"...")
