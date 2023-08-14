from coffee_api.models import CoffeeMenu
from coffee_api.models import MenuDetail

# 메뉴카테고리에따라 정렬한 것임.
# 오프라인 매장 확인후 type과 Detail_page 수정할 것.

menu = [
    CoffeeMenu(
        menu_category = "커피(HOT)",
        name = "(HOT)아메리카노",
        price = 1500,
        Detail_page = True,
        type = "아메리카노"),
    CoffeeMenu( 
        menu_category = "커피(HOT)",
        name = "(HOT)꿀아메리카노",
        price = 2500,
        Detail_page = True,
        type = "아메리카노"),
    CoffeeMenu(
        menu_category = "커피(HOT)",
        name = "(HOT)바닐라아메리카노",
        price = 2500,
        Detail_page = True,
        type = "아메리카노"),
    CoffeeMenu(
        menu_category = "커피(HOT)",
        name = "(HOT)카페라떼",
        price = 2700,
        Detail_page = True,
        type = "라떼"),
    CoffeeMenu(
        menu_category = "커피(ICE)",
        name = "(ICE)아메리카노",
        price = 2000,
        Detail_page = True,
        type = "아메리카노"),
    CoffeeMenu(
        menu_category = "커피(ICE)",
        name = "(ICE)꿀아메리카노",
        price = 2700,
        Detail_page = True,
        type = "아메리카노"),
    CoffeeMenu(
        menu_category = "커피(ICE)",
        name = "(ICE)카페라떼",
        price = 2700,
        Detail_page = True,
        type = "라떼"),
    CoffeeMenu(
        menu_category = "커피(ICE)",
        name = "(ICE)바닐라라떼",
        price = 3200,
        Detail_page = True,
        type = "라떼"),
    CoffeeMenu(
        menu_category = "스무디&프라페",
        name = "쿠키프라페",
        price = 3900,
        Detail_page = True,
        type = "프라페"),
    CoffeeMenu(
        menu_category = "스무디&프라페",
        name = "민트프라페",
        price = 3900,
        Detail_page = True,
        type = "프라페"),
    CoffeeMenu(
        menu_category = "스무디&프라페",
        name = "리얼초코프라페",
        price = 3900,
        Detail_page = True,
        type = "프라페"),
    CoffeeMenu(
        menu_category = "스무디&프라페",
        name = "딸기쿠키프라페",
        price = 3900,
        Detail_page = True,
        type = "프라페"),
    CoffeeMenu(
        menu_category = "에이드&주스",
        name = "레몬에이드",
        price = 3500,
        Detail_page = True,
        type = "에이드"),
    CoffeeMenu(
        menu_category = "에이드&주스",
        name = "자몽에이드",
        price = 3500,
        Detail_page = True,
        type = "에이드"),
    CoffeeMenu(
        menu_category = "에이드&주스",
        name = "딸기주스",
        price = 3800,
        Detail_page = True,
        type = "주스"),
    CoffeeMenu(
        menu_category = "에이드&주스",
        name = "오곡바나나주스",
        price = 3800,
        Detail_page = True,
        type = "주스"),
    CoffeeMenu(
        menu_category = "티",
        name = "(HOT)녹차",
        price = 2500,
        Detail_page = True,
        type = "티"),
    CoffeeMenu(
        menu_category = "티",
        name = "(HOT)허니자몽블랙티",
        price = 3500,
        Detail_page = True,
        type = "티"),
    CoffeeMenu(
        menu_category = "티",
        name = "(ICE)녹차",
        price = 2500,
        Detail_page = True,
        type = "티"),
    CoffeeMenu(
        menu_category = "티",
        name = "(ICE)케모마일",
        price = 2500,
        Detail_page = True,
        type = "티"),
    CoffeeMenu(
        menu_category = "커피(콜드브루)",
        name = "(HOT)콜드브루오리지널",
        price = 3300,
        Detail_page = True,
        type = "콜드브루"),
    CoffeeMenu(
        menu_category = "커피(콜드브루)",
        name = "(ICE)콜드브루오리지널",
        price = 3300,
        Detail_page = True,
        type = "콜드브루"),
    CoffeeMenu(
        menu_category = "커피(콜드브루)",
        name = "(HOT)콜드브루라떼",
        price = 3800,
        Detail_page = True,
        type = "콜드브루"),
    CoffeeMenu(
        menu_category = "커피(콜드브루)",
        name = "(ICE)콜드브루라떼",
        price = 3800,
        Detail_page = True,
        type = "콜드브루"),
    CoffeeMenu(
        menu_category = "음료",
        name = "(HOT)고구마라떼",
        price = 3500,
        Detail_page = True,
        type = "음료"),
    CoffeeMenu(
        menu_category = "음료",
        name = "(ICE)흑당라떼(펄X)",
        price = 3000,
        Detail_page = True,
        type = "음료"),
    CoffeeMenu(
        menu_category = "음료",
        name = "(ICE)딸기라떼",
        price = 3500,
        Detail_page = True,
        type = "음료"),
    CoffeeMenu(
        menu_category = "음료",
        name = "(ICE)녹차라떼",
        price = 3500,
        Detail_page = True,
        type = "음료"),
    CoffeeMenu(
        menu_category = "디저트",
        name = "허니브레드",
        price = 4500,
        Detail_page = True,
        type = "디저트"),
    CoffeeMenu(
        menu_category = "디저트",
        name = "크로크무슈",
        price = 3800,
        Detail_page = True,
        type = "디저트"),
    CoffeeMenu(
        menu_category = "디저트",
        name = "생크림카스테라",
        price = 3300,
        Detail_page = True,
        type = "디저트"),
    CoffeeMenu(
        menu_category = "디저트",
        name = "아이스크림크로플",
        price = 3500,
        Detail_page = True,
        type = "디저트"),
    CoffeeMenu(
        menu_category = "병음료",
        name = "뽀로로딸기",
        price = 1500,
        Detail_page = False),
    CoffeeMenu(
        menu_category = "병음료",
        name = "뽀로로밀크",
        price = 1500,
        Detail_page = False),
    CoffeeMenu(
        menu_category = "병음료",
        name = "뽀로로보리차",
        price = 1500,
        Detail_page = False),
]


detali = [
    MenuDetail(
    option = "연하게",
    price = 0,
    type="아메리카노",    
    ),
    MenuDetail(
    option = "샷 추가",
    price = 500,
    type="아메리카노",     
    ),
    MenuDetail(
    option = "2샷 추가",
    price = 1000,
    type="아메리카노",     
    )
]
CoffeeMenu.objects.bulk_create(menu)
MenuDetail.objects.bulk_create(detali)