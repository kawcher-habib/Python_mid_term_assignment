class Star_Cinema:
    hall_list = []
    
    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)


class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_List  = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        self.entry_hall(self)
    
    def entry_show(self, show_id, movie_name, time):

        showInfo = (show_id, movie_name, time)
        self.show_List.append(showInfo)

        self.seats[show_id] = [['Free' for _ in range(self.cols)] for _ in range(self.rows)]

    
    def book_seats(self, show_id, seat_list):

        if show_id not in self.seats:
      
            return "Invalid ID"
        seatChecker = self.seats[show_id]

        for row, col in seat_list:
            if row < self.rows and col < self.cols:
                if seatChecker[row][col] == 'Free':
                    seatChecker[row][col] = 'Booked'
                    
                else:
                    print(f'seat {row}, {col} is already booked')
            else:
                print("Seat is out of bounds")
        
        return "seat booked successfully"
            

    def view_show_list(self):

        if not self.show_List:
            print("no shows are running")
        
        else:

            for show_id, movie_name, time in self.show_List:
                print(show_id, movie_name, time)

        

    def view_available_seats(self, show_id):

        if show_id not in self.seats:
            print("Invalid ID")
            return
        
        seatChecker = self.seats[show_id]
        
        for row in range(self.rows):
            for col in range(self.cols):

                if seatChecker[row][col] == 'Free':
                    print(row,' ', col, end="")
            print()
        




hall = Hall(3, 3, "H1")

run = True

while run:

    print("Select Option: \n")

    print("1 : Add Show")
    print("2 : Show List ")
    print("3 : Available Seats")
    print("4 : Book Seat")
    print("5 : Exit")

    ch = int(input("\nEnter Option: "))

    if ch == 1:

        showId = int(input("\nEnter Show ID: "))
        movieName = input("\nEnter Movie Name: ")
        showTime = input("\nEnter Time: ")
        hall.entry_show(showId, movieName, showTime)

    elif ch == 2:

        print()
        hall.view_show_list()
        print()

    elif ch == 3:

        print()
        showId = int(input("\nEnter Show ID: "))
        hall.view_available_seats(showId)
        print()
    elif ch == 4:
        print()
        showId = int(input("\nEnter Show ID: "))
        seatRow = int(input("\nEnter Seat Row: "))
        seatCol = int(input("\nEnter Seat Col: "))
        hall.book_seats(showId,[(seatRow, seatCol)])
        print()

    else:
        break
