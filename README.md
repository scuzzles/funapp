example docs for project in testing:

First install python socketIO
```
pip install python-socketio requests websocket-client
```
then you can use the following code
```python
import socketio
import json

socket = socketio.Client()

socket.connect('https://ai.nahcrof.com/test')

socket.emit("start_stream", "token goes here")

@socket.on("chunk")
def handle_chunk(data):
    print(data)
    if data == "ENDOFMESSAGE":
        socket.disconnect()

data = {
    "model": "llama3-8b",
    "prompt": "summarize the titanic",
}
socket.emit("prompt", json.dumps(data))

socket.wait()

```
