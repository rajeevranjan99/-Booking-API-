# -Booking-API-
Build a simple Booking API for a fictional fitness studio using Python. 
Project setup instructions
---->install python
----->install django
----> Install djangorestframework,pytz
----> create project
----->create app

Seed data usage
----> create a seed file data for classes

API documentation (endpoints, sample requests)
--->GET: http://127.0.0.1:8000/bookings?email=john@example.com 

    [
    {
        "id": 1,
        "client_name": "John Doe",
        "client_email": "john@example.com",
        "booking_time": "2025-06-06T06:20:32.716666Z",
        "fitness_class": 1
    },
    {
        "id": 2,
        "client_name": "John Doe",
        "client_email": "john@example.com",
        "booking_time": "2025-06-06T07:24:28.671689Z",
        "fitness_class": 2
    }
]


--->POST: http://127.0.0.1:8000/book 

{
    "id": 2,
    "client_name": "John Doe",
    "client_email": "john@example.com",
    "booking_time": "2025-06-06T07:24:28.671689Z",
    "fitness_class": 2
}
---->GET: http://127.0.0.1:8000/classes 

[
    {
        "id": 1,
        "name": "Yoga",
        "date_time": "2025-06-07 11:38:27 IST",
        "instructor": "Aarti",
        "total_slots": 10,
        "available_slots": 9
    },
    {
        "id": 2,
        "name": "Zumba",
        "date_time": "2025-06-08 11:38:27 IST",
        "instructor": "Raj",
        "total_slots": 10,
        "available_slots": 9
    },
    {
        "id": 3,
        "name": "HIIT",
        "date_time": "2025-06-09 11:38:27 IST",
        "instructor": "Meera",
        "total_slots": 10,
        "available_slots": 10
    }
]


. Booking slot validation
. IST ↔ UTC handling
. Logging, edge-case handling, unit test

video_link: https://www.loom.com/share/181b1ea47ca443d0b43fc5e7bffd72cf