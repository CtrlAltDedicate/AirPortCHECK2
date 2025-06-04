# ✈️ Airport Control System Simulation

This is a Python simulation of a simplified **Airport Control System** for a small airport. It manages incoming and outgoing flight requests (landing, takeoff, and emergency landings) using queue-based logic to prioritize landings and emergencies.

---

## Features

- Simulates incoming flight requests randomly.
- Prioritizes **emergency landings** over regular landings and takeoffs.
- Ensures **no takeoff occurs when landing queue is non-empty**.
- Uses `deque` for efficient queue handling.
- Displays real-time queue and runway status in the console.

---

## Data Structures Used

- `collections.deque`: for efficient and flexible double-ended queue operations.

---
Requirements
Python 3.7 or higher

No external libraries beyond the Python Standard Library
