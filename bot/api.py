import dataclasses

import structlog

from blacksheep import Request
from blacksheep.server.routing import Router
from teleapp_auth import get_secret_key, parse_webapp_data, validate_webapp_data

from bot.config import BOT_TOKEN


router = Router()
secret_key = get_secret_key(BOT_TOKEN)
logger = structlog.get_logger()


@dataclasses.dataclass
class AuthResponse:
    status: bool
    user: dict


@router.post("/api/check_data")
async def check_data(request: Request) -> bool:
    request_json = await request.json()
    auth_data = request_json.get("auth_data")
    webapp_data = parse_webapp_data(auth_data)

    logger.info("Checking data", user=webapp_data.user)

    return AuthResponse(
        status=validate_webapp_data(webapp_data, secret_key),
        user=webapp_data.user.to_dict() if webapp_data.user else {},
    )
