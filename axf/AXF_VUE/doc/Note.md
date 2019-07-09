# AXF

## 模块
- 首页
- 商品
- 用户
- 购物车


## 明确我们的端
- 用户端的后端 + 前端


## 开干
- 调通
    - 包括本机调试通过
    - 和远端环境通过
        - 跨域请求
        - 跨域检测是浏览器的行为
    - 解决跨域
        - 服务器解决
        - 客户端自己解决
- 按照模块进行开发
    - 尽量先开发不依赖其它模块的模块
- 用户
    - 数据表
        - 字段
            - 用户名
            - 密码
            - 逻辑删除
            - 是否激活
            - 头像
            - 邮箱
    - 接口
        - 注册
            - 用户名预校验
            - 用户激活
            - 数据安全（不用接口）
        - 登录
        - 获取个人信息
        - 个人信息修改
        - 密码找回
        - 用户认证
        
        
## 用户激活
- 策略
    - 邮箱
        - 内部存在链接，点击链接就激活了
    - 验证码
        - 注册之前就有获取验证码，输入正确的验证码就可以激活了
        
## 文件服务器
- 云存储
    - 阿里云存储
    - 七牛云
    - 金山云
    - 腾讯云
    - ...


## 端的概念
- 淘宝
    - 用户端
    - 商家
        - 商家端
    - 淘宝后端
- 京东
    - 用户端
    - 商家端
        - 都是自营
    - 后端管理
        - 和商家端是一个
- 滴滴
    - 用户端
        - 打车
    - 司机端
        - 出车拉人
    - 后端管理
- 美团
    - 用户端
        - 后端
        - 前端
    - 商家端
        - 后端
        - 前端
    - 骑手端
    - 后台管理
        - 后端
        - 前端
        
        
### 异步任务
- Celery
    - 任务队列（消息载体）
    - 任务
    - 任务调用
    - worker
- 生产者消费者模式

### Celery
- 异步任务
- 定时任务


### Bug
- Celery 和 Cache 对Redis存在版本冲突
- django-celery-results
    - 1.1.2 Celery4.3
- celery
    - redis 3.2.0
- django-redis-cache
    - redis 2.10.6
    
- 解决
    - django-redis-cache
        - 正常
    - celery
        - 4.1.0
        - 依赖
            - kombu==4.1.0

## uwsgi
- pip install uwsgi
- 很容易出问题
    - Python.h文件找不到
    - 安装 python-dev  python3-dev
        - apt install