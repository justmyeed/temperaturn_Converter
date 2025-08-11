def to_celsius(value, from_unit):
    conversions = {
        "celsius": lambda x: x,
        "fahrenheit": lambda x: (x - 32) * 5 / 9,
        "kelvin": lambda x: x - 273.15,
        "rankine": lambda x: (x - 491.67) * 5 / 9,
        "reaumur": lambda x: x * 5 / 4
    }

    func = conversions.get(from_unit.lower())
    if func:
        return func(value)
    else:
        raise ValueError(f"Unsupported from_unit: {from_unit}")

def from_celsius(value, to_unit):
    conversions = {
        "celsius": lambda x: x,
        "fahrenheit": lambda x: x * 9 / 5 + 32,
        "kelvin": lambda x: x + 273.15,
        "rankine": lambda x: (x + 273.15) * 9 / 5,
        "reaumur": lambda x: x * 4 / 5
    }

    func = conversions.get(to_unit.lower())
    if func:
        return func(value)
    else:
        raise ValueError(f"Unsupported to_unit: {to_unit}")

def convert_temperature(value, from_unit, to_unit):
    # แมปชื่อย่อให้ตรงกับ dictionary
    unit_map = {
        "C": "celsius",
        "F": "fahrenheit",
        "K": "kelvin",
        "RK": "rankine",
        "RM": "reaumur"
    }

    from_unit_full = unit_map.get(from_unit)
    to_unit_full = unit_map.get(to_unit)

    if not from_unit_full or not to_unit_full:
        raise ValueError("Invalid unit abbreviation.")

    celsius = to_celsius(value, from_unit_full)
    result = from_celsius(celsius, to_unit_full)
    return result
