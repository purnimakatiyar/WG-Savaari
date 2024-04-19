from fastapi import APIRouter, Header, Path, Body


router = APIRouter(tags=['Rides'])


@router.get("/rides")
def rides(source: str, destination: str, ride_date_time: str, authorization: str = Header()):
    ...


@router.post("/rides")
def publish_ride(source: str = Body(), destination: str = Body(), ride_date_time: str = Body(), vehicle_id: str = Body(), vaccant_seats: int = Body(), authorization: str = Header()):
    ...

@router.delete("/rides/{ride_id}")
def delete_ride(authorization: str = Header(), ride_id: str = Path()):
    ...
