# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_scheme_advanced 1'] = '''--- order = 607
CREATE TABLE IF NOT EXISTS "public"."image"
(
\t"id"       serial  UNIQUE PRIMARY KEY NOT NULL,
\t"original" text    DEFAULT \'\' NOT NULL,
\t"preview"  text    DEFAULT \'\' NOT NULL,
\t"x96"      text    DEFAULT \'\' NOT NULL,
\t"x48"      text    DEFAULT \'\' NOT NULL
    
) with (oids = false);
CREATE INDEX IF NOT EXISTS "image_idx" ON "public"."image" USING btree ("id");'''

snapshots['test_scheme_advanced 10'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."rates_statuses_stats_m2m"
(
\t"id"                       serial   PRIMARY KEY NOT NULL,
\t"rates_statuses_stats_m2m" text     NOT NULL,
\t"anime_id"                 integer  REFERENCES anime (id),
    CONSTRAINT "rates_statuses_stats_m2m_unique" UNIQUE ("rates_statuses_stats_m2m", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "rates_statuses_stats_m2m_idx" ON "public"."rates_statuses_stats_m2m" USING btree ("id");'''

snapshots['test_scheme_advanced 11'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."genres_m2m"
(
\t"id"         serial   PRIMARY KEY NOT NULL,
\t"genres_m2m" text     NOT NULL,
\t"anime_id"   integer  REFERENCES anime (id),
    CONSTRAINT "genres_m2m_unique" UNIQUE ("genres_m2m", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "genres_m2m_idx" ON "public"."genres_m2m" USING btree ("id");'''

snapshots['test_scheme_advanced 12'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."studios_m2m"
(
\t"id"          serial   PRIMARY KEY NOT NULL,
\t"studios_m2m" text     NOT NULL,
\t"anime_id"    integer  REFERENCES anime (id),
    CONSTRAINT "studios_m2m_unique" UNIQUE ("studios_m2m", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "studios_m2m_idx" ON "public"."studios_m2m" USING btree ("id");'''

snapshots['test_scheme_advanced 13'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."videos_m2m"
(
\t"id"         serial   PRIMARY KEY NOT NULL,
\t"videos_m2m" text     NOT NULL,
\t"anime_id"   integer  REFERENCES anime (id),
    CONSTRAINT "videos_m2m_unique" UNIQUE ("videos_m2m", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "videos_m2m_idx" ON "public"."videos_m2m" USING btree ("id");'''

snapshots['test_scheme_advanced 14'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."screenshots_m2m"
(
\t"id"              serial   PRIMARY KEY NOT NULL,
\t"screenshots_m2m" text     NOT NULL,
\t"anime_id"        integer  REFERENCES anime (id),
    CONSTRAINT "screenshots_m2m_unique" UNIQUE ("screenshots_m2m", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "screenshots_m2m_idx" ON "public"."screenshots_m2m" USING btree ("id");'''

snapshots['test_scheme_advanced 15'] = '''--- order = 0
CREATE TABLE IF NOT EXISTS "public"."rates_statuses_stats"
(
\t"id"    serial   UNIQUE PRIMARY KEY NOT NULL,
\t"name"  text     DEFAULT \'\' NOT NULL,
\t"value" integer  DEFAULT 0 NOT NULL,
    CONSTRAINT "rates_statuses_stats_unique" UNIQUE ("name", "value")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "rates_statuses_stats_idx" ON "public"."rates_statuses_stats" USING btree ("id");'''

snapshots['test_scheme_advanced 16'] = '''--- order = 0
CREATE TABLE IF NOT EXISTS "public"."genres"
(
\t"id"         integer  UNIQUE PRIMARY KEY DEFAULT 0 NOT NULL,
\t"name"       text     DEFAULT \'\' NOT NULL,
\t"russian"    text     DEFAULT \'\' NOT NULL,
\t"kind"       text    ,
\t"entry_type" text     DEFAULT \'\' NOT NULL,
    CONSTRAINT "genres_unique" UNIQUE ("name", "russian", "kind", "entry_type")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "genres_idx" ON "public"."genres" USING btree ("id");'''

snapshots['test_scheme_advanced 17'] = '''--- order = 0
CREATE TABLE IF NOT EXISTS "public"."studios"
(
\t"id"            integer  UNIQUE PRIMARY KEY DEFAULT 0 NOT NULL,
\t"name"          text     DEFAULT \'\' NOT NULL,
\t"filtered_name" text     DEFAULT \'\' NOT NULL,
\t"real"          integer  DEFAULT 0 NOT NULL,
\t"image"         text    ,
    CONSTRAINT "studios_unique" UNIQUE ("name", "filtered_name", "real", "image")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "studios_idx" ON "public"."studios" USING btree ("id");'''

snapshots['test_scheme_advanced 18'] = '''--- order = 0
CREATE TABLE IF NOT EXISTS "public"."screenshots"
(
\t"id"       serial  UNIQUE PRIMARY KEY NOT NULL,
\t"original" text    DEFAULT \'\' NOT NULL,
\t"preview"  text    DEFAULT \'\' NOT NULL,
    CONSTRAINT "screenshots_unique" UNIQUE ("original", "preview")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "screenshots_idx" ON "public"."screenshots" USING btree ("id");'''

snapshots['test_scheme_advanced 19'] = '''--- order = 0
CREATE TABLE IF NOT EXISTS "public"."rates_scores_stats"
(
\t"id"    serial   UNIQUE PRIMARY KEY NOT NULL,
\t"name"  integer  DEFAULT 0 NOT NULL,
\t"value" integer  DEFAULT 0 NOT NULL,
    CONSTRAINT "rates_scores_stats_unique" UNIQUE ("name", "value")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "rates_scores_stats_idx" ON "public"."rates_scores_stats" USING btree ("id");'''

snapshots['test_scheme_advanced 2'] = '''--- order = 606
CREATE TABLE IF NOT EXISTS "public"."anime"
(
\t"id"                   integer  UNIQUE PRIMARY KEY DEFAULT 0 NOT NULL,
\t"name"                 text     DEFAULT \'\' NOT NULL,
\t"russian"              text     DEFAULT \'\' NOT NULL,
\t"image"                serial   REFERENCES image (id),
\t"url"                  text     DEFAULT \'\' NOT NULL,
\t"kind"                 text     DEFAULT \'\' NOT NULL,
\t"score"                text     DEFAULT \'\' NOT NULL,
\t"status"               text     DEFAULT \'\' NOT NULL,
\t"episodes"             integer  DEFAULT 0 NOT NULL,
\t"episodes_aired"       integer  DEFAULT 0 NOT NULL,
\t"aired_on"             text    ,
\t"released_on"          text    ,
\t"rating"               text     DEFAULT \'\' NOT NULL,
\t"english"              char(8) ,
\t"japanese"             char(8) ,
\t"synonyms"             char(8) ,
\t"license_name_ru"      text    ,
\t"duration"             integer  DEFAULT 0 NOT NULL,
\t"description"          text    ,
\t"description_html"     text     DEFAULT \'\' NOT NULL,
\t"description_source"   text    ,
\t"franchise"            text    ,
\t"favoured"             integer  DEFAULT 0 NOT NULL,
\t"anons"                integer  DEFAULT 0 NOT NULL,
\t"ongoing"              integer  DEFAULT 0 NOT NULL,
\t"thread_id"            integer ,
\t"topic_id"             integer ,
\t"myanimelist_id"       integer  DEFAULT 0 NOT NULL,
\t"rates_scores_stats"   char(8) ,
\t"rates_statuses_stats" char(8) ,
\t"updated_at"           text     DEFAULT \'\' NOT NULL,
\t"next_episode_at"      text    ,
\t"fansubbers"           char(8) ,
\t"fandubbers"           char(8) ,
\t"licensors"            char(8) ,
\t"genres"               char(8) ,
\t"studios"              char(8) ,
\t"videos"               char(8) ,
\t"screenshots"          char(8) ,
\t"user_rate"            text    
    
) with (oids = false);
CREATE INDEX IF NOT EXISTS "anime_idx" ON "public"."anime" USING btree ("id");'''

snapshots['test_scheme_advanced 20'] = '''--- order = 0
CREATE TABLE IF NOT EXISTS "public"."videos"
(
\t"id"         integer  UNIQUE PRIMARY KEY DEFAULT 0 NOT NULL,
\t"url"        text     DEFAULT \'\' NOT NULL,
\t"image_url"  text     DEFAULT \'\' NOT NULL,
\t"player_url" text     DEFAULT \'\' NOT NULL,
\t"name"       text    ,
\t"kind"       text     DEFAULT \'\' NOT NULL,
\t"hosting"    text     DEFAULT \'\' NOT NULL,
    CONSTRAINT "videos_unique" UNIQUE ("url", "image_url", "player_url", "name", "kind", "hosting")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "videos_idx" ON "public"."videos" USING btree ("id");'''

snapshots['test_scheme_advanced 3'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."english"
(
\t"id"       serial   PRIMARY KEY NOT NULL,
\t"english"  text    ,
\t"anime_id" integer  REFERENCES anime (id),
    CONSTRAINT "english_unique" UNIQUE ("english", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "english_idx" ON "public"."english" USING btree ("id");'''

snapshots['test_scheme_advanced 4'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."japanese"
(
\t"id"       serial   PRIMARY KEY NOT NULL,
\t"japanese" text    ,
\t"anime_id" integer  REFERENCES anime (id),
    CONSTRAINT "japanese_unique" UNIQUE ("japanese", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "japanese_idx" ON "public"."japanese" USING btree ("id");'''

snapshots['test_scheme_advanced 5'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."synonyms"
(
\t"id"       serial   PRIMARY KEY NOT NULL,
\t"synonyms" text     NOT NULL,
\t"anime_id" integer  REFERENCES anime (id),
    CONSTRAINT "synonyms_unique" UNIQUE ("synonyms", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "synonyms_idx" ON "public"."synonyms" USING btree ("id");'''

snapshots['test_scheme_advanced 6'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."fansubbers"
(
\t"id"         serial   PRIMARY KEY NOT NULL,
\t"fansubbers" text     NOT NULL,
\t"anime_id"   integer  REFERENCES anime (id),
    CONSTRAINT "fansubbers_unique" UNIQUE ("fansubbers", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "fansubbers_idx" ON "public"."fansubbers" USING btree ("id");'''

snapshots['test_scheme_advanced 7'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."fandubbers"
(
\t"id"         serial   PRIMARY KEY NOT NULL,
\t"fandubbers" text     NOT NULL,
\t"anime_id"   integer  REFERENCES anime (id),
    CONSTRAINT "fandubbers_unique" UNIQUE ("fandubbers", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "fandubbers_idx" ON "public"."fandubbers" USING btree ("id");'''

snapshots['test_scheme_advanced 8'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."licensors"
(
\t"id"        serial   PRIMARY KEY NOT NULL,
\t"licensors" text     NOT NULL,
\t"anime_id"  integer  REFERENCES anime (id),
    CONSTRAINT "licensors_unique" UNIQUE ("licensors", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "licensors_idx" ON "public"."licensors" USING btree ("id");'''

snapshots['test_scheme_advanced 9'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."rates_scores_stats_m2m"
(
\t"id"                     serial   PRIMARY KEY NOT NULL,
\t"rates_scores_stats_m2m" text     NOT NULL,
\t"anime_id"               integer  REFERENCES anime (id),
    CONSTRAINT "rates_scores_stats_m2m_unique" UNIQUE ("rates_scores_stats_m2m", "anime_id")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "rates_scores_stats_m2m_idx" ON "public"."rates_scores_stats_m2m" USING btree ("id");'''

snapshots['test_scheme_basic 1'] = '''--- order = 100
CREATE TABLE IF NOT EXISTS "public"."poor_anime"
(
\t"id"         serial  PRIMARY KEY NOT NULL,
\t"poor_anime" text    NOT NULL,
    CONSTRAINT "poor_anime_unique" UNIQUE ("poor_anime")
) with (oids = false);
CREATE INDEX IF NOT EXISTS "poor_anime_idx" ON "public"."poor_anime" USING btree ("id");'''

snapshots['test_scheme_basic 2'] = '''--- order = 1
CREATE TABLE IF NOT EXISTS "public"."image"
(
\t"id"       serial  UNIQUE PRIMARY KEY NOT NULL,
\t"original" text    DEFAULT \'\' NOT NULL,
\t"preview"  text    DEFAULT \'\' NOT NULL,
\t"x96"      text    DEFAULT \'\' NOT NULL,
\t"x48"      text    DEFAULT \'\' NOT NULL
    
) with (oids = false);
CREATE INDEX IF NOT EXISTS "image_idx" ON "public"."image" USING btree ("id");'''

snapshots['test_scheme_basic 3'] = '''--- order = 0
CREATE TABLE IF NOT EXISTS "public"."poor_anime"
(
\t"id"             integer  UNIQUE PRIMARY KEY DEFAULT 0 NOT NULL,
\t"name"           text     DEFAULT \'\' NOT NULL,
\t"russian"        text     DEFAULT \'\' NOT NULL,
\t"image"          serial   REFERENCES image (id),
\t"url"            text     DEFAULT \'\' NOT NULL,
\t"kind"           text     DEFAULT \'\' NOT NULL,
\t"score"          text     DEFAULT \'\' NOT NULL,
\t"status"         text     DEFAULT \'\' NOT NULL,
\t"episodes"       integer  DEFAULT 0 NOT NULL,
\t"episodes_aired" integer  DEFAULT 0 NOT NULL,
\t"aired_on"       text     DEFAULT \'\' NOT NULL,
\t"released_on"    text    
    
) with (oids = false);
CREATE INDEX IF NOT EXISTS "poor_anime_idx" ON "public"."poor_anime" USING btree ("id");'''
