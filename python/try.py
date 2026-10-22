import os
from pathlib import Path

from dotenv import load_dotenv

from apiClient import SophtronApiClient, sophtron_auth_code


load_dotenv(Path(__file__).resolve().with_name(".env"))

user_id = os.getenv("SophtronApiUserId")
user_secret = os.getenv("SophtronApiUserSecret")
if not user_id or not user_secret:
    raise RuntimeError(
        "Set SophtronApiUserId and SophtronApiUserSecret in the environment "
        "or in python/.env."
    )

print("Example: calculating auth token with a dummy")
token = sophtron_auth_code(user_id, user_secret, "example/", "GET")
print(token)

print('Retrieving an example institution "Sophtron Bank"')
client = SophtronApiClient(
    "https://api.sophtron.com/api/",
    user_id,
    user_secret,
)

banks = client.getInstitutionByName("Sophtron Bank")

print(banks[0]['InstitutionName'])
