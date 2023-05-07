"""
ID:M22W0064
Name: VALERIJS KANEVS
Written on:23/4/25
"""
import math
def volume_cuboid():
    w = int(input("Please input the width:\n"))
    l = int(input("Please input the lenght:\n"))
    h = int(input("Please input the height\n"))
    volume = (w * l *h)/2
    print(f"The volume of the figure is:\n {volume} sqcm")

def surface_rectangle(a,b):
    return a * b

def surface_squere(a):
    return a * a

def surface_triangle(a,b):
    return surface_rectangle(a,b)/2

def surface_piramid(w,l,h):
    m = math.sqrt(h*h+(l/2)*(l/2))
    surface_base = surface_rectangle(w,l)
    surface_side = 2*(surface_triangle(w,m)+surface_triangle(l,m))
    surface_total = surface_base + surface_side
    return surface_total
def main():
    print(surface_rectangle(5,7))
    print(surface_triangle(5,7))
    print(surface_piramid(5,7,9))
if __name__ == "__main__": main()