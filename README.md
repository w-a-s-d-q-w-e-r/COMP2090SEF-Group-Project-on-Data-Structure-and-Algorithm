# COMP2090SEF-Group-Project-on-Data-Structure-and-Algorithm
Task 2 - Self study on a new data structure and a new algorithm
## Part 1 - Data Structure : Matrix
Matrix is a two-dimensional array with rows and columns. Each horizontal line represent a row and the vertical line represent a column.
It is usually used to process mathematical problems, computer graphics or data processing.
## Abstract Data Type in matrix :
* Abstraction : Users can identify how many rows and columns in the matrix, input the values of each element, using variables to store the matrix, and use different modules to execute different functions
* Encapsulation : Users can easily create a matrix, and can only change the values in matrix by modules instead of simple code
* Modularity : Use modules to do mathematical operations of matrix and the modules can be reused
## Examples on solving real life problems :
* Solving algebra or equations
* Editing photos
* Moving an object on a 2d plate

## Part 2 - Algorithm : Tim Sort
Tim sort use 2 algorithms, insertion sort inside a run and merge sort for multiple runs.
### Step 1 : Identify runs
- Check the whole array and combine a sequence in either ascending or descending order, and convert into ascending order if it is descending
- Add how many number in each sequence
- Usually use minimum 32 to 64 numbers as 1 run, and keep repeating to find how many runs in whole array
### Step 2 : Insertion sort inside each run
- After finding how many runs, we also know how many sequences are in 1 run, and use insertion sort to sort the first 2 sequences
- After sorting all sequences in 1 run by insertion sort, keep sorting in other run until all run are sorted
### Step 3 : Merge sort for each run
- 
