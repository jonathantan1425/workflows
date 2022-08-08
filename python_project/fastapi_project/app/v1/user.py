from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", status_code=200)
def get_users() -> dict:
    return {"msg": "Hello World"}
