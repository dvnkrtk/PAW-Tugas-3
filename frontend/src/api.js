const BASE_URL = "http://localhost:8000/api";

export const analyzeReview = async (text) => {
  const res = await fetch(`${BASE_URL}/analyze-review`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ review_text: text }),
  });
  return res.json();
};

export const getReviews = async () => {
  const res = await fetch(`${BASE_URL}/reviews`);
  return res.json();
};

export const deleteAllReviews = async () => {
  const res = await fetch(`${BASE_URL}/reviews`, {
    method: "DELETE",
  });
  return res.json();
};
