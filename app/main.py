from fastapi import Depends, FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAccessTokenInfo, FiefAsync
from fief_client.integrations.fastapi import FiefAuth

fief = FiefAsync(
    "https://fief.knh.cloud",
    "ArGeq7v90-4rB8SzT3qMZN2ysu4JZzBYLZn8Pw02jlU",
    "jt_lw8wUwaKY2Yx8rO42G1aV4pCsyc67Ucu16nf6Qd0",
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
