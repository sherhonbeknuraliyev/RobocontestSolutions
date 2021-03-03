""""

https://robocontest.uz/tasks/0250

Nokia

"""


s = input()
my_dict = {
    'a':1,
    'b':2,
    'c':3,
    'd':1,
    'e':2,
    'f':3,
    'g':1,
    'h':2,
    'j':1,
    'k':2,
    'l':3,
    'z':4,
    'x':2,
    'v':3,
    'n':2,
    'm':1,
    'q':2,
    'p':1,
    'r':3,
    's':4,
    'w':1,
    'y':3,
    'u':2,
    'i':3,
    'o':3,
    't':1,
    ' ':1,
}
res = 0
for i in s:
    res += my_dict[i]
print(res)
