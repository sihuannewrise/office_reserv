from fastapi import Depends, FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAccessTokenInfo, FiefAsync
from fief_client.integrations.fastapi import FiefAuth

fief = FiefAsync(
    "https://fief.knh.cloud",
    "3wI6H-nVkVZLc2h0OJFl91zV_RoyGMfUqjYR-z3uA-M",
    "lUVKMrNdudjh3XCSnUeaJaJy3pH-PacGIcC8yUamL4U",
)

scheme = OAuth2AuthorizationCodeBearer(
    "https://fief.knh.cloud/authorize",
    "https://fief.knh.cloud/api/token",
    scopes={"openid": "openid", "offline_access": "offline_access"},
    auto_error=False,
)

auth = FiefAuth(fief, scheme)

app = FastAPI()


@app.get("/user")
async def get_user(
    access_token_info: FiefAccessTokenInfo = Depends(auth.authenticated()),
):
    return access_token_info
