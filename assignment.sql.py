# Databricks notebook source
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS Customers1;
# MAGIC CREATE TABLE Customers1 (
# MAGIC     CustomerID INT,
# MAGIC     CustomerName STRING,
# MAGIC     City STRING,
# MAGIC     AccountType STRING,
# MAGIC     Balance INT,
# MAGIC     LoanAmount INT
# MAGIC );
# MAGIC INSERT INTO Customers1 VALUES
# MAGIC (101,'John','Dallas','Savings',5000,10000),
# MAGIC (102,'Mary','Austin','Current',2500,5000),
# MAGIC (103,'David','Dallas','Savings',8000,0),
# MAGIC (104,'Emma','Houston','Savings',1500,3000),
# MAGIC (105,'Alex','Austin','Current',7000,12000),
# MAGIC (106,'Sophia','Dallas','Savings',5000,8000);
# MAGIC SELECT CustomerName, City, Balance, LoanAmount
# MAGIC FROM Customers1;
# MAGIC SELECT DISTINCT City
# MAGIC FROM Customers1;
# MAGIC SELECT *
# MAGIC FROM Customers1
# MAGIC ORDER BY LoanAmount DESC;
# MAGIC SELECT *
# MAGIC FROM Customers1
# MAGIC ORDER BY LoanAmount DESC
# MAGIC LIMIT 5;
# MAGIC SELECT COUNT(*) AS TotalCustomers
# MAGIC FROM Customers1;
# MAGIC SELECT MIN(Balance) AS MinimumBalance
# MAGIC FROM Customers1;
# MAGIC SELECT MAX(Balance) AS MaximumBalance
# MAGIC FROM Customers1;
# MAGIC SELECT AVG(Balance) AS AverageBalance
# MAGIC FROM Customers1;