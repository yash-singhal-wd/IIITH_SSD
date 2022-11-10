###SSD LAB ACTIVITY - 12

## Common assumoptions
1. The steps taken by the subject fall in front of each other for either leg - right leg falls in front of the next right step.
3. The median timestamp of each map is considered as the timestamp for that mat, which is 42x25 for part1 and 126x75 for part2

## PART 1

- The iput file is a sparse matrix and is stored as list of list of lists.There are overall 20 mats in the input file.
- The input file path is taken as an input from the user and is attached to the solution, named "file1.txt"

## Approach

1. It is assumed that the first few non zero values on the mat are caused by the toe of respective foot (of each new mat).

Subtracting the first and the second step gives the stride length. Measurement units.

Dividing the stride length by the time stamps of the mats gives the stride velocity. Measurement: units/sec.

The cadence is calculated by dividing the number of steps(3 in this case) by the time difference and multiplying the result by 60.

# How to run
```
python3 part1.py 
Filepath (with extension): file1.txt
```


## Question 2

## Approach
- The approach is identical to the part1. The difference is in the median timestamps and the matlength- 126x75 in this case.
- The given inputfile has been slightly modified so as to combine the 3 mats.
- The input file is - file2.txt.

# How to run
```
python3 part2.py
```
