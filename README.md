# ProgrammingTest

## Question_1_1.

The "count_csv_files" Function takes "folder_path" as an input argument. It uses the "os.walk" method to traverse the folder structure starting from the "folder_path".

"for root, _, files in os.walk(folder_path):" generates 3 tuples of iterations.

      > 1. root      - The current directory being visited.
	  > 2. dirs      - This value is not used in the for loop. Therefore, '_' is used to discard it.
	  > 3. files     - The list of files in the current directory.

"if file.endswith('.csv'):"

	Within the for loop, this conditional statement is used to check whether the current file ends with the string '.csv'. 

"if __name__ == "__main__":"

	A common Python construct that allows you to control the execution of code when a Python script is run as the main program.

The output is:
