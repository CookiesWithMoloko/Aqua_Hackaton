from app import app, db
import services
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)