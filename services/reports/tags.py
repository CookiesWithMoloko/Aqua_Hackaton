from .models.tags import Tag

def get_tags(content: str) -> list:
    r = Tag.query.all()
    print(r)
