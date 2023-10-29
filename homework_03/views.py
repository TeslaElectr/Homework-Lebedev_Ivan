from fastapi import APIRouter


router = APIRouter()

@router.get('/')
def helloworld():
    return {'message': 'Hello World'}

@router.get("/ping")
def ping():
    return {"message": "pong"}
    
