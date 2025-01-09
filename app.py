from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'airline_reservation.db'

# Helper function to interact with the database
def query_db(query, args=(), one=False, commit=False):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    if commit:
        conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# Initialize database with sample data
def init_db():
    with open('flights.sql', 'r') as f:
        query = f.read()
    query_db(query, commit=True)
    query_db("""
    INSERT INTO Flights (FlightID, Source, Destination, Time, SeatsAvailable)
    VALUES 
    (1, 'Chennai', 'Delhi', '10:00 AM', 100),
    (2, 'Mumbai', 'Bangalore', '01:00 PM', 50);
    """, commit=True)

@app.route('/flights', methods=['GET'])
def get_flights():
    source = request.args.get('source')
    destination = request.args.get('destination')
    flights = query_db(
        "SELECT * FROM Flights WHERE Source=? AND Destination=?", 
        (source, destination)
    )
    return jsonify(flights)

@app.route('/book', methods=['POST'])
def book_flight():
    data = request.json
    user_name = data['user_name']
    flight_id = data['flight_id']

    flight = query_db("SELECT SeatsAvailable FROM Flights WHERE FlightID=?", (flight_id,), one=True)
    if flight and flight[0] > 0:
        seat_number = flight[0]
        query_db("INSERT INTO Bookings (UserName, FlightID, SeatNumber) VALUES (?, ?, ?)", 
                 (user_name, flight_id, seat_number), commit=True)
        query_db("UPDATE Flights SET SeatsAvailable = SeatsAvailable - 1 WHERE FlightID=?", 
                 (flight_id,), commit=True)
        return jsonify({"message": "Booking successful", "seat_number": seat_number})
    return jsonify({"error": "No seats available"}), 400

@app.route('/cancel', methods=['POST'])
def cancel_booking():
    data = request.json
    booking_id = data['booking_id']
    booking = query_db("SELECT FlightID, SeatNumber FROM Bookings WHERE BookingID=?", (booking_id,), one=True)
    if booking:
        flight_id, seat_number = booking
        query_db("DELETE FROM Bookings WHERE BookingID=?", (booking_id,), commit=True)
        query_db("UPDATE Flights SET SeatsAvailable = SeatsAvailable + 1 WHERE FlightID=?", 
                 (flight_id,), commit=True)
        return jsonify({"message": "Booking canceled"})
    return jsonify({"error": "Booking ID not found"}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

