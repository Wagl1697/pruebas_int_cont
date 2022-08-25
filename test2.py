import pytest
import prog1

def comprobar_ingreso_string():
	assert type(prog1.p1.retornar_nombre()) == "str"
def comprobar_ingreso_int():
	assert type(prog1.p1.retornar_edad()) == "int"

