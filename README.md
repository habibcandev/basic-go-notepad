# basic-go-notepad
A basic online notepad made with Go.

### 🌴 Simple Notes App

This simple note-taking application allows users to add, edit, and delete text-based notes. Users can access and edit their personal notes using this application. Additionally, continuous session-based storage is provided to store the notes.
Error Situations and Solutions

🚨 Error reading request body
        Problem: There was an error reading the request body.
        Solution: This usually occurs due to network or server issues. Check your internet connection or see if there are any network issues on the server side.

🚨 Invalid JSON format
        Problem: The JSON format sent is invalid.
        Solution: Check the JSON data being sent and ensure it is in the correct format. If there's a JSON formatting error, correct it and try again.

🚨 Invalid note ID
        Problem: The note ID provided is invalid.
        Solution: Make sure you specify the note ID correctly. Use the note IDs provided by the application to perform operations.

🚨 Note not found
        Problem: The note could not be found.
        Solution: Check if there is a note with the specified ID. Consider that the note may have been deleted or may have an incorrect ID. If you suspect the note has been deleted, you may consider re-adding the note.

### 🌴 How the Program Works

··  Server Initialization: When the program starts, an HTTP server is initialized to listen on a specific port (by default 8080).

··  Handling Requests: The server listens for incoming HTTP requests to specific URLs and routes them to appropriate handlers to perform the necessary actions.

··  Home Page Request: When a request for the home page (/) is received, the server responds with a message "Welcome to Simple Notes App!"

··  Notes List Request: A request for the list of notes (/notes) returns all the notes stored on the server in JSON format.

··  Add Note Request: An add note request (/add) is used to add a new note to the server. It receives JSON data sent by the user, assigns an ID to the note, and adds it to the list of notes.

··  Edit Note Request: An edit note request (/edit/:id) is used to edit a specific note. It receives JSON data sent by the user and finds the note with the specified ID. The title and body of the note are then updated.

··  Delete Note Request: A delete note request (/delete/:id) is used to delete a specific note. It removes the note from the list of notes based on the provided ID.

··  Error Situations: In case of any error, the server responds with an appropriate HTTP status code and a message explaining the cause of the error. Users can understand the reasons for the errors and make necessary corrections.
