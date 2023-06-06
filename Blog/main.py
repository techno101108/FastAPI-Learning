import schemas
from fastapi import Body, FastAPI

app = FastAPI(debug=True)


@app.get('/')
async def root():
    return {"message": "hello world!"}


@app.get("/users/me")
async def read_user_me():
    user = ['Ram', 'veera', 'gokul', 'jai']
    return {"user": user}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.post('/post')
def create_post(payload: dict = Body):
    return {'msg': payload['title'], "content": payload['content  ']}


@app.post('/demo')
def demo_post(new_post: schemas.create_post):
    print(new_post.rating)
    return {"new-post": new_post}
