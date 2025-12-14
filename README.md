# Product Review Analyzer
Product Review Analyzer adalah aplikasi **AI-powered Full Stack** yang digunakan untuk menganalisis review produk berbasis teks dengan melakukan:
- Analisis sentimen menggunakan **Hugging Face**
- Ekstraksi key points menggunakan **Google Gemini**
- Menampilkan hasil analisis di **React Frontend**
- Menyimpan data ke **PostgreSQL Database**

---

## Fitur Utama

- Input review produk (text-based)
- Sentiment analysis (positive / negative / neutral)
- Key points extraction (ringkasan poin penting)
- Menampilkan hasil analisis secara real-time
- Menyimpan histori review ke database
- Error handling & loading state
- REST API terpisah (backend & frontend)

---

## Tech Stack

### Backend
- Python
- FastAPI
- Hugging Face Transformers
- Gemini API
- SQLAlchemy
- PostgreSQL

### Frontend
- React.js
- Axios

---

## Arsitektur Sistem
Aplikasi ini menggunakan **arsitektur client-server** dengan pendekatan **RESTful API** dan integrasi layanan AI eksternal.

## Struktur Folder
product-review-analyzer/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── services/
│   │   │   ├── sentiment.py
│   │   │   └── keypoints.py
│   │   └── routers/
│   │       └── reviews.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/api.js
│   │   └── App.jsx
│   └── package.json
│
├── README.md

---

## Setup dan Cara menjalankannya

### Backend Setup
1. Clone Repository
```bash
git clone https://github.com/dvnkrtk/PAW-Tugas-3.git 
cd product-review-analyzer/backend

2. Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3. Install Dependencies
```bash
pip install -r requirements.txt

4. Environment Variables
```bash
DATABASE_URL=postgresql://user:123@localhost:5432/review_db
HUGGINGFACE_API_KEY=your_huggingface_api_key
GEMINI_API_KEY=your_gemini_api_key

5. Run Backend
```bash
uvicorn app.main:app --reload

---

### Frontend Setup
```bash
cd ../frontend
npm install
npm run dev

---

## API Endpoints

### 🔹 POST /api/analyze-review
Menganalisis review baru.

**Request Body**
```json
{
  "review": "Produk ini sangat bagus dan berkualitas"
}

**Response**
```json
{
  "sentiment": "positive",
  "key_points": ["kualitas bagus", "produk memuaskan"],
  "created_at": "2025-01-01T10:00:00"
}

### 🔹 GET /api/reviews
Mengambil seluruh data
```json
[
  {
    "id": 1,
    "review": "Produk ini sangat bagus",
    "sentiment": "positive",
    "key_points": ["kualitas bagus"],
    "created_at": "2025-01-01T10:00:00"
  }
]

