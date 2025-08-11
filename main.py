from converter import convert_temperature

def author_info():
    info = {
        "Author": "Wanvisa Phumam",
        "YouTube": "Just Myeed",
        "Telegram": "@JustMyeed",
        "GitHub": "https://github.com/JustMyeed"
    }

    print("-" * 40)
    for key, value in info.items():
        print(f"{key:<8}: {value}")
    print("-" * 40)

def get_abbreviations():
    return ["C", "F", "K", "RK", "RM"]

def temperature_info():
    info = {
        "[C]": "Celsius",
        "[F]": "Fahrenheit",
        "[K]": "Kelvin",
        "[RK]": "Rankine",
        "[RM]": "Reaumur"
    }

    print("🌡 Welcome to Temperature Converter 🌡")
    for key, value in info.items():
        print(f"{key:<4} {value}")

def input_temperature():
    print("-" * 40)
    print("Select the unit you want to convert (Ex. C)")

    valid_units = get_abbreviations()

    while True:
        from_unit = input(">> ").upper()
        if from_unit in valid_units:
            break
        else:
            print("❌ Invalid unit. Please try again.")

    print(f"Enter the number you want to convert (Ex. 36)")
    while True:
        value = input(">> ")
        try:
            value = float(value)
            break
        except ValueError:
            print("❌ Invalid value. Please enter a number.")

    print("Select the unit you want to convert (Ex. C)")
    while True:
        to_unit = input(">> ").upper()
        if to_unit in valid_units:
            break
        else:
            print("❌ Invalid unit. Please try again.")

    try:
        result = convert_temperature(value, from_unit, to_unit)
        print(f"\n✅ Result: {value} {from_unit} = {result:.2f} {to_unit}")
    except ValueError as e:
        print(f"❌ Error: {e}")


def main():
    author_info()
    temperature_info()
    input_temperature()



if __name__ == "__main__":
    main()