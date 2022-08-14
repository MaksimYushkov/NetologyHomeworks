--количество исполнителей в каждом жанре
select genre_name, COUNT(musician_id) musician_q from genres g
join musiciansgenres m on g.id = m.genre_id 
group by g.genre_name 
order by musician_q desc;

--количество треков, вошедших в альбомы 2019-2020 годов
select count(track_name) from tracks t
join albums a on t.album_id = a.id
where a.album_release_year between 2019 and 2020;

--средняя продолжительность треков по каждому альбому
select album_name, avg(track_duration) avg_duration from albums a
join tracks t on t.album_id = a.id
group by a.album_name
order by avg_duration desc;

--все исполнители, которые не выпустили альбомы в 2020 году
select musician_name from musicians m 
join albums a on m.id = a.id
where album_release_year != 2020;

--названия сборников, в которых присутствует конкретный исполнитель (выберите сами)
select collection_name from collections c
join collectionstracks ct on c.id = ct.collection_id
join tracks t on t.id = ct.track_id
join albums a on a.id = t.album_id
join musiciansalbums ma on a.id = ma.album_id
join musicians m on m.id = ma.musician_id
where musician_name = 'Nickelback'
group by collection_name;

--название альбомов, в которых присутствуют исполнители более 1 жанра
select album_name from albums a 
join musiciansalbums ma on a.id = ma.album_id 
join musiciansgenres mg on ma.musician_id = mg.musician_id 
group by album_name
having count(mg.genre_id) > 1;

--наименование треков, которые не входят в сборники
select track_name from tracks t 
left join collectionstracks ct on t.id = ct.track_id
where collection_id is null;

--самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
select track_name, track_duration from tracks 
where track_duration = (select min(track_duration) from tracks);

--название альбомов, содержащих наименьшее количество треков
select album_name, count(album_name) from albums a 
join tracks t on t.album_id = a.id
group by album_name
having count(album_name) < 
(select max(count(album_name)) over () from albums a
join tracks t on t.album_id = a.id
group by album_name
limit 1);













