import random

class Process:
    def __init__(self, pid, tickets):
        self.pid = pid
        self.tickets = tickets

class Scheduler:
    def __init__(self):
        self.processes = []
        self.total_tickets = 0

    def add_process(self, process):
        self.processes.append(process)
        self.total_tickets += process.tickets

    def allocate_tickets(self):
        allocated_tickets = []
        ticket_counter = 0
        for process in self.processes:
            for _ in range(process.tickets):
                allocated_tickets.append((ticket_counter, process.pid))
                ticket_counter += 1
        return allocated_tickets

    def select_winner(self):
        allocated_tickets = self.allocate_tickets()
        winning_ticket = random.choice(allocated_tickets)
        winner_pid = winning_ticket[1]
        return winner_pid

# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()
    
    # Adding processes
    scheduler.add_process(Process(1, 5))
    scheduler.add_process(Process(2, 3))
    scheduler.add_process(Process(3, 7))
    
    # Selecting winner
    winner_pid = scheduler.select_winner()
    print(f"Process {winner_pid} wins the lottery!")

