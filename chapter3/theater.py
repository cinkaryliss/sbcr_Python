age = 19
pointcard = True
count = 5
if (age <= 18):
    print('チケットを売ることはできません')
elif ((age >= 60) or ((pointcard == True) and (count == 5))):
    print('チケットは1000円です')
else:
    print('チケットは1800円です')
