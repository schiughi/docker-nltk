FROM python:2.7.8

RUN pip install -U nltk
RUN python -c "import nltk; nltk.download(['book'])"
CMD python
