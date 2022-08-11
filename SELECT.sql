--Select запросы
select album_name, album_release_year from albums
where album_release_year = 2018;

select track_duration, track_name from tracks
where track_duration=(select max(track_duration) from tracks);

select track_name from tracks 
where track_duration >= '00:03:30';

select collection_name from collections
where collection_release_year between 2018 and 2020;

select musician_name from musicians
where musician_name not like '% %';

select track_name from tracks
where lower(track_name) like '%мой' or lower(track_name) like '%my%';


