from sklearn.preprocessing import LabelEncoder
import pandas as pd
import spacy
import joblib

filename = "C:/Users/qwerty/PycharmProjects/LazyProject/app/LP_model_RFC.sav"
modelML = joblib.load(open(filename, 'rb'))
filenameVocab = "C:/Users/qwerty/PycharmProjects/LazyProject/app/Vocab_model.sav"
vocab = joblib.load(open(filenameVocab, 'rb'))
label = LabelEncoder()
nlp = spacy.load(name="C:/Users/qwerty/PycharmProjects/LazyProject/app/en_core_web_sm/en_core_web_sm-3.7.1")


def preprocess(text):
    # remove stop words and lemmatize the text
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)

    return " ".join(filtered_tokens)


def process_data(text: str):
    df = pd.DataFrame(data=[[text, 'happy']], columns=['Text', 'Emotion'])
    df['preprocessed_text'] = df['Text'].apply(preprocess)
    df['Emotion_label'] = label.fit_transform(df['Emotion'])
    ML_input = vocab.transform(df['preprocessed_text'])
    predict = modelML.predict(ML_input)
    if predict == 0: output = 'anger'
    elif predict == 1: output = 'fear'
    elif predict == 2: output = 'happy'
    elif predict == 3: output = 'love'
    elif predict == 4: output = 'sadness'
    elif predict == 5: output = 'surprise'
    else: output = 'why?'
    return output


print(process_data("You donkey, why can't you make me some soup"))
print(process_data("I am scared my friend, I hear him rumbling and whispering"))
print(process_data("I am happy, that i am still alive"))
print(process_data("My darling, I love you"))
print(process_data("hate hate hate hate hate hate"))
print(process_data("I am surprised you got that far"))
