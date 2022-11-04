from time import sleep
from fastapi import APIRouter
from schemas.bio_schema import BioSch
from schemas.user_schema import UserSch
from services.user_service import UserService
from database.user_model import User
from fastapi_cache.decorator import cache as redis_cache

router = APIRouter(prefix='/user', tags=['User Crud'])
user_services = UserService(model=User)

@router.get('/all')
@redis_cache(expire=10)
async def get_all_users(limit: int = 10):
    users, error = user_services.get_all(limit)
    if error:
        return error
    return users

@router.get('/get/{pk}')
@redis_cache(expire=10)
async def get_user(pk: str):
    user, error = user_services.get_by_pk(pk)
    if error or not user:
        return "User not found"  
    return user

@router.post('/create')
async def create_user(user: UserSch):
    user, errors = user_services.create_new(user)
    if errors:
        return errors
    return user

@router.put('/update-bio/{pk}')
async def update_user_bio(pk: str, bio: BioSch):
    user, errors = user_services.update_bio(pk, bio)
    if errors:
        return errors
    return user

@router.delete('/delete/{pk}')
async def delete_user(pk: str):
    user, errors = user_services.delete_by_pk(pk)
    if errors:
        return errors
    return user

@router.get('/search/{search}')
@redis_cache(expire=3)
async def delete_user(search: str):
    user, errors = user_services.search(search)
    if errors:
        return errors
    return user