# DECISIONS.md

## 1. What is an ODM and why do we use Beanie instead of writing raw MongoDB queries?

a ODM lets us work with Python classes instead of raw MongoDB queries and using an Event class with .create() feels much cleaner and safer because Python tells me when a required field is missing and it helps avoid mistakes even before the data goes to the database.

## 2. What is the role of the Database class â€” why wrap Beanie methods inside it instead of calling them directly in routes?

if we ever switch databases, updating every route would be a bad, but with the Database class all the logic stays in one place and the routes just call simple methods like save() or get() without thinking about the details.

## 3. What happens if `initialize_database()` is not called on startup? What would break and why?

I saw this happen while developing the project the app ran but any request caused a Beanie initialization error because Beanie needs to connect to MongoDB and register the models before any queries run and if this step is skipped none of the database operations work.

## 4. What is the difference between the Event document and the EventUpdate model, and why are they two separate classes?

We use Event when creating a new record because all fields are required. For updates we use EventUpdate since its fields are optional and the user can change just one thing without sending everything again. If we used Event for updates the user would have to send all fields and it would fail if anything was missing.
## Part B — Docker Reflection

**1. Why does `DATABASE_URL` use `mongo` as the hostname instead of `localhost`?**

When the app runs inside a container, `localhost` refers to that container itself — not the MongoDB container. Since both services are on the same Docker network, Docker lets them reach each other by service name. So `mongo` is the correct hostname. If I had kept `localhost`, the app would fail to connect because there is no MongoDB running inside the app container.

**2. What does `depends_on` do? Does it guarantee MongoDB is fully ready?**

`depends_on` makes Docker start the `mongo` container before the `app` container. It controls startup order, but it does not guarantee that MongoDB is fully ready to accept connections. The app container starts as soon as the mongo container process begins, not when MongoDB is actually listening. To truly wait for readiness, a healthcheck would be needed.

**3. What is the purpose of the volume? What happens without it?**

The volume maps MongoDB's `/data/db` directory to a `mongo-data/` folder in the project directory on my machine. This means data is stored on the host, not inside the container. After running `docker compose down` and starting again, the data was still there because of this folder. Without the volume, all data would be lost every time the container stops.

**4. Why copy `requirements.txt` and run `pip install` before copying the app code?**

Docker caches each build step as a layer. If `requirements.txt` hasn't changed, Docker reuses the cached pip install layer and skips it entirely. This made rebuilds much faster when I only changed app code. If I copied all files first, any small change in a `.py` file would invalidate the cache and force pip to reinstall everything from scratch.
