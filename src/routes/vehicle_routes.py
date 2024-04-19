from fastapi import APIRouter


router = APIRouter(tags=['Vehicle', 'Users'])


@router.get('user/{user_id}/vehicles')
def get_user_vehicles():
    ...


@router.get('vehicles')
def get_vehicles():
    ...


@router.post('vehicles')
def add_vehicle():
    ...

@router.get('vehicles/{vehicle_id}')
def get_vehicle():
    ...
