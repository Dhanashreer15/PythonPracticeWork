class Route:
    def __init__(self, route_name, start, end, stops=None):
        self.route_name=route_name
        self.start=start
        self.end=end
        self.stops=stops if stops else []

    def display_details(self):
        print(f"Route: {self.route_name}, From: {self.start} To: {self.end}")
        if self.stops:
            print("Stops:", ", ".join(self.stops))
