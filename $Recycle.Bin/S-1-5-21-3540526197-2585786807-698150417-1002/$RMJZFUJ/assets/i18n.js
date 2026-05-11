// НОМИН Холдинг — i18n Translation System v1
// Supports: mn (Монгол), en (English), ru (Русский)
window.NominI18n = (function(){

const T = {
  mn: {
    // UTIL BAR
    util_supplier: 'Нийлүүлэгч',
    util_careers:  'Ажлын байр',
    util_news:     'Мэдээ мэдээлэл',
    util_stores:   'Салбар байршил',
    util_tender:   'Худалдан авалт',
    util_contact:  'Холбоо барих',
    // NAV
    nav_about:     'Бидний тухай',
    nav_business:  'Бизнес',
    nav_brands:    'Брэнд',
    nav_social:    'Нийгмийн хариуцлага',
    nav_supplier:  'Нийлүүлэгч',
    nav_catalogue: 'Группын танилцуулга',
    // ABOUT DROPDOWN
    dd_intro:      'Танилцуулга',
    dd_mission:    'Бидний зорилго',
    dd_history:    'Түүхэн замнал',
    dd_leadership: 'Удирдлагын баг',
    dd_why:        'Биднийг сонгох шалтгаан',
    dd_awards:     'Шагнал, өргөмжлөл',
    // BUSINESS DROPDOWN
    dd_retail:     'Борлуулалт үйлчилгээ',
    dd_import:     'Импорт / Экспорт',
    dd_finance:    'Санхүү & Даатгал',
    dd_construction:'Барилга / Үл хөдлөх',
    dd_tech:       'Технологи',
    dd_aviation:   'Агаарын тээвэр',
    // HERO SLIDES
    hero_cat1: 'Шагнал', hero_title1: '"Номин Холдинг" ХХК "Entrepreneur-2025"-аас Оны шилдэг аж ахуйн нэгжээр шалгарлаа', hero_link: 'Дэлгэрэнгүй унших',
    hero_cat2: 'Компанийн мэдээ', hero_title2: '6000+ Номинчууд — Амжилтаа хамтдаа тэмдэглэв',
    hero_cat3: 'Ойн тэмдэглэл', hero_title3: 'Итгэл дээр бүтсэн 25 жил — "Номин Даатгал" ХХК',
    hero_cat4: 'Шинэ үйлчилгээ', hero_title4: 'Chingis Airlines — Монголын тэнгэрт шинэ дэвшил',
    // STATS
    stat1_n:'32+', stat1_l:'Жил туршлага',
    stat2_n:'6,200+', stat2_l:'Ажилтан',
    stat3_n:'260+', stat3_l:'Брэнд',
    stat4_n:'34', stat4_l:'Охин компани',
    stat5_n:'800K+', stat5_l:'Бонус карт',
    stat6_n:'2M+', stat6_l:'Үйлчлүүлэгч',
    // NEWS
    sec_news_label: 'Мэдээ мэдээлэл', sec_news_title: 'Шинэ мэдээ', view_all: 'Бүгдийг үзэх',
    news_feat_cat: 'Онцлох', news_feat_title: '"Номин Холдинг" ХХК шилдгүүдийн хамт тугаа мандууллаа — Entrepreneur 2025', news_feat_date: '2026 оны 3 дугаар сарын 13',
    news_sm1_cat: 'Урамшуулал', news_sm1_title: '"Цалгим Халгим" урамшуулал — супер азтангуудаа хүлээн авлаа', news_sm1_date: '2026 оны 3 дугаар сарын 13',
    news_sm2_cat: 'Ойн тэмдэглэл', news_sm2_title: 'Итгэл дээр бүтсэн 25 жил — "Номин Даатгал" ХХК-ийн ой', news_sm2_date: '2026 оны 1 дүгээр сарын 23',
    // WHO
    who_label: 'Бидний тухай', who_title: 'Бид хэн бэ?',
    who_p1: '"НОМИН Холдинг" 1992 онд байгуулснаас хойш 450 гаруй мэргэжлийн чиглэлээр 6,200 гаруй ажлын байрыг бий болгож Монгол Улсын Хөдөлмөрийн зах зээлийн 6%-г бүрдүүлж байна.',
    who_p2: 'Бид үйл ажиллагаа эрхэлж эхэлсэн цагаас өнөөг хүртэл нийт 700 гаруй тэрбум төгрөгийн татвар, шимтгэлийг Улсын төсөвт төвлөрүүлсэн байна.',
    who_btn1: 'Танилцуулга үзэх', who_btn2: 'Каталог татах',
    // WHAT
    what_label: 'Бизнесийн чиглэл', what_title: 'Бид юу хийдэг вэ?',
    what_p1: '5 чиглэлд — Борлуулалт, Санхүү, Импорт Экспорт, Технологи, Үйлдвэрлэл Инженерингийн 34 салбар компанитайгаар үйл ажиллагаагаа явуулсаар байна.',
    what_p2: 'Электрон, хүнсний бараа, хөнгөлөлтийн карт, барилгын материал, онлайн худалдаа зэрэг шинэ үйлчилгээг Монголд анх удаа нэвтрүүлсэн.',
    what_btn: 'Дэлгэрэнгүй',
    // AIM
    aim_label: 'Бидний зорилго', aim_title: 'Бид юуг зорьдог вэ?',
    aim_p1: 'Хэрэглэгч, түншүүдээ эрхэмлэн дээдэлж, зорьсон бизнесээ дээд зэргийн чанар хурдтайгаар эрхэлдэг, эх орныхоо хөгжил дэвшилд бодитой хувь нэмрээ оруулдаг манлайлагч компани байхыг зорьдог.',
    aim_p2: 'Олон улсын хэмжээнд үйл ажиллагаа нь түгсэн, <strong>Бадрангуй Тэмүүлэлтэй Манлайлагч</strong> компани болох нь бидний алсын зорилго юм.',
    aim_btn: 'Бидний эрхэм зорилго',
    // NEWS LIST
    newslist_label: 'Сүүлийн мэдээ', newslist_title: 'Шинээр нэмэгдсэн мэдээ',
    nl1_cat:'Компанийн мэдээ', nl1_title:'"ЦАЛГИМ ХАЛГИМ" урамшуулал — азтангуудаа хүлээн авлаа', nl1_sub:'Хайнанд аялах эрх болон iPhone 17 Pro Max зэрэг бэлгүүдийг гардан авлаа.', nl1_date:'2026-03-13',
    nl2_cat:'Шагнал', nl2_title:'"Номин Холдинг" ХХК шилдгүүдийн хамт тугаа мандууллаа', nl2_sub:'Монголын ҮХАҮТ-аас зохион байгуулсан "Энтрепренер–2025" арга хэмжээ.', nl2_date:'2026-03-13',
    nl3_cat:'Ойн тэмдэглэл', nl3_title:'Итгэл дээр бүтсэн 25 жил — "Номин Даатгал"', nl3_sub:'"Номин Даатгал" ХХК үүсгэн байгуулагдсаны 25 жилийн ой.', nl3_date:'2026-01-23',
    nl4_cat:'Компанийн мэдээ', nl4_title:'"6000+ НОМИНЧУУД — АМЖИЛТАА ХАМТДАА ТЭМДЭГЛЭВ"', nl4_sub:'ТОП 100 ААН-д 24 дэх жилдээ багтаж, шилдэг 10-д шалгарлаа.', nl4_date:'2026-01-02',
    nl5_cat:'Шилдэг ААН', nl5_title:'"Entrepreneur-2025"-аас Оны шилдэг аж ахуйн нэгж', nl5_sub:'Монгол Улсын эдийн засгийн хөгжилд оруулж буй хувь нэмрийг бататгалаа.', nl5_date:'2025-12-24',
    news_more: 'Мэдээ мэдээлэл рүү зочлох',
    // CARD
    card_label: 'Лояалти хөтөлбөр', card_title: 'НОМИН бонус карт',
    card_p: 'НОМИН бонус карт нь Номин-ийн бүх салбар дэлгүүрээс хийх худалдан авалт бүрдээ 3–10% хүртэлх бонус оноог цуглуулан, дараагийн худалдан авалтдаа зарцуулах боломжтой Монголын хамгийн том лояалти хөтөлбөр юм.',
    card_btn: 'Дэлгэрэнгүй мэдэх',
    // CAREERS
    careers_label: 'Карьер', careers_title: 'Таныг ажилд урьж байна',
    careers_p: 'Хэрэв та нээлттэй ажлын байрны дэлгэрэнгүй мэдээлэл авахыг хүсэж байвал доорх товч дарна уу. Номин Холдинг нь ажилчдынхаа хөгжлийг эрхэмлэдэг Монголын тэргүүлэгч ажил олгогч юм.',
    careers_btn1: 'Ажлын байр харах', careers_btn2: 'Анкет илгээх',
    // SOCIAL
    social_title: 'Сошиал хаяг',
    // FOOTER
    ft_about: 'Бидний Тухай', ft_business: 'Бидний Бизнес', ft_contact_title: 'Холбоо барих',
    ft_desc: '1992 оноос хойш Монголын эдийн засгийг тэргүүлж, иргэдэд чанартай бараа, үйлчилгээ хүргэж буй холдинг компани.',
    ft_intro:'Танилцуулга', ft_president:'Ерөнхийлөгчийн мэндчилгээ', ft_directors:'Захирлууд', ft_history:'Түүхэн замнал', ft_awards:'Шагнал, Өргөмжлөл',
    ft_structure:'Бүтэц', ft_retail:'Борлуулалт', ft_import:'Импорт / Экспорт', ft_fin:'Санхүү / Даатгал', ft_build:'Барилга / Үл хөдлөх', ft_tech:'Технологи',
    ft_terms:'Үйлчилгээний нөхцөл', ft_privacy:'Нууцлалын бодлого', ft_sitemap:'Site Index', ft_contacts:'Холбоо барих',
    ft_copy:'Copyright © 2025 Nomin Holding. All rights reserved.',
    // CHAT
    chat_name:'Номин Туслах', chat_status:'Онлайн байна', chat_placeholder:'Асуулт бичнэ үү...',
    chat_welcome:'Сайн байна уу! Номин Холдингийн туслахтай холбогдлоо. Үйлчилгээ, байршил, мэдээллийн талаар асуугаарай.',
    // SEARCH
    search_placeholder:'Хайх...', search_hint:'Ctrl+K — хайлт нээх / Esc — хаах',
    stag1:'Бонус карт', stag2:'E-Shop', stag3:'Карьер', stag4:'Дэлгүүр байршил', stag5:'Century 21', stag6:'Тендер',
  },

  en: {
    util_supplier:'Suppliers', util_careers:'Careers', util_news:'Newsroom', util_stores:'Store Locator', util_tender:'Procurement', util_contact:'Contact Us',
    nav_about:'About Us', nav_business:'Business', nav_brands:'Brands', nav_social:'Social Responsibility', nav_supplier:'Suppliers', nav_catalogue:'Group Introduction',
    dd_intro:'Introduction', dd_mission:'Our Mission', dd_history:'History', dd_leadership:'Leadership Team', dd_why:'Why Choose Us', dd_awards:'Awards',
    dd_retail:'Retail & Services', dd_import:'Import / Export', dd_finance:'Finance & Insurance', dd_construction:'Construction / Real Estate', dd_tech:'Technology', dd_aviation:'Aviation & Transport',
    hero_cat1:'Award', hero_title1:'Nomin Holding LLC Named Company of the Year at Entrepreneur 2025', hero_link:'Read More',
    hero_cat2:'Company News', hero_title2:'6000+ Nominchuud — Celebrating Success Together',
    hero_cat3:'Anniversary', hero_title3:'25 Years Built on Trust — Nomin Insurance LLC',
    hero_cat4:'New Service', hero_title4:'Chingis Airlines — A New Era in Mongolian Aviation',
    stat1_n:'32+', stat1_l:'Years of Experience', stat2_n:'6,200+', stat2_l:'Employees', stat3_n:'260+', stat3_l:'Brands', stat4_n:'34', stat4_l:'Subsidiaries', stat5_n:'800K+', stat5_l:'Bonus Cards', stat6_n:'2M+', stat6_l:'Customers',
    sec_news_label:'Newsroom', sec_news_title:'Latest News', view_all:'View All',
    news_feat_cat:'Featured', news_feat_title:'Nomin Holding LLC Wins Top Company Award at Entrepreneur 2025', news_feat_date:'March 13, 2026',
    news_sm1_cat:'Promotion', news_sm1_title:'"Tsalgim Halgim" Lunar New Year Promotion — Winners Announced', news_sm1_date:'March 13, 2026',
    news_sm2_cat:'Anniversary', news_sm2_title:'25 Years Built on Trust — Nomin Insurance Anniversary', news_sm2_date:'January 23, 2026',
    who_label:'About Us', who_title:'Who We Are',
    who_p1:'Since its founding in 1992, NOMIN Holding has created over 6,200 jobs across 450+ professional fields, contributing 6% to Mongolia\'s labor market and 0.5% to national GDP tax revenue.',
    who_p2:'Since inception, we have contributed over 700 billion MNT in taxes and social contributions to the state budget.',
    who_btn1:'View Introduction', who_btn2:'Download Catalogue',
    what_label:'Business Areas', what_title:'What We Do',
    what_p1:'We operate 34 subsidiary companies across 5 business areas: Retail, Finance, Import-Export, Technology, and Manufacturing & Engineering.',
    what_p2:'We pioneered many firsts in Mongolia: electronics retail chains, loyalty cards, construction materials hypermarkets, and online shopping platforms.',
    what_btn:'Learn More',
    aim_label:'Our Vision', aim_title:'What We Aspire To',
    aim_p1:'We strive to be a leading company that values our customers and partners, operates our businesses with the highest quality and speed, and makes a tangible contribution to our country\'s development.',
    aim_p2:'Our vision is to become a globally recognized, <strong>Boldly Ambitious Leader</strong> whose operations extend beyond borders.',
    aim_btn:'Our Mission',
    newslist_label:'Latest News', newslist_title:'Recently Added News',
    nl1_cat:'Company News', nl1_title:'"Tsalgim Halgim" Lunar Promotion — Winners Claim Prizes', nl1_sub:'Winners received a trip to Hainan Island and iPhone 17 Pro Max among other prizes.', nl1_date:'2026-03-13',
    nl2_cat:'Award', nl2_title:'Nomin Holding Hoists Its Flag Among the Best', nl2_sub:'At the Entrepreneur-2025 event organized by the Mongolian employers association.', nl2_date:'2026-03-13',
    nl3_cat:'Anniversary', nl3_title:'25 Years Built on Trust — Nomin Insurance', nl3_sub:'Nomin Insurance LLC celebrates its 25th founding anniversary this year.', nl3_date:'2026-01-23',
    nl4_cat:'Company News', nl4_title:'"6000+ NOMINCHUUD — WE CELEBRATE SUCCESS TOGETHER"', nl4_sub:'In the TOP 100 for 24th consecutive year, ranked in top 10 companies of 2025.', nl4_date:'2026-01-02',
    nl5_cat:'Top Company', nl5_title:'Nomin Holding Named Company of the Year at Entrepreneur-2025', nl5_sub:'Affirming our contribution to the economic development of Mongolia.', nl5_date:'2025-12-24',
    news_more:'Visit Newsroom',
    card_label:'Loyalty Program', card_title:'NOMIN Bonus Card',
    card_p:'The NOMIN Bonus Card is Mongolia\'s largest loyalty program, allowing cardholders to earn 3–10% bonus points on every purchase at any Nomin branch or partner store, redeemable on future purchases.',
    card_btn:'Learn More',
    careers_label:'Careers', careers_title:'We\'re Hiring',
    careers_p:'If you would like detailed information about open positions, click the button below. Nomin Holding is Mongolia\'s leading employer committed to developing its people.',
    careers_btn1:'View Openings', careers_btn2:'Submit CV',
    social_title:'Social Media',
    ft_about:'About Us', ft_business:'Our Business', ft_contact_title:'Contact',
    ft_desc:'Mongolia\'s leading holding company since 1992, delivering quality goods and services to the people.',
    ft_intro:'Introduction', ft_president:'President\'s Message', ft_directors:'Board of Directors', ft_history:'History', ft_awards:'Awards',
    ft_structure:'Structure', ft_retail:'Retail', ft_import:'Import / Export', ft_fin:'Finance / Insurance', ft_build:'Construction / Real Estate', ft_tech:'Technology',
    ft_terms:'Terms of Service', ft_privacy:'Privacy Policy', ft_sitemap:'Site Index', ft_contacts:'Contact Us',
    ft_copy:'Copyright © 2025 Nomin Holding. All rights reserved.',
    chat_name:'Nomin Assistant', chat_status:'Online', chat_placeholder:'Ask a question...',
    chat_welcome:'Hello! You are connected with Nomin Holding\'s assistant. Feel free to ask about our services, locations, or information.',
    search_placeholder:'Search...', search_hint:'Ctrl+K — open search / Esc — close',
    stag1:'Bonus Card', stag2:'E-Shop', stag3:'Careers', stag4:'Store Locator', stag5:'Century 21', stag6:'Tender',
  },

  ru: {
    util_supplier:'Поставщикам', util_careers:'Вакансии', util_news:'Новости', util_stores:'Магазины', util_tender:'Закупки', util_contact:'Контакты',
    nav_about:'О нас', nav_business:'Бизнес', nav_brands:'Бренды', nav_social:'Социальная ответственность', nav_supplier:'Поставщикам', nav_catalogue:'Презентация группы',
    dd_intro:'Введение', dd_mission:'Наша миссия', dd_history:'История', dd_leadership:'Руководство', dd_why:'Почему выбирают нас', dd_awards:'Награды',
    dd_retail:'Розничная торговля', dd_import:'Импорт / Экспорт', dd_finance:'Финансы & Страхование', dd_construction:'Строительство / Недвижимость', dd_tech:'Технологии', dd_aviation:'Авиация и Транспорт',
    hero_cat1:'Награда', hero_title1:'АО «Номин Холдинг» признано Компанией года на Entrepreneur 2025', hero_link:'Подробнее',
    hero_cat2:'Новости компании', hero_title2:'6000+ сотрудников Номин — Отмечаем успех вместе',
    hero_cat3:'Юбилей', hero_title3:'25 лет, построенных на доверии — «Номин Страхование»',
    hero_cat4:'Новый сервис', hero_title4:'Chingis Airlines — Новая эра монгольской авиации',
    stat1_n:'32+', stat1_l:'Лет опыта', stat2_n:'6 200+', stat2_l:'Сотрудников', stat3_n:'260+', stat3_l:'Брендов', stat4_n:'34', stat4_l:'Дочерних компаний', stat5_n:'800K+', stat5_l:'Бонусных карт', stat6_n:'2M+', stat6_l:'Клиентов',
    sec_news_label:'Новости', sec_news_title:'Последние новости', view_all:'Все новости',
    news_feat_cat:'Главное', news_feat_title:'«Номин Холдинг» завоевал звание Компании года на Entrepreneur 2025', news_feat_date:'13 марта 2026',
    news_sm1_cat:'Акция', news_sm1_title:'Акция «Цалгим Халгим» — объявлены победители', news_sm1_date:'13 марта 2026',
    news_sm2_cat:'Юбилей', news_sm2_title:'25 лет на доверии — юбилей «Номин Страхование»', news_sm2_date:'23 января 2026',
    who_label:'О нас', who_title:'Кто мы?',
    who_p1:'С момента основания в 1992 году «НОМИН Холдинг» создал более 6 200 рабочих мест по 450+ специальностям, обеспечивая 6% рынка труда Монголии и 0,5% налоговых поступлений в ВВП.',
    who_p2:'За всё время деятельности мы перечислили в государственный бюджет свыше 700 млрд тугриков в виде налогов и социальных взносов.',
    who_btn1:'Смотреть презентацию', who_btn2:'Скачать каталог',
    what_label:'Направления бизнеса', what_title:'Чем мы занимаемся?',
    what_p1:'Мы работаем в 5 направлениях через 34 дочерних компании: Розничная торговля, Финансы, Импорт-Экспорт, Технологии и Инжиниринг.',
    what_p2:'Мы первыми в Монголии запустили сети электронных магазинов, карты лояльности, гипермаркеты стройматериалов и онлайн-торговлю.',
    what_btn:'Подробнее',
    aim_label:'Наше видение', aim_title:'К чему мы стремимся?',
    aim_p1:'Мы стремимся быть ведущей компанией, которая ценит клиентов и партнёров, ведёт бизнес с высочайшим качеством и вносит реальный вклад в развитие страны.',
    aim_p2:'Наша цель — стать <strong>Дерзко Амбициозным Лидером</strong> с международным присутствием.',
    aim_btn:'Наша миссия',
    newslist_label:'Последние новости', newslist_title:'Недавно добавленные новости',
    nl1_cat:'Новости компании', nl1_title:'Акция «Цалгим Халгим» — победители получили призы', nl1_sub:'Победители получили путёвку на Хайнань и iPhone 17 Pro Max.', nl1_date:'2026-03-13',
    nl2_cat:'Награда', nl2_title:'«Номин Холдинг» в числе лучших компаний страны', nl2_sub:'На мероприятии «Entrepreneur-2025» Монгольской ассоциации работодателей.', nl2_date:'2026-03-13',
    nl3_cat:'Юбилей', nl3_title:'25 лет на доверии — «Номин Страхование»', nl3_sub:'«Номин Страхование» отмечает 25-летие со дня основания.', nl3_date:'2026-01-23',
    nl4_cat:'Новости компании', nl4_title:'"6000+ НОМИНЦЕВ — ОТМЕЧАЕМ УСПЕХ ВМЕСТЕ"', nl4_sub:'24-й год в ТОП-100 компаний, вошли в топ-10 лучших предприятий 2025 года.', nl4_date:'2026-01-02',
    nl5_cat:'Лучшее предприятие', nl5_title:'Компания года по итогам Entrepreneur-2025', nl5_sub:'Подтверждён вклад в экономическое развитие Монголии.', nl5_date:'2025-12-24',
    news_more:'Перейти в новости',
    card_label:'Программа лояльности', card_title:'Бонусная карта НОМИН',
    card_p:'Бонусная карта НОМИН — крупнейшая программа лояльности в Монголии. Накапливайте 3–10% бонусных баллов при каждой покупке в сети магазинов Номин и тратьте их на следующие покупки.',
    card_btn:'Узнать больше',
    careers_label:'Карьера', careers_title:'Приглашаем на работу',
    careers_p:'Если вас интересуют открытые вакансии, нажмите кнопку ниже. «Номин Холдинг» — ведущий работодатель Монголии, ценящий профессиональное развитие сотрудников.',
    careers_btn1:'Смотреть вакансии', careers_btn2:'Отправить резюме',
    social_title:'Социальные сети',
    ft_about:'О компании', ft_business:'Наш бизнес', ft_contact_title:'Контакты',
    ft_desc:'Ведущая холдинговая компания Монголии с 1992 года, обеспечивающая качественными товарами и услугами.',
    ft_intro:'Введение', ft_president:'Обращение президента', ft_directors:'Совет директоров', ft_history:'История', ft_awards:'Награды',
    ft_structure:'Структура', ft_retail:'Розница', ft_import:'Импорт / Экспорт', ft_fin:'Финансы / Страхование', ft_build:'Строительство / Недвижимость', ft_tech:'Технологии',
    ft_terms:'Условия использования', ft_privacy:'Политика конфиденциальности', ft_sitemap:'Карта сайта', ft_contacts:'Контакты',
    ft_copy:'© 2025 Номин Холдинг. Все права защищены.',
    chat_name:'Помощник Номин', chat_status:'Онлайн', chat_placeholder:'Задайте вопрос...',
    chat_welcome:'Здравствуйте! Вы подключились к помощнику Номин Холдинг. Спрашивайте об услугах, расположении магазинов или любой другой информации.',
    search_placeholder:'Поиск...', search_hint:'Ctrl+K — открыть поиск / Esc — закрыть',
    stag1:'Бонусная карта', stag2:'Интернет-магазин', stag3:'Вакансии', stag4:'Магазины', stag5:'Century 21', stag6:'Тендер',
  }
};

let current = localStorage.getItem('nomin_lang') || 'mn';

function t(key){ return (T[current] && T[current][key]) || T['mn'][key] || key; }

function apply(){
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const k = el.dataset.i18n;
    if(el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') el.placeholder = t(k);
    else el.innerHTML = t(k);
  });
  // active lang button
  document.querySelectorAll('.lang-btn').forEach(b => {
    b.classList.toggle('act', b.dataset.lang === current);
  });
  // html lang attr
  document.documentElement.lang = current === 'mn' ? 'mn' : current === 'ru' ? 'ru' : 'en';
}

function setLang(lang){
  current = lang;
  localStorage.setItem('nomin_lang', lang);
  apply();
}

// expose
return { t, setLang, apply, current: () => current };
})();
