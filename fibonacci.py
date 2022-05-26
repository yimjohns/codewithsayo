# a, b  = 0, 1

# while a < 10:
#     print(a)
#     a, b = b, a+b

# 0 1 1 2 3 5 ... 
  

#   a b
# 0 1 1 2 3

a = 0
b = 1

while a < 1000:
    print(a, end=' ')
    a, b = b, a+b

# while True:
   # print('I will loop forever!')
