from fief_client import Fief

fief = Fief(
    "https://fief.knh.cloud",
    "ArGeq7v90-4rB8SzT3qMZN2ysu4JZzBYLZn8Pw02jlU",
    "jt_lw8wUwaKY2Yx8rO42G1aV4pCsyc67Ucu16nf6Qd0",
)

redirect_url = "http://localhost:8000/callback"

auth_url = fief.auth_url(redirect_url, scope=["openid"])
print(f"Open this URL in your browser: {auth_url}")

code = input("Paste the callback code: ")

tokens, userinfo = fief.auth_callback(code, redirect_url)
print(f"Tokens: {tokens}")
print(f"Userinfo: {userinfo}")
