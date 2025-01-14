from django.shortcuts import render


DATA = {
    # здесь словарь с рецептами
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def omlet(request, a=None):
    """Функция обработки словаря по маршруту "/omlet" \

        и передача значений словаря в шаблон.

    """
    recipe = DATA.get('omlet', {})
    # Получаем рецепт для омлета из DATA

    if a is not None:
        """Здесь указано условие при котором, \

            при вводе значений от пользователя в адресной строке, \

                производить умножение на заданное число порций, \

                    для получения кол-ва ингредиентов "omlet".

        """
        for key, value in recipe.items():
            recipe[key] = value * int(a)
        # Если аргумент "a" имеет значение,
        # переданное пользователем в адресной строке,
        # то вычисляем кол-во ингредиентов на порцию и выводим в шаблон.
        # Если аргумент "a" не указан в адресе,
        # то отображать в шаблоне дефолтные значения словара-рецептов.

    context = {
        'recipe': recipe,
    }

    return render(request, 'calculator/index.html', context)


def pasta(request, a=None):
    """Функция обработки словаря по маршруту "/pasta" \

        и передача значений словаря в шаблон.

    """
    recipe = DATA.get('pasta', {})
    # Получаем рецепт для пасты из DATA

    if a is not None:
        """Здесь указано условие при котором, \

            при вводе значений от пользователя в адресной строке, \

                производить умножение на заданное число порций, \

                    для получения кол-ва ингредиентов "pasta".

        """
        for key, value in recipe.items():
            recipe[key] = value * int(a)
        # Если аргумент "a" имеет значение,
        # переданное пользователем в адресной строке,
        # то вычисляем кол-во ингредиентов на порцию и выводим в шаблон.
        # Если аргумент "a" не указан в адресе,
        # то отображать в шаблоне дефолтные значения словара-рецептов.

    context = {
        'recipe': recipe,
    }

    return render(request, 'calculator/index.html', context)


def buter(request, a=None):
    """Функция обработки словаря по маршруту "/buter" \

        и передача значений словаря в шаблон.

    """
    recipe = DATA.get('buter', {})
    # Получаем рецепт для бутерброда из DATA

    if a is not None:
        """Здесь указано условие при котором, \

            при вводе значений от пользователя в адресной строке, \

                производить умножение на заданное число порций, \

                    для получения кол-ва ингредиентов "buter".

        """
        for key, value in recipe.items():
            recipe[key] = value * int(a)
        # Если аргумент "a" имеет значение,
        # переданное пользователем в адресной строке,
        # то вычисляем кол-во ингредиентов на порцию и выводим в шаблон.
        # Если аргумент "a" не указан в адресе,
        # то отображать в шаблоне дефолтные значения словара-рецептов.

    context = {
        'recipe': recipe,
    }

    return render(request, 'calculator/index.html', context)
