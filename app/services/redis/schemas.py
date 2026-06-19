from pydantic import BaseModel

class UserRedis(BaseModel):
    name: str

class UserRedisResponse(BaseModel):
    name: str | None