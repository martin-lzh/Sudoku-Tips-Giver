# Sudoku Tips Giver | 数独提示器

A web application that helps users solve Sudoku puzzles with intelligent hints.

一个帮助用户解决数独谜题的智能提示工具。

## Features | 功能特点

- **Multiple Difficulty Levels | 多难度级别**
  - Easy (35-40 numbers) | 简单 (35-40 个数字)
  - Medium (25-30 numbers) | 中等 (25-30 个数字)
  - Hard (20-25 numbers) | 困难 (20-25 个数字)

- **Smart Hint System | 智能提示系统**
  - Provides intelligent hints | 提供智能提示
  - Shows possible numbers | 显示可能数字
  - Highlights the most logical next move | 高亮显示最合理的下一步

- **Interactive Interface | 交互式界面**
  - Clean and modern design | 简洁现代的设计
  - Dark/Light theme support | 深色/浅色主题支持
  - Bilingual support (English/Chinese) | 双语支持 (中文/英文)
  - Keyboard navigation | 键盘导航
  - Real-time validation | 实时验证

- **Auto-Save Progress | 自动保存进度**
  - Automatically saves game state | 自动保存游戏状态
  - Remembers last played puzzle | 记住上次玩的数独
  - Preserves user preferences | 保存用户偏好设置
  - Works offline | 支持离线使用
  - Cross-device sync (static version) | 跨设备同步（静态版本）

## Live Demo | 在线演示

[Try it online](https://your-username.github.io/sudoku-tips-giver) | [在线体验](https://your-username.github.io/sudoku-tips-giver)

## Deployment Options | 部署选项

### Option 1: Static Version (GitHub Pages) | 选项一：静态版本（GitHub Pages）

The static version is a pure frontend implementation that can be deployed directly to GitHub Pages:

静态版本是纯前端实现，可直接部署到 GitHub Pages：

1. Fork this repository | 复刻此仓库
2. Go to Settings > Pages | 进入设置 > 页面
3. Select branch `main` and folder `/ (root)` | 选择分支 `main` 和文件夹 `/ (root)`
4. Click Save | 点击保存

#### Features | 特点
- Pure frontend implementation | 纯前端实现
- No server required | 无需服务器
- Works offline | 支持离线使用
- Auto-saves to browser storage | 自动保存到浏览器存储
- Cross-device sync via browser | 通过浏览器实现跨设备同步

### Option 2: Full Version (with Backend) | 选项二：完整版本（带后端）

The full version includes a Flask backend for enhanced functionality:

完整版本包含 Flask 后端，提供更多功能：

1. Clone this repository | 克隆此仓库
2. Install dependencies | 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application | 运行应用
   ```bash
   python app.py
   ```
4. Access at `http://localhost:5000` | 访问 `http://localhost:5000`

#### Features | 特点
- Full backend support | 完整后端支持
- Enhanced security | 增强的安全性
- Server-side validation | 服务器端验证
- Database support | 数据库支持
- User accounts (optional) | 用户账户（可选）

### Option 3: Docker Deployment | 选项三：Docker 部署

Deploy using Docker for containerized environment:

使用 Docker 在容器化环境中部署：

1. Build and run with Docker Compose | 使用 Docker Compose 构建和运行
   ```bash
   docker-compose up -d --build
   ```

2. Access at `http://localhost:5000` | 访问 `http://localhost:5000`

#### Docker Commands | Docker 命令

- View logs | 查看日志
  ```bash
  docker-compose logs -f
  ```

- Restart application | 重启应用
  ```bash
  docker-compose restart
  ```

- Stop application | 停止应用
  ```bash
  docker-compose down
  ```

- Update code | 更新代码
  ```bash
  git pull
  docker-compose up -d --build
  ```

## File Structure | 文件结构

```
.
├── app.py              # Flask backend | Flask 后端
├── functions.py        # Core functions | 核心函数
├── sudoku_solver.py    # Sudoku solver | 数独求解器
├── templates/          # HTML templates | HTML 模板
├── static/            # Static files | 静态文件
├── requirements.txt   # Python dependencies | Python 依赖
├── Dockerfile        # Docker configuration | Docker 配置
├── docker-compose.yml # Docker Compose config | Docker Compose 配置
└── README.md         # This file | 本文件
```

## License | 许可证

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## Copyright | 版权

Copyright (c) 2025 Sudoku Tips Giver. All rights reserved.

版权所有 (c) 2025 数独提示器。保留所有权利。

## Advanced Features | 高级功能

- **Unique solution guarantee for generated puzzles | 保证生成的数独有唯一解**
- **Auto-save progress | 自动保存进度**
  - Saves game state automatically | 自动保存游戏状态
  - Remembers last played puzzle | 记住上次玩的数独
  - Preserves user preferences | 保存用户偏好设置
  - Works offline | 支持离线使用
- **Step-by-step solution display | 逐步显示解决方案**
- **Instant completion validation | 即时完成验证** 