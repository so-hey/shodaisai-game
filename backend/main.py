from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Landmark(BaseModel):
    x: float
    y: float
    z: float


class LandmarksData(BaseModel):
    landmarks: list[Landmark]


@app.post("/api/mediapipe")
def predict(landmarks: LandmarksData = []):
    print(landmarks)
    return {"isOk": random.random() < 0.01}
