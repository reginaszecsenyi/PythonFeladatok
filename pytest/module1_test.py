import pytest


from module1 import total

def test_total_many_items():                #mindig test-el kell kezdődnie, csak azt találja meg a pytest
    assert total([1, 2, 3]) == 6            #bal oldal:kapott érték, jobb oldal:elvárt eredmény


