def generate_init(fields):
    fs = [field.strip() for field in fields.split(",")]
    first_line = "    def __init__(self, %s):" % (", ".join(fs))
    print(first_line)
    for field in fs:
        field_line = "        self.%s = %s" % (field, field)
        print(field_line)
