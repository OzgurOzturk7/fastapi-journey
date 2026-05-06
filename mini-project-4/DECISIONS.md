\# DECISIONS — Mini Project 4



\## 1. Connection Management

ConnectionManager stores connections for each poll\_id in a list. When a client disconnects WebSocketDisconnect is caught and that connection is removed. The app does not crash because the error is handled with try/except.



\## 2. State Storage

Votes are stored in a dictionary in memory. It is simple and works for a small project. But if the server restarts all data is lost For production database like MongoDB would be needed.



\## 3. Concurrency

If two users vote at the same tim one vote might overwrite the other.I did not handle this. In production lock or atomic database operation would be needed.





\## 4. REST vs WebSocket

POST /polls/{id}/vote updates the vote but only the requesting client sees the result. WebSocket broadcasts the update to all connected clients. REST is for simple one time actions WebSocket is for real time updates.

