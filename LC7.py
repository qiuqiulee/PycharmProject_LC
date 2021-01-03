x = -120
if x < 0:
    fc = -1
    x = -1*x
else:
    fc = 1
y=0
while x //10 >0:
    y=y*10+x%10
    x=x//10
y=y*10+x%10
print(y*fc)