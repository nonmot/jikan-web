from datetime import UTC

from jikan.core.entry import get_running_entry

from app.schemas.entry import EntryDTO, ProjectDTO, TagDTO


def running_entry() -> EntryDTO | None:
    entries = get_running_entry()

    if len(entries) > 1:
        raise RuntimeError("Multiple entries running")
    elif len(entries) == 0:
        return

    entry = entries[0]

    project = entry.project
    project_dto = (
        ProjectDTO(
            id=project.id,
            name=project.name,
            archived=project.archived,
        )
        if project is not None
        else None
    )

    tags = entry.tags
    tags_dto = [
        TagDTO(
            id=tag.id,
            name=tag.name,
        )
        for tag in tags
    ]

    return EntryDTO(
        id=entry.id,
        title=entry.title,
        description=entry.description,
        start_at=entry.start_at.replace(tzinfo=UTC).isoformat().replace("+00:00", "Z"),
        end_at=entry.end_at.astimezone(UTC).isoformat().replace("+00:00", "Z") if entry.end_at else None,
        project=project_dto,
        tags=tags_dto,
    )
