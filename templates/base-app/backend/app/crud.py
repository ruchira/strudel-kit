from sqlalchemy import select
from app.models import User
from app.database import SessionDep


def create_user(id: int, email: str, fullname: str = None, 
    orcid: str = None, is_admin: bool = False, profile_url: str = None):
    db_user = User(id=user_id, email=email, fullname=fullname, orcid=orcid,
                    is_admin=is_admin, profile_url=profile_url)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return(db_user)
    
def get_user_by_id(db: SessionDep, user_id: int) -> User | None:
    user = db.scalar(select(User).filter_by(id=user_id))
    return user


def get_users(db: SessionDep) -> list[User]:
    users = db.scalars(select(User)).all()
    return users
