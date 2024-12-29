from app import create_app
from config import Config
from database import db
from modules.users.models import User
from modules.inventory.models import BeerInventory

app = create_app(Config)

with app.app_context():
    user_admin = User(name="Admin", email="admin@test.com", role="admin")
    user_staff = User(name="Staff", email="staff@test.com", role="staff")

    db.session.add_all([user_admin, user_staff])
    
    beer1 = BeerInventory(name="Pale Ale", description="Refrescante", price=3.5, quantity=100)
    beer2 = BeerInventory(name="Stout", description="Oscura", price=4.0, quantity=50)
    
    db.session.add_all([beer1, beer2])

    db.session.commit()
    print("¡Datos iniciales insertados!")