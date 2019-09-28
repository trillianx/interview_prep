# Data Structures Notes

In python a list is an ordered sequence of heterogeneous elements. In other words, a list can contain different data types. 

## In-built Functions

Let’s have a look at some useful built-in python list functions. The time complexity of each of these are the average case taken from the [Python Wiki](https://wiki.python.org/moin/TimeComplexity) page. 

| Function    | Description                                | Time Complexity | Example                     |
| ----------- | ------------------------------------------ | --------------- | --------------------------- |
| `append()`  | Adds a single element to the end of a list | O(1)            | `list.append(2)`            |
| `insert()`  | Inserts element to the list                | O(n)            | `list.insert(index, value)` |
| `remove()`  | Removes the given element from the list    | O(n)            | `list.remove(element)`      |
| `pop()`     | Removes the element at given index         | O(1)            | `list.pop(index)`           |
| `reverse()` | Reverses the list                          | O(n)            | `list.reverse()`            |

## Slicing 

Slicing in python is done in the following way: 

```python
# list[start:end]

List = list(range(10))
print(List[3:]) # 3, 4, 5, 6, 7, 8, 9
print(List[:3]) # 0 1 2
print(List[:]) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

### Step Slicing 

You can step through the list at arbitrary intervals as follows: 

```python
# list[start:stop:step]

List = list(range(10))
print(List[0:9:2]) # 0, 2, 4, 6, 8
print(List[9:0:-2]) # 9, 7, 5, 3, 1
```

We can also use slicing techniques on strings since strings *are* lists of characters! (well, technically, they’re *arrays* of characters, but we’ll get to that in a bit!) For example, the string “somehow” can be broken down into two strings like:

```python
my_string = "somehow"
string1 = my_string[:4]
string2 = my_string[4:]
print(string1, string2)

some how
```

To begin indexing from the end of the list use negative numbers. For example, to access the fifth-last element of a list,

```python
List = list(range(10))
print(List[4:-1]) # 4, 5, 6, 7, 8

[4, 5, 6, 7, 8]
```

