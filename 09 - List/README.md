# Python List

```python
mylist = ["apple", "banana", "cherry"]

```

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store **collections of data**, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using **square brackets[]:**

```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

## List Items

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

### Ordered

When we say that lists are ordered, it means that the items have a defined order, and **that order will not change.**

If you add new items to a list, the new items will be placed at the end of the list.

### Changeable

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

### Allow Duplicates

Since lists are indexed, lists can have items with the same value:

```python
thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)
```

### List Items - Data Types

List items can be of any data type. From string to boolean.

+ in one list can contain multiple type of data

```python
list1 = ["abc", 34, True, 40, "male"]

```

From Python's perspective, lists are defined as objects with the data type 'list':

## Python Collections (Arrays)

There are four collection data types in the Python programming language:

+ `List` is a collection which is ordered and changeable. Allows duplicate members.

+ `Tuple` is a collection which is ordered and unchangeable. Allows duplicate members.

+ `Set` is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

+ `Dictionary` is a collection which is **ordered** and changeable. No duplicate members.

## Access list - Range of Indexes

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
```


## Check if Item Exists

```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

Output :
```
Yes, 'apple' is in the fruits list
```



## Change Item Value

```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```

## Insert Items

The `insert()` method inserts an item at the specified index:

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
```