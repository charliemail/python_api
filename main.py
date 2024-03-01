from fastapi import FastAPI
from app.routers.companies import router as companies_router

app = FastAPI()

# 引入用户路由
app.include_router(companies_router, prefix="/company")

# 根路由
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)