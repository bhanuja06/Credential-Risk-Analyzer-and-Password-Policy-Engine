```markdown
# Setup Instructions - Credential Risk Analyzer

## Prerequisites
- **Python 3.7 or higher** installed on your system
- **Git** (optional, for cloning the repository)

## Quick Setup (3 Steps)

### 1. Clone or Download the Repository
```bash
git clone https://github.com/yourusername/credential-risk-analyzer.git
cd credential-risk-analyzer
```

### 2. Verify Python Installation
```bash
python --version  # or python3 --version
```

### 3. Run the Tool
```bash
python password_analyzer.py  # or python3 password_analyzer.py
```

That's it! The tool uses **only Python standard library** – no external dependencies.

## Windows Setup (Detailed)
1. Download Python from [python.org](https://python.org) (check "Add Python to PATH")
2. Open Command Prompt and run:
```cmd
cd Desktop
git clone https://github.com/yourusername/credential-risk-analyzer.git
cd credential-risk-analyzer
python password_analyzer.py
```

## Linux/macOS Setup
```bash
# Install Python if needed (Ubuntu/Debian)
sudo apt update && sudo apt install python3

# Clone and run
git clone https://github.com/yourusername/credential-risk-analyzer.git
cd credential-risk-analyzer
python3 password_analyzer.py
```

## Verify It Works
You should see the analyzer prompt. Enter `password123` to test.

## Troubleshooting
| Issue | Solution |
|-------|----------|
| `python: command not found` | Use `python3` instead |
| `Permission denied` | Run `chmod +x password_analyzer.py` |
| `File not found` | Check you're in the correct directory |

## Customizing Policy
Edit `password_analyzer.py` and change:
```python
self.min_length = 8          # Minimum length
self.min_uppercase = 1       # Uppercase letters
self.min_lowercase = 1       # Lowercase letters
self.min_digits = 1          # Numbers
self.min_special = 1         # Special characters
```

## Optional: Create Executable
```bash
pip install pyinstaller
pyinstaller --onefile password_analyzer.py
```

## Docker Setup (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY password_analyzer.py .
CMD ["python", "password_analyzer.py"]
```
```bash
docker build -t password-analyzer .
docker run -it password-analyzer
```

