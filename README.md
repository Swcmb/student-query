# 学号查询系统

一个简单易用的学号查询网站，用户输入学号即可查询自己是否入围及排名信息。

## 功能特点

- 🔍 **快速查询**: 输入学号即可快速查询结果
- 📊 **排名显示**: 显示具体排名信息
- 📱 **响应式设计**: 支持手机和电脑访问
- 🎨 **美观界面**: 现代化的用户界面设计
- 📄 **CSV数据源**: 支持从CSV文件读取数据
- 🐳 **Docker支持**: 支持Docker容器化部署
- 📝 **日志记录**: 服务器请求日志记录
- 💚 **健康检查**: 提供健康检查端点

## 文件结构

```
query/
├── index.html          # 主页面
├── style.css          # 样式文件
├── script.js          # JavaScript逻辑
├── students.csv       # 学生数据文件
├── server.py          # Python HTTP服务器
├── Dockerfile         # Docker构建文件
├── docker-compose.yml # Docker Compose配置
├── .gitignore         # Git忽略规则
├── LICENSE            # MIT许可证
├── README.md          # 说明文档
├── CLAUDE.md          # Claude项目文档
├── 使用说明.md         # 用户使用说明
└── 宝塔部署指南.md     # 宝塔面板部署指南
```

## 使用方法

### 方法一：使用Python服务器（推荐）

1. 确保已安装Python 3
2. 在项目目录下运行：
   ```bash
   python server.py
   ```
3. 浏览器会自动打开 http://localhost:8000

### 方法二：使用Docker部署

1. 确保已安装Docker
2. 构建并运行容器：
   ```bash
   docker build -t student-query .
   docker run -p 8000:8000 student-query
   ```
3. 访问 http://localhost:8000

### 方法三：使用Docker Compose

1. 在项目目录下运行：
   ```bash
   docker-compose up -d
   ```
2. 访问 http://localhost:8000

### 方法四：使用其他HTTP服务器

如果你有Node.js，可以使用：
```bash
npx http-server -p 8000
```

或者使用Python的内置服务器：
```bash
python -m http.server 8000
```

## 数据格式

CSV文件格式（students.csv）：
```csv
学号,排名,姓名,成绩,通过状态
2021001,1,张三,95.5,通过
2021002,2,李四,94.2,通过
```

## 自定义数据

1. 编辑 `students.csv` 文件
2. 按照格式添加学生信息
3. 保存文件后刷新网页即可

## 技术栈

- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **后端**: Python HTTP服务器
- **数据**: CSV文件存储
- **部署**: Docker, Docker Compose

## 浏览器支持

- Chrome (推荐)
- Firefox
- Safari
- Edge

## 注意事项

- 确保CSV文件编码为UTF-8
- 学号查询不区分大小写
- 支持移动端访问
- 生产环境建议使用Nginx反向代理

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情