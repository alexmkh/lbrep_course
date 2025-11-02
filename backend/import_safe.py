import os
import django
import json
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lbrep_course.settings")
django.setup()

User = get_user_model()

# Используем data.json вместо users.json
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for obj in data:
    if obj["model"] != "auth.user":
        continue

    fields = obj["fields"]
    username = fields["username"]

    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            "first_name": fields.get("first_name", ""),
            "last_name": fields.get("last_name", ""),
            "email": fields.get("email", ""),
            "is_staff": fields.get("is_staff", False),
            "is_superuser": fields.get("is_superuser", False),
            "is_active": fields.get("is_active", True),
            "password": fields["password"],
        },
    )

    if created:
        print(f"✅ Добавлен новый пользователь: {username}")
    else:
        print(f"⚙️  Пропущен (уже есть): {username}")
