from pydantic import BaseModel


class ProjectDTO(BaseModel):
    id: int | None
    name: str
    description: str | None = None
    archived: bool


class TagDTO(BaseModel):
    id: int | None
    name: str | None = None


class EntryDTO(BaseModel):
    id: int | None
    title: str | None = None
    description: str | None = None
    start_at: str
    end_at: str | None = None
    project: ProjectDTO | None = None
    tags: list[TagDTO] = []
