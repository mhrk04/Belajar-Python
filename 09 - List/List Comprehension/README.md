# List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a `for` statement with a conditional test inside:

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```

Output :
```python
['apple', 'banana', 'mango']
```

With **list comprehension** you can do all that with only one line of code:

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
```

> Output will be same as basic `for` loop with `if` conditional

## The Syntax

```python
newlist = [expression for item in iterable if condition == True]
```

The return value is a `newlist`, leaving the old list unchanged.

### Condition

The condition is like a filter that only accepts the items that valuate to `True`.

example:

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
```

>output
>['banana', 'cherry', 'kiwi', 'mango']