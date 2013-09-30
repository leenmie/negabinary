'''
Created on Sep 30, 2013

@author: leen
'''
"""Reference: http://en.wikipedia.org/wiki/Negative_base
A is an array represent for a negabinary of a decimal X if X = sum{A[i]*(-2)**i}, 0<=i<len(A)
"""

def negaternary(d, base):
    """Return negative base number of a decimal"""
    result = []
    if not d:
        result = [0,]
    else:
        while d != 0:
            d, remainder = divmod(d, base)
            if remainder < 0:
                d, remainder = d + 1, remainder - base
            result.append(remainder)
    """d = sum{result[k]*(-base)**k}
    when print out, the result is backward of written number"""
    return result
    
def get_decimal_from_negabinary(A):
    """Convert a negabinary to a decimal"""
    result = 0
    for i in xrange(len(A)):
        result = result + A[i]*((-2)**i)
    return result

def get_negabinary_from_decimal(d):
    """Convert a negabinary to decimal"""
    return negaternary(d, -2)

def add_two_negabinary(A, B):
    """Add two negabinary"""
    lookup_table = {
                    -2:(0,1),
                    -1:(1,1),
                    0:(0,0),
                    1:(1,0),
                    2:(0,-1),
                    3:(1,-1),
                    }
    carry = 0
    i = 0
    result = []
    if len(A) < len(B):
        A, B = B, A
    for i in xrange(len(A) - len(B)):
        B.append(0)    
    for i in xrange(len(A)):
        _sum = A[i] + B[i] + carry
        _res, carry = lookup_table[_sum]
        result.append(_res)
    while carry!=0:        
        _res, carry = lookup_table[carry]
        result.append(_res)        
    """remove most significant 0 bits"""
    for k in xrange(len(result)-1,-1,-1):
        if result[k]!=0:
            break
    return result[:k+1]
