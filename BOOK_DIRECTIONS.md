# Book directions — Caesar Cipher

**Catalog #442** · Al Sweigart, *The Big Book of Small Python Projects* — **Caesar Cipher**

- Online chapter: [inventwithpython.com/bigbookpython/project42.html](https://inventwithpython.com/bigbookpython/project42.html)
- Upstream: [caesar.py](https://github.com/asweigart/the-big-book-of-small-python-projects/blob/main/caesar.py)
- Local reference: [`reference/caesar.py`](./reference/caesar.py)
- Shared logic: [`caesar_core.py`](./caesar_core.py)

## What the book asks you to build

Ask encrypt vs decrypt, a key from **1–25**, and a message. Shift each letter; leave non-letters unchanged.

## Web version (`web/` — FastAPI, port **3011**)

- `GET /` — message field, shift slider, encrypt/decrypt actions
- `POST /api/transform` — JSON `{ text, shift, mode }` → `{ result }`

Run from `web/`:

```text
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 3011
```
