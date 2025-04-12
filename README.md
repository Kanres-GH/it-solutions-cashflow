# CashFlow: Приложение для управления движением денежных средств (ДДС)

## Описание проекта

**CashFlow** — это веб-приложение на Django для управления движением денежных средств (ДДС). Оно позволяет:

- Вести учёт финансовых операций (пополнение и списание).
- Фильтровать записи по дате, статусу, типу, категории и подкатегории.
- Управлять справочниками (статусы, типы, категории, подкатегории) через удобный интерфейс.
- Создавать, редактировать и удалять записи и элементы справочников.

Проект разработан с использованием Django 5.2 и Bootstrap 5.3 для стилизации интерфейса.

---

## Требования

- Python 3.8+
- Django 5.2
- SQLite (используется по умолчанию, но можно настроить другую базу данных)

---

## Установка

1. **Клонируйте репозиторий**:
```bash
git clone https://github.com/Kanres-GH/it-solutions-cashflow.git
cd cashflow
```
2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
venv\Scripts\activate # или `source venv/bin/activate` для Linux
```
3. Установите зависимости:
```bash
pip install django==5.2
```
4. Примените миграции:
```bash
python manage.py migrate
```
5. Создайте суперпользователя (для доступа к админ-панели):
```bash
python manage.py createsuperuser
```
6. Запустите сервер:
```bash
python manage.py runserver
```
Приложение будет доступно по адресу `http://127.0.0.1:8000/`.

## Добавление тестовых данных
### Через Django Shell
1. Запустите Django Shell
```bash
python manage.py shell
```
2. Выполните следующий код для добавления тестовых данных:
```bash
from dds.models import Status, Type, Category, SubCategory, CashFlow
from datetime import date

# Очищаем существующие данные (необязательно)
Status.objects.all().delete()
Type.objects.all().delete()
Category.objects.all().delete()
SubCategory.objects.all().delete()
CashFlow.objects.all().delete()

# СТАТУСЫ
business = Status.objects.create(name="Бизнес")
personal = Status.objects.create(name="Личное")
tax = Status.objects.create(name="Налог")

# ТИПЫ
popolnenie = Type.objects.create(name="Пополнение")
spisanie = Type.objects.create(name="Списание")

# КАТЕГОРИИ
infra = Category.objects.create(name="Инфраструктура", type=spisanie)
marketing = Category.objects.create(name="Маркетинг", type=spisanie)
dohody = Category.objects.create(name="Доходы", type=popolnenie)
investitsii = Category.objects.create(name="Инвестиции", type=popolnenie)

# ПОДКАТЕГОРИИ
vps = SubCategory.objects.create(name="VPS", category=infra)
proxy = SubCategory.objects.create(name="Proxy", category=infra)
farpost = SubCategory.objects.create(name="Farpost", category=marketing)
avito = SubCategory.objects.create(name="Avito", category=marketing)
zarplata = SubCategory.objects.create(name="Зарплата", category=dohody)
freelance = SubCategory.objects.create(name="Фриланс", category=dohody)
aktsii = SubCategory.objects.create(name="Акции", category=investitsii)
obligatsii = SubCategory.objects.create(name="Облигации", category=investitsii)

# ЗАПИСИ ДДС
CashFlow.objects.create(
    created_at=date(2025, 1, 1),
    status=business,
    type=spisanie,
    category=infra,
    subcategory=vps,
    amount=5000,
    comment="Аренда VPS для проекта"
)
CashFlow.objects.create(
    created_at=date(2025, 2, 15),
    status=personal,
    type=spisanie,
    category=marketing,
    subcategory=avito,
    amount=2000,
    comment="Реклама на Avito"
)
CashFlow.objects.create(
    created_at=date(2025, 3, 10),
    status=tax,
    type=spisanie,
    category=infra,
    subcategory=proxy,
    amount=1000,
    comment="Покупка прокси для налогового проекта"
)
CashFlow.objects.create(
    created_at=date(2025, 4, 1),
    status=business,
    type=popolnenie,
    category=dohody,
    subcategory=zarplata,
    amount=50000,
    comment="Зарплата за март"
)
CashFlow.objects.create(
    created_at=date(2025, 4, 5),
    status=personal,
    type=popolnenie,
    category=investitsii,
    subcategory=aktsii,
    amount=10000,
    comment="Инвестиции в акции"
)
```
### Через миграции
1. Нужно убедиться, что в `dds/migrations/` есть миграция с тестовыми данными (например `0002_add_test_data.py`).
2. Сделать `python manage.py migrate`
----
Проект разработан в рамках тестового задания для компании IT-Solutions.
- Темирлан Гайсин
- Моя почта: ktnrgs1817@gmail.com
- Моё резюме: https://hh.kz/resume/22a2bd4fff0c0c89c20039ed1f386f48734b4f