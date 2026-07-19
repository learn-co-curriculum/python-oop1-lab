# Object Oriented Programming Lab - Bookstore 

This scenario should encompass all of the topics provided in the module. Now that you’ve delved into creating a new class in Python it is now time to practice this concept.

## The Scenario

You are tasked with building two different classes to aid with representing and modeling a bookstore. First will be a book object to allow for reading an online book and the second will be a coffee object as another object carried by the store. Both objects will have several attributes and functions to be called. 

## Tools & Resources

* [GitHub Repo](https://github.com/learn-co-curriculum/python-oop1-lab)
* [Python Classes](https://docs.python.org/3/tutorial/classes.html)

## Instructions

### Set Up

Before we begin coding, let's complete the initial setup for this lesson: 

* Part 1: Fork and Clone- For this lesson, you will need the previously linked GitHub Repo:
  * Go to the provided GitHub repository link.
  * Fork the repository to your GitHub account.
  * Clone the forked repository to your local machine.
* Part 2: Open and Run File
  * Open the project in VSCode.
  * Run `pipenv install` to install all necessary dependencies.
  * Run `pipenv shell` to enter the virtual environment.

This lab is test-driven. You will write your code in `lib/book.py` and
`lib/coffee.py`. Run the tests and work your way through the test errors one by
one until you get everything passing.

You're also encouraged to look at the test files to see what the tests are
expecting to be able to do with your classes. These tests won't force you to
use everything that you've learned in this module- feel free to add any
features that might be useful!

Note that there are separate test files for the two classes inside the `testing`
folder. If you'd like to run the tests separately for the two classes, you can
specify which test file to run:

```console
$ pytest -x testing/book_test.py
```

or:

```console
$ pytest -x testing/coffee_test.py
```

Remember that the optional `-x` flag makes your tests stop after the first
failure - this setting is ideal for test-driven development!

### Task 1: Define the Problem

Build a model for a book and a coffee
<br />
As a user, one should be able to:
* Build a book object
* Build a coffee object
* Call to turn a book page
* Call to tip for the coffee

### Task 2: Determine the Design

Book
* Attributes:
  * title
  * page_Count
* Methods:
  * turn_page()
Coffee
* Attributes:
  * size
  * price
* Methods:
  * tip()

### Task 3: Develop, Test, and Refine the Code

#### Step 1: Feature Branch and Book Class

* Create Feature Branch

* Create Book class:
  * __init__:
    * title
      * Require user to input
    * page_count
      * Require user to input
* Properties:
  * page_count:
    * Ensure it is an integer
    * if not print “page_count must be an integer”
* Methods:
  * turn_page():
    * Will print “Flipping the page...wow, you read fast!”

#### Step 2: Create Coffee Class & Push Feature Branch and Merge

* __init__:
  * size
    * Require user to input
  * price
    * Require user to input
* Properties:
  * Size
    * Ensure size is either Small, Medium, or Large
    * If not print “size must be Small, Medium, or Large”
* Methods:
  * tip():
    * Will print “This coffee is great, here’s a tip!”
    * Will increase price by 1 

#### Step 3: Push Feature Branch and Merge

* Push feature branch and open a PR on GitHub
* Merge to main

### Task 4: Document and Maintain

Best Practice documentation steps:
* Add comments to code to explain purpose and logic. This clarifies intent / functionality of code to other developers
* Add screenshot of completed work included in Markdown in README.
* Update README text to reflect the functionality of the application following https://makeareadme.com.
* Delete any stale branches on GitHub
* Remove unnecessary/commented out code
* If needed, update git ignore to remove sensitive data 

## Save your work and push to GitHub

Before you submit your solution, you need to save your progress with git.
1. Add your changes to the staging area by executing git add .
2. Create a commit by executing git commit -m "Your commit message"
3. Push your commits to GitHub by executing git push origin main or git push origin master , depending on the name of your branch (use git branch to check on which branch you are).

## Submission and Grading Criteria

1. Use the rubric in Canvas as a guide for how this lab is graded.
2. Your submission will be automatically scored in CodeGrade, using the most recent commit. Remember to make sure you have pushed your commit to GitHub before submitting your assignment. 
3. You can review your submission in CodeGrade and see your final score in your Canvas gradebook.
4. When you are ready to submit, click the ***Load Lab: Object Oriented Programming (OOP)- Part 1- Bookstore*** button in Canvas to launch CodeGrade.
  * Click on + Create Submission. Connect your repository for this lab.
  * For additional information on submitting assignments in CodeGrade: [Getting Started in Canvas](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas)

# Python OOP Lab – Setup and Troubleshooting Guide

## Overview

This document records the steps followed to set up the development environment for the Python OOP Lab, along with the errors encountered and the solutions used to resolve them.

---

# Environment

* Operating System: Ubuntu 26.04 LTS (WSL)
* Python: 3.14.4
* Package Manager: Pipenv
* Editor: Visual Studio Code
* Version Control: Git & GitHub

---

# Initial Project Setup

## 1. Fork the Repository

Fork the GitHub repository provided in Canvas to your own GitHub account.

## 2. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

## 3. Open in VS Code

```bash
code .
```

---

# Problem 1: Unable to Install Packages with apt

## Error

```text
Temporary failure resolving 'archive.ubuntu.com'
Temporary failure resolving 'security.ubuntu.com'
```

## Cause

WSL generated an incorrect DNS configuration.

The generated `/etc/resolv.conf` contained:

```text
nameserver 10.255.255.254
```

which prevented Ubuntu from resolving package repositories.

## Solution

### Edit `/etc/wsl.conf`

```ini
[boot]
systemd=true

[user]
default=user

[network]
generateResolvConf = false
```

### Shutdown WSL

Run in Windows PowerShell:

```powershell
wsl --shutdown
```

### Recreate `resolv.conf`

```bash
sudo rm /etc/resolv.conf
sudo nano /etc/resolv.conf
```

Insert:

```text
nameserver 1.1.1.1
nameserver 8.8.8.8
```

### Update Ubuntu

```bash
sudo apt update
```

Successful output:

```text
Fetched 2424 kB
42 packages can be upgraded.
```

---

# Problem 2: Pipenv Not Installed

## Solution

```bash
sudo apt install pipenv
```

Verify installation:

```bash
pipenv --version
```

---

# Problem 3: Python Version Mismatch

## Error

```text
Python 3.8.13 was not found on your system.
```

## Cause

The project's `Pipfile` required:

```toml
[requires]
python_full_version = "3.8.13"
```

while the installed version was:

```text
Python 3.14.4
```

## Solution

Update the `Pipfile` to use the installed version:

```toml
[requires]
python_version = "3.14"
```

Create the environment:

```bash
pipenv --python $(which python3)
```

Install dependencies:

```bash
pipenv install
```

Activate the environment:

```bash
pipenv shell
```

---

# Problem 4: Pipenv Lock Timeout

## Error

```text
HTTPSConnectionPool(host='pypi.org'): Read timed out.
```

## Cause

Temporary network timeout while downloading packages from PyPI.

## Solution

Retry the installation.

The second attempt completed successfully and regenerated the lock file.

---

# Problem 5: No Tests Found

## Error

```text
collected 0 items
ERROR: file or directory not found: testing/book_test.py
```

## Cause

The repository did not contain any test files.

The directory:

```text
lib/testing
```

was empty.

## Resolution

Implemented and tested the classes manually using the Python interpreter instead of automated tests.

---

# Problem 6: Invalid Non-Printable Character

## Error

```text
SyntaxError: invalid non-printable character U+0016
```

## Cause

An invisible control character was inserted while pasting into the Python interpreter.

## Solution

Exit Python and restart it.

Use **Shift + Ctrl + V** or right-click to paste instead of **Ctrl + V**.

---

# Problem 7: ModuleNotFoundError

## Error

```text
ModuleNotFoundError: No module named 'lib'
```

## Cause

Python was started from inside the `lib` directory.

Current directory:

```text
.../python-oop1-lab/lib
```

Python therefore searched for another `lib` directory inside it.

## Solution

Return to the project root:

```bash
cd ..
```

Start Python again:

```bash
python
```

Import the module:

```python
from lib.book import Book
```

---

# Manual Testing

## Book Class

```python
from lib.book import Book

book = Book("Python Basics", 45)

print(book.title)
print(book.page_count)

book.turn_page()
```

Expected output:

```text
Python Basics
45
Flipping the page...wow, you read fast!
```

---

## Coffee Class

```python
from lib.coffee import Coffee

coffee = Coffee("Large", 5)

print(coffee.size)
print(coffee.price)

coffee.tip()

print(coffee.price)
```

Expected output:

```text
Large
5
This coffee is great, here's a tip!
6
```

---

# Git Workflow

Create a feature branch:

```bash
git checkout -b feature/book-class
```

Commit changes:

```bash
git add .
git commit -m "Create Book class"
```

Push to GitHub:

```bash
git push origin feature/book-class
```

Create a Pull Request and merge into `main`.

Repeat the same process for the `Coffee` class.

---

# Final Outcome

* WSL networking fixed.
* Ubuntu package manager functioning correctly.
* Pipenv installed successfully.
* Virtual environment created.
* Dependencies installed.
* `Book` class implemented and manually tested.
* `Coffee` class implemented and manually tested.
* Project ready for GitHub submission.
