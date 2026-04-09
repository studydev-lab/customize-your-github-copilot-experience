from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: list[Task] = []
next_id = 1


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the FastAPI Task Manager API"}


@app.get("/tasks")
def get_tasks() -> list[Task]:
    return tasks


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> Task:
    global next_id
    task = Task(id=next_id, title=payload.title, completed=payload.completed)
    tasks.append(task)
    next_id += 1
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, payload: TaskCreate) -> Task:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated = Task(id=task_id, title=payload.title, completed=payload.completed)
            tasks[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict[str, str]:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
