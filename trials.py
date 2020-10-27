"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    result = []

    for item in range(len(items)):
        if item % 2 != 0:
            result.append(items[item])
    
    return result


def print_as_numbered_list(items):
    counter = 1
    for item in items:
        print (f'{counter}.{item}')
        counter +=1



def get_range(start, stop):
    range_list = []

    for num in range(start, stop):
        range_list.append(num)
    
    return range_list


def censor_vowels(word):
    chars = []
    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    return '' .join(chars)




def snake_to_camel(string):
    camelCase = []

    words = string.split('_')

    for word in words:
        camelCase.append(word.title())

    return ''.join(camelCase)



def longest_word_length(words):
    longest = len(words[0])
    for word in words:
       if longest<len(word):
           longest = len(word)
    return longest


def truncate(string):
    result = []

    for character in string:
        if len(result) == 0 or character != result[(len(result) - 1)]:
            result.append(character)
            

    return ''.join(result) 



def has_balanced_parens(string):

    parens = 0
    for char in string:
        if char == '(':
            parens += 1
        elif char== ')':
            parens -= 1
            
    if parens < 0:
        return False
    else:
        return True
    
    




def compress(string):
    pass  # TODO: replace this line with your code
