"""
ID:M22W0064
Assignment 1
Name: VALERIJS KANEVS
Written on:23/4/25
"""
import math

"""
We know a,b,c and height(H).
Formula for Surface of a Scalene triangular base pyramid is... 
What we need to find for the Surface area?
Area of a base triangle - to find out the surface of a base.
height of a base - Heron formula
s-semi-perimeter
Slant height(https://sciencing.com/properties-triangular-pyramid-8215309.html)
To determine the slant height of a triangular pyramid, square the length of one of the base triangle sides,
then multiply this value by 1/12. The square root of this value plus the pyramid height squared is the slant
height.
Total surface area.
https://www.geeksforgeeks.org/surface-area-of-a-triangular-pyramid-formula/
A = 1/2 (b × h) + 3/2 (b × l)
Where,
b is the side of triangular base,
h is the height of triangular base,
l is the slant height of pyramid.
"""
def triangle_base_high(a,b,c): #returns height of a surface triangle
    s = (a + b + c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def vtp(triangle_base_high,a,b,c,H): #volume of triangular pyramid
    volume = (triangle_base_high(a, b, c)*H)/3
    return volume

def sh(a,H):#slant height
    slant = math.sqrt(math.pow(a,2)*1/12)+math.pow(H,2)
    return slant

def tsa(a,b,c,sh,H): #total surface area of triangular pyramid
    total_surface_area = 1/2*a*triangle_base_high(a,b,c)+3/2*a*sh(a,H)
    return total_surface_area

def main():
    a = int(input("Please input the a:\n"))
    b = int(input("Please input the b:\n"))
    c = int(input("Please input the c\n"))
    H = int(input("Please input the H\n"))
    print(f"The Base area of a triangle is: {triangle_base_high(a,b,c)}")
    print(f"The volume of the triangular pyramid is: {vtp(triangle_base_high,a,b,c,H)}")
    print(f"The slant height of the triangular pyramid is: {sh(a,H)}")
    print(f"The total surface area of a pyramid is: {tsa(a,b,c,sh,H)}")
if __name__ == "__main__": main()