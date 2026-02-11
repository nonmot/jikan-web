from datetime import datetime

from pydantic import BaseModel


class ProjectDTO(BaseModel):
    id: int
    name: str
    description: str | None = None
    archived: bool


class EntryDTO(BaseModel):
    id: int
    title: str | None = None
    description: str | None = None
    start_at: datetime
    end_at: datetime | None = None
