import qrcode
from PIL import ImageColor
import sys
from datetime import datetime

def is_valid_color(color):
    """Check if a color name or hex value is valid."""
    try:
        ImageColor.getrgb(color)
        return True
    except ValueError:
        return False


def get_non_empty_input(prompt):
    """Keep asking until user enters non-empty input."""
    while True:
        try:
            data = input(prompt).strip()
            if not data:
                raise ValueError("Input cannot be empty.")
            return data
        except ValueError as e:
            print(f"❌ {e}")


def get_color_input(prompt, default):
    """Validate color input with default fallback."""
    while True:
        color = input(prompt).strip()
        if not color:
            return default
        if is_valid_color(color):
            return color
        else:
            print("❌ Invalid color. Try again (e.g., black, red, #FF5733).")


def get_error_correction():
    """Let user choose error correction level."""
    levels = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H
    }

    while True:
        choice = input("Choose error correction (L/M/Q/H) [default M]: ").upper().strip()
        if not choice:
            return levels["M"]
        if choice in levels:
            return levels[choice]
        print("❌ Invalid choice. Please enter L, M, Q, or H.")


# Main Program Logic


def generate_qr():
    print("\n=== QR Code Generator ===\n")

    #  Get Inputs
    data = get_non_empty_input("Enter text or URL: ")
    fill_color = get_color_input("Enter QR color (default black): ", "black")
    back_color = get_color_input("Enter background color (default white): ", "white")
    error_level = get_error_correction()

    # Generate QR
    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=error_level,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # 3️⃣ Safe Filename with Timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.png"

        img.save(filename)
        img.show()

        print(f"\n✅ QR Code generated successfully!")
        print(f"📁 Saved as: {filename}\n")

    except Exception as e:
        print(f"\n❌ Unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        generate_qr()
    except KeyboardInterrupt:
        print("\n⚠ Program interrupted by user. Exiting safely.")
        sys.exit(0)
