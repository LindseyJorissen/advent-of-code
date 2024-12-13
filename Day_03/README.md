# Day 3: Part 2

For **Day 1**, **Day 2**, and **Day 3: Part 1**, I tried to use basic Python without imports, mainly for practice but also because I'm a noob and didn't want to go and learn a bunch of packages.

I managed to do this until **Day 3: Part 2**, where I got stuck for 2 days...

I finally caved and looked up **regex** since I’d seen many people use it for this puzzle.  
Below is some documentation for myself and other noobs attempting Advent of Code with very basic knowledge.

---

## **Day 3: Part 2 Code**

### Importing `re`
```python
import re
```
- Importing the `re` module to use regular expressions.

---

### Reading Input File
```python
def read_input_file(inputfile):
    with open(inputfile, "r") as inputfile:
        return inputfile.read()
```
- Opens the file in read mode, reads the content, and returns it as a single string.

---

### Finding Valid Patterns
```python
def find_valid_mul(input):
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", input)
```
- Uses `re.findall` to find all instances of:
  - `mul(x,y)`
  - `do()`
  - `don't()`
- **Output Example**:
  ```python
  ["mul(10,20)", "do()", "mul(3,4)", "don't()", "mul(5,6)"]
  ```

---

### Multiplication Function
```python
def find_multiplications(expressions):
    total = 0
    for i in expressions:
        if i.startswith("m"):
            nums = list(map(int, re.findall(r'\d{1,3}', i)))
            total += nums[0] * nums[1]
    return total
```
- **Input**: `expressions` - The list returned by `find_valid_mul()`.
- **Explanation**:
  - Takes numbers from `mul(x,y)` strings using `re.findall` and converts them into integers.
  - Multiplies the numbers found and adds the result to the total.
- **Output Example** (for `mul(123,456)`):  
  ```python
  nums = [123, 456]
  ```

---

### Conditional Multiplications
```python
def multiplications_if_do(expressions):
    total = 0
    do_enabled = True
    for i in expressions:
        if i == "do()":
            do_enabled = True
        elif i == "don't()":
            do_enabled = False
        elif do_enabled and i.startswith("m"):
            nums = list(map(int, re.findall(r'\d{1,3}', i)))
            total += nums[0] * nums[1]
    return total
```
- **Explanation**:
  - Checks whether `do_enabled` is `True` or `False` based on  `do()` or `don't()`.
  - Only calculates `mul(x,y)` when `do_enabled` is `True`.

---

### Main Function
```python
def main():
    inputfile = "input.txt"
    input = read_input_file(inputfile)
    expressions = find_valid_mul(input)

    part1 = find_multiplications(expressions)
    part2 = multiplications_if_do(expressions)

    print(f"Part 1: {part1}\nPart 2: {part2}")
```
- Reads the input file and finds all valid patterns.
- Prints results for:
  - **Part 1**: Multiplying all `mul(x,y)`.
  - **Part 2**: Multiplying only when `do()` is active and skipping when `don't()` is active.

---

