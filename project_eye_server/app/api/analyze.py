from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_hello_world():
    return {"message": "hello world"}