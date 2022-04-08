from .models.tags import Tag
import pymorphy2 as pm
import re
class TagChecker:
    def __init__(self):
        self.tags = [i.as_dict() for i in Tag.query.all()]
        self.morph = pm.MorphAnalyzer()
        for i in self.tags:
            if i['keywords'] is not None:
                i['keywords'] = i.keywords.split(',')
    def get_tags(self, content: str) -> list:
        content = re.sub(r'[^а-яА-ЯA-Za-z0-9\- ]', '', content)
        ct = ""
        for i in content.split(' '):
            m = self.morph.parse(i)[0]
            if m.tag.POS not in ['PREP', 'CONJ', 'PRCL', 'INTJ']:
                ct += m.normal_form + ' '
        content = ct
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
get_tags = TagChecker().get_tags


