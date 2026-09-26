## Description
Introduces a FastAPI microservice designed to generate deterministic SHA-256 cryptographic checksums for text inputs. 

Key implementation details:
- **`GET /`**: Renders an HTML landing page welcoming users and directing them to the API endpoint.
- **`POST /generate`**: Accepts a JSON payload containing `text`, validates it using Pydantic (`TextInput`), and returns the input alongside its SHA-256 hexadecimal hash.
- **`generate()` helper**: Encodes text explicitly to UTF-8 before computing the hash via Python's `hashlib`.
- Integrated `uvicorn` entry point to allow starting the app directly via `python main.py`.

## Related Issue / Ticket
Fixes # (issue_number)

## Type of Change
- [x] ✨ New feature (non-breaking change which adds functionality)
- [ ] 🐛 Bug fix
- [ ] 📝 Documentation update
- [ ] ⚙️ Refactoring / Performance improvement

## How Has This Been Tested?
- [x] Tested `GET /` locally via browser (`http://127.0.0.1:8000/`) to verify HTML rendering.
- [x] Tested `POST /generate` via Swagger UI (`http://127.0.0.1:8000/docs`) with sample JSON payloads:
  ```json
  {
    "text": "hello"
  }
