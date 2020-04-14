

from descriptors import TypeChecked

from jinja2 import Template


init_template = Template("""
def __init__(
    self, 
  {% for f in fields %} 
    {{ f }}, 
  {% endfor %}
):
  {% for f in fields %} 
    self.{{f}} = {{f}} 
  {% endfor %}""")



class TemplatedAutoInit(type):
    def __new__(meta, name, bases, attrs):
        fields = [
            key for key, value in attrs.items() 
            if isinstance(value, TypeChecked)
        ]
        code = init_template.render(fields=fields)
        print(code)
        exec(code, globals(), attrs)
        return super().__new__(meta, name, bases, attrs)



class CodeGeneratedPerson(metaclass=TemplatedAutoInit):
    name = TypeChecked(str)
    age = TypeChecked(int)




p = CodeGeneratedPerson("Max", 22)

print(p.name)
print(p.age)



