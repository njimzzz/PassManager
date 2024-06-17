from models import Session, Password

session = Session()

def add_password(user, service, password):
    new_password = Password(user=user, service=service, password=password)
    session.add(new_password)
    session.commit()


def view_passwords(user):
    return session.query(Password).filter(Password.user == user).all()

def update_password(user, service, new_password):
    password_entry = session.query(Password).filter(Password.user == user, Password.service == service).first()
    if password_entry:
        password_entry.password = new_password
        session.commit()

def delete_password(user, service):
    password_entry = session.query(Password).filter(Password.user == user, Password.service == service).first()
    if password_entry:
        session.delete(password_entry)
        session.commit()
