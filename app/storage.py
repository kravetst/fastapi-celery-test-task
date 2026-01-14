tasks = []
next_id = 1


def get_tasks():
    """
    Returns a list of all tasks
    """
    return tasks


def add_task(task_data):
    """
    Adds a new task.
    task_data - dictionary with keys title, description, completed
    """
    global next_id
    task = {
        "id": next_id,
        "title": task_data["title"],
        "description": task_data.get("description", ""),
        "completed": task_data.get("completed", False)
    }
    tasks.append(task)
    next_id += 1
    return task


def update_task(task_id, updated_data):
    """
    Updates a task by id.
    updated_data - dictionary with fields to be updated
    """
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_data.get("title", task["title"])
            task["description"] = updated_data.get("description", task["description"])
            task["completed"] = updated_data.get("completed", task["completed"])
            return task
    return None


def delete_task(task_id):
    """
    Deletes a task by id.
    """
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            return tasks.pop(i)
    return None


def clear_tasks():
    global next_id
    tasks.clear()
    next_id = 1
