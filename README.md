# Запуск проекта локально

## Предварительные требования

- **Python 3.12**: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Node.js**: [https://nodejs.org/](https://nodejs.org/) (рекомендуемая версия указана в `front/package.json`)
- **npm**: устанавливается вместе с Node.js

## Шаги
0. **Распакуйте ```files/model.zip```**

1. **Создайте и активируйте виртуальное окружение Python (рекомендуется):**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Установите зависимости backend:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Запустите backend:**

   ```bash
   cd back
   fastapi run main.py
   ```

4. **В новом окне терминала, установите зависимости frontend:**

   ```bash
   cd front
   npm install
   ```

5. **Запустите frontend:**
   ```bash
   npm run dev
   ```

## Дополнительная информация

- Frontend будет доступен по адресу [http://localhost:3000](http://localhost:3000)
- Backend будет доступен по адресу [http://localhost:8000](http://localhost:8000)
