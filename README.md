# Homework_01 UTUS school. 
### Includes functions which do operation with integer numbers and lists with  integer numbers
#### Funcions

    1) def power_numbers(*args):

- `power_numbers` get integer number as `*args`  and return list of squares numbers
  In this function uses `map(function, iterable, *iterables)` and lambda function



    2) def filter_numbers(numbers_list: list, filter_type: str):
- `filter_numer` get input list with integer numbers and one of types filter: ODD, EVEN, PRIME
- In `filter_numer` function uses three functions
    - `def filter_odd(number)` checks if a number is odd and return True or False
    - `def filter_even(number)` checks if a number is even and return True or False
    - `def filter_prime(number)` checks if a number is prime and return True or False
    - `filter(function, iterable)` which filters by `filter_type`

  
### Ivan Lebedev