#Using map()
#Use map() method for mapping str (for converting elements in list to string) with given iterator, the list.


# Python program to convert a list
# to string using list comprehension
   
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
  
# using list comprehension
listToStr = ' '.join(map(str, s))
  
print(listToStr) 
