# COP6526_Homework3

Please parallelize the following simple nonlinear regression program using multiprocessing and MPI in python on your single computer. According to the number of CPU cores in your computer, you may use the same number of processes. Please compare the entire runtime of the three different implementations (sequential, multiprocessing, MPI) in a report.

### Question 1.1 Multiprocessing
In the file COP6526_Homework3.ipynb

### Question 1.2 MPI

<img width="681" alt="image" src="https://user-images.githubusercontent.com/58046234/202930406-762fa937-e28e-46e3-bf4a-bf338dd6bc5f.png">
Command: mpiexec -n 4 python "NonlinearRegression.py"

Output:

<img width="485" alt="image" src="https://user-images.githubusercontent.com/58046234/202930420-87d670ca-e0c6-4e73-8306-f823e9b262c0.png">
<img width="485" alt="image" src="https://user-images.githubusercontent.com/58046234/202930426-e083c7fe-a9cc-40ae-a695-476b372e1497.png">
<img width="485" alt="image" src="https://user-images.githubusercontent.com/58046234/202930437-630cbcec-1a98-4a0b-9fdd-aac0cf544633.png">
<img width="485" alt="image" src="https://user-images.githubusercontent.com/58046234/202930457-00ba3947-815f-4861-98c7-af26c5bda93f.png">
