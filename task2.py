'''Write a program which will find all such numbers which are divisible by 7 but are not a m
ultiple of 5 between 2000 and 3200(both included). The numbers obtained should be printed
in a comma seperated sequence on a songle line.'''

ans = []
num = range(2000, 3201)
for i in num:
    if(i % 7 == 0) and (i % 5 != 0):
        ans.append(i)
print("Total numbers:", len(ans))
print(ans)

