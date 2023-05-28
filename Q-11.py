Q-11 Something fishy there -
Find output of following:




def f(x,l=[]):
for i in range(x):
l.append(i*i)
print(l)
f(2)
f(3,[3,2,1])
f(3)






The output of the given code will be:


[0, 1]                  # Output of f(2)
[3, 2, 1, 0, 1, 4]      # Output of f(3, [3, 2, 1])
[0, 1, 0, 1, 4]         # Output of f(3)