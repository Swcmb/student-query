# 学号查询系统 - Claude 项目文档

## 项目概述
这是一个简单的学号查询网站，用户输入学号即可查询自己是否入围及排名信息。系统采用纯前端 + Python HTTP 服务器 + CSV 数据文件的架构。

## 技术栈
- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **后端**: Python 3 HTTP 服务器 (内置 http.server)
- **数据存储**: CSV 文件 (students.csv)
- **部署**: 支持 Docker、宝塔面板、Nginx 等多种方式

## 项目结构
```
query/
├── index.html          # 主页面
├── style.css          # 样式文件
├── script.js          # JavaScript 逻辑
├── students.csv       # 学生数据文件 (23条示例数据)
├── server.py          # Python HTTP 服务器
├── README.md          # 项目说明文档
├── 使用说明.md         # 用户使用说明
├── 宝塔部署指南.md     # 宝塔面板部署指南
└── deploy.sh          # 部署脚本 (空文件)
```

## 核心功能
1. **学号查询**: 输入学号查询成绩、排名、通过状态
2. **结果展示**: 显示排名、成绩、通过状态，使用不同颜色区分通过/未通过
3. **响应式设计**: 支持手机和电脑访问
4. **数据管理**: 通过 CSV 文件管理学生数据

## 数据格式
CSV 文件格式 (`students.csv`):
```
学号,排名,姓名,成绩,通过状态
2021001,1,张三,95.5,通过
2021002,2,李四,94.2,通过
...
```

## 运行方式

### 方法一: Python 服务器 (推荐)
```bash
python server.py
```
自动打开浏览器访问 http://localhost:8000

### 方法二: Docker 部署
```bash
docker build -t student-query .
docker run -p 8000:8000 student-query
```

### 方法三: 其他 HTTP 服务器
```bash
npx http-server -p 8000
# 或
python -m http.server 8000
```

## 开发说明
- 修改 `students.csv` 更新学生数据
- 前端文件 (HTML/CSS/JS) 修改后刷新浏览器即可生效
- 服务器支持 CORS，可跨域访问

## 注意事项
- CSV 文件必须使用 UTF-8 编码
- 学号查询不区分大小写
- 生产环境建议使用 Nginx 反向代理