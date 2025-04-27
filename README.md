# SearchSpeedAnalyzer
Interactive Streamlit app to compare and visualize search algorithm performance in real-time

# Prerequisities

- Python

# Installing dependencies
```bash
pip install streamlit
```

# Usage
```bash
python -m streamlit run search_algo.py
```
After running the above command, a browser window will open with the user interface. The user can enter the size of the array and select the algorithms to compare. The runtimes of the selected algorithms are displayed as a bar graph.

If browser window does not open automatically, you can open the browser and enter the URL displayed in the terminal.

# Details of Implementation

Used streamlit to create a user interface for the user to enter the size of array and select the algorithms you would like to compare. The user can select the algorithms from the dropdown list and click on the "Compare" button to compare the runtimes of the selected algorithms. The runtimes of the selected algorithms are displayed as a bar graph.

![alt text](https://github.com/user-attachments/assets/1afca24b-3939-4653-ae17-d3921f49b0b1)

![alt text](https://github.com/user-attachments/assets/a6bb06d9-67dc-4d3b-8f63-f3f8ecef6718)


# Array used for Comparison

- Size of the array is taken as input from the user. Then, a random array of the given size is generated using random module. The array is generated using the randint() function of the random module. The array is generated with random integers ranging from `1 to size * 2`, the search element is also generated using randint() function of the random module.

![alt text](https://github.com/user-attachments/assets/95624509-7f68-4b7a-82b8-0f5b1f7d1c21)


# Calculation of RunTime

- Using the time module's perf_counter() function, the runtime of each algorithm is calculated. Time is taken before and after the algorithm is executed and the difference is calculated to get the runtime. In this way, the runtime of each algorithm is calculated and displayed as bar graph.

![alt text](https://github.com/user-attachments/assets/9fbfafd4-8af1-49ef-b7d7-fcce95b44d2e)


