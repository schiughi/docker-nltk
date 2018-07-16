from nltk.corpus import gutenberg

# 「グーテンベルク電子出版アーカイブ」のtextファイルをnltk.corpusから取得し、
# それぞれのtextファイルについて統計処理を行う
for fileid in gutenberg.fileids():
  num_chars = len(gutenberg.raw(fileid))
  num_words = len(gutenberg.words(fileid))
  num_sents = len(gutenberg.sents(fileid))
  num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
  print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid


# webtext
from nltk.corpus import webtext
for fileid in webtext.fileids():
  print fileid, webtext.raw(fileid)[:65], '...'

# chat
from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]


# 
from nltk.corpus import inaugural

cfd = nltk.ConditionalFreqDist(
  (target, fileid[:4])
  for fileid in inaugural.fileids()
  for w in inaugural.words(fileid)
  for target in ['america', 'citizen']
  if w.lower().startswith(target)
)
cfd.plot()
