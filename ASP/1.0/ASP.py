#!/usr/bin/python3

# STACK INTERPRETER
import string
import sys
import os
import logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class CodeEception(Exception):
    def __init__(self, err):
        super(CodeEception, self).__init__("")
        logging.error(err)
class Block():
    def execute(self):
        global stack
        run()
        return stack.pop()

    def __init__(self, func):
        self.func = func
        self.execute()
        logging.debug("A BLOCK has been initialised with function" + func)

    def __str__(self):
        return str(self.execute())

    def __int__(self):
        return int(self.execute())

    def __bool__(self):
        return bool(self.execute())


def numisprime(number):
    thres = 2
    amount = 0
    for i in range(1, number + 1):
        if number % i == 0:
            amount += 1
    return amount <= thres


ats = []
ats += (list(str(string.digits)))


def addall():
    global stack
    stack = [sum(stack)]


def char():
    global stack
    global code
    global place
    stack.append(code[place + 1])
    place += 1


def pall():
    global stack
    for i in stack:
        print(i)
    stack = []


def pop():
    global stack
    print(stack.pop())


def STR():
    global code
    global place
    global stack
    found = False
    inplace = 0
    internal = code[place + 1:]
    end = ""
    while not found:
        try:
            if internal[inplace] != "\"":
                end += str(internal[inplace])

            else:
                stack.append(end)
                found = True
            inplace += 1
            place += 1
            # stack.append(str(place))
        except IndexError:
            raise CodeEception("Could not find final '\"'")



def decompose(string):
    end = []
    num = ""
    usin = False
    for i in string:
        if i.isdigit():
            usin = True
            num += str(i)
        else:
            if usin:
                end.append(num)
                num = ""
                usin = False
                end.append(i)
            else:
                end.append(i)
    end += num
    return end


def timesall():
    global stack
    num = 1
    for i in stack:
        if type(i) == str:
            if i.isdigit():
                num *= int(i)
            else:
                num *= ord(i)
        else:
            num *= i
    stack = [num]


def add():
    global stack
    x = stack.pop()
    y = stack.pop()
    stack.append(x + type(x)(y))


def times():
    global stack
    x = stack.pop()
    y = stack.pop()
    stack.append(x * y)


def divide():
    global stack
    x=stack.pop()
    y=stack.pop()
    stack.append(y/x)


def minus():
    global stack
    x = stack.pop()
    y = stack.pop()
    stack.append(y - x)
    pass


def reverseall():
    global stack
    stack = stack[::-1]

def swap():
    global stack
    x=stack.pop()
    y=stack.pop()
    stack.append(x)
    stack.append(y)


def printstack():
    global stack
    print(str(stack).replace(", ", " "))


def addchars():
    global code
    global place
    global stack
    found = False
    inplace = 0
    internal = code[place + 1:]
    end = ""
    while not found:
        if internal[inplace] != "\'":
            end += str(internal[inplace])

        else:
            stack += (list(end))
            found = True
        inplace += 1
        place += 1
        # stack.append(str(place))


def run():
    global stack
    global place
    global code
    # print("check BEFORE"+str(stack))
    incode = code
    inplace = place
    place = 0
    code = ""
    x = stack.pop()
    x = str(x)
    # print("RUNNING: "+x)
    # print(x)
    interpret(decompose(x))
    # print("Check AFTER run: "+str(stack))
    code = incode
    place = inplace


def exponent():
    global stack
    x = stack.pop()
    y = stack.pop()
    stack.append(y ** x)


def isprime():
    global stack
    stack.append(numisprime(stack.pop))


def isallprime():
    global stack
    stack=[]
    stack.append(all([numisprime(i) for i in stack]))


def Wloop():
    global stack
    global code
    global place
    fcode = code[place + 2:]
    incode = ""
    for i in fcode:
        if i != "]":
            incode += i
            place += 1
        else:
            place += 1
            break
    place += 1
    try:
        testval = stack.pop()
    except:
        raise CodeEception("Could not find value to repeat by")
    while testval:
        stack.append(incode)
        run()
    stack.pop()


formatchar = "$"


def Floop():
    global stack
    global code
    global place
    global formatchar
    fcode = code[place + 2:]
    print(fcode)
    incode = ""
    for i in fcode:
        if i != "]":
            if i not in["["]:
                incode += i
                place += 1
            else:
                place+=1
        else:
            place+=i
            break
    place += 1
    try:
        repeat = stack.pop()
    except:
        raise CodeEception("Could not find value to repeat by")
    if type(repeat) == Block:
        run()
    if type(repeat) == int:
        for i in range(repeat):
            # print(incode)
            # print(incode.replace("%N", str(i)))
            stack.append(incode.replace(formatchar, str(i)))
            run()
    else:
        for i in repeat:
            stack.append(incode.replace(formatchar, str(i)))
            run()


def SFLoop():
    global stack
    global code
    global place
    global formatchar
    fcode = code[place + 1:]
    print(fcode)
    incode = ""
    for i in fcode:
        if i != "]":
            if i not in["["]:
                incode += i
                place += 1
            else:
                place+=i
        else:
            place += 1
            break
    place += 1
    try:
        repeat = stack.pop()
    except:
        raise CodeEception("Could not find value to repeat by")
    if type(repeat) == Block:
        run()
    if type(repeat) == int:
        for i in range(repeat+1):
            # print(incode)
            # print(incode.replace("%N", str(i)))
            stack.append(incode.replace(formatchar, str(i)))
            run()
    else:
        for i in repeat:
            stack.append(incode.replace(formatchar, str(i)))
            run()


def block():
    global code
    global place
    global stack
    fcode = code[place + 1:]
    incode = ""
    for i in fcode:
        if i != "}":
            incode += i
            place += 1
        else:
            break
    place += 1
    # print(incode)

    # print(fcode)
    # print(incode)
    # stack.append(Block(str(incode)))
    stack.append(incode)
    run()


def ten():
    global stack
    stack.append(10)


def alphabet():
    global stack
    stack.append(string.ascii_lowercase)


keywords = {
    "+": addall,
    "\\": char,
    "\"": STR,
    "P": pall,
    "p": pop,
    "*": timesall,
    "A": add,
    "T": times,
    "M": minus,
    "R": reverseall,
    "r":swap,
    "/": printstack,
    "\'": addchars,
    "c": isprime,
    "C": isallprime,
    "^": exponent,
    "E": run,
    "W": Wloop,
    "{": block,
    "F": Floop,
    "f": SFLoop,
    "X": ten,
    "G": alphabet,
    "D":divide}
ignore = [" ", "-", "\n", "\t"]
stack = []
place = 0
processing = False
processer = None
code = ""


def interpret(c):
    global code
    global place
    global stack
    global ignore
    code = decompose(c)
    # print(code)
    while True:  # code not finished
        # print("[PLACE]"+str(place))
        if place >= len(code):
            break
        char = code[place]
        if char in ignore:
            place += 1
            continue

        if char in keywords:
            keywords[char]()
            place += 1
            continue
        # elif char in ats:
        if char.isdigit():
            char = int(char)
            stack.append(char)
            place += 1
            continue
        else:
            print("nope: " + char + " pos: " + str(place))
            break


def finish():
    global stack
    # er=""
    # print(stack)
    for i in stack:  # IMPLICIT PRINTING!!!
        print(i)
    global code
    global place
    code=""
    stack=[]
    place=0
"""
        #er+=str(i)
        sys.stdout.write(str(i))
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()
    """


        # print(stack)

if __name__ == "__main__":
    if os.path.isfile(sys.argv[-1]) and sys.argv[-1] != __file__:
        file = open(os.path.abspath(sys.argv[-1]))
        code = file.read()
        file.close()
    else:
        while True:
            try:
                interpret(input("[Code] Input code:"))
                finish()
            except Exception as e:
                print(e)
                pass
