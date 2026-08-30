# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
While completing this assignment, I learned how Python lists handle insertion, deletion, and searching. I gained 
better understanding of how elements shift when values get inserted or removed in different parts of the list. I
also learned how to perform a linear search and use exception handling to safely manage invalid indexes.

2. What challenges did you encounter, and how did you overcome them?
One challenge I ran into was handling an invalid deletion. Originally I was going to return "None", but didn't
since it can be a valid value. Due to this I decided to go with an "IndexError" with a message and handling the
error with a try/except block in the main() function. This allows the program to handle errors without terminating.

3. How do list operations impact performance in real-world applications?
List operations can have a major impact. Inserting or deleting elements near the beginning or middle of the list
can require other elements to shift. This would result in O(n) time complexity. A good real-world example would 
be when someone cuts in front of people in a line. This changes the order and makes people that get bumped backwards
wait longer.