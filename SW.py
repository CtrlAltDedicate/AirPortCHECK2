from collections import deque
import random
import time

class FlightRequest:
    def __init__(self, flight_id, request_type):
        self.flight_id = flight_id
        self.request_type = request_type
        self.timestamp = time.time()

class AirportControl:
    def __init__(self):
        self.landing_queue = deque()
        self.takeoff_queue = deque()
        self.runway_busy = False

    def display_queues(self):
        print("\nQueue Status:")
        print("Landing Queue:", [f"Flight {req.flight_id} ({req.request_type})" for req in self.landing_queue])
        print("Takeoff Queue:", [f"Flight {req.flight_id}" for req in self.takeoff_queue])
        print("-" * 50)

    def add_request(self, request):
        if request.request_type == "emergency":
            print(f"⚠️ EMERGENCY: Flight {request.flight_id} needs immediate landing!")
            self.landing_queue.appendleft(request)
        elif request.request_type == "landing":
            print(f"📥 Flight {request.flight_id} requests landing clearance")
            self.landing_queue.append(request)
        elif request.request_type == "takeoff":
            print(f"📤 Flight {request.flight_id} requests takeoff clearance")
            self.takeoff_queue.append(request)

    def process_next(self):
        if self.runway_busy:
            print("❌ Runway is busy")
            return

        if self.landing_queue:
            request = self.landing_queue.popleft()
            self.runway_busy = True
            waiting_time = round(time.time() - request.timestamp, 2)
            print(f"✈️ CONTROL: Flight {request.flight_id} is landing (Waiting time: {waiting_time}s)")
        elif self.takeoff_queue:
            request = self.takeoff_queue.popleft()
            self.runway_busy = True
            waiting_time = round(time.time() - request.timestamp, 2)
            print(f"🛫 CONTROL: Flight {request.flight_id} is taking off (Waiting time: {waiting_time}s)")

        # Simulate runway usage time
        time.sleep(1)
        self.runway_busy = False

def simulate():
    airport = AirportControl()
    flight_id = 100

    print("🛩️ Starting Airport Simulation")
    print("-" * 50)

    for _ in range(15):
        # Random probability for each type of request
        action = random.choices(
            ["landing", "takeoff", "emergency"],
            weights=[0.4, 0.4, 0.2]
        )[0]

        request = FlightRequest(flight_id, action)
        airport.add_request(request)
        airport.display_queues()
        airport.process_next()
        flight_id += 1

        # Random delay between requests
        time.sleep(random.uniform(0.5, 2))

    print("\n✨ End of Simulation")

if __name__ == "__main__":
    simulate()