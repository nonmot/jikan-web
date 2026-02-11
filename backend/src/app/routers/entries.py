from fastapi import APIRouter, HTTPException

from app.schemas.entry import EntryDTO
from app.services.entry_service import running_entry

router = APIRouter()


@router.get("/entries/running")
def get_running_entry() -> EntryDTO:
    try:
        entry = running_entry()
        return entry
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}") from e
