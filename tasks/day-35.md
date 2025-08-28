# День 35 — Чек-лист

- [ ] Створити репозиторій **day-35-human-passport**
- [ ] Додати файли: `README.md`, `streak.py`, `tasks/day-35.md`
- [ ] Запустити `python3 streak.py` (очікувано: Day 35)
- [ ] Зробити коміт: `feat: Day 35 streak CLI + checklist`
- [ ] Push на GitHub (гілка `main`)
- [ ] Layer3: виконати мін. 1 квест
- [ ] Supra: перевірити стейкінг / ноди
- [ ] Тренування + вода + креатин
- [ ] Mishkin: 5–10 сторінок конспекту

# 1) Локально
mkdir day-35-human-passport && cd $_
printf "" > README.md && printf "" > streak.py
mkdir -p tasks
printf "" > tasks/day-35.md

# Встав копірайт з цього чату у відповідні файли:
# - README.md
# - streak.py
# - tasks/day-35.md

# 2) Git
git init
git add .
git commit -m "feat: Day 35 streak CLI + checklist"
git branch -M main
git remote add origin git@github.com:<YOUR_GH_USERNAME>/day-35-human-passport.git
# або HTTPS:
# git remote add origin https://github.com/<YOUR_GH_USERNAME>/day-35-human-passport.git
git push -u origin main
