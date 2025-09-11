from bus import Bus
from passenger import Passenger
from driver import Driver
from route import Route

# Create driver, route, passengers
driver1=Driver("Ravi Kumar", "D001", "LIC12345")
route1=Route("Route A", "Chennai", "Coimbatore", ["Vellore", "Salem"])
p1=Passenger("Aarav", "T101", "Coimbatore")
p2=Passenger("Diya", "T102", "Salem")

# Create bus and assign driver and route
bus1=Bus("TN01", 2)
bus1.assign_driver(driver1)
bus1.assign_route(route1)

# Add passengers
bus1.add_passenger(p1)
bus1.add_passenger(p2)

# Start trip
bus1.start_trip()

# End trip
bus1.end_trip()

# Display bus status
bus1.display_status()
