# Neural Networks Multimodal Dataset
## Мультимодальный датасет для разработки систем искусственного интеллекта

## Описание проекта

Проект представляет собой мультимодальный набор данных, посвящённый **искусственным нейронным сетям**. Данные собраны в трёх модальностях: **текст**, **изображения** и **аудио**. Датасет предназначен для обучения и оценки моделей машинного обучения, способных:

- Классифицировать типы нейронных сетей по текстовому описанию.
- Распознавать архитектуры нейронных сетей на схемах.
- Транскрибировать и анализировать аудиолекции по теме ИИ.

## Структура репозитория

```
neural-networks-multimodal-dataset/
├── README.md
├── LICENSE
├── .gitignore
├── data/
│   ├── text/           # Текстовые данные (10 объектов)
│   │   ├── raw/        # Исходные тексты
│   │   └── processed/  # Обработанные данные (CSV)
│   ├── images/         # Изображения (10 объектов)
│   │   ├── raw/        # Исходные изображения
│   │   └── annotations/# Аннотации (JSON)
│   └── audio/          # Аудиоданные (10 объектов)
│       ├── raw/        # Исходные аудиофайлы
│       └── transcriptions/ # Транскрипции (JSON)
├── code/               # Скрипты для сбора и обработки
├── docs/               # Документация
└── presentation/       # Презентация
```

## Источники данных

### Текстовые данные
- **Википедия** (русскоязычные статьи): [Искусственная нейронная сеть](https://ru.wikipedia.org/wiki/Искусственная_нейронная_сеть), [Свёрточная нейронная сеть](https://ru.wikipedia.org/wiki/Свёрточная_нейронная_сеть), [Рекуррентная нейронная сеть](https://ru.wikipedia.org/wiki/Рекуррентная_нейронная_сеть) и др.
- **Habr**: статьи по машинному обучению.
- **Научные публикации**: arXiv, КиберЛенинка.

### Изображения
- **Wikimedia Commons**: схемы архитектур нейронных сетей.
- **Открытые датасеты**: TensorFlow Playground, Neural Network Zoo.
- **Собственные визуализации**: построены с помощью библиотек Matplotlib и Plotly.

### Аудиоданные
- **Открытые лекции**: Coursera, Stepik, YouTube (с соблюдением лицензий).
- **Подкасты**: «Data Science», «ИИ сегодня».
- **Собственные записи**: озвученные описания архитектур.

## Описание кода

| Файл | Назначение |
|------|------------|
| `collect_text.py` | Сбор текстов из Википедии через API |
| `collect_images.py` | Загрузка изображений из открытых источников |
| `collect_audio.py` | Запись и загрузка аудиолекций |
| `preprocess_text.py` | Очистка и токенизация текстов |

## Аннотационная схема

Подробное описание аннотационной схемы доступно в файле:
[docs/annotation_scheme.md](docs/annotation_scheme.md)

### Уровни аннотаций

| Модальность | Уровень 1 | Уровень 2 | Уровень 3 |
|-------------|-----------|-----------|-----------|
| Текст | Модель (MODEL_NAME) | Термин (TERM) | Токен (TOKEN) |
| Изображения | Область (REGION) | Слой (LAYER) | Нейрон (NEURON) |
| Аудио | Фрагмент (SEGMENT) | Термин (TERM_AUDIO) | Фонема (PHONEME) |

### Форматы аннотаций

- **Текст:** CoNLL-U
- **Изображения:** COCO JSON / CVAT
- **Аудио:** Praat TextGrid
  
### Установка зависимостей

```bash
pip install -r code/requirements.txt
```

### Запуск кода

```bash
python code/collect_text.py
python code/preprocess_text.py
```

## Примеры данных

### Текст (`data/text/raw/wiki_cnn.txt`)

```
Свёрточная нейронная сеть (CNN) — класс глубоких нейронных сетей, 
наиболее часто применяемых для анализа изображений. Архитектура CNN 
включает свёрточные слои, слои подвыборки (pooling) и полносвязные слои.
```

### Изображение (`data/images/annotations/image_labels.json`)

```json
{
  "cnn_architecture.png": {
    "label": "Архитектура CNN",
    "type": "схема",
    "objects": ["свёрточный слой", "pooling", "полносвязный слой", "карты признаков"]
  }
}
```

### Аудио (`data/audio/transcriptions/audio_transcripts.json`)

```json
{
  "lecture_cnn.mp3": {
    "duration": "03:20",
    "language": "ru",
    "transcription": "Свёрточная нейронная сеть применяется для анализа изображений...",
    "keywords": ["CNN", "свёртка", "pooling", "изображения"]
  }
}
```

## Сводная таблица объектов

| № | Объект | Текст | Изображение | Аудио |
|---|--------|-------|-------------|-------|
| 1 | ANN (перцептрон) | `wiki_ann.txt` | `ann_architecture.png` | `lecture_ann.mp3` |
| 2 | CNN | `wiki_cnn.txt` | `cnn_architecture.png` | `lecture_cnn.mp3` |
| 3 | RNN | `wiki_rnn.txt` | `rnn_architecture.png` | `lecture_rnn.mp3` |
| 4 | Transformer | `wiki_transformer.txt` | `transformer_architecture.png` | `lecture_transformer.mp3` |
| 5 | GAN | `wiki_gan.txt` | `gan_architecture.png` | `lecture_gan.mp3` |
| 6 | SVM | `wiki_svm.txt` | `svm_hyperplane.png` | `lecture_svm.mp3` |
| 7 | Random Forest | `wiki_random_forest.txt` | `random_forest.png` | `lecture_random_forest.mp3` |
| 8 | KNN | `wiki_knn.txt` | `knn_visualization.png` | `lecture_knn.mp3` |
| 9 | Autoencoder | `wiki_autoencoder.txt` | `autoencoder_schema.png` | `lecture_autoencoder.mp3` |
| 10 | LSTM | `wiki_lstm.txt` | `lstm_cell.png` | `lecture_lstm.mp3` |

## Лицензия

- **Код:** MIT License.
- **Данные:** CC BY 4.0 (с указанием источников).

## Контактная информация

- **Автор:** Ilya Kleshnin
- **GitHub:** [@ilya-kleshnin](https://github.com/ilya-kleshnin)

## Презентация

Ссылка на презентацию: [project_presentation.pdf](presentation/project_presentation.pdf)

> ⚠️ Презентация будет добавлена после выполнения Шага 5.

## Разметка текстовых данных (ЛР №3)

Разметка выполнена в формате **CoNLL-U**. Все размеченные файлы находятся в:
[`data/text/annotations/`](data/text/annotations/)

### Формат разметки

Каждый файл `.conllu` содержит предложения с 10 колонками:

| № | Колонка | Описание |
|---|---------|----------|
| 1 | ID | Номер токена |
| 2 | FORM | Слово |
| 3 | LEMMA | Начальная форма |
| 4 | UPOS | Часть речи |
| 5 | XPOS | Доп. тег |
| 6 | FEATS | Признаки |
| 7 | HEAD | Главное слово |
| 8 | DEPREL | Синтаксическое отношение |
| 9 | DEPS | Доп. зависимости |
| 10 | MISC | **NER-теги** |

### Использованные NER-теги

| Тег | Описание | Пример |
|-----|----------|--------|
| `MODEL_NAME` | Название архитектуры | свёрточная нейронная сеть |
| `TERM` | Ключевой термин | свёртка, pooling |
| `RESEARCHER` | Исследователь | Ян Лекун |
| `ORGANIZATION` | Организация | Google |
| `YEAR` | Год | 1989 |
| `ABBREVIATION` | Аббревиатура | CNN, RNN, LSTM |

## Разметка изображений (ЛР №5)

Разметка выполнена в **CVAT** (Computer Vision Annotation Tool).
Экспортирована в формате **COCO JSON**.

### Файлы

- `data/images/annotations/image_labels.json` — ручная разметка (базовая)
- `data/images/annotations/cvat_annotations.json` — экспорт из CVAT

### Классы объектов

| Класс | Описание | Цвет |
|-------|----------|------|
| `LAYER` | Слой нейронной сети | 🔵 Синий |
| `NEURON` | Отдельный нейрон | 🟢 Зелёный |
| `CONNECTION` | Связь между нейронами | ⚪ Серый |
| `ACTIVATION` | Функция активации | 🟠 Оранжевый |
| `INPUT_OUTPUT` | Входные/выходные данные | 🔴 Красный |

### Статистика разметки

| № | Изображение | Объектов |
|---|-------------|----------|
| 1 | `ann_architecture.png` | 3 |
| 2 | `autoencoder_schema.png` | 5 |
| 3 | `cnn_architecture.png` | 6 |
| 4 | `gan_architecture.png` | 5 |
| 5 | `knn_visualization.png` | 12 |
| 6 | `lstm_cell.png` | 10 |
| 7 | `random_forest.png` | 4 |
| 8 | `rnn_architecture.png` | 3 |
| 9 | `svm_hyperplane.png` | 3 |
| 10 | `transformer_architecture.png` | 5 |
| **Итого** | | **56** |

### Инструмент

- **CVAT Cloud:** https://app.cvat.ai/
- **Формат экспорта:** COCO 1.0
