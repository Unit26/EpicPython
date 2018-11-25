from math import sqrt
def geron(a, b, c): 
    ''' Вычисляет площадь треугольника по формуле Герона:
    >>> geron(3, 4, 5)
    6.0
    
    >>> geron(7, 8, 9)
    26.83
    '''
    def geron1(p, a, c, b):
        def p(a, b, c):
            return (a + b + c) / 2
        return p(p-a)(p-b)(p-c)
    return sqrt.geron1(p, a, c, b)
    
  
if __name__ == "__main__":
    import doctest
    doctest.testmod()
