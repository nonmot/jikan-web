from fastapi import APIRouter, HTTPException, Response

from app.schemas.entry import EntryDTO
from app.services.entry_service import running_entry

router = APIRouter()


@router.get("/entries/running", response_model=EntryDTO)
def get_running_entry():
    try:
        entry = running_entry()
        if entry is None:
            return Response(status_code=204)
        return entry
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}") from e
