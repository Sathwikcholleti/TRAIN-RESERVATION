import random

class TrainReservationSystem:
    def __init__(self):
        self.passengers = []
        self.ticket_id_counter = 1000
        self.fares = {
            'AC': 1500,
            'Sleeper': 800,
            'Unreserved': 300
        }

    def generate_berth(self, coach_type):
        berth_types = {
            'AC': ['Lower', 'Upper', 'Side Lower'],
            'Sleeper': ['Lower', 'Middle', 'Upper', 'Side Lower', 'Side Upper'],
            'Unreserved': ['General']
        }
        return random.choice(berth_types[coach_type])

    def generate_coach_number(self, coach_type):
        prefixes = {
            'AC': 'A',
            'Sleeper': 'S',
            'Unreserved': 'U'
        }
        return f"{prefixes[coach_type]}{random.randint(1, 15)}"

    def calculate_fare(self, coach_type):
        return self.fares.get(coach_type, 0)

    def book_ticket(self):
        print("\n--- Book Train Ticket ---")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender (M/F/O): ")
        source = input("Enter Source Station: ")
        destination = input("Enter Destination Station: ")

        print("\nCoach Types:\n1. AC\n2. Sleeper\n3. Unreserved")
        coach_choice = input("Choose Coach Type (1/2/3): ")

        coach_map = {'1': 'AC', '2': 'Sleeper', '3': 'Unreserved'}
        coach_type = coach_map.get(coach_choice)

        if not coach_type:
            print("Invalid coach type selection.")
            return

        berth = self.generate_berth(coach_type)
        coach_number = self.generate_coach_number(coach_type)
        fare = self.calculate_fare(coach_type)
        ticket_id = self.ticket_id_counter
        self.ticket_id_counter += 1

        passenger = {
            'Ticket ID': ticket_id,
            'Name': name,
            'Age': age,
            'Gender': gender,
            'Source': source,
            'Destination': destination,
            'Coach Type': coach_type,
            'Berth': berth,
            'Coach Number': coach_number,
            'Fare': fare
        }

        self.passengers.append(passenger)
        print("\n✅ Ticket Booked Successfully!")
        self.print_ticket(passenger)

    def print_ticket(self, passenger):
        print("\n----- TICKET -----")
        for key, value in passenger.items():
            print(f"{key}: {value}")
        print("------------------")

    def view_all_bookings(self):
        print("\n--- All Bookings ---")
        if not self.passengers:
            print("No tickets booked yet.")
            return
        for passenger in self.passengers:
            self.print_ticket(passenger)

    def run(self):
        while True:
            print("\n===== IRCTC Train Ticket Reservation =====")
            print("1. Book Ticket")
            print("2. View All Bookings")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                self.book_ticket()
            elif choice == '2':
                self.view_all_bookings()
            elif choice == '3':
                print("Thank you for using IRCTC Train Reservation System!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    system = TrainReservationSystem()
    system.run()
