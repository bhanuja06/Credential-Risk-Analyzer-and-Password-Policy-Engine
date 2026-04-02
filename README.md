# Credential-Risk-Analyzer-and-Password-Policy-Engine


A simple, zero-dependency Python tool that evaluates password strength, checks policy violations, and tells you exactly how to improve weak passwords.

## Features

-  Checks password against custom policy rules (length, uppercase, lowercase, digits, special chars)
-  Scores passwords from 0-100 (Very Weak → Very Strong)
-  Identifies weak patterns (repeated chars, sequential patterns, common substitutions)
-  Provides actionable recommendations to fix weak passwords
-  Detects common passwords and keyboard patterns
-  No external dependencies - just Python

## Quick Start

```bash
git clone https://github.com/yourusername/credential-risk-analyzer.git
cd credential-risk-analyzer
python password_analyzer.py
```

Enter a password and get instant feedback.

## Example Output

```
============================================================
Password: ********
Strength: WEAK (Score: 32/100)
============================================================

 POLICY VIOLATIONS:
  • At least 1 uppercase letter(s)
  • At least 1 special character(s)

 WEAK POINTS:
  • No uppercase letters
  • Contains sequential pattern '123'

 RECOMMENDATIONS:
  • Add uppercase letters (A-Z)
  • Add special characters (!@#$%^&*)
  • Avoid sequential patterns like '123'
```

## Customize Policy

Edit `password_analyzer.py`:

```python
self.min_length = 12        # Minimum length
self.min_uppercase = 2      # Uppercase letters required
self.min_lowercase = 2      # Lowercase letters required
self.min_digits = 2         # Numbers required
self.min_special = 2        # Special characters required
```

## Use as a Module

```python
from password_analyzer import CredentialRiskAnalyzer

analyzer = CredentialRiskAnalyzer()
result = analyzer.analyze("MyP@ssw0rd")

print(f"Strength: {result['strength']}")
print(f"Score: {result['score']}/100")
print(f"Recommendations: {result['recommendations']}")
```

## Project Structure

```
credential-risk-analyzer/
├── README.md               # This file
├── SETUP.md                # Detailed setup instructions
└── password_analyzer.py    # Main Script
```

## Requirements

- Python 3.7 or higher


## Author

S.BHANUJA

## Contributing

Issues and pull requests welcome.
```
