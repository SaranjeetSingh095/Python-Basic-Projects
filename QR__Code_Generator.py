import qrcode

try:
    data = input("Enter Text or URL: ").strip()
    if not data:
        raise ValueError("Input cannot be empty!")

    img = qrcode.make(data)
    img.save("QR_Code.png")
    print("QR Code Created Successfully!")

except Exception as e:
    print("Error:", e)
