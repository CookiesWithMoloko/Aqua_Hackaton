from app import app, db
import services
def as_dict(self):
    r = dict()
    for c in self.__table__.columns:
        a = getattr(self, c.name)
        if isinstance(a, db.Model):
            r[c.name] = a.as_dict()
        else:
            r[c.name] = a
    return r

db.Model.as_dict = as_dict
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)