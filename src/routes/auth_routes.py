from fastapi import APIRouter, Body, Header


router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(email: str = Body(), password: str = Body()):
    pass


@router.post('/logout')
def logout(authorization: str = Header()):
    pass


@router.post('/refresh')
def refresh(authorization: str = Header()):
    pass
