# 控制层————接收数据，返回数据
# 引入路由管理
from fastapi import APIRouter
import json
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
from model.commentModel import CommentModel,UserCcontentModel,NewCcontentModel
from service import commentService
# 构建api路由
router = APIRouter()

# 发布评论
@router.post("/createComment", tags=["comment"])
async def creatComment(comment:CommentModel):
    return commentService.createCommentInfos(comment)

# 查看个人发布的评论
@router.get("/searchMyComment", tags=["comment"])
async def searchMyComment(uid:str):
    return commentService.searchComment(uid)

# 删除个人发布的评价
@router.post("/deleteMyComment", tags=["comment"])
async def deleteMyComment(userCcontent:UserCcontentModel):
    return commentService.deleteComment(userCcontent)

# 更改个人发布的评价
@router.post("/editMyComment", tags=["comment"])
async def deleteMyComment(newCcontent:NewCcontentModel):
    return commentService.editComment(newCcontent)



