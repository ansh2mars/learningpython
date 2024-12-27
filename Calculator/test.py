'''import math
def M(nu, de):
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
    rx = math.asin(x)
    print(f"The arcsine in radians is about {round(rx, 10)} radians.")
    dx = (rx * 180) / math.pi
    print(f"The arcsine in degrees is about {round(dx, 5)}°.")
ndbo = input("Before we begin, is there square root in the sine? If so, in which of the following? (n for numerator/d for denominator/b for both/o for none): ")
if ndbo == 'n':
    M(True, False)
elif ndbo == 'd':
    M(False, True)
elif ndbo == 'b':
    M(True, True)
elif ndbo == 'o':
    M(False, False)
else:
    print(f"Invalid input for square root choice.")'''
