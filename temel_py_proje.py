# Patika, temel python sonu projesi;

# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) 
# oluşabileceği gibi, non-scalar verilerden de oluşabilir. 
# Örnek olarak:
input =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output = [1,'a','cat',2,3,'dog',4,5]

def flatten_list(L):
    """
    Flattens lists into to a 1D shape list. 
    Arg:
        L (list): List to flatten.
    """
    flat_list = []

    def flatten(L): # Return the item when it's type is not a list 
        for item in L:
            if type(item) is list:
                flatten(item)
            else:
                flat_list.append(item)
        return flat_list

    return flatten(L)

print(f'Input: {input}')
print(f'Flatten output: {flatten_list(input)}')


# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
# Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
# Örnek olarak:

input_2 = [[1, 2], [3, 4], [5, 6, 7]]
input_3 = [[1, 2], [3, 4], [5, 6, 7],1,2,3] # Does not work for some cases!!
output_2 = [[7, 6, 5], [4, 3], [2, 1]]


def reverse_list(L):
    """
    Reverse the items in a given list.
    Arg:
        L (list): List to reverse
    """
    rev_list = [] 
    def reverse(L):
        for item in L:
            if type(item) is list: # For every item(which type is list) in the list; reverse the item (list) and call function again 
                rev_list.append(item[::-1])
                reverse(item)
        return rev_list[::-1]
    return reverse(L)
    
print(f'Input: {input_2}')
print(f'Reversed Output: {reverse_list(input_2)}')




