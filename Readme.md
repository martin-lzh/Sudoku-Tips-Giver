# Sudoku Tips Giver | 数独提示器

A modern, interactive Sudoku web application that helps users solve Sudoku puzzles with intelligent hints and features.

一个现代化的数独提示器 Web 应用，帮助用户解决数独难题，提供智能提示和功能。

## Copyright | 版权

Copyright (c) 2025 Sudoku Tips Giver. All rights reserved.

版权所有 (c) 2025 数独提示器。保留所有权利。

## Features | 功能特点

- **Multiple Difficulty Levels | 多难度级别**
  - Easy (35-40 numbers) | 简单 (35-40 个数字)
  - Medium (25-30 numbers) | 中等 (25-30 个数字)
  - Hard (20-25 numbers) | 困难 (20-25 个数字)

- **Smart Hint System | 智能提示系统**
  - Provides intelligent hints based on Sudoku solving techniques | 基于数独解题技巧提供智能提示
  - Shows possible numbers for each cell | 显示每个格子的可能数字
  - Highlights the most logical next move | 高亮显示最合理的下一步

- **Interactive Interface | 交互式界面**
  - Clean and modern design | 简洁现代的设计
  - Dark/Light theme support | 深色/浅色主题支持
  - Bilingual support (English/Chinese) | 双语支持 (中文/英文)
  - Keyboard navigation | 键盘导航
  - Real-time validation | 实时验证

- **Advanced Features | 高级功能**
  - Unique solution guarantee for generated puzzles | 保证生成的数独有唯一解
  - Auto-save progress | 自动保存进度
  - Step-by-step solution display | 逐步显示解决方案
  - Instant completion validation | 即时完成验证

## Quick Start | 快速开始

### Deploy with Docker | 使用 Docker 部署

1. Clone the repository | 克隆仓库：
```bash
git clone https://github.com/yourusername/sudoku-tips-giver.git
cd sudoku-tips-giver
```

2. Build and run with Docker Compose | 使用 Docker Compose 构建和运行：
```bash
docker-compose up -d --build
```

3. Access the application | 访问应用：
Open your browser and visit `http://localhost` or your server IP | 打开浏览器访问 `http://localhost` 或服务器 IP 地址

### Manual Deployment | 手动部署

1. Install dependencies | 安装依赖：
```bash
pip install -r requirements.txt
```

2. Run the application | 运行应用：
```bash
python app.py
```

3. Access the application | 访问应用：
Open your browser and visit `http://localhost:5000` | 打开浏览器访问 `http://localhost:5000`

## Usage Guide | 使用说明

1. **Generate a New Puzzle | 生成新数独**
   - Select difficulty level (Easy/Medium/Hard) | 选择难度级别 (简单/中等/困难)
   - Click "Generate Sudoku" button | 点击"生成数独"按钮

2. **Game Controls | 游戏操作**
   - Click on any cell to input numbers | 点击格子输入数字
   - Use arrow keys for navigation | 使用方向键导航
   - Input numbers 1-9 | 输入数字 1-9
   - Press Space to move to next cell | 按空格键移动到下一个格子
   - Press Backspace to clear current cell | 按退格键清除当前格子

3. **Getting Help | 获取帮助**
   - Click "Get Hint" for suggestions | 点击"获取提示"获取建议
   - Click "Show Answer" to reveal the correct number | 点击"显示答案"显示高亮格子的正确答案
   - System automatically validates when completed | 系统会在完成时自动验证

4. **Interface Controls | 界面控制**
   - Use theme toggle (🌓) for dark/light mode | 使用主题切换按钮 (🌓) 切换深色/浅色模式
   - Use language toggle (中/En) to switch languages | 使用语言切换按钮 (中/En) 切换中英文
   - Click "Clear Board" to reset the puzzle | 点击"清空棋盘"重置当前数独

## Technical Details | 技术细节

- Frontend: HTML5, CSS3, JavaScript (Vanilla) | 前端：HTML5, CSS3, JavaScript (原生)
- Backend: Python Flask | 后端：Python Flask
- Deployment: Docker & Docker Compose | 部署：Docker & Docker Compose
- Features | 特性：
  - CORS support | CORS 支持
  - Responsive design | 响应式设计
  - Local storage for settings | 本地存储设置持久化
  - Efficient Sudoku generation | 高效的数独生成算法
  - Unique solution verification | 唯一解验证
  - Original implementation | 原创实现
  - No third-party dependencies for core logic | 核心逻辑无第三方依赖

## Code Origin | 代码来源

All code in this project is original and developed from scratch. The implementation of Sudoku generation and solving algorithms is our own work, not copied from any other source.

本项目中的所有代码均为原创，从头开发。数独生成和解题算法的实现都是我们自己的作品，并非复制自其他来源。

## Maintenance Commands | 维护命令

```bash
# View application logs | 查看应用日志
docker-compose logs -f

# Restart application | 重启应用
docker-compose restart

# Stop application | 停止应用
docker-compose down

# Update code and redeploy | 更新代码并重新部署
git pull
docker-compose up -d --build
```

## License | 许可证

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## Acknowledgments | 致谢

- Thanks to all contributors and users who provided feedback | 感谢所有贡献者和提供反馈的用户
- Special thanks to the Flask and Python communities for their excellent documentation | 特别感谢 Flask 和 Python 社区提供的优秀文档