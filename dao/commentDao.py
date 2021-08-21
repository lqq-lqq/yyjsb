# 数据持久化  方法名前缀 insert update select delete

## pymysql 用来做数据库操作的

import time
from model.commentModel import CommentModel,UserCcontentModel,NewCcontentModel
from model.sqlModel import SqlModel
def addComment(commentModel:CommentModel):      # 增加一条评论，返回该评论的id
    sqlmodel = SqlModel()
    # 对评论内容id和评论内容表 添加数据，评论内容id自增
    sql = """INSERT INTO `cid_ccontent`(`cdate`,`ccontent`)  
                VALUES 
                (%s,%s)
                """%(commentModel.cdate,commentModel.ccontent)
    comment_id = sqlmodel.sqlInsert(sql)

    # comment_id = db.insert_id()  # 需要得到前面添加到数据库里自增的评论内容id,

    # 对评论者id和评论内容id表 添加数据
    sql = """INSERT INTO `uid_cid`(`user_id`,`comment_id`)
                VALUES
                (%s,%s)
                    """%(commentModel.user_id,comment_id)
    sqlmodel.sqlInsert(sql)

    # 对评论内容id和原文章id表 添加数据
    sql = """INSERT INTO `cid_pid`(`comment_id`,`passage_id`)
                VALUES
                (%s,%s)
                    """%(comment_id, commentModel.passage_id)
    sqlmodel.sqlInsert(sql)
    return comment_id


# 由用户id来查找该用户所发表的评论内容的id,返回一个“评论内容id-时间-评论内容”的集合
def selectCommentId(uid:str):
    sqlmodel = SqlModel()
    sql = """SELECT * FROM uid_cid
            WHERE user_id='%s'
            """ % (uid)
    uid_commentid_list = sqlmodel.sqlSelect(sql,False)
    ccontent_list=[]
    for row in uid_commentid_list:
        commentid = row[2]            # row
        sql = """SELECT * FROM cid_ccontent
            WHERE comment_id='%s'
            """ % (commentid)
        temp = sqlmodel.sqlSelect(sql, True)
        ccontent_list.append(temp)
    return ccontent_list

# 删除评论
def deleteComment(userCcontent:UserCcontentModel):
    sqlmodel = SqlModel()
    sql = '''SELECT * FROM cid_ccontent
            WHERE ccontent='%s'
            '''%(userCcontent.ccontent)
    item = sqlmodel.sqlSelect(sql, True)
    commentid = item[0]
    sql = '''DELETE FROM uid_ccontent
                WHERE comment_id='%s'
                ''' % (commentid)
    sqlmodel.sqlDelete(sql)

    sql = '''DELETE FROM uid_cid
            WHERE comment_id='%s'
            '''%(commentid)
    sqlmodel.sqlDelete(sql)

    sql = '''DELETE FROM cid_pid
                WHERE comment_id='%s'
                ''' % (commentid)
    sqlmodel.sqlDelete(sql)


# 修改评论
def editComment(newCcontent:NewCcontentModel):
    sqlmodel = SqlModel()
    sql = '''UPDATE cid_ccontent set cdate='%s',ccontent='%s'
            WHERE comment_id='%s'
            '''%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
                 newCcontent.new_ccontent, newCcontent.comment_id)
    sqlmodel.sqlUpdate(sql)



