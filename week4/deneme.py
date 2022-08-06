class A:
    def a(self):
        return "Function inside A"


class B:
    def a(self):
        return "Function inside B"


class C:
    pass


class D(C, A, B):
    pass


d = D()
print(d.a())

emp_info = {
    'first_name': 'isim',
    'age': 17,
    'title': 'mudur'
}

"""
def write_json_to_file(json_obj, output_file):
    with open(output_file, 'w') as f:
        f = json.dumps(json_obj)
    return f
"""
