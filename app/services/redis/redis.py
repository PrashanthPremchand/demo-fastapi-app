import redis
from app.core.config import settings

r = redis.Redis(
    host=settings.REDIS_HOST,
    port=int(settings.REDIS_PORT),
    db=0
)