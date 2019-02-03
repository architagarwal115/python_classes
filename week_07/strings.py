'''hello = "hello python world"
print(hello[-18])
print(hello[0:5])

a = "hello "
b = "python"

print(a + b)

print(a*20)

if "h" in a:
    print("h is present")

if "p" in b:
    print("p is present")

hero_list = ["superman","batman","spiderman","ironman"]

if "superman" in hero_list:
    print("superman is alive")
else:
    print("superman is dead")

if "ironman" not in hero_list:
    print("ironman is dead")
else:
    print("ironman is alive")

car_list = ["ferrari","lamborgini","bugati","venom",]

if "honda" in car_list:
    print("honda is speedy")
else:
    print("honda is dead last")

if "ferrari" not in car_list:
    print("ferrari is in the hall of shame")
else:
    print("ferrari in hall of fame")'''

'''s = "I Am A Superboy"
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.isalpha())
print(s.isalnum())
c = (s.replace("I", "Everyone"))
c1 = (c.replace("Am", "Are"))
print(c1.replace("A Superboy", "Superboys And Supergirls"))
print("Trueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")'''

def string_to_uppercase(s):
    y = s.upper()
    return y

output = string_to_uppercase("i am a superboy")
print(output)

hero_list = ["superman","batman","spiderman","ironman"]

for hero in hero_list:
    print(string_to_uppercase(hero))

def string_to_capitalize(v):
    z = v.capitalize()
    return z

print(string_to_capitalize("archit"))

def string_to_lowercase(a):
    b = a.lower()
    return b

print(string_to_lowercase("AWESOME"))

def replace(c):
    d = c.replace("a", "1")
    return d

print(replace("siddhanth"))



