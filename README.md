# Research Repository: "Analysis of Student Trajectories in Early Alert Programs Adapting Process Mining Techniques"

This repository contains the source code related to the research titled "Analysis of student trajectories in Early Alert Programs adapting Process Mining techniques." The content of the repository is organized into five folders:

## 01 Data
The original research data is private and cannot be shared, so fictitious data containing random student information has been created. Sample data has been generated for four Law students and 100 students in Law and Civil Construction. The files and structure enable processing by available code to generate data logs for each model. The information covers courses, academic periods, and general student information for both active and inactive students.

## 02 Code
This folder contains Jupyter Notebook files for the Law and Civil Construction programs. Each program includes the following files, executed in the specified order:

- `alerts.ipynb`: Code containing logic to apply alert criteria to each student. It creates a dictionary that, for each academic period, retrieves alerted students and the type of alert they receive.
- `students_data.ipynb`: Code creating a dictionary storing each student's general information and semester-specific details, including alerts.
- `model_1.ipynb`: Code that, based on the dictionary generated in "students_data," creates event logs according to model 1.
- `model_2.ipynb`: Code that, based on the dictionary generated in "students_data," creates event logs according to model 2.
- `model_3.ipynb`: Code that, based on the dictionary generated in "students_data," creates event logs according to model 3.
- `conformance.ipynb`: Code containing conformance checking analysis.

## 03 Logs
In this folder, CSV files of event logs obtained from `model_1.ipynb`, `model_2.ipynb`, and `model_3.ipynb` are stored for both Law and Civil Construction.

## 04 Model
PNG files corresponding to event logs processed by the Disco tool are stored here.

## 05 Conformance checking
In this folder, a PDF file contains the results of the conformance checking analysis. Different values are explored for alert and stop-out weights to validate that the results are not sensitive to weight values.
