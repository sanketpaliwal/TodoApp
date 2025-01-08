API DETAILS ABOUT CRUD OPERATIONS:

1. Get All Tasks (GET /)
Purpose: Retrieve all tasks from the database.
Request: Method: GET, URL: /, Body: None.
Response: Status Code: 200 OK, Body: JSON array of tasks.

2. Save a Task (POST /)
Purpose: Create a new task in the database.
Request: Method: POST, URL: /, Body: Task data (e.g., task description).
Response: Status Code: 200 OK, Body: Success message with inserted_id of the new task.

3. Delete a Task (DELETE /)
Purpose: Delete a task by its _id.
Request: Method: DELETE, URL: /, Body: Task _id to delete.
Response: Status Code: 200 OK, Body: Success message with deleted_count (should be 1

4. Edit a Task (PUT /)
Purpose: Update an existing task in the database based on its _id.
Request: Method: PUT, URL: /, Body: Task data with _id and updated fields (e.g., task description).
Response: Status Code: 200 OK, Body: Success message with modified_count indicating the number of tasks updated.


