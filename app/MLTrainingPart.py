from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import spacy
import joblib


def preprocess(text):
    # remove stop words and lemmatize the text
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)

    return " ".join(filtered_tokens)


df = pd.read_csv(filepath_or_buffer="C:/Users/qwerty/PycharmProjects/LazyProject/app/Emotion_final.csv")
print(df.shape)
print(df['Emotion'].value_counts())
nlp = spacy.load(name="C:/Users/qwerty/PycharmProjects/LazyProject/app/en_core_web_sm/en_core_web_sm-3.7.1")
df['preprocessed_text'] = df['Text'].apply(preprocess)
print("TextTransformationFinished")
label = LabelEncoder()
df['Emotion_label'] = label.fit_transform(df['Emotion'])
X_train, X_test, y_train, y_test = train_test_split(df['preprocessed_text'], df['Emotion_label'],
                                                    test_size=0.25, random_state=42, stratify=df['Emotion_label'])


vocab = TfidfVectorizer()
X_train_cv = vocab.fit_transform(X_train)
X_test_cv = vocab.transform(X_test)
print("VocabFinish")


RFC_model = RandomForestClassifier()
RFC_model.fit(X_train_cv, y_train)

filenameML = "LP_model_RFC.sav"
joblib.dump(RFC_model, open(filenameML, 'wb'))
modelML = joblib.load(open(filenameML, 'rb'))

filenameVocab = "Vocab_model.sav"
joblib.dump(vocab, open(filenameVocab, 'wb'))

y_predict = modelML.predict(X_test_cv)
print(accuracy_score(y_test, y_predict))
