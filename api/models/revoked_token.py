from sqlalchemy import Column, Integer, String, Boolean
from database.db_config import Base, session

class RevokedToken(Base):
    __tablename__ = 'revoked_tokens'
    id = Column(Integer, primary_key=True, index=True)
    jti = Column(String(120))
    type = Column(String(120))

    def add(self):
        session.add(self)
        session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = session.query(cls).filter_by(jti=jti).first()
        return bool(query)
