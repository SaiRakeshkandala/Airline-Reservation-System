-- flights.sql
CREATE TABLE Flights (
    FlightID INTEGER PRIMARY KEY,
    Source TEXT NOT NULL,
    Destination TEXT NOT NULL,
    Time TEXT NOT NULL,
    SeatsAvailable INTEGER NOT NULL
);

CREATE TABLE Bookings (
    BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserName TEXT NOT NULL,
    FlightID INTEGER NOT NULL,
    SeatNumber INTEGER NOT NULL,
    FOREIGN KEY (FlightID) REFERENCES Flights(FlightID)
);
