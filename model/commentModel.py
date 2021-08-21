from pydantic import BaseModel


class CommentModel(BaseModel):
    passage_id: str  # 文章的id
    user_id: str  # 评论者的id
    ccontent:str  # 评论的内容
    cdate:str    # 评论的时间
    def __int__(self, passage_id, user_uid, ccontent):
        self.passage_id = passage_id
        self.user_uid = user_uid
        self.ccontent = ccontent
        self.date = ''

# 用于接收“删除评论信息”的类
class UserCcontentModel(BaseModel):
    user_id: str        # 评论所属的用户id
    ccontent:str        # 评论的内容
    def __int__(self,user_id, ccontent):
        self.user_id = user_id
        self.ccontent=ccontent

# 用于接收“修改评论信息”的类
class NewCcontentModel(BaseModel):
    comment_id: str        # 评论所属的用户id
    new_ccontent : str
    def __int__(self,comment_id, new_ccontent):
        self.comment_id = comment_id
        self.new_ccontent=new_ccontent