
INSERT INTO genres (name) VALUES
('Rock'),
('Pop'),
('Hip-hop'),
('Electronic'),
('Jazz');

INSERT INTO artists (name) VALUES
('Queen'),
('Michael Jackson'),
('Kanye West'),
('Daft Punk'),
('Miles Davis'),
('Led Zeppelin'),
('Beyonce'),
('Jay-Z'),
('The Beatles'),
('David Bowie'),
('Prince'),
('Radiohead'),
('Coldplay'),
('Ariana Grande'),
('Drake');

INSERT INTO artist_genres (artist_id, genre_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 1),
(7, 2),
(8, 3),
(9, 1),
(10, 4),
(11, 2),
(12, 1),
(13, 1),
(14, 5);

INSERT INTO albums (title, year) VALUES
('A Night at the Opera', 1975),
('Thriller', 1982),
('My Beautiful Dark Twisted Fantasy', 2010),
('Random Access Memories', 2020),
('Kind of Blue', 1959),
('Led Zeppelin IV', 1971),
('Lemonade', 2018),
('The Blueprint', 2019),
('Sgt. Pepper''s Lonely Hearts Club Band', 1967),
('The Rise and Fall of Ziggy Stardust and the Spiders from Mars', 1918),
('Purple Rain', 1984),
('OK Computer', 1997);

INSERT INTO album_artists (album_id, artist_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12);


INSERT INTO tracks (title, duration, album_id) VALUES
('Bohemian Rhapsody', 354, 1),
('Beat It', 258, 2),
('Runaway', 346, 3),
('Get Lucky', 369, 4),
('So What', 569, 5),
('Stairway to Heaven', 482, 6),
('Formation', 239, 7),
('Takeover', 324, 8),
('Lucy in the Sky with Diamonds', 209, 9),
('Starman', 258, 10),
('When Doves Cry', 333, 11),
('Paranoid Android', 386, 12),
('Viva La Vida', 242, 12),
('God is a Woman', 197, 13),
('In My Feelings', 217, 14),
('Radio Ga Ga', 348, 1),
('Billie Jean', 293, 2),
('All of the Lights', 300, 3),
('Instant Crush', 339, 4),
('Blue in Green', 360, 5),
('Black Dog', 295, 6),
('Sorry', 203, 7),
('99 Problems', 235, 8),
('With a Little Help from My Friends', 161, 9),
('Life on Mars?', 236, 10),
('Let''s Go Crazy', 292, 11);

INSERT INTO collections (title, year) VALUES
('The Essential Queen', 2011),
('The Essential Michael Jackson', 2005),
('The Essential Kanye West', 2010),
('The Essential Daft Punk', 2018),
('The Essential Miles Davis', 2019),
('The Essential Led Zeppelin', 2021),
('The Essential Beyonce', 2019),
('The Essential Jay-Z', 2010),
('The Essential Beatles', 2000),
('The Essential David Bowie', 2014),
('The Essential Prince', 2020),
('The Essential Radiohead', 2016);

INSERT INTO collection_tracks (collection_id, track_id) VALUES
(1, 27),
(1, 28),
(2, 35),
(2, 32),
(3, 45),
(3, 28),
(4, 27),
(4, 36),
(5, 29),
(5, 32),
(6, 34),
(6, 50),
(7, 45),
(7, 27),
(8, 31),
(8, 33),
(9, 39),
(9, 42),
(10, 27),
(10, 44),
(11, 42),
(11, 40),
(12, 47),
(12, 35);
