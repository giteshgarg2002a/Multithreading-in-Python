# Multithreading-in-Python
Problem : Tansforming a large database file to format needed.
Data.py : python file created to get input files for all the three cases.
Case1.py : In this case data is transformed by transforming a complete column in a single command.
Case2.py : In this case each cell is transformed individually.
Case3.py : it is the optimised solution for the problem. In this case multithreading is used for a large database file.
It breaks down the file into subfiles and perform three functions (load, transform, ) simultaneously.
