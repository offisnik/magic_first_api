from pydantic import BaseModel, Field


class CheckParamsLimits(BaseModel):
    max_resource_size: int
    max_resources_per_type: int
    ttl: str


class CheckParamsAll(BaseModel):
    bearer_token: str
    is_authenticated: bool
    limits: CheckParamsLimits
    session_id: str
    storage: str
    user_id: int


class CheckParamsNoToken(BaseModel):
    error: str = Field(pattern="Authorization required")
    example: str = Field(pattern="Authorization: Bearer sandbox_xxx...")
    message: str = Field(pattern="Use Bearer token in Authorization header or access via web interface")
