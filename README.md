# Record Management Software (Python):

A simple command-line based record management system that allows users to create, update, and retrieve personal records stored in text files with date and time tracking.

## Description:

The Record Management Software is a Python-based application designed to help users maintain a personal progress log or record file. Each user can create a uniquely named .txt file where they can continuously add records. Every entry is automatically saved along with the current date and time using the datetime module.The program also checks for existing files using the os module and allows users to retrieve previously saved records. This project focuses on practicing core Python concepts such as file handling, functions, loops, conditional statements, and standard library usage.

## Dependencies

-Any version after Python 3.10

-Any operating system that supports Python:

  .Windows
  
  .Linux
  
  .macOS
  
-Built-in Python modules only:

   .os
   
   .datetime
   
-No external libraries are required

## Concepts Used

-File Handling

-datetime module

-os module

-Functions & Docstrings

## How the Program Works

-The user enters their name.

-The user specifies the name of the file where records should be stored.

-The program checks whether the file already exists:

-If not, it creates the file and writes a welcome message.

-If yes, it allows the user to:

  ### Add new records

  ### Retrieve and view existing records
 
  ### Each record is saved with a timestamp using the datetime module.

## Installation

-Download or clone the repository:

  ### git clone https://github.com/Immortal-code-creator/record-management-python.git


-Navigate to the project directory.

-Ensure Python is installed and added to PATH.

-No file or folder modifications are required before running.

## Executing Program

-Open a terminal or command prompt.

-Navigate to the project folder.

-Run the program using:

   ### python record_management.py

-Follow the on-screen instructions:

   ### Enter your name

   ### Enter the file name for storing records

   ### Choose to add new records or retrieve existing ones

## Help

-If the program does not run:

-Ensure Python is installed correctly.

-Make sure you are using Python 3.10 or later.

-Check file permissions if records are not being saved.

-To verify Python installation:

  ### python --version

## Authors

Aeshan Chowdhury

 ### GitHub: https://github.com/Immortal-code-creator
