def func(lst):
    lst.sort(key= len)
    
    return lst[-1]

st = input().split()
print(f'The longest word in given string is {func(st)} and its length is {len(st)}')
