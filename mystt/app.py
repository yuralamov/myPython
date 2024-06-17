'''
pip install sounddevice         # Устройства ввода-вывода 
                                # python -m sounddevice
                                https://python-sounddevice.readthedocs.io/en/0.4.7/
                                https://pypi.org/project/sounddevice/
                                https://www.sounddevices.com/
pip install vosk                # Библиотека распознавания речи с ИИ
                                https://alphacephei.com/vosk/
                                https://github.com/alphacep/vosk-api                                
pip install pyttsx3             # Библиотека текст в звук
                                https://pypi.org/project/pyttsx3/
                                https://pyttsx3.readthedocs.io/en/latest/
pip install scikit-learn        # Машинное обучение в Python
                                https://scikit-learn.org/stable/
                                https://github.com/scikit-learn/scikit-learn
ast                             # Абстрактные синтаксические деревья
                                https://docs.python.org/3/library/ast.html                                
queue                           # Класс синхронизированной очереди
                                https://docs.python.org/3/library/queue.html
json                            # Кодер и декодер JSON
                                https://docs.python.org/3/library/json.html

'''
from ast import List
import queue
import sounddevice as sd
import vosk
from vosk import Model, KaldiRecognizer
import json
import words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from skills import *


q = queue.Queue() # Контейнер с данными
model = vosk.Model('model_small') # Модель для vosk

device = sd.default.device = 19, 19 # Устройства ввода и вывода звука
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate']) 

def recognize(data, vectorizer, clf):
    '''
    
    '''
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    print(answer)
    func_name = answer.split()[0]
    exec(func_name + '()')
    
def callback(indata, frames, time, status):
    '''
    Создает поток с данными с микрофона
    '''
    q.put(bytes(indata))

def main():
    '''
    Обрабатываем фразы в ИИ и ищем похожие в words
    '''
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))
    '''
    По ключу в words определяем значение
    '''
    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))
    
    del words.data_set # Очистка памяти
    
    with sd.RawInputStream(samplerate=samplerate, blocksize = 16000, device=device[0],
            dtype="int16", channels=1, callback=callback):
        '''
        Получаем поток с микрофона 
        '''
        rec = vosk.KaldiRecognizer(model, samplerate)
        '''
        Передаем сэмплы в vosk для обработки в цикле постоянно. Как только пауза, формируется text,
        который разбирается json и передается в recognize(data, vectorizer, clf)
        '''
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)
        



if __name__ == '__main__':
    main()
