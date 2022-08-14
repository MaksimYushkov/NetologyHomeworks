--Insert запросы 
insert into genres values (1,'Рок'), (2, 'Поп'), (3, 'Джазз'), (4, 'Хип-хоп'), (5,'Шансон');

insert into musicians values (1,'Eminem'), (2, 'Red Hot Chili Peppers'), (3, 'Звери'), 
(4, 'Louis Armstrong'), (5,'Бутырка'), (6,'Nickelback'), (7, 'Miyagi'), (8, 'Рита Дакота');

insert into albums values (1,'Recovery', 2010), (2, 'Unlimited Love', 2022), (3, 'Акустика', 2009), 
(4, 'Ella and Louis', 1956), (5,'Хулиган', 2010), (6,'Feed the machine', 2018), 
(7, 'Yamakasi', 2020), (8, 'Стаи китов', 2020);

insert into tracks values (1, 'Cold wind blows', '00:05:04', 1), (2, 'Seduction', '00:04:36', 1),
(3, 'Black Summer', '00:03:53', 2), (4, 'The great apes', '00:05:01', 2),
(5, 'Я с тобой', '00:04:30', 3), (6, 'Для тебя', '00:04:36', 3),
(7, 'Moonlight in Vermont', '00:03:39', 4), (8, 'A foggy day', '00:04:31', 4),
(9, 'Временно', '00:03:48', 5), (10, 'До дона', '00:04:34', 5),
(11, 'Feed the machine', '00:05:00', 6), (12, 'Song on fire', '00:03:50', 6),
(13, 'Мало нам', '00:04:02', 7), (14, 'Minor', '00:02:55', 7),
(15, 'Армагеддон', '00:03:43', 8), (16, 'Ты мой', '00:02:55', 8),
(17, 'Not afraid','00:04:08', 1);

insert into collections values (1, 'Best of rock', 2022), (2, 'Best of Pop', 2020), (3,'Best of Jazz', 2021),
(4, 'Best of hip-hop', 2015), (5, 'Шансон лучшее', 2012);

insert into musiciansgenres values (1, 2), (1, 6), (2, 3), (2, 8), (3, 4), (4, 1), (4, 7), (5, 5), (1,8);
insert into musiciansalbums values (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8);
insert into collectionstracks values (1, 3), (1, 4), (1, 11), (1, 12), (2, 5), (2, 6), (2, 15), (2, 16),
(3, 7), (3, 8), (4, 1), (4, 14), (5, 9), (5, 10);