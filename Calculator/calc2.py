import math
import statistics
from fractions import Fraction
from collections import Counter

def FRS(dec):
    dpart = dec
    for start in range(len(dpart)):
        for i in range(1, (len(dpart) - start) // 2 + 1):
            patt = dpart[start:start + i]
            rcount = (len(dpart) - start) // i
            if patt * rcount == dpart[start:start + rcount * i]:
                return patt
    
    return None

def RDTF(dec):
    frac = Fraction(dec).limit_denominator()
    denominator = frac.denominator
    while denominator % 2 == 0:
        denominator //= 2
    while denominator % 5 == 0:
        denominator //= 5
    return denominator != 1

def Add():
    n = int(input("How many numbers would you like to add: "))
    res = 0
    for i in range(n):
        num = int(input(f"Enter #{i+1}: "))
        res += num
    print(f"The total sum is {res}.")

def Sub():
    m = int(input("Enter the main number: "))
    n = int(input("How many numbers would you like to subtract from the main number: "))
    for i in range(n):
        num = int(input(f"Enter subtrahend #{i+1}: "))
        m -= num
    print(f"The total difference is {m}.")

def Mult():
    n = int(input("How many numbers would you like to multiply: "))
    res = 1
    for i in range(n):
        num = int(input(f"Enter multiplier #{i+1}: "))
        res *= num
    print(f"The total product is {res}.")
 
def Div():
    m = int(input("Enter the dividend: "))
    d = int(input("Enter the divisor: "))
    res = str(m/d)
    fres = m//d
    rem = m%d
    if RDTF(res) == True:
        res = f"{fres}.{FRS(res)}"
    print(f"{m}÷{d} is about {res}, or {fres} with a remainder of {rem}.")

def Exp():
    b = input("Enter the base: ")
    e = input("Enter the exponent: ")
    if "." in b:
        b = float(b)  
    else:
        b = int(b)
    if "." in e:
        e = float(e)
    else:
        e = int(e)  
    res = b**e
    print(f"{b} to the power of {e} is about {round(res, 5)}.")

def Fact():
    x = int(input("Enter the number you want to find the factorial of: "))
    nx = x
    res = 1
    for i in range(x):
        res *= x
        x -= 1
    print(f"{nx} factorial is {res}.")

def Mean():
    n = int(input("How many numbers do you want to find the mean of: "))
    res = 0
    for i in range(n):
        y = input(f"Enter # {i+1}: ")
        if "." in y:
            y = float(y)
        else:
            y = int(y)
        res += y
    res /= n
    print(f"The mean is {res}.")
    
def Med():
    n = int(input("How many numbers do you want to find the median of: "))
    ln = []
    for i in range(n):
        x = input(f"Enter #{i+1}: ")
        if "." in x:
            x = float(x)
        else:
            x = int(x)
        ln.append(x)
    res = statistics.median(ln)
    print(f"The median is {res}.")

def Mode():
    n = int(input("How many numbers would you like to find the mode of: "))
    ln = []
    for i in range(n):
        x = input(f"Enter #{i + 1}: ")
        if "." in x:
            x = float(x)
        else:
            x = int(x)
        ln.append(x)
    cs = Counter(ln)
    mc = max(cs.values())
    m = [key for key, value in cs.items() if value == mc]
    if len(m) == 1:
        print(f"The mode is {m[0]}.")
    else:
        print(f"The modes are {m}.")

def Range():
    n = int(input("How many numbers would you like to find the range of: "))
    ln = []
    for i in range(n):
        x = input(f"Enter #{i+1}: ")
        if "." in x:
            x = float(x)
        else:
            x = int(x)
        ln.append(x)
    res = max(ln) - min(ln)
    print(f"The range is {res}.")

def Root():
    t = input("Enter the number you want to find the root of: ")
    n = input("Enter the root: ")
    if "." in t:
        t = float(t)
    else:
        t = int(t)
    if "." in n:
        n = float(n)
    else:
        n = int(n)
    res = t**(1/n)
    print(f"Root {n} of {t} is about {round(res, 10)}.")

def Log():
    x = input("Enter the number you want to perform a logarithm on: ")
    b = input("Enter the base: ")
    if "." in x:
        x = float(x)
    else:
        x = int(x)
    if "." in b:
        b = float(b)
    else:
        b = int(b)
    res = math.log(x, b)
    print(f"Log {x} with a base {b} is about {round(res, 5)}")

def NF():
    yn = input("Thanks for using ths calculator. Would you like to do another calculation(y/n): ")
    if 'y' in yn.lower():
        Main()
    else:
        SystemExit

def CTC():
    mmmr = input("Would you like to calculate mean, median, mode, or range: ")
    if mmmr.lower() == 'mean':
        Mean()
    elif mmmr.lower() == 'median':
        Med()
    elif mmmr.lower() == 'mode':
        Mode()
    elif mmmr.lower() == 'range':
        Range()
    else:
        print(f"I'm sorry, but '{mmmr}' is an invalid input. Please try again.")
        CTC()
def Trig(func, arc):
    if arc:
        def Main(nu, de):
            print("Okay, we will continue with the sine.")
            num = int(input("Enter the numerator of the fraction of your sine: "))
            den = int(input("Enter the denominator of the fraction of your sine: "))
            if nu and not de:
                num = math.sqrt(num)
            elif de and not nu:
                den = math.sqrt(den)
            elif nu and de:
                num = math.sqrt(num)
                den = math.sqrt(den)
            if den == 0:
                print("Error: Denominator cannot be zero.")
                return
            x = num / den
            if not -1 <= x <= 1:
                print(f"The fraction {num}/{den} or {x} is out of range for arcsine calculation. It must be between -1 and 1.")
                return
            mf = getattr(math, func)
            rx = mf(x)
            print(f"The arcsine in radians is about {round(rx, 10)} radians.")
            dx = (rx * 180) / math.pi
            print(f"The arcsine in degrees is about {round(dx, 5)}°.")
        ndbo = input("Before we begin, is there square root in the sine? If so, in which of the following? (n for numerator/d for denominator/b for both/o for none): ")
        if ndbo == 'n':
            Main(True, False)
        elif ndbo == 'd':
            Main(False, True)
        elif ndbo == 'b':
            Main(True, True)
        elif ndbo == 'o':
            Main(False, False)
        else:
            print(f"Invalid input for square root choice.")


def Main():
    print("\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n5: Exponents\n6: Factorial\n7: Roots\n8: Central Tendency\n9: Logarithms\n10: Trigonometry\n11: End")
    s = input("Enter your selection: ")
    if s == '1':
        Add()
        NF()
    elif s == '2':
        Sub()
        NF()
    elif s == '3':
        Mult()
        NF()
    elif s == '4':
        Div()
        NF()
    elif s == '5':
        Exp()
        NF()
    elif s == '6':
        Fact()
        NF()
    elif s == '7':
        Root()
        NF()
    elif s == '8':
        CTC()
        NF()
    elif s == '9':
        Log()
        NF()
    elif s == '10':
        ts = input("Which trigonometric function would you like to do: ")
    elif s == '11':
        SystemExit
    else:
        print(f"I'm sorry, but '{s}' is an invalid input. Please try again.")
        Main()

print("Hello, and welcome to this calculator! To use it, select any of the following functions below and enter the number corresponding to it. Have fun!")
Main()