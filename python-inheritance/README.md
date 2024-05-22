# MyList Class

This project defines a class `MyList` that inherits from the built-in `list` class in Python. The `MyList` class includes a method `print_sorted` which prints the list in ascending order without modifying the original list.

## Files

- `1-my_list.py`: Contains the definition of the `MyList` class.
- `tests/1-my_list.txt`: Contains test cases for the `MyList` class.

## Requirements

- Python 3.8.5
- Pycodestyle 2.7.*
- Ubuntu 20.04 LTS

## Usage

To use the `MyList` class, simply import it and use it like a regular list. You can call the `print_sorted` method to print the list in sorted order.

Example:
```python
my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)         # Output: [1, 4, 2, 3, 5]
my_list.print_sorted() # Output: [1, 2, 3, 4, 5]
print(my_list)         # Output: [1, 4, 2, 3, 5]

# MyList Class

This project defines a class `MyList` that inherits from the built-in `list` class in Python. The `MyList` class includes a method `print_sorted` which prints the list in ascending order without modifying the original list.

## Files

- `1-my_list.py`: Contains the definition of the `MyList` class.
- `tests/1-my_list.txt`: Contains test cases for the `MyList` class.

## Requirements

- Python 3.8.5
- Pycodestyle 2.7.*
- Ubuntu 20.04 LTS

## Usage

To use the `MyList` class, simply import it and use it like a regular list. You can call the `print_sorted` method to print the list in sorted order.

Example:
```python
my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)         # Output: [1, 4, 2, 3, 5]
my_list.print_sorted() # Output: [1, 2, 3, 4, 5]
print(my_list)         # Output: [1, 4, 2, 3, 5]

# BaseGeometry Class

This project defines a class `BaseGeometry` with methods for geometric calculations and integer validation.

## Files

- `7-base_geometry.py`: Contains the definition of the `BaseGeometry` class.
- `tests/7-base_geometry.txt`: Contains test cases for the `BaseGeometry` class.

## Requirements

- Python 3.8.5
- Pycodestyle 2.7.*
- Ubuntu 20.04 LTS

## Usage

To use the `BaseGeometry` class, import it and create an instance. You can call the `integer_validator` method to validate integers. The `area` method is not implemented and will raise an exception if called.

Example:
```python
bg = BaseGeometry()

# Validating an integer
bg.integer_validator("my_int", 12)  # No exception

# This will raise a TypeError
try:
    bg.integer_validator("name", "John")
except Exception as e:
    print(e)  # Output: name must be an integer

# This will raise a ValueError
try:
    bg.integer_validator("age", 0)
except Exception as e:
    print(e)  # Output: age must be greater than 0
