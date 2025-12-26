# Learning Path Analyzer 📊

**Learning Path Analyzer** — система анализа пути обучения студентов на основе логов LMS (Moodle, Canvas и др.).  
Проект анализирует активность студентов, строит графики и выдаёт рекомендации по оптимизации обучения.

---

## 📂 Структура проекта
learning-path-analyzer/
│
├── src/
│   ├── __init__.py
│   ├── parser.py
│   ├── analysis.py
│   ├── recommender.py
│   ├── visualization.py
│   ├── report.py
│   └── config.py
│
├── tests/
│   ├── test_parser.py
│   ├── test_analysis.py
│   └── test_recommender.py
│
├── data/
│   └── sample_logs.csv
│
├── reports/
│   └── .gitkeep
│
├── docs/
│   └── input_format.md
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── scheduled.yml
│
├── requirements.txt
├── .gitignore
└── README.md


> **Важно:** входной CSV-файл с логами студентов должен лежать в папке `data/`. Например: `data/sample_logs.csv`.  
> Структура CSV:
student_id,timestamp,event_type,resource,score
1,2024-03-01 09:00,login,system,
1,2024-03-02 12:00,quiz_attempt,quiz_1,78
1,2024-03-04 15:30,assignment_submission,hw_1,85
2,2024-03-01 10:10,login,system,
2,2024-03-03 14:00,forum_post,discussion_1,
2,2024-03-05 16:45,quiz_attempt,quiz_1,92

# Инструкция по запуску:
## 1. Клонируем репозиторий
git clone https://github.com/kr0upy/learning-path-analyzer.git
cd learning-path-analyzer

## 2. Создаем и активируем виртуальное окружение
- macOS / Linux
python3 -m venv venv
source venv/bin/activate

- Windows PowerShell
python -m venv venv
venv\Scripts\Activate.ps1

## 3. Активируем зависимости
pip install --upgrade pip
pip install -r requirements.txt

## 4. Генерация отчета
python - <<EOF
from src.parser import load_logs
from src.report import generate_report

- Загружаем CSV
df = load_logs("data/sample_logs.csv")

- Генерируем отчёт в папку reports/
generate_report(df, "reports")
EOF

