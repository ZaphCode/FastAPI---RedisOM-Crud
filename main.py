from redis_om import Migrator
from fastapi import FastAPI
from routers.user_crud import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from database.connections import redis_cache_db
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache import FastAPICache
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
async def startup():
    FastAPICache.init(RedisBackend(redis_cache_db), prefix="fastapi-cache")
    Migrator().run()

app.include_router(router=user_router)
    
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)