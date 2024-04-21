# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_scheme_advanced 1'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_rates_statuses_stats"
(
\t"id"    serial   UNIQUE PRIMARY KEY NOT NULL,
\t"name"  text     NOT NULL,
\t"value" integer  NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_rates_statuses_stats_idx" ON "anime_rates_statuses_stats" USING btree ("id");'''

snapshots['test_scheme_advanced 10'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_fansubbers"
(
\t"id"         serial  UNIQUE PRIMARY KEY NOT NULL,
\t"fansubbers" text    NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_fansubbers_idx" ON "anime_fansubbers" USING btree ("id");'''

snapshots['test_scheme_advanced 11'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_fandubbers"
(
\t"id"         serial  UNIQUE PRIMARY KEY NOT NULL,
\t"fandubbers" text    NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_fandubbers_idx" ON "anime_fandubbers" USING btree ("id");'''

snapshots['test_scheme_advanced 12'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_licensors"
(
\t"id"        serial  UNIQUE PRIMARY KEY NOT NULL,
\t"licensors" text    NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_licensors_idx" ON "anime_licensors" USING btree ("id");'''

snapshots['test_scheme_advanced 13'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_rates_scores_stats_m2m"
(
\t"id"                     serial  UNIQUE PRIMARY KEY NOT NULL,
\t"rates_scores_stats_m2m" serial  REFERENCES anime_rates_scores_stats (id) NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_rates_scores_stats_m2m_idx" ON "anime_rates_scores_stats_m2m" USING btree ("id");'''

snapshots['test_scheme_advanced 14'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_rates_statuses_stats_m2m"
(
\t"id"                       serial  UNIQUE PRIMARY KEY NOT NULL,
\t"rates_statuses_stats_m2m" serial  REFERENCES anime_rates_statuses_stats (id) NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_rates_statuses_stats_m2m_idx" ON "anime_rates_statuses_stats_m2m" USING btree ("id");'''

snapshots['test_scheme_advanced 15'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_genres_m2m"
(
\t"id"         serial   UNIQUE PRIMARY KEY NOT NULL,
\t"genres_m2m" integer  REFERENCES anime_genres (id) NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_genres_m2m_idx" ON "anime_genres_m2m" USING btree ("id");'''

snapshots['test_scheme_advanced 16'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_studios_m2m"
(
\t"id"          serial   UNIQUE PRIMARY KEY NOT NULL,
\t"studios_m2m" integer  REFERENCES anime_studios (id) NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_studios_m2m_idx" ON "anime_studios_m2m" USING btree ("id");'''

snapshots['test_scheme_advanced 17'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_videos_m2m"
(
\t"id"         serial   UNIQUE PRIMARY KEY NOT NULL,
\t"videos_m2m" integer  REFERENCES anime_videos (id) NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_videos_m2m_idx" ON "anime_videos_m2m" USING btree ("id");'''

snapshots['test_scheme_advanced 18'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_screenshots_m2m"
(
\t"id"              serial  UNIQUE PRIMARY KEY NOT NULL,
\t"screenshots_m2m" serial  REFERENCES anime_screenshots (id) NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_screenshots_m2m_idx" ON "anime_screenshots_m2m" USING btree ("id");'''

snapshots['test_scheme_advanced 19'] = '''--- order = 1
CREATE TABLE IF NOT EXISTS "anime_image"
(
\t"id"       serial  UNIQUE PRIMARY KEY NOT NULL,
\t"original" text    NOT NULL,
\t"preview"  text    NOT NULL,
\t"x96"      text    NOT NULL,
\t"x48"      text    NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_image_idx" ON "anime_image" USING btree ("id");'''

snapshots['test_scheme_advanced 2'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_genres"
(
\t"id"         integer  UNIQUE PRIMARY KEY NOT NULL,
\t"name"       text     NOT NULL,
\t"russian"    text     NOT NULL,
\t"kind"       text    ,
\t"entry_type" text     NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_genres_idx" ON "anime_genres" USING btree ("id");'''

snapshots['test_scheme_advanced 20'] = '''--- order = 0
CREATE TABLE IF NOT EXISTS "anime"
(
\t"id"                   integer  UNIQUE PRIMARY KEY NOT NULL,
\t"name"                 text     NOT NULL,
\t"russian"              text     NOT NULL,
\t"image"                serial   REFERENCES anime_image (id) NOT NULL,
\t"url"                  text     NOT NULL,
\t"kind"                 text     NOT NULL,
\t"score"                text     NOT NULL,
\t"status"               text     NOT NULL,
\t"episodes"             integer  NOT NULL,
\t"episodes_aired"       integer  NOT NULL,
\t"aired_on"             text    ,
\t"released_on"          text    ,
\t"rating"               text     NOT NULL,
\t"english"              serial   REFERENCES anime_english (id) NOT NULL,
\t"japanese"             serial   REFERENCES anime_japanese (id) NOT NULL,
\t"synonyms"             serial   REFERENCES anime_synonyms (id) NOT NULL,
\t"license_name_ru"      text    ,
\t"duration"             integer  NOT NULL,
\t"description"          text    ,
\t"description_html"     text     NOT NULL,
\t"description_source"   text    ,
\t"franchise"            text    ,
\t"favoured"             integer  NOT NULL,
\t"anons"                integer  NOT NULL,
\t"ongoing"              integer  NOT NULL,
\t"thread_id"            integer ,
\t"topic_id"             integer ,
\t"myanimelist_id"       integer  NOT NULL,
\t"rates_scores_stats"   serial   REFERENCES anime_rates_scores_stats_m2m (id) NOT NULL,
\t"rates_statuses_stats" serial   REFERENCES anime_rates_statuses_stats_m2m (id) NOT NULL,
\t"updated_at"           text     NOT NULL,
\t"next_episode_at"      text    ,
\t"fansubbers"           serial   REFERENCES anime_fansubbers (id) NOT NULL,
\t"fandubbers"           serial   REFERENCES anime_fandubbers (id) NOT NULL,
\t"licensors"            serial   REFERENCES anime_licensors (id) NOT NULL,
\t"genres"               serial   REFERENCES anime_genres_m2m (id) NOT NULL,
\t"studios"              serial   REFERENCES anime_studios_m2m (id) NOT NULL,
\t"videos"               serial   REFERENCES anime_videos_m2m (id) NOT NULL,
\t"screenshots"          serial   REFERENCES anime_screenshots_m2m (id) NOT NULL,
\t"user_rate"            text    
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_idx" ON "anime" USING btree ("id");'''

snapshots['test_scheme_advanced 3'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_studios"
(
\t"id"            integer  UNIQUE PRIMARY KEY NOT NULL,
\t"name"          text     NOT NULL,
\t"filtered_name" text     NOT NULL,
\t"real"          integer  NOT NULL,
\t"image"         text    
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_studios_idx" ON "anime_studios" USING btree ("id");'''

snapshots['test_scheme_advanced 4'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_screenshots"
(
\t"id"       serial  UNIQUE PRIMARY KEY NOT NULL,
\t"original" text    NOT NULL,
\t"preview"  text    NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_screenshots_idx" ON "anime_screenshots" USING btree ("id");'''

snapshots['test_scheme_advanced 5'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_rates_scores_stats"
(
\t"id"    serial   UNIQUE PRIMARY KEY NOT NULL,
\t"name"  integer  NOT NULL,
\t"value" integer  NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_rates_scores_stats_idx" ON "anime_rates_scores_stats" USING btree ("id");'''

snapshots['test_scheme_advanced 6'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_videos"
(
\t"id"         integer  UNIQUE PRIMARY KEY NOT NULL,
\t"url"        text     NOT NULL,
\t"image_url"  text     NOT NULL,
\t"player_url" text     NOT NULL,
\t"name"       text    ,
\t"kind"       text     NOT NULL,
\t"hosting"    text     NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_videos_idx" ON "anime_videos" USING btree ("id");'''

snapshots['test_scheme_advanced 7'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_english"
(
\t"id"      serial  UNIQUE PRIMARY KEY NOT NULL,
\t"english" text   
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_english_idx" ON "anime_english" USING btree ("id");'''

snapshots['test_scheme_advanced 8'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_japanese"
(
\t"id"       serial  UNIQUE PRIMARY KEY NOT NULL,
\t"japanese" text   
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_japanese_idx" ON "anime_japanese" USING btree ("id");'''

snapshots['test_scheme_advanced 9'] = '''--- order = 101
CREATE TABLE IF NOT EXISTS "anime_synonyms"
(
\t"id"       serial  UNIQUE PRIMARY KEY NOT NULL,
\t"synonyms" text    NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_synonyms_idx" ON "anime_synonyms" USING btree ("id");'''

snapshots['test_scheme_basic 1'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "poor_anime"
(
\t"id"         serial  UNIQUE PRIMARY KEY NOT NULL,
\t"poor_anime" text    NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "poor_anime_idx" ON "poor_anime" USING btree ("id");'''

snapshots['test_scheme_basic 2'] = '''--- order = 1
CREATE TABLE IF NOT EXISTS "poor_anime_image"
(
\t"id"       serial  UNIQUE PRIMARY KEY NOT NULL,
\t"original" text    NOT NULL,
\t"preview"  text    NOT NULL,
\t"x96"      text    NOT NULL,
\t"x48"      text    NOT NULL
) with (oids = false);
CREATE INDEX IF NOT EXISTS "poor_anime_image_idx" ON "poor_anime_image" USING btree ("id");'''

snapshots['test_scheme_basic 3'] = '''--- order = 0
CREATE TABLE IF NOT EXISTS "poor_anime"
(
\t"id"             integer  UNIQUE PRIMARY KEY NOT NULL,
\t"name"           text     NOT NULL,
\t"russian"        text     NOT NULL,
\t"image"          serial   REFERENCES poor_anime_image (id),
\t"url"            text     NOT NULL,
\t"kind"           text     NOT NULL,
\t"score"          text     NOT NULL,
\t"status"         text     NOT NULL,
\t"episodes"       integer  NOT NULL,
\t"episodes_aired" integer  NOT NULL,
\t"aired_on"       text     NOT NULL,
\t"released_on"    text    
) with (oids = false);
CREATE INDEX IF NOT EXISTS "poor_anime_idx" ON "poor_anime" USING btree ("id");'''
