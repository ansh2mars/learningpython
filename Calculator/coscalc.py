import math
roots = input("Before we begin, does your cosine have the square root of a base in the numerator or the denominator?(y/n): ")
if roots == "y":
  n_or_d = input("Is the square root in the numerator or denominator?(n/d/b): ")
  if n_or_d == "n":
    print("Okay, we will continue with the cosine.")
    n = int(input("Enter the numerator of the fraction of your cosine: "))
    d = int(input("Enter the denominator of the fraction of your cosine: "))
    n = math.sqrt(n)
    x=n/d
    rx = math.acos(x)
    print('The cosine in radians is', rx, "radians.")
    dx = int(rx*180/math.pi)
    print("The cosine in degrees is about", dx, "˚.")
  if n_or_d == "d":
    print("Okay, we will continue with the cosine.")
    n = int(input("Enter the numerator of the fraction of your cosine: "))
    d = int(input("Enter the denominator of the fraction of your cosine: "))
    d = math.sqrt(d)
    x=n/d
    rx = math.acos(x)
    print('The cosine in radians is', rx, "radians.")
    dx = int(rx*180/math.pi)
    print("The cosine in degrees is about", dx, "˚.")
  if n_or_d == "b":
    print("Okay, we will continue with the cosine.")
    n = int(input("Enter the numerator of the fraction of your cosine: "))
    d = int(input("Enter the denominator of the fraction of your cosine: "))
    n = math.sqrt(n)
    d = math.sqrt(d)
    x=n/d
    rx = math.acos(x)
    print('The cosine in radians is', rx, "radians.")
    dx = int(rx*180/math.pi)
    print("The cosine in degrees is about", dx, "˚.")
elif roots == "n":
  print("Okay, we will continue with the cosine.")
  n = int(input("Enter the numerator of the fraction of your cosine: "))
  d = int(input("Enter the denominator of the fraction of your cosine: "))
  x=n/d
  rx = math.acos(x)
  print('The cosine in radians is', rx, "radians.")
  dx = int(rx*180/math.pi)
  print("The cosine in degrees is about", dx, "˚.")