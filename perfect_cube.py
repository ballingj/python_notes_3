# Perfect Cube - demonstrates the Exhaustive-enumeration algorithm
#
# Find the cube root of a perfect cube using
# exhaustive-enumerations:  (means try one number at a time!)
#####################################################################

x = int(input("Enter an integer: "))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(f"{x} is not a perfect cube")
else:
    print(f"Cube root of {x} is {ans}")
