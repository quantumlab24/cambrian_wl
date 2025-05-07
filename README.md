# ✅ Cambrian.org Waitlist Registration

Скрипт на Python + Playwright для автоматической регистрации email-адресов в вайтлист на [https://cambrian.org](https://cambrian.org).

---

## 🚀 Основной функционал

- 💬 Поддержка регистрации email-адресов из файла `emails.txt`
- 🌐 Поддержка прокси из `proxies.txt` (опционально, по циклу)
- 🧠 Уникальный user-agent Chrome и случайное разрешение экрана
- 🖱️ Эмуляция кликов по форме: `WAITLIST`, ввод email, submit
- ✅ Проверка успешной регистрации (по кнопке `Success`)
- 🧾 Логирование успешных и ошибочных попыток в файлы:
  - `results_*.txt` — успехи
  - `errors_*.txt` — ошибки
- ⚙️ Многопоточность через `ThreadPoolExecutor`
- 🐢 Случайные задержки между действиями (антибот-мимикрия)

---

## 📂 Структура проекта

| Файл              | Назначение                                   |
|-------------------|-----------------------------------------------|
| `main.py`         | Главный скрипт запуска                        |
| `emails.txt`      | Список email-адресов по одному в строке       |
| `proxies.txt`     | (опционально) список прокси в формате URL     |
| `utils/logger.py` | Логгер `logger`                               |
| `results_*.txt`   | Успешные регистрации                          |
| `errors_*.txt`    | Ошибки регистрации                            |

---

## 📋 Формат файлов

### `emails.txt`

```
example1@gmail.com
example2@yahoo.com
...
```

### `proxies.txt` (если USE_PROXY = True)

```
http://user:pass@ip:port
socks5://ip:port
...
```

---

## ⚙️ Установка

1. Убедитесь, что у вас установлен Python 3.11+
2. Установите зависимости:

```bash
python -m venv .venv
```
```bash
.venv\Scripts\Activate
```
```bash
pip install -r requirements.txt
```
```bash
playwright install
```


Содержимое `requirements.txt`:
```
playwright~=1.52.0
loguru~=0.7.3
```

3. Установи Google Chrome (используется `channel="chrome"`)

---

## ▶️ Запуск

```bash
python main.py
```

Файл настроен на работу с:

- `MAX_THREADS = 2` — количество потоков можно изменить в `main.py`
- `USE_PROXY = False` — изменить на `True` для использования прокси из `proxies.txt`, если указано меньшее кол-во прокси, чем emails, то прокси берутся по второму кругу.

---

## 📝 Выводы сохраняются в:

- `results_<timestamp>.txt` — удачные регистрации (email:proxy)
- `errors_<timestamp>.txt` — ошибки (например, если кнопка Success не найдена)

---

## 📄 Лицензия

Предоставляется в ознакомительных и образовательных целях.
