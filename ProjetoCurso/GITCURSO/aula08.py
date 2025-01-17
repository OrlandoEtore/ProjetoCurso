#import emoji
#print(emoji.emojize('Olá, Mundo :sunglasses:'))
#print(emoji.emojize("Python is fun :red_heart:"))

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

for x in "banana":
  print(x)

  b = "Hello, World!"
print(b[2:5])


a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"