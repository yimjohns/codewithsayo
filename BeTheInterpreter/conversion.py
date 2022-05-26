Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(tuple('Sammy'))
('S', 'a', 'm', 'm', 'y')
print(list('Sammy'))
['S', 'a', 'm', 'm', 'y']
tuple(5000)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tuple(5000)
TypeError: 'int' object is not iterable
tuple(str(5000))
('5', '0', '0', '0')
sam_list = list('Sammy')
sam_list[:3]
['S', 'a', 'm']
