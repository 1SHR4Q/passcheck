from main import *

def weak():
    assert strengthCheck("abc") == "weak."

def medium():
    assert strengthCheck("Abc1!") == "ok?"

def strong():
    assert strengthCheck("Abcccc!1") == "strong!"