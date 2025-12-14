from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Review
from ..schemas import ReviewCreate
from ..services.sentiment import analyze_sentiment
from ..services.keypoints import extract_key_points

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ===============================
# POST - ANALYZE & SAVE REVIEW
# ===============================
@router.post("/analyze-review")
def analyze_review(data: ReviewCreate, db: Session = Depends(get_db)):
    sentiment = analyze_sentiment(data.review_text)
    key_points = extract_key_points(data.review_text)

    review = Review(
        review_text=data.review_text,
        sentiment=sentiment,
        key_points=key_points
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    return review

# ===============================
# GET - ALL REVIEWS (HISTORY)
# ===============================
@router.get("/reviews")
def get_reviews(db: Session = Depends(get_db)):
    return db.query(Review).order_by(Review.id.desc()).all()

# ===============================
# DELETE - DELETE ALL REVIEWS
# ===============================
@router.delete("/reviews")
def delete_all_reviews(db: Session = Depends(get_db)):
    db.query(Review).delete()
    db.commit()
    return {"message": "Semua riwayat review berhasil dihapus"}
