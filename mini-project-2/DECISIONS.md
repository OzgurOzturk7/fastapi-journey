# DECISIONS.md

## 1. What is an ODM and why do we use Beanie instead of writing raw MongoDB queries?

a ODM lets us work with Python classes instead of raw MongoDB queries and using an Event class with .create() feels much cleaner and safer because Python tells me when a required field is missing and it helps avoid mistakes even before the data goes to the database.

## 2. What is the role of the Database class — why wrap Beanie methods inside it instead of calling them directly in routes?

if we ever switch databases, updating every route would be a bad, but with the Database class all the logic stays in one place and the routes just call simple methods like save() or get() without thinking about the details.

## 3. What happens if `initialize_database()` is not called on startup? What would break and why?

I saw this happen while developing the project the app ran but any request caused a Beanie initialization error because Beanie needs to connect to MongoDB and register the models before any queries run and if this step is skipped none of the database operations work.

## 4. What is the difference between the Event document and the EventUpdate model, and why are they two separate classes?

We use Event when creating a new record because all fields are required. For updates we use EventUpdate since its fields are optional and the user can change just one thing without sending everything again. If we used Event for updates the user would have to send all fields and it would fail if anything was missing.