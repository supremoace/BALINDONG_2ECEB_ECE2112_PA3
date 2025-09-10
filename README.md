# BALINDONG_2ECEB_ECE2112_PA3
## Programming Assignment 3  

This repository contains my solutions for **Experiment 3: Python Data Analysis (Pandas)**.

## Table of Contents  
Problem 1: 
Problem 2: 

## Programming Assignment 3  

### Problem 1  
**Task:**  
In this project, we are tasked to load a .csv file into a Pandas DataFrame and display the first and last five rows.
1. I started by importing pandas and reading the CSV file.
```python
import pandas as pd  

cars = pd.read_csv("cars.csv")  
print("First 5 rows:")  
print(cars.head())  

print("\nLast 5 rows:")  
print(cars.tail())  
```

**Notebook:** [[PA3.1.ipynb](./PA3.1.ipynb) ](https://github.com/supremoace/BALINDONG_2ECEB_ECE2112_PA3/blob/main/PA3.1.ipynb) 

---

### Problem 2  
**Task:** Using the `cars` DataFrame from Problem 1, perform the following operations:  
1. Display the first five rows with **odd-numbered columns** (1, 3, 5, 7, …).  
2. Display the row that contains the `Model` **Mazda RX4**.  
3. Determine how many **cylinders (`cyl`)** the car model **Camaro Z28** has.  
4. Determine how many **cylinders (`cyl`)** and what **gear type (`gear`)** the car models **Mazda RX4 Wag**, **Ford Pantera L**, and **Honda Civic** have.  

**Notebook:** [PA3.2.ipynb](./PA3.2.ipynb)  
