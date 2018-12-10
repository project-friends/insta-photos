"""Models and database functions for Photo Sharing Project."""

from flask_sqlalchemy import SQLAlchemy

#Connection to PostgreSQL database using Flask-SQLAlchemy helper library.
db = SQLAlchemy()

#Model definitions: database information.


class User(db.Model):
    """User of Photo Sharing website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)


    photo = db.relationship("Photos")

    def __repr__(self):
        """Provide helpful representatble when printed."""

        return f"<user_id: {self.user_id} \n username: {self.username} \n email: {self.email} \n password: {self.password}>"


class Photos(db.Model):
    """Photos."""

    __tablename__ = "photos"

    photo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    photo_source = db.Column(db.String(300), nullable=True)

    user = db.relationship('User')

    def __repr__(self):
        return f"<photo_id: {self.photo_id} \n user_id: {self.user_id} \n photo_source: {self.photo_source}>"


class Followers(db.Model):
    """Followers of users."""

    __tablename__ = "followers"

    connection_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)

    def __repr__(self):
        return f"<user_id: {self.user_id} \n follower_id: {self.user_id}>"


#Functions to connect to database.
def connect_to_db(app, db_uri="postgresql:///testdb"):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    db_uri = "postgresql:///projectdb"

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)



if __name__ == "__main__":
    """Import app & connect to database as soon as file is run."""
    from server import app
    connect_to_db(app)
    db.create_all()
    print("Connected to DB.")
