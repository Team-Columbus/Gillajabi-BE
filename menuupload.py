from coffee_api.models import CoffeeMenu
from coffee_api.models import MenuDetail

# 메뉴카테고리에따라 정렬한 것임.
# 오프라인 매장 확인후 type과 Detail_page 수정할 것.

menu = [
# 커피(HOT)
    CoffeeMenu(
        menu_category = "커피(HOT)",
        name = "(HOT)아메리카노",
        price = 1500,
        Detail_page = True,
        type = "아메리카노",
        explanation = "(20oz)[기본 2샷] 메가MGC커피 블렌드 원두로 추출한 에스프레소에 물을 더해, 풍부한 바디감을 느낄 수 있는 스탠다드 커피."),
    CoffeeMenu( 
        menu_category = "커피(HOT)",
        name = "(HOT)꿀아메리카노",
        price = 2700,
        Detail_page = True,
        type = "꿀아메리카노",
        explanation = "(20oz) 아메리카노의 묵직한 바디감에 달콤한 사양벌꿀이 소프트하게 어우러진 커피"),

# 커피(ICE)

    CoffeeMenu(
        menu_category = "커피(ICE)",
        name = "(ICE)아메리카노",
        price = 2000,
        Detail_page = True,
        type = "아메리카노",
        explanation = "(20oz)[기본 2샷] 메가MGC커피 블렌드 원두로 추출한 에스프레소에 물을 더해, 풍부한 바디감을 느낄 수 있는 스탠다드 커피."),
    CoffeeMenu(
        menu_category = "커피(ICE)",
        name = "(ICE)꿀아메리카노",
        price = 2700,
        Detail_page = True,
        type = "꿀아메리카노",
        explanation = "(20oz) 아메리카노의 묵직한 바디감에 달콤한 사양벌꿀이 소프트하게 어우러진 커피"),

# 스무디&프라페

    CoffeeMenu(
        menu_category = "스무디&프라페",
        name = "쿠키프라페",
        price = 3900,
        Detail_page = True,
        type = "프라페",
        explanation = "(20oz) 오레오의 특유의 맛과 부드러운 우유, 그리고 바닐라 향의 조화를 느낄 수 있는 메가MGC커피 베스트 메뉴"),
    CoffeeMenu(
        menu_category = "스무디&프라페",
        name = "딸기쿠키프라페",
        price = 3900,
        Detail_page = True,
        type = "프라페",
        explanation = "(20oz)상큼한 딸기시럽과 바삭한 쿠키가 어우러진 프라페 위에 휘핑과 쿠키크런치를 토핑한 음료"),
    CoffeeMenu(
        menu_category = "스무디&프라페",
        name = "리얼초코프라페",
        price = 3900,
        Detail_page = True,
        type = "프라페",
        explanation = "(20oz)진한 초코소스와 바닐라향이 더해져 씹는 재미가 있는 달콤한 프라페"),

# 에이드 & 주스

    CoffeeMenu(
        menu_category = "에이드&주스",
        name = "레몬에이드",
        price = 3500,
        Detail_page = True,
        type = "에이드",
        explanation = "(24oz) 레몬의 상큼함과 달콤함 그리고 탄산의 청량감을 즐길 수 있는 음료"),
    CoffeeMenu(
        menu_category = "에이드&주스",
        name = "자몽에이드",
        price = 3800,
        Detail_page = True,
        type = "에이드",
        explanation = "(24oz)자몽의 쌉싸름한 맛과 상큼함을 동시에 느낄 수 있는 음료"),
    CoffeeMenu(
        menu_category = "에이드&주스",
        name = "딸기주스",
        price = 3500,
        Detail_page = True,
        type = "꿀",
        explanation = "(20oz) 피쉬 콜라겐 500mg을 더한 산뜻한 맛과 향의 딸기 주스"),

# 티

    CoffeeMenu(
        menu_category = "티",
        name = "(HOT)녹차",
        price = 2500,
        Detail_page = True,
        type = "꿀",
        explanation = "(24oz)고소한 감칠맛과 부드러운 목넘김이 국내산 녹차"),
    CoffeeMenu(
        menu_category = "티",
        name = "(HOT)허니자몽블랙티",
        price = 3500,
        Detail_page = True,
        type = "꿀",
        explanation = "(24oz) 달콤한 꿀청에 재운 자몽에 홍차의 부드러움을 어우른 상큼한 과일티"),
    CoffeeMenu(
        menu_category = "티",
        name = "(ICE)녹차",
        price = 2500,
        Detail_page = True,
        type = "꿀",
        explanation = "(24oz)고소한 감칠맛과 부드러운 목넘김이 국내산 녹차"),
    CoffeeMenu(
        menu_category = "티",
        name = "(ICE)케모마일",
        price = 2500,
        Detail_page = True,
        type = "꿀",
        explanation = "(24oz)특유의 플내음을 통해 마음을 진정 시켜주는 마일드한 허브차"),

# 음료

    CoffeeMenu(
        menu_category = "음료",
        name = "(HOT)고구마라떼",
        price = 3500,
        Detail_page = True,
        type = "라떼",
        explanation = "(20oz) 달콤한 고구마와 부드러운 우유의 만남. 남녀노소 좋아하는 인기메뉴"),
    CoffeeMenu(
        menu_category = "음료",
        name = "(ICE)딸기라떼",
        price = 3000,
        Detail_page = True,
        type = "라떼",
        explanation = "(20oz)산뜻하고 달콤한 딸기가 부드러운 우유 속에 어우러져 더욱 상큼하게 즐기는 아이스라떼"),
]



detali = [
 # 농도,스테비아
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
    ),
    MenuDetail(
    option = "스테비아 추가",
    price = 600,
    type="아메리카노",
    ),

# 농도, 꿀
    MenuDetail(
    option = "연하게",
    price = 0,
    type="꿀아메리카노",    
    ),
    MenuDetail(
    option = "샷 추가",
    price = 500,
    type="꿀아메리카노",     
    ),
    MenuDetail(
    option = "2샷 추가",
    price = 1000,
    type="꿀아메리카노",
    ),
    MenuDetail(
    option = "꿀 추가",
    price = 700,
    type="꿀아메리카노",
    ),

# 스테비아,꿀, 우유
    MenuDetail(
    option = "스테비아 변경",
    price = 300,
    type="라떼",    
    ),
    MenuDetail(
    option = "꿀 추가",
    price = 700,
    type="라떼",     
    ),
    MenuDetail(
    option = "아몬드밀크변경",
    price = 500,
    type="라떼",
    ),
    MenuDetail(
    option = "오트밀크변경",
    price = 500,
    type="라떼",
    ),

# 스테비아, 꿀, 제로사이다
    MenuDetail(
    option = "스테비아 변경",
    price = 0,
    type="에이드",    
    ),
    MenuDetail(
    option = "꿀 추가",
    price = 500,
    type="에이드",     
    ),
    MenuDetail(
    option = "제로사이다 변경",
    price = 500,
    type="에이드",
    ),

# 휘핑, 꿀
MenuDetail(
    option = "휘핑 O",
    price = 0,
    type="프라페",    
    ),
    MenuDetail(
    option = "휘핑 X",
    price = 0,
    type="프라페",     
    ),
    MenuDetail(
    option = "꿀 추가",
    price = 700,
    type="프라페",
    ),

# 꿀
    MenuDetail(
    option = "꿀 추가",
    price = 700,
    type="꿀",    
    ),
]
CoffeeMenu.objects.bulk_create(menu)
MenuDetail.objects.bulk_create(detali)