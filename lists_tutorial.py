li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a', True]

#lists
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

#list slicing
print(amazon_cart[0:4])

amazon_cart[0] = 'laptop'

print(amazon_cart)

#List methods
# len() is a function - not a method
basket = [1,2,3,4,5]
print(len(basket))

#methods are added with a . following the object

basket.reverse()
new_basket = basket
basket[::-1]
print(new_basket)

basket.append(100)
next_basket = new_basket
print(new_basket)

letters = ['a','b','c','d','e','f']

#prints true of false and checks if letter is in the list.
print('b' in letters)

print('z' in 'zakia')

print(letters.count('d'))

print(range(1,20))

print(list(range(1,20)))

new_sentence = ' '.join(['my','name','is','zakia'])
print(new_sentence)