# SearchSpeedAnalyzer
Interactive Streamlit app to compare and visualize search algorithm performance in real-time

# Runtime Comparison of Search Algorithms

Used Streamlit to compare the runtimes of different search algorithms

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

![alt text](1-1.png)

![alt text](2-1.png)

# Array used for Comparison

- Size of the array is taken as input from the user. Then, a random array of the given size is generated using random module. The array is generated using the randint() function of the random module. The array is generated with random integers ranging from `1 to size * 2`, the search element is also generated using randint() function of the random module.

![alt text](4-1.png)

# Calculation of RunTime

- Using the time module's perf_counter() function, the runtime of each algorithm is calculated. Time is taken before and after the algorithm is executed and the difference is calculated to get the runtime. In this way, the runtime of each algorithm is calculated and displayed as bar graph.

![alt text](3-1.png)

