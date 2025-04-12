from django.db import migrations
from datetime import date

def add_test_data(apps, schema_editor):
    Status = apps.get_model('dds', 'Status')
    Type = apps.get_model('dds', 'Type')
    Category = apps.get_model('dds', 'Category')
    SubCategory = apps.get_model('dds', 'SubCategory')
    CashFlow = apps.get_model('dds', 'CashFlow')

    business = Status.objects.create(name="Бизнес")
    personal = Status.objects.create(name="Личное")
    tax = Status.objects.create(name="Налог")

    popolnenie = Type.objects.create(name="Пополнение")
    spisanie = Type.objects.create(name="Списание")

    infra = Category.objects.create(name="Инфраструктура", type=spisanie)
    marketing = Category.objects.create(name="Маркетинг", type=spisanie)
    dohody = Category.objects.create(name="Доходы", type=popolnenie)
    investitsii = Category.objects.create(name="Инвестиции", type=popolnenie)

    vps = SubCategory.objects.create(name="VPS", category=infra)
    proxy = SubCategory.objects.create(name="Proxy", category=infra)
    farpost = SubCategory.objects.create(name="Farpost", category=marketing)
    avito = SubCategory.objects.create(name="Avito", category=marketing)
    zarplata = SubCategory.objects.create(name="Зарплата", category=dohody)
    freelance = SubCategory.objects.create(name="Фриланс", category=dohody)
    aktsii = SubCategory.objects.create(name="Акции", category=investitsii)
    obligatsii = SubCategory.objects.create(name="Облигации", category=investitsii)

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

class Migration(migrations.Migration):
    dependencies = [
        ('dds', '0002_alter_cashflow_subcategory'),  # Укажи зависимость от предыдущей миграции
    ]

    operations = [
        migrations.RunPython(add_test_data),
    ]