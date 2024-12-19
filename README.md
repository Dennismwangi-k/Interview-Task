# Closest Points API

This Django-based API finds the closest pair of points from a given string of coordinates and 
saves the results to a database. The program has two endpoints: one for submitting points and calculating 
the closest pair, and another for getting all stored results.

## **Setup Instructions**

## **1. Install dependencies**
Make sure Python is installed on your machine. To install the required dependencies, run:


pip install -r requirements.txt

---

### **2. Apply Migrations**
Set up the database by applying migrations:

python manage.py migrate


---

### **3. Create a Superuser**
Create a superuser account for authentication purposes:

python manage.py createsuperuser


### **4. Start the Server**
Run the server:

python manage.py runserver

Application will be available at:

http://127.0.0.1:8000/


---

## **Use the API**

## **Authorisation**
The API requires Basic Authentication. Enter the username and password for the superuser you created earlier.

---

### **End Points**

#### **POST api/points/**
Enter a string of  points to find the nearest pair.

**Request body:**
Format: JSON Field: 'points_string'


**Example Valid Input:**

{
    "points_string": "(2,3), (1,1), (5,4)"
}


**Example Responses:**
- **Success (201 Created):**

{
    "id": 1,
    "points_string": "(2,3), (1,1), (5,4)",
    "closest_pair": "(1, 1) and (2, 3)",
    "created_at": "2024-12-18T10:30:00Z"
}

- **Error (400 Bad Request):**

{
    "error": "Invalid format. Ensure points_string is in the correct format, e.g., '(2,3), (1,1), (5,4)'."
}


---

#### **GET /api/points/**
Retrieve all stored computations.

**Example Response:**

[
    {
        "id": 1,
        "points_string": "(2,3), (1,1), (5,4)",
        "closest_pair": "(1, 1) and (2, 3)",
        "created_at": "2024-12-18T10:30:00Z"
    }
]


---

## **Testing the App**

### **Manual testing using Postman**

#### **1. Authorization. **
- Under the Authorization tab in Postman, pick **Basic Auth**.
- Enter the superuser's username and password.

#### **2. Test the POST Method**.
- Change the HTTP method to **POST**.
- Use this endpoint:

  http://127.0.0.1:8000/api/points/

- In the Body tab, pick **raw** and change the format to **JSON**.
- Include test data, for example:


  {
      "points_string": "(2,3), (1,1), (5,4)"
  }

- Send the request and confirm the response.

#### **3. Test the GET Method**.
- Change the HTTP method to **GET**.
- Use the same endpoint.

  http://127.0.0.1:8000/api/points/

- Send the request and ensure that the return contains the saved results.

---

### **Automated Testing using Unit Tests**
Run the following command to conduct the automated unit tests:

Python manage.py test.


Tests will validate:
1. **POST Method**: - Valid inputs are processed accurately.
   - Confirms that incorrect inputs return appropriate error messages.
2. **GET Method**: - Ensures saved computations are correctly retrieved.


---

## **Examples of Test Data for POST Requests**

### Valid Input

{
    "points_string": "(2,3), (1,1), (5,4)"
}


### Large Dataset

{
    "points_string": "(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)"
}


### Edge Case (Invalid Format)

{
    "points_string": "(2,3) (1,1), (5,4)"
}


### Single Point (Error Expected)

{
    "points_string": "(2,3)"
}


---

## **summary**
This application accepts a string of points using the '/api/points/' POST endpoint.
- Uses the Euclidean distance calculation to find the closest pair of locations.
- Stores the input and output in a database.
- Offers a '/api/points/' GET endpoint for retrieving all saved results.
- Basic authentication is required for API access.
- Unit tests are included to ensure validation.

Let me know if you have any problems while running the application!

