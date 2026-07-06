print('''
===========================================
      🔐 Welcome to Text Encryptor 🔐
===========================================

This program can:
✅ Encrypt your text
✅ Decrypt encrypted text

Supported:
• A-Z
• a-z
• 0-9
• Special Characters

-------------------------------------------
1. Encrypt Text
2. Decrypt Text
3. Exit
-------------------------------------------
''')


encrypt = {

    # ==========================
    # Uppercase (A-Z)
    # ==========================
    "A": "α", "B": "β", "C": "γ", "D": "δ", "E": "ε",
    "F": "ζ", "G": "η", "H": "θ", "I": "ι", "J": "κ",
    "K": "λ", "L": "μ", "M": "ν", "N": "ξ", "O": "ο",
    "P": "π", "Q": "ρ", "R": "σ", "S": "τ", "T": "υ",
    "U": "φ", "V": "χ", "W": "ψ", "X": "ω", "Y": "Ω",
    "Z": "Δ",

    # ==========================
    # Lowercase (a-z)
    # ==========================
    "a": "①", "b": "②", "c": "③", "d": "④", "e": "⑤",
    "f": "⑥", "g": "⑦", "h": "⑧", "i": "⑨", "j": "⑩",
    "k": "⑪", "l": "⑫", "m": "⑬", "n": "⑭", "o": "⑮",
    "p": "⑯", "q": "⑰", "r": "⑱", "s": "⑲", "t": "⑳",
    "u": "ⓐ", "v": "ⓑ", "w": "ⓒ", "x": "ⓓ", "y": "ⓔ",
    "z": "ⓕ",

    # ==========================
    # Numbers (0-9)
    # ==========================
    "0": "🄀",
    "1": "🄁",
    "2": "🄂",
    "3": "🄃",
    "4": "🄄",
    "5": "🄅",
    "6": "🄆",
    "7": "🄇",
    "8": "🄈",
    "9": "🄉",

    # ==========================
    # Space & Symbols
    # ==========================
    " ": "□",
    ".": "•",
    ",": "‚",
    "!": "¡",
    "?": "¿",
    ":": "∶",
    ";": "∷",
    "'": "′",
    '"': "″",
    "(": "❨",
    ")": "❩",
    "[": "❲",
    "]": "❳",
    "{": "❴",
    "}": "❵",
    "-": "−",
    "_": "‗",
    "+": "⊕",
    "=": "≋",
    "/": "∕",
    "\\": "⧵",
    "*": "✶",
    "&": "⅋",
    "%": "‰",
    "@": "✉",
    "#": "♯",
    "$": "¤"
}


decrypt = {value: key for key, value in encrypt.items()}

while True:
    try:

        user = int(input("Enter Your Choice >> "))



        if user == 1:
            text = input("Enter Your Text: ")

            encrypted_text = ""

            for char in text:
                encrypted_text += encrypt.get(char, char)
            print(f"Your Encrypted Text -> {encrypted_text}")




        elif user == 2:
            text2 = input("Enter Your Encrypted Text: ")

            decrypted_text = ""

            for char in text2:
                decrypted_text += decrypt.get(char, char)

            print(f"Your Decrypted Text -> {decrypted_text}")

        elif user == 3:
            print("👋 Goodbye!")
            break
    except:
        print("❌ Invalid Choice!")
