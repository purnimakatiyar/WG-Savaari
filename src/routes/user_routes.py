from fastapi import APIRouter, Body, Header, Path


router = APIRouter(tags=['Users'])


@router.get('/users/{user_id}')
def view_profile(user_id: str = Path(), authorization: str = Header()):
    pass


@router.put('/users/{user_id}')
def update_profile(user_id: str = Path(), username: str = Body(), gender: str = Body(), phone_no: str = Body(), age: int = Body(), authorization: str = Header()):
    pass

@router.put('/change_password')
def change_password(old_password: str = Body(), new_password: str = Body(), authorization: str = Header()):
    pass
