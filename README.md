# Task Scheduler Simulation

This Python script simulates a task scheduler using a round-robin scheduling algorithm.

## Overview

The task scheduler simulates the execution of processes using a time quantum. Each process is represented by a `Process` object, which has an ID, name, and execution time. The `Scheduler` class manages the scheduling of processes using a queue-based approach.

## Usage

1. Define processes: Instantiate `Process` objects with appropriate IDs, names, and execution times. Add them to an array.
2. Configure the scheduler: Instantiate a `Scheduler` object with the array of processes and the time quantum.
3. Run the scheduler: Call the `assignProcessor()` method on the `Scheduler` object to simulate the execution of processes.

```python
# Example usage
arr = [Process(1, "notepad", 65), Process(2, "mp3player", 5), Process(3, "bcc", 30), Process(4, "explorer", 10)]
s = Scheduler(arr, 4, 5)
s.assignProcessor()

This project is licensed under the MIT License. See the LICENSE file for details.
