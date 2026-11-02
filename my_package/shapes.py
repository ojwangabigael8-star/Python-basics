def triangle_area(a:int,b:int,c:int):
    s = (a + b + c)/2
    area = s* (s-a)*(s-b)*(s-c)
    return area**0.5
