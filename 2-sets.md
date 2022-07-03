# Sets

Sets are an interesting type of data structure in python. The order of items doesn't matter and you can't use indexing with a set. Sets only allow unique items, no duplicates. You define a set by using curly braces like this:

```python
first_set = {5, 1, 3, 2, 7}

```
Or, you can call the set function like this:

```python
second_set = set(7, 9, 1, 0)

```

## Why Sets are Useful

Sets are most useful because of the fact that they can not contain any duplicates. You can also use Hashing with a set which allows you to perform insertion, deletion and test for membership in O(1) time. We can also use math operations to find the interestcion or union of sets. 

To find the union of 2 sets you use the bar symbol, like this:

```python
set_1 = {5, 1, 3, 2, 7}
set_2 = {2, 3, 4, 5, 6, 7, 8}

print(set_1 | set_2)
```
You get {1, 2, 3, 4, 5, 6, 7, 8}. Notice this set has no duplicates and contains the numbers found in both sets. Unions with sets are very useful in python.

To find the intersection of 2 sets you use the ampersand symbol, like this:

```python
set_1 = {5, 1, 3, 2, 7}
set_2 = {4, 5, 6, 7, 8}

print(set_1 & set_2)
```
You get {5, 7}. Notice this set contains only the numbers found in both sets and no duplicates.


## Common Errors

A commor error with sets is when you try to create a new empty set using curly braces, like this:

```python
new_set = {}

```

This is wrong because this will create a dictionary, not a set. You must use the set function, like this:

```python
new_set = set()

```



## Example: Random Number Guessing Game

Here is a program that will take a given set of numbers or letters and remove all duplicates using a set.

```python
def using_sets(text):
    set_one = set(text)
    
    return set_one


print()
text = input("Type several numbers and letters and include several duplicates:")
print()
print(using_sets(text))
print()
```
You can see that the set returned is enclosed in curly braces and that all duplicates are gone.


## Problem to Solve : Find The Intersection

Write a program that will find the intersection of 2 sets without using the built-in python function bar symbol.

- Test 1: set_one = {3, 4, 5} set_two = {1, 2, 3}                               -You should get {3} back.
- Test 2: set_one = {'n', 'o', 'p'} set_two = {'l', 'm', 'n', 'o'}              -You should get {'n', 'o'} back.
- Test 3: set_one = {'cat', 'bird', 'lizard'} set_two = {'dog', 'fish', 'cat'}  -You should get {'cat'} back.
- Test 4: set_one = {1, 'k', 4, 'goose', 9} set_two = {0, 'john', 3, 'd', 'a'}  -You should get an empty set (set()) back.




You can check your code with the solution here: [Solution](find_the_intersection.py)



[Back to Welcome Page](0-welcome.md)