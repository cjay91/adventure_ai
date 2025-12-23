import uuid
from typing import Optional
from fastapi import APIRouter, Depends, Cookie, HTTPException

from sqlalchemy.orm import Session

from db.database import get_db, SessionLocal
from models.story import Story, StoryNode
from models.job import StoryJob
from schemas.story import (
    CreateStoryRequest,
    CompleteStoryResponse,          
    CompleteStoryNodeResponse)
from schemas.job import StoryJobCreate, StoryJobResponse


router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

@router.get("/{job_id}", response_model=StoryJobResponse)
def get_story_job(job_id: str, db: Session = Depends(get_db)):
    job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job