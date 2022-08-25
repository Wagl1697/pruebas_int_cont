import pytest
import prog1

def comprobar_ingreso_string():
	assert isistance(prog1.p1.retornar_nombre(),"str") == True
def comprobar_ingreso_int():
	assert isistance(prog1.p1.retornar_edad(),"int") == False

