from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

SECRET_KEY = "your_secret_key" # Must match user-service secret key
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:9001/users/token")

# Extract token payload info
def get_token_payload(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session signature validation failed"
        )

# Require Seller role gatekeeper
def require_seller(payload: dict = Depends(get_token_payload)):
    if payload.get("role") != "seller":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Write access restricted to distribution nodes (Sellers) only."
        )
    return payload # Returns payload containing username under 'sub'
