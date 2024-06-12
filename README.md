# seat-reservations

This program is designed to manage seating arrangements, reading an initial seating layout from a text file and updating it based on a predefined set of rules.

## Files

- `EmptySeating.txt`: Contains the initial seating layout.
- `FillSeating.py`: Contains the Python script to update the seating layout.

## EmptySeating.txt

This file contains the initial seating layout as a grid of characters. Each character represents the state of a seat:

- `L`: An empty seat.
- `.`: A floor space (not a seat).

Here is a sample from the file:

```
LLLLL.LLLLLLLLL.LLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLL.LL.L.LLLL.LLL..LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLL
...
LLLLL.LLLLLLLLL.LLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL
```

## FillSeating.py

This Python script processes the initial seating layout and updates it according to a set of rules:

1. If a seat is empty (`L`) and there are no occupied seats adjacent to it, the seat becomes occupied.
2. If a seat is occupied (`#`) and four or more seats adjacent to it are also occupied, the seat becomes empty.
3. Floor (`.`) never changes.

### How to Run

1. Ensure that `EmptySeating.txt` and `FillSeating.py` are in the same directory.
2. Run the Python script using the following command:
   ```sh
   python FillSeating.py
   ```
3. The script will output the updated seating layout.

### Example

If the initial layout is:

```
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
```

After running the script, the output might be:

```
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
```

### Requirements

- Python 3.x

### Additional Information

The script includes functions to read the initial seating layout from the file, apply the rules iteratively, and print the final updated layout.

## Author

- Kavia Shirkoohi
