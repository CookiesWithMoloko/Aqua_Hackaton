from .models.tags import Tag
class TagChecker:
    def __init__(self):
        self.tags = [i.as_dict() for i in Tag.query.all()]
        for i in self.tags:
            if i['keywords'] is not None:
                i['keywords'] = i.keywords.split(',')
    def get_tags(self, content: str) -> list:
        r = []
        for i in self.tags:
            p = 0
            for j in i['keywords']:
                if j in content:
                    p += 1
            p = p / len(i['keywords'])
            if p >= 0.5:
                r.append(i)
        return r


