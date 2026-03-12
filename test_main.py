from main import *

def test_weak():
    assert strengthCheck("abc") == "weak."

def test_medium():
    assert strengthCheck("Abc1!") == "ok?"

def test_strong():
    assert strengthCheck("Abcccc!1") == "strong!"