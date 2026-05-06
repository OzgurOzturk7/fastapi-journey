from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from dotenv import load_dotenv
import uuid
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

load_dotenv()

app = FastAPI()

polls = {}

class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, poll_id, websocket):
        await websocket.accept()
        if poll_id not in self.active_connections:
            self.active_connections[poll_id] = []
        self.active_connections[poll_id].append(websocket)

    def disconnect(self, poll_id, websocket):
        if poll_id in self.active_connections:
            self.active_connections[poll_id].remove(websocket)

    async def broadcast(self, poll_id, message):
        if poll_id in self.active_connections:
            for ws in self.active_connections[poll_id]:
                await ws.send_json(message)

manager = ConnectionManager()

@app.post("/polls")
def create_poll(data: dict):
    poll_id = str(uuid.uuid4())[:8]
    polls[poll_id] = {
        "id": poll_id,
        "question": data.get("question", ""),
        "options": {opt: 0 for opt in data.get("options", [])}
    }
    return polls[poll_id]

@app.get("/polls")
def list_polls():
    return list(polls.values())

@app.get("/polls/{poll_id}")
def get_poll(poll_id: str):
    return polls.get(poll_id, {"error": "not found"})

@app.post("/polls/{poll_id}/vote")
def vote_rest(poll_id: str, data: dict):
    option = data.get("option")
    if poll_id in polls and option in polls[poll_id]["options"]:
        polls[poll_id]["options"][option] += 1
        return polls[poll_id]
    return {"error": "invalid"}

@app.delete("/polls/{poll_id}")
def delete_poll(poll_id: str):
    if poll_id in polls:
        del polls[poll_id]
        return {"message": "deleted"}
    return {"error": "not found"}

@app.websocket("/ws/polls/{poll_id}")
async def websocket_endpoint(websocket: WebSocket, poll_id: str):
    await manager.connect(poll_id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            option = data.get("option")
            if poll_id in polls and option in polls[poll_id]["options"]:
                polls[poll_id]["options"][option] += 1
                await manager.broadcast(poll_id, polls[poll_id])
    except WebSocketDisconnect:
        manager.disconnect(poll_id, websocket)
        
        
app.mount("/static", StaticFiles(directory="app"), name="static")

@app.get("/test")
def test_page():
    return FileResponse("app/test.html")