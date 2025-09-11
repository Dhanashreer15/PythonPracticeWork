class Bus:
    def __init__(self,bus_number,capacity):
        self.bus_number=bus_number
        self.capacity=capacity
        self.driver=None
        self.passengers=[]
        self.route=None

    def assign_driver(self,driver):
        self.driver=driver
        print(f"Driver {driver.name} assigned to Bus {self.bus_number}")

    def assign_route(self,route):
        self.route=route
        print(f"Route '{route.route_name}' assigned to Bus {self.bus_number}")

    def add_passenger(self,passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Passenger {passenger.name} boarded Bus {self.bus_number}")
        else:
            print("Bus is full. Cannot add more passengers.")

    def remove_passenger(self,ticket_number):
        for p in self.passengers:
            if p.ticket_number == ticket_number:
                self.passengers.remove(p)
                print(f"Passenger {p.name} removed from Bus {self.bus_number}")
                return
        print("Passenger not found.")

    def start_trip(self):
        if not self.driver or not self.route:
            print("Cannot start trip. Driver or route not assigned.")
            return
        print(f"Starting trip on Bus {self.bus_number}")
        self.driver.display_details()
        self.route.display_details()
        print(f"Passengers on board: {len(self.passengers)}")
        for p in self.passengers:
            p.display_details()

    def end_trip(self):
        print(f"Ending trip on Bus {self.bus_number}. Clearing passengers.")
        self.passengers.clear()

    def display_status(self):
        print(f"Bus {self.bus_number} Status:")
        print(f"Driver: {self.driver.name if self.driver else 'None'}")
        print(f"Passengers: {len(self.passengers)} / {self.capacity}")
        print(f"Route: {self.route.route_name if self.route else 'None'}")
