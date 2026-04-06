def convert_units(value, from_unit='meters', to_unit='feet', **kwargs):
    units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'feet': 0.3048,
        'miles': 1609.344,
        'kilograms': 1000,
    }

    units.update(kwargs)

    return value * units[from_unit] / units[to_unit]