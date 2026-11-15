Python OOP -- Inheritance and Polymorphism

Description

This project introduces inheritance and polymorphism in Python through a guided example using a parent class and child classes.

Learning Objectives

- Understand inheritance.
- Identify parent and child classes.
- Create subclasses.
- Override inherited methods.
- Understand polymorphism.
- Use isinstance() and issubclass().

Requirements

- Ubuntu 20.04
- Python 3.8
- All Python files must be executable.
- All Python files must start with #!/usr/bin/env python3.
- Follow PEP8.
- Include documentation strings.
- End files with a newline.
- Use only the Python standard library unless otherwise stated.
- Do not use the words `import` or `from` inside comments.
- Use `__import__()` to import any base class.


### 1. Base Geometry

**Objective:** create a foundational `BaseGeometry` class.

**Methods:**
- `area()`: Raises an exception indicating that area calculation is not implemented.
- `integer_validator(name, value)`: Validates that a value is an integer greater than zero.


**Learning Objectives:**
- Understand base classes.
- Raise exceptions.
- Validate data types and values.
- Reuse methods through inheritance.


### 2. Rectangle

**Objective:** Create a Rectangle class that inherits from BaseGeometry.

**Requirements:**
- Accept width and height during initialization.
- Store both values as private attributes.
- Validate both values using the inherited integer_validator() method.
- Do not create getters or setters.

**Learning Objectives:**
- Reuse parent class methods.
- Understand private attributes.
- Apply inheritance to validate object data.


### 3. Full Rectangle

**Objective:** Extend the Rectangle class with area calculation and a readable string representation.

**Requirements:**
- Validate width and height using the inherited integer_validator().
- Store width and height as private attributes.
- Implement area() to calculate the rectangle's area.
- Implement __str__() to return the format [Rectangle] <width>/<height>.
- Do not create getters or setters.

**Learning Objectives:**
- Implement inherited methods.
- Calculate an object's area.
- Customize an object's string representation.
- Understand polymorphism through a common interface.


### 4. Square #1

**Objective:** Create a Square class that inherits from Rectangle.

**Requirements:**
- Accept one size parameter.
- Validate size using inherited integer_validator().
- Store size as a private attribute.
- Initialize the parent Rectangle with equal width and height.
- Implement area().