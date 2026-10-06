# Phone Calculator

A simple phone-style calculator UI backed by a FastAPI service. The browser sends arithmetic operations to the API, which returns the result as JSON.

## Requirements

- Python 3.9 or later
- `fastapi`
- `uvicorn`

## Run the API

From the project directory, install the dependencies and start the development server:

```bash
python -m pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Run the calculator UI

With the API running, serve `index.html` from the project directory using a separate terminal:

```bash
python -m http.server 5500
```

Open `http://127.0.0.1:5500` in a browser. The UI sends requests to `http://127.0.0.1:8000/calculate` by default.

## API

### `POST /calculate`

Request body:

```json
{
  "x": 12,
  "y": 3,
  "operator": "/"
}
```

Supported operators are `+`, `-`, `*`, and `/`. A successful response contains the result:

```json
{
  "result": 4
}
```

An unsupported operator or division by zero returns HTTP `400` with a `detail` message. Inputs `x` and `y` must be numbers.

## Project files

- `main.py` — FastAPI application and calculation endpoint.
- `index.html` — standalone calculator interface.

The `%` button is present in the interface, but percentage calculations are not currently supported by the API.
