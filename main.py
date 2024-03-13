from fastapi import FastAPI
from app.routers import member_router, member_group_router

app = FastAPI()

# 引入用户路由
app.include_router(member_router.router)
app.include_router(member_group_router.router)

# 根路由
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080)