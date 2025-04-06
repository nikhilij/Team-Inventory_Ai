# main.py

from agents.coordinator import CoordinatorAgent

def main():
    print("Running Multi-Agent Inventory Optimization System")
    coordinator = CoordinatorAgent()
    coordinator.run_all_agents()

if __name__ == '__main__':
    main()
