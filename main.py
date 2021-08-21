# 配置跨域
import uvicorn as uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
# 返回json格式的数据
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse
# 配置静态资源
from fastapi.staticfiles import StaticFiles
from api import comment
# 声明fastapi的实例
app = FastAPI()
# 配置静态资源的存放路径以及请求的路径
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
# 跨域配置
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# 注册api模块
app.include_router(comment.router,prefix="/yyjsb/comment")

# 配置容器启动相应的实例
if __name__ == '__main__':
    uvicorn.run(app='main:app', port=10086,reload=True)         # 端口更改
