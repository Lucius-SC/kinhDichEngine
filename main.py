
---

## ⚙️ `main.py`
```python
from core.logic import rut_que, hien_thi_quai

def main():
    print("=== 🔮 RÚT QUẺ KINH DỊCH ===")
    que = rut_que()
    hien_thi_quai(que)

if __name__ == "__main__":
    main()
