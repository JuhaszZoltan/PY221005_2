# szöveges, egész, lebegőpontos, logikai

# string
a:str = 'cica'

# integer
b:int = 1984

# floating point number
c:float = 3.1415

# Boolean
d:bool = True # vagy False


print(10 / 3) # 'sima' osztás OP: 3.333333...
print(10 // 3) # egész osztás (div) OP: 3
print(10 % 3) # maradékszámítás (mod) OP: 1

print(2 ** 10) # hatványozás OP: 1024
print(16 ** (1/2)) # x^1/n = n sqrt(x)

print('kutya' + 'ház') # összefűzés/konkatenáció OP: 'kutyaház'
print(3 * 'kutya ') # OP: 'kutya kutya kutya '

print(True and False) # OP: False
print(True or False) # OP: True
print(not True) # OP: False

# 'tartalmazza': <elem> benne van e a <kollekció>-ban?
print(65 in [3, 5, 65, 12, 1, 7, 3]) # OP: True
print('a' in {'v', 'W', 'q', 'A'}) # OP: False

# comparison (összehaszonlító) operátorok
# <, >, <=, >=, ==, !=
print(10 != 5) # OP: True

#             T
#        F             T
print(10 < 5 or 3 / 2 != 11)