"""Small FastAPI application for generating SHA-256 checksum tokens."""

import hashlib

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


class TextInput(BaseModel):
    """Request body containing the text that should be checksummed."""

    text: str


def generate(text: str) -> str:
    """Return the SHA-256 hexadecimal checksum for ``text``.

    UTF-8 encoding makes the conversion from Python text to bytes explicit and
    deterministic before the cryptographic hash is calculated.
    """

    return hashlib.sha256(text.encode("utf-8")).hexdigest()


app = FastAPI(
    title="Checksum Generator",
    description="A small API that generates SHA-256 checksum tokens.",
)


@app.get("/", response_class=HTMLResponse)
async def home() -> str:
    """Render the welcome page shown at the application's root URL."""

    # Keep the landing page dependency-free while providing valid, readable HTML.
    return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checksum Generator</title>
  </head>
  <body>
    <main>
      <h1>Welcome, Gujju Mukesh Rao</h1>
      <p>Use the <code>/generate</code> endpoint to create a SHA-256 checksum.</p>
    </main>
  </body>
</html>"""


@app.post("/generate")
async def generate_checksum(payload: TextInput) -> dict[str, str]:
    """Generate a checksum and return it with the submitted text.

    FastAPI validates the incoming JSON against ``TextInput`` before this
    function runs, so the route can focus on generating and formatting the
    response.
    """

    checksum = generate(payload.text)
    return {
        "message": "Welcome, Gujju Mukesh",
        "text": payload.text,
        "checksum": checksum,
    }


if __name__ == "__main__":
    # Allow the module to be started directly with: python main.py
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)