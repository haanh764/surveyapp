from sqlalchemy import Column, Integer, String, Boolean
from database.db_config import Base

class RevokedToken(Base):
    __tablename__ = 'revoked_tokens'
    id = Column(Integer, primary_key=True, index=True)
    jti = Column(String(120))
    type = Column(String(120))
