def get_property(property):
    """
    Return a property in the .db.properties file
    Args:
        property: name of the property. E.g. db_user
    """
    with open(".db.properties") as f:
        line = f.readline()
        while (line):
            if (property in line):
                p = line.split(":")[1]
                return p.strip()
            line = f.readline()
    return None

DB_USER = get_property("db_user")
DB_PWD = get_property("db_pwd")
DB_HOST = get_property("db_host")
DB_NAME = get_property("db_name")
