import re
import getpass

def check_password_strength(password):
    """
    Analyzes password strength based on security criteria
    Returns: 'Strong', 'Medium', or 'Weak'
    """
    score = 0
    
    # Criteria checks
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    
    # Strength assessment
    if score >= 4:
        return "✅ Strong"
    elif score >= 2:
        return "⚠️ Medium"
    else:
        return "❌ Weak"

def main():
    print("=== 🔒 Password Strength Checker ===")
    
    while True:
        password = getpass.getpass("Enter password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            break
            
        strength = check_password_strength(password)
        print(f"Password Strength: {strength}\n")

if __name__ == "__main__":
    main()
