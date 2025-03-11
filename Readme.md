# Sudoku Tips Giver

A modern, interactive Sudoku web application that helps users solve Sudoku puzzles with intelligent hints and features.

## Features

- **Multiple Difficulty Levels**
  - Easy (35-40 numbers)
  - Medium (25-30 numbers)
  - Default (20-25 numbers)

- **Smart Hint System**
  - Provides intelligent hints based on Sudoku solving techniques
  - Shows possible numbers for each cell
  - Highlights the most logical next move

- **Interactive Interface**
  - Clean and modern design
  - Dark/Light theme support
  - Bilingual support (English/Chinese)
  - Keyboard navigation
  - Real-time validation

- **Advanced Features**
  - Unique solution guarantee for generated puzzles
  - Auto-save progress
  - Step-by-step solution display
  - Instant completion validation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sudoku-tips-giver.git
cd sudoku-tips-giver
```

2. Install the required dependencies:
```bash
pip install flask flask-cors
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. **Generate a New Puzzle**
   - Select difficulty level (Easy/Medium/Hard)
   - Click "Generate Sudoku" button

2. **Playing the Game**
   - Click on any cell to input numbers
   - Use keyboard arrows for navigation
   - Use Space key to move to next cell
   - Use Backspace key to clear and move to previous cell
   - Numbers 1-9 for input
   - System automatically moves to next cell after input

3. **Getting Help**
   - Click "Get Hint" for suggestions
   - Click "Show Answer" to reveal the correct number in the highlighted cell
   - The system will automatically validate your solution when completed

4. **Additional Controls**
   - Use the theme toggle (🌓) for dark/light mode
   - Use the language toggle (中/En) to switch between Chinese and English
   - Click "Clear Board" to reset the current puzzle

## Technical Details

- Frontend: HTML5, CSS3, JavaScript (Vanilla)
- Backend: Python Flask
- Features:
  - CORS support for API access
  - Responsive design
  - Local storage for settings persistence
  - Efficient Sudoku generation algorithm
  - Unique solution verification

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors and users who provided feedback
- Special thanks to the Flask and Python communities for their excellent documentation