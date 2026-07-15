import re

# List of common phishing keywords
phishing_keywords = [
    "urgent",
    "verify",
    "password",
    "bank",
    "account",
    "click here",
    "login",
    "winner",
    "congratulations",
    "free",
    "gift",
    "limited time",
    "update",
    "confirm",
    "security alert"
]

print("========== Phishing Awareness Analyzer ==========")

message = input("\nPaste the email/message:\n\n")

red_flags = []

# Check phishing keywords
for keyword in phishing_keywords:
    if keyword.lower() in message.lower():
        red_flags.append(f"Keyword found: {keyword}")

# Find URLs
urls = re.findall(r'https?://\S+|www\.\S+', message)

if urls:
    for url in urls:
        red_flags.append(f"Suspicious Link: {url}")

print("\n========== Analysis Result ==========")

if red_flags:
    print("\n⚠ Possible Phishing Message Detected!\n")

    print("Red Flags Found:")
    for flag in red_flags:
        print("-", flag)

    print("\nWhy is this unsafe?")
    print("- It contains phishing keywords.")
    print("- It may try to steal personal information.")
    print("- Suspicious links can redirect to fake websites.")

else:
    print("\nNo obvious phishing indicators were found.")