from sys import getsizeof
import os
from xml.etree import ElementTree
import pickle
import tqdm

articles = []
categories = []
# for xml_file in os.listdir(''):
xml_iter = ElementTree.iterparse('', events=('start', 'end'))

not_duplicate = False
try:
    for i, (event, elem) in enumerate(tqdm.tqdm(xml_iter)):
        if i % 10000000 == 0:
            print('\nSize:', getsizeof(articles) / 1000000)
        if event == 'start':
            if elem.tag == 'ArticleText':
                if elem.text not in articles:
                    articles.append(elem.text)
                    not_duplicate = True
                else:
                    not_duplicate = False

            elif elem.tag == 'ArticleSection' and not_duplicate:
                categories.append(elem.text)

        elem.clear()
except:
    print('except, article/category len:', len(articles), len(categories))

with open("articles_and_categories.pkl", "wb") as fp:
    pickle.dump([articles, categories], fp)

import pdb;pdb.set_trace()