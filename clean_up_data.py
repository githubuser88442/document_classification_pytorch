import pickle
from bs4 import BeautifulSoup

with open('DATA/articles_and_categories.pkl', 'rb') as f:
    X,Y = pickle.load(f)


NEW_X = []
NEW_Y = []
STOP_WORDS = ['http', 'src', 'javascript', 'script', 'gallery']
STOP_WORDS = STOP_WORDS + list(set('АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'.lower()))
print(STOP_WORDS)

def remove_with_html_and_stopwords(x, y, stop_words, min_len, max_len):
    failed_count = 0
    for ind, i in enumerate(x):
        if ind % 10000 == 0:
            print(f'{ind}, {len(NEW_X)}|{len(NEW_Y)} out of {len(x)}|{len(y)}')
        try:
            if len(i.split(' ')) > min_len and len(i.split(' ')) < max_len and not any(w in i.lower() for w in stop_words) and not bool(BeautifulSoup(i, "html.parser").find()):
                print('here')
                NEW_X.append(i)
                NEW_Y.append(y[ind])
        except:
            failed_count += 1
    print(f'failed: {failed_count}')

def clean_up_html(x, y):
    failed_count = 0
    for ind, i in enumerate(x):
        if ind % 10000 == 0:
            print(f'{ind}, ({len(NEW_X)}|{len(NEW_Y)}) out of {len(x)}|{len(y)}')
        try:
            soup = BeautifulSoup(i)
            text = soup.get_text()
            NEW_X.append(text)
            NEW_Y.append(y[ind])
        except:
            failed_count += 1
    print(f'failed: {failed_count}')

# clean_up_html(X, Y)
# remove_with_html_and_stopwords(X, Y, STOP_WORDS, 5, 100000000)

print('new_x/new_y len: ', len(NEW_X), len(NEW_Y))

# Just in case
# import pdb;pdb.set_trace()
with open('DATA/x_and_y_cleaned.pkl', 'wb') as f:
    pickle.dump([NEW_X, NEW_Y], f)