https://iss.moex.com/iss/reference/

v.0.14.1

ISS Queries

/iss/securities
Список бумаг торгуемых на московской бирже.

/iss/securities/[security]
Получить спецификацию инструмента. Например: https://iss.moex.com/iss/securities/IMOEX.xml

/iss/securities/[security]/indices
Список индексов в которые входит бумага

/iss/securities/[security]/aggregates
Агрегированные итоги торгов за дату по рынкам

/iss/engines/[engine]/markets/[market]/secstats
Промежуточные "Итоги дня". Только для фондового рынка

/iss/turnovers
Получить сводные обороты по рынкам. Например: https://iss.moex.com/iss/turnovers.xml

/iss/turnovers/columns
Получить описание полей для запросов оборотов по рынку/торговой системе. Например: https://iss.moex.com/iss/engines/stock/turnovers/columns.xml

/iss/engines/[engine]/turnovers
Получить текущее значение оборотов торговой сессии по рынкам торговой системы

/iss/engines/[engine]/markets/[market]/turnovers
Получить текущее значение оборота по рынку

/iss/engines/[engine]/markets/zcyc
Получить данные по кривой бескупонной доходности (Прекращены расчеты с 2018-01-03)

/iss/engines/[engine]/zcyc
/iss/index
Получить глобальные справочники ISS. Например: https://iss.moex.com/iss/index.xml

/iss/engines
Получить доступные торговые системы. Например: https://iss.moex.com/iss/engines.xml

/iss/history/engines/[engine]/markets/[market]/.*?listing/columns
Получить описание полей для запросов торгуемости бумаг (листинга)

/iss/history/engines/[engine]/markets/[market]/listing
Список неторгуемых инструментов с указанием интервалов торгуемости по режимам

/iss/history/engines/[engine]/markets/[market]/boards/[board]/listing
Получить данные по листингу бумаг в историческом разрезе по указанному режиму

/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/listing
Получить данные по листингу бумаг в историческом разрезе по указанной группе режимов

/iss/engines/[engine]
Получить описание и режим работы торговой системы. Например: https://iss.moex.com/iss/engines/stock.xml

/iss/history/engines/[engine]/markets/[market]/sessions
Список сессий доступных в итогах торгов. Только для фондового рынка!

/iss/history/engines/[engine]/markets/[market]/sessions/[session]/securities
Получить историю по всем бумагам на рынке за одну дату. Например: https://iss.moex.com/iss/history/engines/stock/markets/index/securities.xml?date=2010-11-22

/iss/engines/[engine]/markets/[market]/.*?orderbook/columns
Получить описание полей для запросов стакана котировок для рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/orderbook/columns.xml

/iss/history/engines/[engine]/markets/[market]/sessions/[session]/securities/[security]
Получить историю по одной бумаге на рынке за интервал дат.

/iss/history/engines/[engine]/markets/[market]/session/[session]/boardgroups/[boardgroup]/securities
Получить историю торгов для всех бумаг на указанной группе режимов торгов за указанную дату.

/iss/history/engines/[engine]/markets/[market]/sessions/[session]/boardgroups/[boardgroup]/securities/[security]
Получить историю торгов для указанной бумаги на выбранной группе режимов торгов за указанный интервал дат.

/iss/history/engines/[engine]/markets/[market]/sessions/[session]/boards/[board]/securities
Получить историю торгов для всех бумаг на указанном режиме торгов отфильтрованных по дате.

/iss/history/engines/[engine]/markets/[market]/sessions/[session]/boards/[board]/securities/[security]
Получить историю торгов для указанной бумаги на указанном режиме торгов за указанный интервал дат.

/iss/engines/[engine]/markets/[market]/.*?securities/columns
Получить описание полей для запросов публикуемых бумаг для рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/securities/columns.xml

/iss/history/engines/[engine]/markets/[market]/.*?securities/columns
Получить описание полей для запросов исторических данных по бумагам для рынка.

/iss/history/engines/[engine]/markets/[market]/.*?[securities]/columns
Получить описание полей для запросов исторических данных по бумагам для рынка.

/iss/engines/[engine]/markets
Получить список рынков торговой системы. Например: https://iss.moex.com/iss/engines/stock/markets.xml

/iss/statistics/engines/stock/securitieslisting
Таблица соответствия торгуемых ценных бумаг по режимам торгов

/iss/engines/[engine]/markets/[market]/.*?trades/columns
Получить описание полей для запроса сделок по рынку. Например: https://iss.moex.com/iss/engines/stock/markets/shares/trades/columns.xml

/iss/engines/[engine]/markets/[market]
Получить описание: словарь доступных режимов торгов, описание полей публикуемых таблиц данных и т.д. Например: https://iss.moex.com/iss/engines/stock/markets/shares.xml

/iss/engines/[engine]/markets/[market]/securities
Получить таблицу инструментов торговой сессии по рынку в целом. Например: https://iss.moex.com/iss/engines/stock/markets/shares/securities.xml

/iss/engines/[engine]/markets/[market]/securities/[security]
Получить данные по конкретному инструменту рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/securities/AFLT.xml

/iss/statistics/engines/stock/markets/index/analytics/columns
/iss/engines/[engine]/markets/[market]/securities/[security]/trades
Получить сделки по инструменту. Например: https://iss.moex.com/iss/engines/stock/markets/shares/securities/AFLT/trades.xml

/iss/statistics/engines/stock/markets/index/bulletins
Бюллетени для индексов

/iss/statistics/engines/stock/markets/index/rusfar
RUSFAR расшифровка показателей

/iss/engines/[engine]/markets/[market]/securities/[security]/orderbook
Получить стакан заявок по инструменту. Например: https://iss.moex.com/iss/engines/stock/markets/shares/securities/AFLT/orderbook.xml

/iss/engines/[engine]/markets/[market]/trades
Получить все сделки рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/trades.xml

/iss/engines/[engine]/markets/[market]/orderbook
Получить стаканы заявок всех инструментов рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/orderbook.xml

/iss/engines/[engine]/markets/[market]/boards
Получить справочник режимов торгов рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards.xml

/iss/engines/[engine]/markets/[market]/boards/[board]
Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml

/iss/engines/[engine]/markets/[market]/boards/[board]/securities
Получить таблицу инструментов по режиму торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.xml

/iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]
Получить данные по указанному инструменту на выбранном режиме торгов.

/iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]/trades
Получить все сделки указанного инструмента по выбранному режиму торгов.

/iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]/orderbook
Получить стакан котировок указанного инструмента по выбранному режиму торгов.

/iss/engines/[engine]/markets/[market]/securities/[security]/candles
Получить свечи указанного инструмента по дефолтной группе режимов.

/iss/engines/[engine]/markets/[market]/securities/[security]/candleborders
/iss/history/otc/providers/nsd/markets
Обобщенные данные ОТС ПФИ и РЕПО - список рынков.

/iss/history/otc/providers/nsd/markets/[market]/daily
Ежедневные обобщенные данные ОТС ПФИ и РЕПО.

/iss/history/otc/providers/nsd/markets/[market]/monthly
Ежедневные обобщенные данные ОТС ПФИ и РЕПО.

/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]/candleborders
/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]/candles
Получить свечи указанного инструмента по выбранной группе режимов торгов.

/iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]/candles
Получить свечи указанного инструмента по выбранному режиму торгов.

/iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]/candleborders
Получить период дат рассчитанных свечей.

/iss/engines/[engine]/markets/[market]/boards/[board]/trades
Получить все сделки по выбранному режиму торгов.

/iss/engines/[engine]/markets/[market]/boards/[board]/orderbook
Получить все лучшие котировки по выбранному режиму торгов.

/iss/engines/[engine]/markets/[market]/boardgroups
Получить справочник групп режимов торгов.

/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]
Получить описание группы режимов торгов.

/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities
Получить список всех инструментов, торгуемых на выбранной группе режимов торгов.

/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]
Получить данные по указанному инструменту, торгуемому на выбранной группе режимов торгов.

/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]/trades
Получить сделки выбранного инструмента, торгуемого на выбранной группе режимов торгов.

/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]/orderbook
Получить лучшие заявки выбранного инструмента, торгуемого на выбранной группе режимов торгов.

/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/trades
Получить сделки инструментов, торгуемых на выбранной группе режимов торгов.

/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/orderbook
Получить лучшие заявки всех инструментов, торгуемых на выбранной группе режимов торгов.

/iss/history/engines/stock/markets/shares/securities/changeover
Информация по техническому изменению торговых кодов

/iss/history/engines/stock/zcyc
История изменения параметров КБД (Кривая Бескупоной Доходности).

/iss/history/engines/[engine]/markets/[market]/securities
Получить историю по всем бумагам на рынке за одну дату. Например: https://iss.moex.com/iss/history/engines/stock/markets/index/securities.xml?date=2010-11-22

/iss/history/engines/[engine]/markets/[market]/yields
Получить историю рассчитанных доходностей для всех бумаг на указанном режиме торгов отфильтрованных по дате.

/iss/history/engines/[engine]/markets/[market]/dates
Получить даты, за которые доступны данные на указанных рынке и торговой системе.

/iss/history/engines/[engine]/markets/[market]/securities/[security]
Получить историю по одной бумаге на рынке за интервал дат.

/iss/history/engines/[engine]/markets/[market]/yields/[security]
Получить историю доходностей по одной бумаге на рынке за интервал дат.

/iss/history/engines/[engine]/markets/[market]/securities/[security]/dates
Получить интервал дат в истории для указанного рынка и бумаги.

/iss/history/engines/[engine]/markets/[market]/boards/[board]/dates
Получить интервал дат, доступных в истории для рынка по заданному режиму торгов.

/iss/history/engines/[engine]/markets/[market]/boards/[board]/securities
Получить историю торгов для всех бумаг на указанном режиме торгов отфильтрованных по дате.

/iss/history/engines/[engine]/markets/[market]/boards/[board]/yields
Получить историю доходностей для всех бумаг на указанном режиме торгов отфильтрованных по дате.

/iss/history/engines/[engine]/markets/[market]/boards/[board]/securities/[security]
Получить историю торгов для указанной бумаги на указанном режиме торгов за указанный интервал дат.

/iss/history/engines/[engine]/markets/[market]/boards/[board]/yields/[security]
Получить историю доходностей для указанной бумаги на указанном режиме торгов за указанный интервал дат.

/iss/history/engines/[engine]/markets/[market]/boards/[board]/securities/[security]/dates
Получить интервал дат в истории, за которые доступна указанная бумага на рынке на указанном режиме торгов.

/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/dates
Получить интервал дат для указанной группы режимов торгов.

/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities
Получить историю аукционов даркпул отфильтрованных по дате.

/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]
Получить историю аукционов даркпул за интервал дат.

/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities
Получить историю торгов для всех бумаг на указанной группе режимов торгов за указанную дату.

/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/yields
Получить доходности торгов для всех бумаг на указанной группе режимов торгов за указанную дату.

/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]
Получить историю торгов для указанной бумаги на выбранной группе режимов торгов за указанный интервал дат.

/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/yields/[security]
Получить историю доходностей для указанной бумаги на выбранной группе режимов торгов за указанный интервал дат.

/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]/dates
Получить интервал дат для указанной бумаги на заданной группе режимов торгов.

/iss/archives/engines/[engine]/markets/[market]/[datatype]/years
Список годов, за которые существуют ссылки на файлы с архивом сделок и исторической биржевой информацией. datatype может принимать значения securities или trades.

/iss/archives/engines/[engine]/markets/[market]/[datatype]/[period]
Получить список ccылок на годовые/месячные/дневные файлы с архивом сделок и исторической биржевой информацией. datatype может принимать значения securities или trades. period может принимать значения yearly, monthly или daily. Помесячные данные доступны только за последние 30 дней.

/iss/archives/engines/[engine]/markets/[market]/[datatype]/years/[year]/months
Список месяцев в году, за которые существуют ссылки на файлы с архивом сделок и исторической биржевой информацией. datatype может принимать значения securities или trades.

/iss/securitygroups
Группы ценных бумаг

/iss/securitygroups/[securitygroup]
Группа ценных бумаг

/iss/securitygroups/[securitygroup]/collections
Коллекции ценных бумаг входящие в группу

/iss/securitygroups/[securitygroup]/collections/[collection]
Коллекция ценных бумаг входящие в группу

/iss/securitygroups/[securitygroup]/collections/[collection]/securities
Описание инструментов

/iss/securitytypes
Типы ценных бумаг

/iss/securitytypes/[securitytype]
Справочник: тип ценной бумаги

/iss/statistics/engines/stock/markets/shares/correlations
Коэффициенты корелляции фондового рынка

/iss/statistics/engines/currency/markets/selt/rates
Курсы ЦБРФ

/iss/statistics/engines/stock/splits
Справочник дроблений и консолидаций бумаг фондового рынка

/iss/statistics/engines/stock/splits/[security]
/iss/statistics/engines/state/markets/repo/mirp
/iss/statistics/engines/state/markets/repo/dealers
/iss/statistics/engines/state/markets/repo/cboper
Средневзвешенные ставки по операциям центрального банка

/iss/statistics/engines/stock/deviationcoeffs
Показатели для определения критериев существенного отклонения

/iss/statistics/engines/stock/quotedsecurities
Cписок акций, по которым рассчитывается рыночная котировка

/iss/statistics/engines/stock/currentprices
Текущие цены бумаг

/iss/sitenews
Новости биржи

/iss/sitenews/[news_id]
Новость сайта

/iss/events
Мероприятия биржи

/iss/events/[event_id]
Контент мероприятия биржи

/iss/statistics/engines/stock/markets/bonds/aggregates
Агрегированные показатели рынка облигаций

/iss/statistics/engines/stock/markets/bonds/aggregates/columns
/iss/statistics/engines/stock/markets/index/analytics
Индексы фондового рынка

/iss/statistics/engines/stock/markets/index/analytics/[indexid]
Аналитические показатели за дату

/iss/statistics/engines/stock/markets/index/analytics/[indexid]/tickers
Список тикеров за все время торгов

/iss/statistics/engines/stock/markets/index/analytics/[indexid]/tickers/[ticker]
Информация по тикеру

/iss/statistics/engines/stock/capitalization
Капитализация фондового рынка

/iss/history/engines/stock/totals/boards
Список режимов обобщенной информации по фондовому рынку

/iss/history/engines/stock/totals/securities
Обобщенная информация по фондовому рынку

/iss/history/engines/stock/totals/boards/[board]/securities
Обобщенная информация по фондовому рынку по выбранному режиму

/iss/history/engines/stock/totals/boards/[board]/securities/[security]
Обобщенная информация по фондовому рынку по выбранному режиму и инструменту

/iss/rms/engines/[engine]/objects/irr
Индикаторы риска

/iss/rms/engines/[engine]/objects/irr/filters
Доступные параметры фильтрации для индикаторов рисков

/iss/statistics/engines/state/rates
/iss/statistics/engines/state/rates/columns
/iss/statistics/engines/[engine]/derivatives/[report_name]
Еженедельные отчеты по валютным деривативам: numtrades - Информация о количестве договоров по инструментам, являющимся производными финансовыми инструментами (по валютным парам) participants - Информация о количестве лиц, имеющих открытые позиции по инструментам, являющимся производными финансовыми инструментами (по валютным парам) openpositions - Информация об открытых позициях по инструментам, являющимся производными финансовыми инструментами (по валютным парам) expirationparticipants - Информация о количестве лиц, имеющих открытые позиции по договорам, являющимся производными финансовыми инструментами (по срокам экспирации) expirationopenpositions - Информация об объеме открытых позиций по договорам, являющимся производными финансовыми инструментами (по срокам экспирации)

/iss/statistics/engines/[engine]/monthly/[report_name]
/iss/statistics/engines/currency/markets/fixing/[security]
Фиксинги Московской биржи

/iss/statistics/engines/futures/markets/indicativerates/securities
Индикативные курсы валют срочного рынка

/iss/statistics/engines/futures/markets/indicativerates/securities/[security]
Индикативный курс валют срочного рынка

/iss/statistics/engines/currency/markets/fixing
Фиксинги Московской биржи

/iss/statistics/engines/[engine]/markets/[market]
Курсы переоценки коллатеральных инструментов

/iss/statistics/engines/[engine]/markets/[market]/securities
Курсы переоценки коллатеральных инструментов

/iss/statistics/engines/[engine]/markets/[market]/securities/[security]
Курсы переоценки коллатеральных инструментов. Инструмент за интервал дат.

/iss/analyticalproducts/netflow2/securities
/iss/analyticalproducts/netflow2/securities/[security]
/iss/analyticalproducts/futoi/securities
/iss/analyticalproducts/futoi/securities/[security]