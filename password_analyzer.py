import re
import math
from collections import Counter

class CredentialRiskAnalyzer:
    def __init__(self):
        # Password policy settings
        self.min_length = 8
        self.min_uppercase = 1
        self.min_lowercase = 1
        self.min_digits = 1
        self.min_special = 1
        
        # Common weak patterns
        self.common_passwords = set([
            "password", "123456", "qwerty", "admin", "letmein", "welcome",
            "monkey", "dragon", "master", "football", "baseball", "login"
        ])
        
        self.common_substitutions = {
            'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7'
        }
        
        self.repeated_pattern_regex = re.compile(r'(.)\1{2,}')  # 3+ repeated chars
        self.sequential_regex = re.compile(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz|123|234|345|456|567|678|789|890|qwerty|asdf|zxcv)', re.IGNORECASE)

    def check_policy_violations(self, password):
        """Check password against defined policy rules."""
        violations = []
        
        if len(password) < self.min_length:
            violations.append(f"Minimum length {self.min_length} characters (current: {len(password)})")
        
        if sum(1 for c in password if c.isupper()) < self.min_uppercase:
            violations.append(f"At least {self.min_uppercase} uppercase letter(s)")
        
        if sum(1 for c in password if c.islower()) < self.min_lowercase:
            violations.append(f"At least {self.min_lowercase} lowercase letter(s)")
        
        if sum(1 for c in password if c.isdigit()) < self.min_digits:
            violations.append(f"At least {self.min_digits} digit(s)")
        
        if sum(1 for c in password if not c.isalnum()) < self.min_special:
            violations.append(f"At least {self.min_special} special character(s) (e.g., !@#$%)")
        
        return violations

    def score_length(self, password):
        """Score based on length."""
        length = len(password)
        if length >= 12:
            return 25
        elif length >= 10:
            return 20
        elif length >= 8:
            return 15
        elif length >= 6:
            return 8
        else:
            return 0

    def score_complexity(self, password):
        """Score based on character types used."""
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        
        types_used = sum([has_upper, has_lower, has_digit, has_special])
        
        if types_used == 4:
            return 30
        elif types_used == 3:
            return 20
        elif types_used == 2:
            return 10
        else:
            return 0

    def score_uniqueness(self, password):
        """Penalize repeated patterns and common substitutions."""
        password_lower = password.lower()
        deductions = 0
        
        # Check against common passwords
        if password_lower in self.common_passwords:
            deductions += 25
        
        # Check for repeated characters (e.g., "aaa", "111")
        repeats = self.repeated_pattern_regex.findall(password)
        if repeats:
            deductions += min(15, len(repeats) * 5)
        
        # Check for sequential patterns
        if self.sequential_regex.search(password_lower):
            deductions += 15
        
        # Check for keyboard patterns (simple)
        keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for row in keyboard_rows:
            if row in password_lower or row[::-1] in password_lower:
                deductions += 10
                break
        
        # Entropy calculation (simplified)
        unique_chars = len(set(password))
        if unique_chars < len(password) * 0.7:  # Less than 70% unique
            deductions += 5
        
        return max(0, 35 - deductions)  # Max 35 points

    def identify_weak_parts(self, password):
        """Explain which parts make the password weak."""
        weak_points = []
        
        # Too short
        if len(password) < 10:
            weak_points.append(f"Password is too short ({len(password)} chars)")
        
        # Missing character types
        if not any(c.isupper() for c in password):
            weak_points.append("No uppercase letters")
        if not any(c.islower() for c in password):
            weak_points.append("No lowercase letters")
        if not any(c.isdigit() for c in password):
            weak_points.append("No digits")
        if not any(not c.isalnum() for c in password):
            weak_points.append("No special characters")
        
        # Repeated patterns
        for match in self.repeated_pattern_regex.finditer(password):
            weak_points.append(f"Repeated character '{match.group()[0]}' appears {len(match.group())} times in a row")
        
        # Common substitutions
        password_lower = password.lower()
        for original, sub in self.common_substitutions.items():
            if sub in password_lower:
                weak_points.append(f"Uses common substitution '{sub}' for '{original}'")
        
        # Sequential patterns
        if self.sequential_regex.search(password_lower):
            weak_points.append("Contains easy-to-guess sequential pattern (e.g., 'abc', '123')")
        
        return weak_points[:5]  # Return top 5 issues

    def generate_recommendations(self, password, violations, weak_parts):
        """Provide actionable suggestions to improve password."""
        recommendations = []
        
        if violations:
            recommendations.append("Fix policy violations:")
            for v in violations[:3]:
                recommendations.append(f"  • {v}")
        
        if any("short" in wp for wp in weak_parts):
            recommendations.append("  • Make password at least 12 characters long")
        
        if any("uppercase" in wp for wp in weak_parts):
            recommendations.append("  • Add uppercase letters (A-Z)")
        if any("lowercase" in wp for wp in weak_parts):
            recommendations.append("  • Add lowercase letters (a-z)")
        if any("digits" in wp for wp in weak_parts):
            recommendations.append("  • Add numbers (0-9)")
        if any("special" in wp for wp in weak_parts):
            recommendations.append("  • Add special characters (!@#$%^&*)")
        
        if any("Repeated" in wp for wp in weak_parts):
            recommendations.append("  • Avoid repeating the same character multiple times")
        
        if any("substitution" in wp for wp in weak_parts):
            recommendations.append("  • Avoid common letter substitutions (e.g., '@' for 'a')")
        
        if any("sequential" in wp for wp in weak_parts):
            recommendations.append("  • Avoid sequential patterns like 'abc' or '123'")
        
        if password.lower() in self.common_passwords:
            recommendations.append("  • Don't use common or easily guessable passwords")
        
        if not recommendations:
            recommendations.append("✓ Password is strong! Consider using a passphrase with 4+ random words.")
        
        return recommendations

    def analyze(self, password):
        """Main analysis function."""
        violations = self.check_policy_violations(password)
        weak_parts = self.identify_weak_parts(password)
        
        # Calculate total score (0-100)
        length_score = self.score_length(password)
        complexity_score = self.score_complexity(password)
        uniqueness_score = self.score_uniqueness(password)
        
        total_score = length_score + complexity_score + uniqueness_score
        
        # Determine strength rating
        if total_score >= 80:
            strength = "VERY STRONG"
        elif total_score >= 65:
            strength = "STRONG"
        elif total_score >= 45:
            strength = "MODERATE"
        elif total_score >= 25:
            strength = "WEAK"
        else:
            strength = "VERY WEAK"
        
        recommendations = self.generate_recommendations(password, violations, weak_parts)
        
        return {
            "password": password,
            "strength": strength,
            "score": total_score,
            "violations": violations,
            "weak_parts": weak_parts,
            "recommendations": recommendations
        }

def main():
    print("=" * 60)
    print("   CREDENTIAL RISK ANALYZER & PASSWORD POLICY ENGINE")
    print("=" * 60)
    
    while True:
        print("\nEnter a password to analyze (or 'quit' to exit):")
        password = input("> ")
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not password:
            print("Please enter a password.")
            continue
        
        analyzer = CredentialRiskAnalyzer()
        result = analyzer.analyze(password)
        
        # Display results
        print("\n" + "=" * 60)
        print(f"Password: {'*' * len(result['password'])}")
        print(f"Strength: {result['strength']} (Score: {result['score']}/100)")
        print("=" * 60)
        
        if result['violations']:
            print("\n❌ POLICY VIOLATIONS:")
            for v in result['violations']:
                print(f"  • {v}")
        else:
            print("\n✓ All policy requirements met!")
        
        if result['weak_parts']:
            print("\n⚠️  WEAK POINTS IDENTIFIED:")
            for wp in result['weak_parts']:
                print(f"  • {wp}")
        
        print("\n💡 RECOMMENDATIONS:")
        for rec in result['recommendations']:
            print(f"  {rec}")
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    main()