from fastapi import FastAPI
from app.routers import router_member_groups

app = FastAPI()

# 引入用户路由
app.include_router(router_member_groups.router)

# 根路由
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080)