
## Setup Instructions

## 1. Make sure you have Python 3.7+
```bash
python --version
```

## 2. Download the project
```bash
git clone https://github.com/yourusername/credential-risk-analyzer.git
cd credential-risk-analyzer
```

## 3. Run the analyzer
```bash
python password_analyzer.py
```

That's it. No extra packages needed.

## Example
Enter a password like `password123` and see the analysis.

## Change password rules
Open `password_analyzer.py` and edit:
```python
self.min_length = 8
self.min_uppercase = 1
self.min_lowercase = 1
self.min_digits = 1
self.min_special = 1
```

## Troubleshooting
- On Mac/Linux use `python3` instead of `python`
- Make sure you're in the right folder with `ls` (Mac/Linux) or `dir` (Windows)
```
