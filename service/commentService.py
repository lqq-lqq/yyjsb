from model.commentModel import CommentModel,UserCcontentModel,NewCcontentModel
from fastapi.responses import JSONResponse
from dao import commentDao
import time

# 创建评论信息
def createCommentInfos(comment:CommentModel):
    # commentDao的操作
    comment.cdate = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    comment_id = commentDao.addComment(comment)
    return JSONResponse(
        content={
            "code": "200",
            "data": {
                "date": comment.cdate,
                "comment_id": comment_id,        # 需要数据库返回id
                "content": comment.ccontent,
                "passage_id": comment.passage_id,
                "music_url":"xxx"
            },
            "message": "评论发布成功"
        }
    )

# 查看个人发布的评论
def searchComment(user_id:str):
    ccontent_list = commentDao.selectCommentId(user_id)
    return ccontent_list

def deleteComment(userCcontent:UserCcontentModel):
    commentDao.deleteComment(userCcontent)
    return JSONResponse(
        content={
            "code": "200",
            "data": {
            },
            "message": "评论删除成功"
        }
    )

def editComment(newCcontent:NewCcontentModel):
    commentDao.editComment(newCcontent)
    return JSONResponse(
        content={
            "code": "200",
            "data": {
            },
            "message": "评论修改成功"
        }
    )
