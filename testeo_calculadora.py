import calculadora
import pytest

calculadora = calculadora.Calculadora(4,1)
def test1():
	assert calculadora.sumar() == 5
def test2():
	assert calculadora.restar() == 3
def test3():
	assert calculadora.dividir() == 4
