﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿**Interface documents ：**
 given: 一个dict对象，要求格式如下
 given={"function"：操作码，  
 res:一个dict对象，格式如下
 res={ "success": True or False ,  
 根据用户名称检索用户数据
 given["content“]:dict对象，要求具有value为用户名，key为name的键
 res["content"]:dict对象，用户信息，key和value的对应关系可见database.models.model.UserInfo，查询失败时为None
 插入用户
 given["content“]:dict对象，要求具有所有用户信息的键，key和value的对应关系可见database.models.model.UserInfo
 res["content"]:None
 删除用户
 given["content“]:dict对象，要求具有value为用户名，key为name的键
 res["content"]:None
 更新用户密码
 given["content“]:dict对象，要求具有value为用户名，key为name以及value为新密码，key为password的键
 res["content"]:dict对象，用户信息，key和value的对应关系可见database.models.model.UserInfo，查询失败时为None
 获取推荐问题列表
 given["content“]:dict对象，要求具有value为问题数量，key为number的键
 res["content"]:list对象，list中的每一个元素都为dict对象，存储问题信息，key和value的对应关系可见database.models.model.QuestionInfo
 获取用户关注的问题列表
 given["content“]:dict对象，要求具有value为问题数量，key为number的键
 res["content"]:list对象，list中的每一个元素都为dict对象，存储问题信息，key和value的对应关系可见database.models.model.QuestionInfo