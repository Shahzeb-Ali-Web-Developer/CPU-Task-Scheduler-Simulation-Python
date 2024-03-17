class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty.")
            return None

    def is_empty(self):
        return len(self.items) == 0


class Process:
    def __init__(self, processId, processName, processExecTime):
        self.processId = processId
        self.processName = processName
        self.processExecTime = processExecTime

    def display(self):
        print(f"Process ID: {self.processId}, Process Name: {self.processName}, Execution Time: {self.processExecTime}")

class Scheduler:
    def __init__(self, processArray, processArrayLength, timeQuantum):
        self.processArray = processArray
        self.processArrayLength = processArrayLength
        self.timeQuantum = timeQuantum

    def assignProcessor(self):
        time = 0
        queue = Queue()
        for process in self.processArray:
            queue.enqueue(process)

        while not queue.is_empty():
            current_process = queue.dequeue()
            current_process.display()

            if time > 0 and time % 10 == 0:
                print(f"{current_process.processName} pausing execution")
                queue.dequeue()

            if current_process.processExecTime > self.timeQuantum:
                current_process.processExecTime -= self.timeQuantum
                time += self.timeQuantum
                print(f"Time passed: {time}")

                # Move the current process to the end of the queue
                queue.enqueue(current_process)

            else:
                time += current_process.processExecTime
                print(f"Time passed: {time}")
                print(f"{current_process.processName} completed execution")




arr = [Process(1, "notepad", 65), Process(2, "mp3player", 5), Process(3, "bcc", 30), Process(4, "explorer", 10)]
s = Scheduler(arr, 4, 5)
s.assignProcessor()



