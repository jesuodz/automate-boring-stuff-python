# Comma code

def listToStr(array):
    lastItem = str( array.pop() )
    return ', '.join( str(i) for i in array ) + ' and ' + lastItem

print(listToStr(['apples', 'bananas', 'tofu', 'cats']))
print(listToStr([1, 2, 3, 4]))
print(listToStr([1, '2 dogs' , 'three bananas', 4]))