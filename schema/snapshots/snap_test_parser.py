# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_parse_basic 1'] = '''{
  "root": {
    "path": "root",
    "children": {
      "id": [
        "int"
      ],
      "name": [
        "str"
      ],
      "russian": [
        "str"
      ],
      "image": [
        "ENTITY:root.image",
        "NoneType"
      ],
      "url": [
        "str"
      ],
      "kind": [
        "str"
      ],
      "score": [
        "str"
      ],
      "status": [
        "str"
      ],
      "episodes": [
        "int"
      ],
      "episodes_aired": [
        "int"
      ],
      "aired_on": [
        "str"
      ],
      "released_on": [
        "NoneType"
      ]
    },
    "types": [],
    "one_to_many": false,
    "one_to_one": true
  },
  "root.image": {
    "path": "root.image",
    "children": {
      "original": [
        "str"
      ],
      "preview": [
        "str"
      ],
      "x96": [
        "str"
      ],
      "x48": [
        "str"
      ]
    },
    "types": [],
    "one_to_many": false,
    "one_to_one": true
  }
}'''

snapshots['test_parse_deep 1'] = '''{
  "root": {
    "path": "root",
    "children": {
      "id": [
        "int"
      ],
      "name": [
        "str"
      ],
      "russian": [
        "str"
      ],
      "image": [
        "ENTITY:root.image"
      ],
      "url": [
        "str"
      ],
      "kind": [
        "str"
      ],
      "score": [
        "str"
      ],
      "status": [
        "str"
      ],
      "episodes": [
        "int"
      ],
      "episodes_aired": [
        "int"
      ],
      "aired_on": [
        "str"
      ],
      "released_on": [
        "str",
        "NoneType"
      ],
      "rating": [
        "str"
      ],
      "english": [
        "ENTITY:root.english"
      ],
      "japanese": [
        "ENTITY:root.japanese"
      ],
      "synonyms": [
        "ENTITY:root.synonyms"
      ],
      "license_name_ru": [
        "str"
      ],
      "duration": [
        "int"
      ],
      "description": [
        "str"
      ],
      "description_html": [
        "str"
      ],
      "description_source": [
        "NoneType"
      ],
      "franchise": [
        "str"
      ],
      "favoured": [
        "int"
      ],
      "anons": [
        "int"
      ],
      "ongoing": [
        "int"
      ],
      "thread_id": [
        "int"
      ],
      "topic_id": [
        "int"
      ],
      "myanimelist_id": [
        "int"
      ],
      "rates_scores_stats": [
        "ENTITY:root.rates_scores_stats"
      ],
      "rates_statuses_stats": [
        "ENTITY:root.rates_statuses_stats"
      ],
      "updated_at": [
        "str"
      ],
      "next_episode_at": [
        "NoneType"
      ],
      "fansubbers": [
        "ENTITY:root.fansubbers"
      ],
      "fandubbers": [
        "ENTITY:root.fandubbers"
      ],
      "licensors": [
        "ENTITY:root.licensors"
      ],
      "genres": [
        "ENTITY:root.genres"
      ],
      "studios": [
        "ENTITY:root.studios"
      ],
      "videos": [
        "ENTITY:root.videos"
      ],
      "screenshots": [
        "ENTITY:root.screenshots"
      ],
      "user_rate": [
        "NoneType"
      ]
    },
    "types": [],
    "one_to_many": false,
    "one_to_one": true
  },
  "root.image": {
    "path": "root.image",
    "children": {
      "original": [
        "str"
      ],
      "preview": [
        "str"
      ],
      "x96": [
        "str"
      ],
      "x48": [
        "str"
      ]
    },
    "types": [],
    "one_to_many": false,
    "one_to_one": true
  },
  "root.english": {
    "path": "root.english",
    "children": {},
    "types": [
      "str"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.japanese": {
    "path": "root.japanese",
    "children": {},
    "types": [
      "str"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.synonyms": {
    "path": "root.synonyms",
    "children": {},
    "types": [
      "str"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.rates_scores_stats": {
    "path": "root.rates_scores_stats",
    "children": {},
    "types": [
      "ENTITY:root.rates_scores_stats.[]"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.rates_scores_stats.[]": {
    "path": "root.rates_scores_stats.[]",
    "children": {
      "name": [
        "int"
      ],
      "value": [
        "int"
      ]
    },
    "types": [],
    "one_to_many": false,
    "one_to_one": true
  },
  "root.rates_statuses_stats": {
    "path": "root.rates_statuses_stats",
    "children": {},
    "types": [
      "ENTITY:root.rates_statuses_stats.[]"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.rates_statuses_stats.[]": {
    "path": "root.rates_statuses_stats.[]",
    "children": {
      "name": [
        "str"
      ],
      "value": [
        "int"
      ]
    },
    "types": [],
    "one_to_many": false,
    "one_to_one": true
  },
  "root.fansubbers": {
    "path": "root.fansubbers",
    "children": {},
    "types": [
      "str"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.fandubbers": {
    "path": "root.fandubbers",
    "children": {},
    "types": [
      "str"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.licensors": {
    "path": "root.licensors",
    "children": {},
    "types": [
      "str"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.genres": {
    "path": "root.genres",
    "children": {},
    "types": [
      "ENTITY:root.genres.[]"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.genres.[]": {
    "path": "root.genres.[]",
    "children": {
      "id": [
        "int"
      ],
      "name": [
        "str"
      ],
      "russian": [
        "str"
      ],
      "kind": [
        "str"
      ],
      "entry_type": [
        "str"
      ]
    },
    "types": [],
    "one_to_many": false,
    "one_to_one": true
  },
  "root.studios": {
    "path": "root.studios",
    "children": {},
    "types": [
      "ENTITY:root.studios.[]"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.studios.[]": {
    "path": "root.studios.[]",
    "children": {
      "id": [
        "int"
      ],
      "name": [
        "str"
      ],
      "filtered_name": [
        "str"
      ],
      "real": [
        "int"
      ],
      "image": [
        "str"
      ]
    },
    "types": [],
    "one_to_many": false,
    "one_to_one": true
  },
  "root.videos": {
    "path": "root.videos",
    "children": {},
    "types": [
      "ENTITY:root.videos.[]"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.videos.[]": {
    "path": "root.videos.[]",
    "children": {
      "id": [
        "int"
      ],
      "url": [
        "str"
      ],
      "image_url": [
        "str"
      ],
      "player_url": [
        "str"
      ],
      "name": [
        "str"
      ],
      "kind": [
        "str"
      ],
      "hosting": [
        "str"
      ]
    },
    "types": [],
    "one_to_many": false,
    "one_to_one": true
  },
  "root.screenshots": {
    "path": "root.screenshots",
    "children": {},
    "types": [
      "ENTITY:root.screenshots.[]"
    ],
    "one_to_many": true,
    "one_to_one": false
  },
  "root.screenshots.[]": {
    "path": "root.screenshots.[]",
    "children": {
      "original": [
        "str"
      ],
      "preview": [
        "str"
      ]
    },
    "types": [],
    "one_to_many": false,
    "one_to_one": true
  }
}'''
