#operator bitwise ( operasi biner / binary )
#bitwise adalah operai masing masing bit
#terdiri dari OR (|), AND (&), XOR (^), NOT ( )
a = 9
b = 5

# example operator bitwise OR (|)
c = a | b
print('======OR======')
print('nilai',a,'binary = ',format(a,'08b'))
print('nilai',b,'binary = ',format(b,'08b'))
print('====OR(|)====')
print('nilai',c,'binary = ',format(c,'08b'))

# example operator bitwise AND (&)
c = a & b
print('======AND======')
print('nilai',a,'binary = ',format(a,'08b'))
print('nilai',b,'binary = ',format(b,'08b'))
print('====AND(&)====')
print('nilai',c,'binary = ',format(c,'08b'))

# example operator bitwise XOR (^)
c = a ^ b
print('======XOR======')
print('nilai',a,'binary = ',format(a,'08b'))
print('nilai',b,'binary = ',format(b,'08b'))
print('====XOR(^)====')
print('nilai',c,'binary = ',format(c,'08b'))

#example operator bitwise NOT (~)
c = ~a
print('=====NOT(~)=====')
print('nilai',a,'binary = ',format(a,'08b'))
print('================(~)')
print('nilai',c,'binary = ',format(c,'08b'))
print('================(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai', e^d, 'binary',format(e^d,'08b'))

