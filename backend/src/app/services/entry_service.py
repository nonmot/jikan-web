from jikan.core.entry import get_running_entry

from app.schemas.entry import EntryDTO


def running_entry() -> EntryDTO:
    entries = get_running_entry()

    if len(entries) > 1:
        raise RuntimeError("Multiple entries running")
    elif len(entries) == 0:
        raise RuntimeError("No entry running")

    entry = entries[0]

    return EntryDTO(
        id=entry.id,
        title=entry.title,
        start_at=entry.start_at,
        end_at=entry.end_at,
    )
