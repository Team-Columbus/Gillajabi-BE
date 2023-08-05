from burgers.models import Mcdonald,SetMenu

mcdonalds = [
    Mcdonald(
        menu_name="불고기 버거",
        price=2800,
        calorie="409 kcal",
        menu_category="버거",
        food_category="불고기",
        menu_size="단품",
        is_set=True,
    ),
    Mcdonald(
        menu_name="불고기 버거 - 세트",
        price=4500,
        calorie="732 kcal",
        menu_category="버거",
        food_category="불고기",
        menu_size="미디움",
        is_set=True,
    ),
    Mcdonald(
        menu_name="불고기 버거 - 라지세트",
        price=5200,
        calorie="872 kcal",
        menu_category="버거",
        food_category="불고기",
        menu_size="라지",
        is_set=True,
    ),
    Mcdonald(
        menu_name="더블 불고기 버거",
        price=4500,
        calorie="635 kcal",
        menu_category="버거",
        food_category="불고기",
        menu_size="단품",
        is_set=True,
    ),
    Mcdonald(
        menu_name="치즈버거",
        price=2400,
        calorie="318 kcal",
        menu_category="버거",
        food_category="불고기",
        menu_size="단품",
        is_set=True,
    ),
    Mcdonald(
        menu_name="더블 치즈버거",
        price=4700,
        calorie="479 kcal",
        menu_category="버거",
        food_category="불고기",
        menu_size="단품",
        is_set=True,
    ),
    Mcdonald(
        menu_name="트리플 치즈버거",
        price=5800,
        calorie="620 kcal",
        menu_category="버거",
        food_category="불고기",
        menu_size="단품",
        is_set=True,
    ),
    Mcdonald(
        menu_name="케이준 비프 스낵랩",
        price=2400,
        calorie="308 kcal",
        menu_category="사이드",
        menu_size="단품",
        is_set=False,
    ),
    Mcdonald(
        menu_name="상하이 치킨 스낵랩",
        price=2700,
        calorie="303 kcal",
        menu_category="사이드",
        menu_size="단품",
        is_set=False,
    ),
    Mcdonald(
        menu_name="코울슬로",
        price=1900,
        calorie="179 kcal",
        menu_category="사이드",
        menu_size="단품",
        is_set=False,
    ),
    Mcdonald(
        menu_name="코카-콜라 - 미디엄",
        price=1700,
        calorie="133 kcal",
        menu_category="음료",
        menu_size="단품",
        is_set=False,
    ),
    Mcdonald(
        menu_name="코카-콜라 - 라지",
        price=2200,
        calorie="185 kcal",
        menu_category="음료",
        menu_size="단품",
        is_set=False,
    ),
    Mcdonald(
        menu_name="스프라이트 - 미디엄",
        price=1700,
        calorie="140 kcal",
        menu_category="음료",
        menu_size="단품",
        is_set=False,
    ),
    Mcdonald(
        menu_name="스프라이트 - 라지",
        price=1700,
        calorie="194 kcal",
        menu_category="음료",
        menu_size="단품",
        is_set=False,
    ),
    Mcdonald(
        menu_name="환타 - 미디엄",
        price=1700,
        calorie="62 kcal",
        menu_category="음료",
        menu_size="단품",
        is_set=False,
    ),
    Mcdonald(
        menu_name="환타 - 라지",
        price=1700,
        calorie="86 kcal",
        menu_category="음료",
        menu_size="단품",
        is_set=False,
    ),
    Mcdonald(
        menu_name="후렌치 후라이 - 미디엄",
        price=2000,
        calorie="324 kcal",
        menu_category="스낵&사이드",
        menu_size="미디엄",
        is_set=False,
    ),
    Mcdonald(
        menu_name="후렌치 후라이 - 라지",
        price=2700,
        calorie="397 kcal",
        menu_category="사이드",
        menu_size="라지",
        is_set=False,
    ),
    Mcdonald(
        menu_name="허니버터 인절미 후라이 - 미디엄",
        price=2700,
        calorie="386 kcal",
        menu_category="사이드",
        menu_size="미디엄",
        is_set=False,
    ),
    Mcdonald(
        menu_name="허니버터 인절미 후라이 - 라지",
        price=3400,
        calorie="460 kcal",
        menu_category="사이드",
        menu_size="라지",
        is_set=False,
    ),
    Mcdonald(
        menu_name="코카 콜라 제로 - 미디엄",
        price=1200,
        calorie="0 kcal",
        menu_category="음료",
        menu_size="미디엄",
        is_set=False,
        is_happy=True
    ),
    Mcdonald(
        menu_name="코카 콜라 제로 - 라지",
        price=2200,
        calorie="0 kcal",
        menu_category="음료",
        menu_size="라지",
        is_set=False,
        is_happy=False
    )
]

instance = Mcdonald.objects.get(menu_name="불고기 버거")

setmenus = [
    SetMenu(
        menu_name="불고기 버거 - 세트",
        price=4500,
        calorie="732 kcal",
        menu_size="미디움",
        single_menu=instance,
    ),
    SetMenu(
        menu_name="불고기 버거 - 라지세트",
        price=5200,
        calorie="872 kcal",
        menu_size="라지",
        single_menu=instance,
    ),
]

instance = Mcdonald.objects.get(menu_name="더블 불고기 버거")
setmenus = [
    SetMenu(
        menu_name="더블 불고기 버거 - 세트",
        price=6000,
        calorie="959 kcal",
        menu_size="미디움",
        single_menu=instance,
    ),
    SetMenu(
        menu_name="더블 불고기 버거 - 라지세트",
        price=6700,
        calorie="1098 kcal",
        menu_size="라지",
        single_menu=instance,
    ),
]

instance = Mcdonald.objects.get(menu_name="치즈버거")
setmenus = [
    SetMenu(
        menu_name="치즈버거 - 세트",
        price=6000,
        calorie="641 kcal",
        menu_size="미디움",
        single_menu=instance,
    ),
    SetMenu(
        menu_name="치즈버거 - 라지세트",
        price=6700,
        calorie="781 kcal",
        menu_size="라지",
        single_menu=instance,
    ),
]
instance = Mcdonald.objects.get(menu_name="더블 치즈 버거")
setmenus = [
    SetMenu(
        menu_name="더블 치즈버거 - 세트",
        price=6000,
        calorie="802 kcal",
        menu_size="미디움",
        single_menu=instance,
    ),
    SetMenu(
        menu_name="더블 치즈버거 - 라지세트",
        price=6700,
        calorie="942 kcal",
        menu_size="라지",
        single_menu=instance,
    ),
]
