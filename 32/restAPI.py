#32. Bygg en enkel REST API med Python Flask eller Node.js.

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Dummy data
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Build an API", "completed": True},
]

# Route: Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# Route: Get a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        abort(404, description="Task not found")
    return jsonify(task)

# Route: Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400, description="Invalid input")
    new_task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,
        "title": request.json["title"],
        "completed": request.json.get("completed", False),
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Route: Update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        abort(404, description="Task not found")
    if not request.json:
        abort(400, description="Invalid input")
    task["title"] = request.json.get("title", task["title"])
    task["completed"] = request.json.get("completed", task["completed"])
    return jsonify(task)

# Route: Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        abort(404, description="Task not found")
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"result": "Task deleted"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

#curl http://127.0.0.1:5000/tasks
#curl -X POST -H "Content-Type: application/json" -d '{"title": "Write a blog post"}' http://127.0.0.1:5000/tasks
#curl -X PUT -H "Content-Type: application/json" -d '{"completed": true}' http://127.0.0.1:5000/tasks/1
#curl -X DELETE http://127.0.0.1:5000/tasks/2
