# TestProblem
This repo is for a test problem to gain experience and test if applicant like TheRealSeat workflow. Problems will be assigned via this readme.

# Big Picture
TheRealSeat will be pulling data continuously and storing the data in S3. The data will be in csv format like example "TestData.csv". TheRealSeat needs to process, clean and store the data in a database. Additionally we will be putting summary statistics into a different table.

# Problem
Attempt to solve the below tasks through a local script.

# Tasks
Write a python script that will read the following csv, clean the data and summarize the data. Questions include
1) What is the total resale value?
2) What is the total resale value by item?

# Recommendations
Write a pure local script
The script should be able to read a file, process all the columns and output (to file) the answers (each a separate file)
The schema of the inputs will be consistent, assume you are writing to ingest many files.

