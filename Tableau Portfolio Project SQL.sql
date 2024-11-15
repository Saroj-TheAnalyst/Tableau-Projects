-- 1. Total Salary Expenditure by Job Title
SELECT JobTitle, SUM(Salary) AS TotalSalaryExpenditure
FROM EmployeeData
GROUP BY JobTitle
ORDER BY TotalSalaryExpenditure DESC;

-- 2. Average Age by Job Title
SELECT JobTitle, AVG(Age) AS AverageAge
FROM EmployeeData
GROUP BY JobTitle
ORDER BY AverageAge;

-- 3. Total Employee Count by Gender
SELECT Gender, COUNT(*) AS TotalEmployees
FROM EmployeeData
GROUP BY Gender
ORDER BY TotalEmployees DESC;

-- 4. Count of Employees by Gender and Job Title
SELECT JobTitle, Gender, COUNT(*) AS EmployeeCount
FROM EmployeeData
GROUP BY JobTitle, Gender
ORDER BY JobTitle, EmployeeCount DESC;

-- 5. List of Employees Who Have Left (End Date is Not Null)
SELECT EmployeeID, FirstName, LastName, JobTitle, EndDate
FROM EmployeeData
WHERE EndDate IS NOT NULL
ORDER BY EndDate;

-- 6. Employees with Highest Salaries
SELECT EmployeeID, FirstName, LastName, JobTitle, Salary
FROM EmployeeData
ORDER BY Salary DESC
LIMIT 5;

-- 7. Average Salary by Gender
SELECT Gender, AVG(Salary) AS AverageSalary
FROM EmployeeData
GROUP BY Gender
ORDER BY AverageSalary DESC;

-- 8. Total Duration of Employment in Years for Each Employee
SELECT EmployeeID, FirstName, LastName, DATEDIFF(YEAR, StartDate, ISNULL(EndDate, GETDATE())) AS YearsEmployed
FROM EmployeeData
ORDER BY YearsEmployed DESC;

-- 9. List of Employees Who Worked More Than 10 Years
SELECT EmployeeID, FirstName, LastName, JobTitle, DATEDIFF(YEAR, StartDate, ISNULL(EndDate, GETDATE())) AS YearsEmployed
FROM EmployeeData
WHERE DATEDIFF(YEAR, StartDate, ISNULL(EndDate, GETDATE())) > 10
ORDER BY YearsEmployed DESC;

-- 10. Total Salary Expenditure by Year
SELECT YEAR(StartDate) AS Year, SUM(Salary) AS TotalSalaryExpenditure
FROM EmployeeData
GROUP BY YEAR(StartDate)
ORDER BY Year;
