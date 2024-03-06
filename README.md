# Programming Assignment #2: Lottery Scheduling 

## Overview
This program simulates a basic lottery scheduling algorithm. Processes are represented by instances of the `Process` class, each having a unique identifier and a certain number of lottery tickets. The `Scheduler` class manages the scheduling algorithm, allowing processes to be added, lottery tickets allocated, and winners selected randomly based on the allocated tickets.

## How it Works
- The program defines two classes: `Process` and `Scheduler`.
- The `Process` class represents a process with a unique identifier (`pid`) and a certain number of lottery tickets (`num_tickets`).
- The `Scheduler` class manages the scheduling algorithm. It allows adding processes, allocating lottery tickets, and selecting winners randomly based on the allocated tickets.
- The main script demonstrates how to use the `Scheduler` class by creating processes, adding them to the scheduler, and running the lottery to select a winner.

## Instructions for Execution
1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone or download this repository to your local machine.
3. Navigate to the directory containing the files using the command line or terminal.
4. Run the program by executing the `OS HW 2.py` script
5. The program will display the winner of the lottery.


## Customization
- You can customize the number of processes and the number of lottery tickets each process has by modifying the example usage section in the `OS HW 2` script.
- Feel free to extend or modify the functionality of the `Scheduler` class to suit your needs.
