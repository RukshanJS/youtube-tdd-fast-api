from fastapi import FastAPI, HTTPException

from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

todos = []

@app.post("/todos/", status_code=201, response_model=Todo)
async def create_todo(todo: Todo):
    todo.id = len(todos) + 1
    todos.append(todo)
    return todo



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)