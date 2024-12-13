# OrangeHRM_Test_Automation


This repository contains automated test cases for the OrangeHRM system using Selenium and Python.

## Test Scenarios

1. User successfully logs into the OrangeHRM system.
2. Navigates to the Employee List page.
3. Verifies the name and ID of an existing employee.
4. Adds a new employee.
5. Confirms the newly added employee is present in the Employee List.
6. Searches for an employee by ID and checks the results.
7. Deletes an employee and verifies they are removed from the Employee List.

## Test Requirements

- **URL**: [https://opensource-demo.orangehrmlive.com/](https://opensource-demo.orangehrmlive.com/)
- **Username**: `Admin`
- **Password**: `admin123`
- **Browser**: Google Chrome (or any other preferred browser)
- **Testing Tool**: Selenium (Python)

## Expected Results

- After login, the user should be able to access the Employee List page.
- Name and ID in the first row of the Employee List should not be empty.
- Newly added employees should appear in the Employee List.
- Search results should correctly reflect employee details.
- Deleted employees should no longer appear in the Employee List.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
