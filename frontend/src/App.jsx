import { useEffect, useState } from "react";
import { analyzeReview, getReviews, deleteAllReviews } from "./api";

function App() {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [reviews, setReviews] = useState([]);

  const loadReviews = async () => {
    const data = await getReviews();
    setReviews(data);
  };

  useEffect(() => {
    loadReviews();
  }, []);

  const handleAnalyze = async () => {
    if (!text.trim()) {
      alert("Review tidak boleh kosong");
      return;
    }

    setLoading(true);
    try {
      await analyzeReview(text);
      setText("");
      await loadReviews();
    } catch (err) {
      alert("Gagal menganalisis review");
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async () => {
    if (!confirm("Hapus semua riwayat?")) return;
    await deleteAllReviews();
    setReviews([]);
  };

  return (
    <div className="page">
      <h1 className="title">Product Review Analyzer</h1>

      <div className="layout">
        {/* FORM ANALISIS */}
        <div className="card">
          <h2>Analyze Review</h2>

          <textarea
            placeholder="Tulis review produk..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          />

          <button onClick={handleAnalyze} disabled={loading}>
            {loading ? "Analyzing..." : "Analyze Review"}
          </button>
        </div>

        {/* RIWAYAT */}
        <div className="card">
          <div className="history-header">
            <h2>Riwayat Analisis</h2>
            <button className="danger" onClick={handleDelete}>
              Hapus
            </button>
          </div>

          {reviews.length === 0 && <p>Belum ada data</p>}

          {reviews.map((r) => (
            <div key={r.id} className={`history-item ${r.sentiment}`}>
              <strong>{r.sentiment.toUpperCase()}</strong>
              <p>{r.review_text}</p>
              <pre>{r.key_points}</pre>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
