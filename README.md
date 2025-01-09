# ✈️ Airline Reservation System  

The **Airline Reservation System** is a Python-based application that allows users to book flights, cancel reservations, and view flight schedules. This system is built using Flask and SQLite, showcasing real-time database operations.  

---

## 📋 Features  
- 🔍 **Search Flights**: View available flights based on source and destination.  
- 🪑 **Book Flights**: Reserve a seat on a selected flight.  
- ❌ **Cancel Bookings**: Cancel a booking and update seat availability.  

---

## 🛠️ Technology Stack  
- **Backend**: Python (Flask)  
- **Database**: SQLite  
- **Frontend (Optional)**: Flask templates  

---

## 🚀 How to Run  

### 1️⃣ Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/airline-reservation.git
   cd airline-reservation
   ```  
2. Install dependencies:  
   ```bash
   pip install flask
   ```  
3. Initialize the database:  
   ```bash
   python app.py
   ```  
   (This will set up the database with sample data.)  

---

### 2️⃣ Run the Application  
1. Start the Flask server:  
   ```bash
   python app.py
   ```  
2. Open your browser and go to:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)  

---

## 📄 API Endpoints  

### 🔍 Search Flights  
**Endpoint:** `/flights`  
**Method:** `GET`  
**Query Params:**  
- `source`: Source city  
- `destination`: Destination city  

**Example:**  
```http
GET /flights?source=Chennai&destination=Delhi
```  

---

### 🪑 Book a Flight  
**Endpoint:** `/book`  
**Method:** `POST`  
**Body:**  
```json
{
  "user_name": "Sai Rakesh",
  "flight_id": 1
}
```  

---

### ❌ Cancel Booking  
**Endpoint:** `/cancel`  
**Method:** `POST`  
**Body:**  
```json
{
  "booking_id": 1
}
```  

---

## 🧪 Testing  
1. Use Postman, curl, or any API testing tool to test the endpoints.  
2. Ensure all scenarios are covered:  
   - No seats available.  
   - Invalid booking IDs.  

---

## 📂 File Structure  
```
📂 airline-reservation  
├── app.py         # Flask application  
├── flights.sql    # SQL script to create and populate database  
└── README.md      # Documentation  
```  

---

## 💡 Future Enhancements  
- 🌐 Add a frontend interface using Flask templates or React.  
- 📱 Build a mobile app for booking and management.  
- 💾 Switch to a more robust database like PostgreSQL.  

---

## 👨‍💻 Author  
Developed by **Sai Rakesh Kandala** 💻  
