import math
roots = input("Before we begin, does your sine have the square root of a base in the numerator or the denominator?(y/n): ")
if roots == "y":
  n_or_d = input("Is the square root in the numerator or denominator?(n for numerator/d for denominator/b for both): ")
  if n_or_d == "n":
    print("Okay, we will continue with the sine.")
    n = int(input("Enter the numerator of the fraction of your sine: "))
    d = int(input("Enter the denominator of the fraction of your sine: "))
    n = math.sqrt(n)
    x=n/d
    rx = math.asin(x)
    print('The arcsine in radians is', rx, "radians.")
    dx = int(rx*180/math.pi)
    print("The arcsine in degrees is about", dx, "˚.")
  if n_or_d == "d":
    print("Okay, we will continue with the sine.")
    n = int(input("Enter the numerator of the fraction of your sine: "))
    d = int(input("Enter the denominator of the fraction of your sine: "))
    d = math.sqrt(d)
    x=n/d
    rx = math.asin(x)
    print('The arcsine in radians is', rx, "radians.")
    dx = int(rx*180/math.pi)
    print("The arcsine in degrees is about", dx, "˚.")
  if n_or_d == "b":
    print("Okay, we will continue with the sine.")
    n = int(input("Enter the numerator of the fraction of your sine: "))
    d = int(input("Enter the denominator of the fraction of your sine: "))
    n = math.sqrt(n)
    d = math.sqrt(d)
    x=n/d
    rx = math.asin(x)
    print('The arcsine in radians is', rx, "radians.")
    dx = int(rx*180/math.pi)
    print("The arcsine in degrees is about", dx, "˚.")
elif roots == "n":
  print("Okay, we will continue with the sine.")
  n = int(input("Enter the numerator of the fraction of your sine: "))
  d = int(input("Enter the denominator of the fraction of your sine: "))
  x=n/d
  rx = math.asin(x)
  print('The arcsine in radians is', rx, "radians.")
  dx = int(rx*180/math.pi)
  print("The arcsine in degrees is about", dx, "˚.")