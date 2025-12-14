from pydantic import BaseModel

class ReviewCreate(BaseModel):
    review_text: str

class ReviewResponse(BaseModel):
    id: int
    review_text: str
    sentiment: str
    key_points: str

    class Config:
        orm_mode = True
