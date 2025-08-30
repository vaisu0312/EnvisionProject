# Simple To-Do Backend using Flask
# Requirements:
# - In-memory storage (data resets when server restarts)
# - Endpoints:
#    GET /to-dos → Returns all tasks
#    POST /to-dos → Adds a new task with a unique ID
#    DELETE /to-dos/<id> → Deletes a task by its ID

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
tasks = []
task_id_counter = 1

# GET → Retrieve all tasks
@app.route('/to-dos', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# POST → Add a new task
@app.route('/to-dos', methods=['POST'])
def add_task():
    global task_id_counter
    data = request.get_json()
    new_task = {
        "id": task_id_counter,
        "task": data.get("task", "")
    }
    tasks.append(new_task)
    task_id_counter += 1
    return jsonify(new_task), 201

# DELETE → Remove a task by ID
@app.route('/to-dos/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": f"Task {task_id} deleted."}), 200


if __name__ == '__main__':
    app.run(debug=True)
