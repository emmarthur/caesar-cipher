"""
FastAPI app — Caesar Cipher.

Endpoints:
  GET  /                 HTML UI
  POST /api/transform    Encrypt or decrypt text

Run: uvicorn main:app --reload --port 3011
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

_DEMO_ROOT = Path(__file__).resolve().parent.parent
if str(_DEMO_ROOT) not in sys.path:
    sys.path.insert(0, str(_DEMO_ROOT))

from caesar_core import MAX_SHIFT, MIN_SHIFT, caesar_transform  # noqa: E402

app = FastAPI(title="Caesar Cipher")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))
app.mount("/static", StaticFiles(directory=str(Path(__file__).parent / "static")), name="static")


class TransformRequest(BaseModel):
    text: str = Field(..., max_length=10_000)
    shift: int = Field(..., ge=MIN_SHIFT, le=MAX_SHIFT)
    mode: Literal["encrypt", "decrypt"]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "index.html",
        {"min_shift": MIN_SHIFT, "max_shift": MAX_SHIFT},
    )


@app.post("/api/transform")
async def api_transform(body: TransformRequest) -> JSONResponse:
    try:
        result = caesar_transform(body.text, body.shift, body.mode)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return JSONResponse({"result": result, "shift": body.shift, "mode": body.mode})
