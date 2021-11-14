from datetime import date

def get_property(property):
    """
    Return a property in the properties file
    Args:
        property: name of the property. E.g. db_user
    """
    with open(".properties") as f:
        line = f.readline()
        while (line):
            if (property in line):
                p = line.split(":")[1]
                return p.strip()
            line = f.readline()
    return None

def str2date(str_date, sep="-"):
    year, month, day = str_date.split(sep)
    return date(int(year), int(month), int(day))
