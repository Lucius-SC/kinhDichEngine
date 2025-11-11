import random
from core.hexagram import HEXAGRAMS
from core.interpreter import giai_nghia

def rut_que():
    """Rút ngẫu nhiên 1 quẻ"""
    return random.choice(HEXAGRAMS)

def hien_thi_quai(que):
    print(f"Quẻ: {que['name']} {que['upper']}{que['lower']}")
    print(f"Ý nghĩa: {que['meaning']}")
    print(f"Giải nghĩa sâu: {giai_nghia(que['name'])}")
