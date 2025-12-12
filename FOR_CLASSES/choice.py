import requests
from config import HF_API_KEY  # or replace with a string token

def check_hf_token(token: str) -> None:
    url = "https://huggingface.co/api/whoami-v2"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)

        # Token valid
        if response.status_code == 200:
            data = response.json()
            print("✔ Token is VALID")
            print(f"Username: {data.get('name', '(unknown)')}")
            print(f"Org memberships: {data.get('orgs', [])}")
            return

        # Token invalid or unauthorized
        elif response.status_code == 401:
            print("✖ Token is INVALID or expired")
            print("Reason: Unauthorized (401)")
            return

        # Other unexpected cases
        else:
            print(f"⚠ Unexpected status: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Error checking token: {e}")


if __name__ == "__main__":
    check_hf_token(HF_API_KEY)
