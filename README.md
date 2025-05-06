# FastAPI PDF Upload

This project is a simple FastAPI application that allows users to upload PDF files and stores them on the server.

## Project Structure

```
fastapi-pdf-upload
├── src
│   ├── main.py          # Entry point of the FastAPI application
│   ├── routes
│   │   └── upload.py    # Endpoint for uploading PDF files
│   ├── services
│   │   └── file_storage.py # Logic for saving uploaded PDF files
│   └── models
│       └── __init__.py  # Placeholder for future data models or schemas
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd fastapi-pdf-upload
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**
   ```bash
   uvicorn src.main:app --reload
   ```

2. **Upload a PDF file:**
   Send a POST request to the `/upload` endpoint with the PDF file included in the form data.

## License

This project is licensed under the MIT License.