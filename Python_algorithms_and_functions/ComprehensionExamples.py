

def main():
    #List comprehensions
    num_list = [1, 3, 5,5, 5, 7, 9, 11, 2, 4, 6, 8, 10, 12, 16, 17, 18, 256, 256]
    str_list = ["a", "b", "b","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r"]

    #Take each element and check if it is even or odd
    is_even = [num for num in num_list if num % 2 == 0]
    print("Even numbers:", is_even)

    #generate even numbers list
    generate_even = [num for num in range(1, 10) if num % 2 == 0]
    print("Even numbers generated :", generate_even)

    #Using filter + lambda
    is_odd_filter = list(filter(lambda odd: odd % 2 !=0, num_list))
    print("Filter odd numbers:", is_odd_filter)

    #Using map + lambda
    #NOTE! map does not modify the length of the input list like filter does
    is_even_map = list(map (lambda even: even if even % 2 == 0 else None, num_list))
    print("Map even numbers:", is_even_map)

    #Nested for loop
    str_int_list = [(num, letter) for num in num_list for letter in str_list]
    print("Nested for loop as a tuple:", str_int_list)

    #Dictionary comprehension
    str_int_list_of_dict = {num:letter for num, letter in zip(num_list,str_list)}
    print("Two lists into a dictionary:", str_int_list_of_dict)

    #Set comprehension
    str_int_set = {num for num in num_list}
    print("Resulted set:", str_int_set)

    #Tuple comprehension
    is_even_tuple = tuple(num for num in num_list if num % 2 == 0)
    print("Even numbers tuple:", is_even_tuple)


if __name__ == "__main__":
    main()
