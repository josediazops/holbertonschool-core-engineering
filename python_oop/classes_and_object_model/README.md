# Python - Classes & Object Model

## Task 1: My First Square


### Learning Objectives


- Understand how to define a Python class.
- Create an instance of a class.
- Inspect an object's type and attrubutes.

## Task 2: Square with Size


### learning Objectives


- Understand instance attributes.
- Learn how to create an object using `--init--`.
- Understandprivate attributes and name mangling.
Introduce the encapsulation principle.


## Task 3: Size Validation

### Learning Objectives

- Understand input validation.
- Learn the difference between TypeError and ValueError.
- Validate an instance attrubute before storing it. 
- Use exceotins to prevent invalid object stage.


## Task 4: Area of a Square

### Learning Objectives


- Understand instance methods.
- Learn how methods interact with instance attrubutes.
- Calculate the area of a square using its side length.
- Understand how to call methods through and object.


### 5. Access and Update Private Attrubute
**Requirements:**
- Add a getter for `size`.
- Add a setter for `size`.
- The setter must validate that the value is an integer.
- the setter must reject negative value.
- Use the required errir messages:
    - `size must be an integer`
    - `size must be >= 0`


### 6. printing a Square

**Objective** Implement a public instance method `my_print()` that printd a square using the `#` character.

**Requierments:**
- Print the square using the object's current size.
- Each row must contain the correct number of `#` characters.
- Print an empty line when size is 0.


### 7. Print Square Instance

**Objective:** Control how Square objects are represented as strings.

**Requirements:**
- Add a private `position` attribute.
- Add a getter and setter for `position`.
- Validate that position is a tuple of two non-negative integers.
- Implement `__str__()` to return the square as a string.
- Update `my_print()` to return the square's position.
- Allow optional `size` and `position` arguments in the constructor.


### 8. Rectangle Class

**Objective:** Reinforce object modeling with a second class.

**Requirements:**
- Define a `Rectangle` class.
- Add private `width` and `height` attributes.
- Implement getters and setters for both attributes.
- Validate that both values are integers.
- Reject negative values.
- Use the required error messages:
    - `width must be an integer`
    - `width must be >= 0`
    - `height must be an integer`
    - `height must be >= 0`
- Implement a constructor with optional width and height, both defaulting to 0.


### 9. Area and Perimeter

**Objective:** Implement behavior for the rectangle class.

**Requirements:**
- Add an `area()` instance method that returns the rectangle's area.
- Add a `perimeter()` instance method that returns the rectangle's perimeter.
- If `width` or `height` is equal to `0`, the perimeter must be `0`.
