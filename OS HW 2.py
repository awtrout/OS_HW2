import random

class Process:
    """
    Represents a process in the lottery scheduling simulation.

    Attributes:
        pid (int): Unique identifier for the process.
        num_tickets (int): Number of lottery tickets assigned to the process.
    """
    def __init__(self, pid, num_tickets):
        """
        Initializes a process with the given identifier and number of tickets.

        Args:
            pid (int): Unique identifier for the process.
            num_tickets (int): Number of lottery tickets assigned to the process.
        """
        self.pid = pid
        self.num_tickets = num_tickets

class Scheduler:
    """
    Manages the lottery scheduling algorithm simulation.

    Attributes:
        processes (list): List of processes added to the scheduler.
        total_tickets (int): Total number of lottery tickets across all processes.
    """
    def __init__(self):
        """
        Initializes the scheduler with an empty list of processes and total tickets.
        """
        self.processes = []
        self.total_tickets = 0

    def add_process(self, process):
        """
        Adds a process to the scheduler.

        Args:
            process (Process): Process object to be added to the scheduler.
        """
        self.processes.append(process)
        self.total_tickets += process.num_tickets

    def allocate_tickets(self):
        """
        Allocates lottery tickets to processes based on their number of tickets.

        Returns:
            list: List of allocated tickets, each representing a process ID.
        """
        allocated_tickets = []
        for process in self.processes:
            for _ in range(process.num_tickets):
                allocated_tickets.append(process.pid)
        return allocated_tickets

    def select_winner(self, allocated_tickets):
        """
        Selects a winner randomly from the allocated tickets.

        Args:
            allocated_tickets (list): List of allocated tickets.

        Returns:
            int: PID of the winning process.
        """
        winner_ticket = random.choice(allocated_tickets)
        winner_pid = winner_ticket
        return winner_pid

    def run_lottery(self):
        """
        Runs the lottery scheduling algorithm and displays the winner.
        """
        if not self.processes:
            print("No processes to run")
            return
        allocated_tickets = self.allocate_tickets()
        winner_pid = self.select_winner(allocated_tickets)
        print(f"Process {winner_pid} wins the lottery!")

# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()

    # Creating processes
    process1 = Process(1, 3)  # Process with 3 lottery tickets
    process2 = Process(2, 2)  # Process with 2 lottery tickets
    process3 = Process(3, 4)  # Process with 4 lottery tickets

    # Adding processes to scheduler
    scheduler.add_process(process1)
    scheduler.add_process(process2)
    scheduler.add_process(process3)

    # Running the lottery
    scheduler.run_lottery()
