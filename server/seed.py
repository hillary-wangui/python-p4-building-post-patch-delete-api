from app import app, db
from app import User
from app import Game
from app import Review

def seed_data():
    user1 = User(user_name='nia', email='nia@gmail.com')
    user2 = User(user_name='john', email='john@gmail.com')
    db.session.add_all([user1, user2])
    db.session.commit()

    game1 = Game(title='Game 1', description='This is game 1')
    game2 = Game(title='Game 2', description='This is game 2')
    db.session.add_all([game1, game2])
    db.session.commit()

    review1 = Review(score=5, comment='Great game!', user_id=user1.id, game_id=game1.id)
    review2 = Review(score=4, comment='Good game!', user_id=user2.id, game_id=game2.id)
    db.session.add_all([review1, review2])
    db.session.commit()

if __name__ == '__main__':
    app = app()
    db.init_app(app)
    seed_data()