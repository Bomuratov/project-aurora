

#  permissions

ADD = "can_add"
UPDATE = "can_update"
DELETE = "can_delete"
VIEW = "can_view"


RESTAURAN = "restaurant"
ORDER = "order"
CATEGORY = "category"
MENU = "menu"
USER = "user"


PERMISSIONS = (
    (ADD, "Доступ добавить"),
    (UPDATE, "Доступ обновить"),
    (DELETE, "Доступ удалить"),
    (VIEW, "Доступ на чтение"),
)


RESOURCE = (
    (RESTAURAN, "restaurant"),
    (ORDER, "order"),
    (CATEGORY, "category"),
    (MENU, "menu"),
    (USER, "user"),
)