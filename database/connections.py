from redis_om.connections import get_redis_connection
import aioredis

redis_db = get_redis_connection(
        host="localhost",
        port=6379,
        password=None,
        decode_responses=True
    )

redis_cache_db = aioredis.from_url(
        url="redis://localhost:6379", 
        encoding="utf8", 
        decode_responses=True
    )

