# N-Puzzle Solver
The N-Puzzle Solver is a Python application that provides a graphical interface for solving the N-Puzzle problem using various search algorithms. The N-Puzzle problem, also known as the 15-Puzzle or 8-Puzzle, is a classic problem in artificial intelligence and computer science, where the goal is to rearrange a scrambled puzzle to its goal state by sliding tiles into the empty space.

![puzzle](/uploads/ee66df6b5225575d04d05c4b4ffcb7c2/puzzle.gif)

## Features
- Graphical User Interface (GUI): The GUI allows users to interact with the solver visually, generating random puzzles and solving them using different algorithms.

- Multiple Search Algorithms: The solver supports several search algorithms for finding the solution to the N-Puzzle problem:

Depth-First Search (DFS) with limited depth
Greedy search
A* search
- Solution Path Visualization: Once a puzzle is solved, the solution path is displayed in the GUI, showing the sequence of moves required to reach the goal state.

- Performance Metrics: The solver provides performance metrics such as the number of explored nodes and execution time for each algorithm, giving insights into their efficiency.

## Files
- Gui.py: Contains the implementation of the graphical user interface using the Tkinter library.

- State.py: Defines the State class representing the state of the puzzle and its attributes. It also includes heuristic functions and methods for expanding states and generating children.

- Search_Algorithms.py: Implements the search algorithms (DFS, Greedy, A*) for solving the N-Puzzle problem.

## Usage
- Run the GUI: Execute the Gui.py file to launch the graphical user interface.

- Generate Random Puzzles: Use the "GENERATE RANDOM" buttons in the GUI to generate random 3x3 or 4x4 puzzles.

- Select Algorithm: Click on the algorithm buttons (Greedy, A*, DFS) to solve the generated puzzle using the respective algorithm.

- View Results: Once solved, the solution path, number of explored nodes, and execution time are displayed in the GUI.

## Dependencies
Python 3.x
Tkinter (Python GUI library)

## How to Run
Ensure you have Python installed on your system. Then, execute the Gui.py file using the Python interpreter.


```
python Gui.py
```

## Contributions
Contributions to this project are welcome! Feel free to fork the repository, make changes, and submit pull requests.
