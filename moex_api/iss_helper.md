Reminder of ISS MOEX categories and how to make urls 

SECID Specification
https://iss.moex.com/iss/securities/IMOEX.xml?lang=en


engines:
   id (int32)	name (string:45)	title (string:765)
1	stock	Фондовый рынок и рынок депозитов
2	state	Рынок ГЦБ (размещение)
3	currency	Валютный рынок
4	futures	Срочный рынок
5	commodity	Товарный рынок
6	interventions	Товарные интервенции
7	offboard	ОТС-система
9	agro	Агро

markets:

id (int32)	NAME (string:45)	title (string:765)
5	index	Индексы фондового рынка
1	shares	Рынок акций
2	bonds	Рынок облигаций
4	ndm	Режим переговорных сделок
29	otc	ОТС
27	ccp	РЕПО с ЦК
35	deposit	Депозиты с ЦК
3	repo	Рынок сделок РЕПО
28	qnv	Квал. инвесторы
36	mamc	Мультивалютный рынок смешанных активов
47	foreignshares	Иностранные ц.б.
49	foreignndm	Иностранные ц.б. РПС
33	moexboard	MOEX Board
46	gcc	РЕПО с ЦК с КСУ
54	credit	Рынок кредитов
23	standard	Standard
25	classica	Classica




/iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]
Get data for the specified security on the specified board.

/iss/engines/[engine]/markets/[market]/securities/[security]
Get metadata and market data for the specified security on the specified market. 
Example: https://iss.moex.com/iss/engines/stock/markets/shares/securities/AFLT.xml?lang=en


securitygroups
https://iss.moex.com//iss/securitygroups.csv

/iss/sitenews
Exchange news

/iss/sitenews/[news_id]
A site news

/iss/events
Exchange activities

/iss/events/[event_id]

Exchange activity content

id;name;title;is_hidden
12;stock_index;Индексы;0
4;stock_shares;Акции;0
3;stock_bonds;Облигации;0
9;currency_selt;Валюта;0
10;futures_forts;Фьючерсы;0
26;futures_options;Опционы;0
18;stock_dr;Депозитарные расписки;0
33;stock_foreign_shares;Иностранные ц.б.;0
6;stock_eurobond;Еврооблигации;0
5;stock_ppif;Паи ПИФов;0
20;stock_etf;Биржевые фонды;0
24;currency_metal;Драгоценные металлы;0
21;stock_qnv;Квал. инвесторы;0
27;stock_gcc;Клиринговые сертификаты участия;0
29;stock_deposit;Депозиты с ЦК;0
17;currency_basket;Бивалютная корзина;1
28;currency_futures;Валютный фьючерс;0
31;currency_indices;Валютные фиксинги;0
40;agro_commodities;Товарные активы;0
22;stock_mortgage;Ипотечный сертификат;1

https://iss.moex.com/iss/securities?q=&group_by_filter=stock_foreign_shares
