from common.factories.project import ProjectFactory
from talkwalker.classes.asker import Asker
from project.models import Post
from django.test import TestCase
import responses
import re
from project.models import *


class AskerTestCase(TestCase):
    body = '\n'.join([
        re.sub(r'\s+', '', """
        {
            "chunk_type": "CT_CONTROL",
            "chunk_control": {
                "connection_id": "#s1ydl1qjeb9r#",
                "resume_offset": "earliest",
                "collector_id": "live_search-1"
            }
        }"""),
        re.sub(r'\s+', '', """{
            "chunk_type": "CT_RESULT",
            "chunk_result": {
                "data": {
                    "data": {
                        "url": "http://www.reddit.com/r/europe/comments/16ykvwa/putins_pals_brag_elon_musk_really_is_our_agent/k39wgb4",
                        "indexed": 1696336379007,
                        "search_indexed": 1696336436980,
                        "published": 1696336284000,
                        "title": "Putin’s Pals Brag: Elon Musk ‘Really Is Our Agent!’",
                        "content": "Lmfao. Damn dude. Go outside and talk to a human being. Jesus. It's entirely possible to think that both Putin and the Russian government are evil as well as United States based billionaires. They are not mutually exclusive. Please, for your own good, get off the internet for a week. Nothing, I repeat, nothing is going to be missed out on, no news worth knowing will be missed, nothing but positives will happen.",
                        "root_url": "http://www.reddit.com/r/europe",
                        "domain_url": "http://reddit.com/",
                        "host_url": "http://www.reddit.com/",
                        "parent_url": "http://www.reddit.com/r/europe/comments/16ykvwa/putins_pals_brag_elon_musk_really_is_our_agent/",
                        "lang": "en",
                        "porn_level": 0,
                        "fluency_level": 100,
                        "sentiment": -5,
                        "source_type": [
                            "MESSAGEBOARD",
                            "MESSAGEBOARD_REDDIT"
                        ],
                        "post_type": [
                            "TEXT"
                        ],
                        "noise_level": 74,
                        "noise_category": "hate_speech",
                        "tokens_title": [
                            "Pals Brag",
                            "Pals Brag",
                            "Elon Musk",
                            "Elon Musk",
                            "Our Agent",
                            "Our Agent",
                            "Agent",
                            "Agent",
                            "Musk",
                            "Musk"
                        ],
                        "tokens_content": [
                            "Lmfao",
                            "Russian",
                            "Putin"
                        ],
                        "tags_internal": [
                            "isComment"
                        ],
                        "source_extended_attributes": {
                            "alexa_pageviews": 3424000000,
                            "alexa_unique_visitors": 683433088,
                            "semrush_pageviews": 1420940,
                            "semrush_unique_visitors": 2195163
                        },
                        "extra_author_attributes": {
                            "id": "ex:www.reddit.com-2059255041",
                            "name": "Latter_Bullfrog247",
                            "gender": "UNKNOWN"
                        },
                        "extra_source_attributes": {
                            "world_data": {
                                "continent": "North America",
                                "country": "United States",
                                "region": "Washington, D.C.",
                                "city": "Washington, D.C.",
                                "longitude": -77.0086669921875,
                                "latitude": 38.89984130859375,
                                "country_code": "us",
                                "resolution": "COUNTRY"
                            },
                            "id": "re:t5_2qh4j",
                            "name": "europe",
                            "url": "http://www.reddit.com/r/europe"
                        },
                        "matched": {
                            "appearance": "NEW"
                        },
                        "word_count": 73
                    },
                    "highlighted_data": [
                        {
                            "title_snippet": "Putin’s Pals Brag: <b>Elon</b> <b>Musk</b> ‘Really Is Our Agent!’",
                            "content_snippet": "Lmfao. Damn dude. Go outside and talk to a human being. Jesus. It&#39;s entirely possible to think that both Putin and the Russian government are evil as well as United States based billionaires. They are not mutually exclusive. Please, for your own...",
                            "matched": {
                                "stream_id": "live_search-1",
                                "rule_ids": [
                                    "live-search-1-rule"
                                ]
                            }
                        }
                    ]
                }
            }
        }"""),
        re.sub(r'\s+', '', """{
            "chunk_type": "CT_RESULT",
            "chunk_result": {
                "data": {
                    "data": {
                        "url": "https://www.scribd.com/document/674870406/Elon-Musk-Sued-For-Defamation-After-Accusing-Student-Of-Being-Federal-Agent-Posing-As-Neo-Nazi",
                        "indexed": 1696265216229,
                        "search_indexed": 1696265241321,
                        "published": 1696265171792,
                        "title": "Elon Musk Sued For Defamation After Accusing Student Of Being Federal Agent Posing As Neo-Nazi",
                        "content": "Ben Brody, a 22-year-old recent college grad, is suing Elon Musk for defamation after the tech billionaire and right-wing sympathizer falsely accused Brody of being part of a neo-Nazi brawl. Brody alleges he was harassed...",
                        "root_url": "https://www.scribd.com/",
                        "domain_url": "http://scribd.com/",
                        "host_url": "http://www.scribd.com/",
                        "parent_url": "https://www.scribd.com/document/674870406/Elon-Musk-Sued-For-Defamation-After-Accusing-Student-Of-Being-Federal-Agent-Posing-As-Neo-Nazi",
                        "lang": "en",
                        "porn_level": 40,
                        "fluency_level": 100,
                        "DEPRECATED_spam_level": 0,
                        "sentiment": -5,
                        "source_type": [
                            "ONLINENEWS",
                            "ONLINENEWS_PRESSRELEASES"
                        ],
                        "post_type": [
                            "TEXT"
                        ],
                        "tokens_title": [
                            "Elon Musk Sued",
                            "Elon Musk Sued",
                            "Federal Agent Posing",
                            "Federal Agent Posing",
                            "Being Federal Agent",
                            "Being Federal Agent",
                            "After Accusing Student",
                            "After Accusing Student",
                            "For Defamation",
                            "For Defamation"
                        ],
                        "tokens_content": [
                            "Rose City Nationalists",
                            "Ben Brody",
                            "Proud Boys",
                            "City Nationalists",
                            "Rose City",
                            "Elon Musk",
                            "Brody",
                            "Brody",
                            "Brody",
                            "Musk"
                        ],
                        "images": [
                            {
                                "url": "https://imgv2-1-f.scribdassets.com/img/document/674870406/149x198/3e0a2468a7/1696259844?v=1"
                            }
                        ],
                        "cluster_id": "https://ca.movies.yahoo.com/elon-musk-hit-lawsuit-falsely-150008110.html",
                        "tags_internal": [
                            "containsImage",
                            "hasImage"
                        ],
                        "article_extended_attributes": {
                            "twitter_shares": 141
                        },
                        "source_extended_attributes": {
                            "alexa_pageviews": 118000000,
                            "alexa_unique_visitors": 50427352,
                            "semrush_pageviews": 159321147,
                            "semrush_unique_visitors": 83604085
                        },
                        "extra_author_attributes": {
                            "id": "ex:www.scribd.com-2088202856",
                            "name": "sign in",
                            "gender": "UNKNOWN"
                        },
                        "extra_source_attributes": {
                            "world_data": {
                                "continent": "North America",
                                "country": "United States",
                                "region": "Washington, D.C.",
                                "city": "Washington, D.C.",
                                "longitude": -77.0086669921875,
                                "latitude": 38.89984130859375,
                                "country_code": "us",
                                "resolution": "COUNTRY"
                            },
                            "id": "ex:www.scribd.com",
                            "name": "www.scribd.com"
                        },
                        "engagement": 141,
                        "reach": 83604085,
                        "matched": {
                            "appearance": "UPDATED"
                        },
                        "word_count": 72,
                        "trending_score": 0
                    },
                    "highlighted_data": [
                        {
                            "title_snippet": "<b>Elon</b> <b>Musk</b> Sued For Defamation After Accusing Student Of Being Federal Agent Posing As Neo-Nazi",
                            "content_snippet": "Ben Brody, a 22-year-old recent college grad, is suing <b>Elon</b> <b>Musk</b> for defamation after the tech billionaire and right-wing sympathizer falsely accused Brody of being part of a neo-Nazi brawl. Brody alleges he was harassed and...",
                            "matched": {
                                "stream_id": "live_search-1",
                                "rule_ids": [
                                    "live-search-1-rule"
                                ]
                            }
                        }
                    ]
                }
            }
        }"""),
        re.sub(r'\s+', '', """{
            "chunk_type": "CT_CONTROL",
            "chunk_control": {
                "connection_id": "#s1ydl1qjeb9r#",
                "resume_offset": "earliest",
                "collector_id": "live_search-1"
            }
        }""")
    ])

    body2 = re.sub(r'\s+', '', """{
                "result_tasks": {
                    "tasks":[
                        {
                            "status": "result_limit_reached"
                        }
                    ]
            }""")

    @responses.activate
    def test_collector_life_cycle(self):
        project = ProjectFactory()
        self.assertEqual(project.status, 'collecting_data')
        token = 'acfaad27-3948-4e13-a617-2d33fd97552a_ZStqaRbxfzpRBT7YfbIqUPJPVwa2.QUzpFqzvPtKdHdc5UNZrYlHyk03MPxVkGKfZ6n3Y4i.meiy.FNZ621ZSmhzzb.gJAlvHtslEq7PP0B3JbDC4BS1y.hwK9fPz7vMQXvSfQFXka9.gEKovum-Pu0LYzy8GSjjSLvBdA1fV5M'

        """Mock __01_create_target_collector request"""
        responses.add(
            responses.PUT,
            f'https://api.talkwalker.com/api/v3/stream/c/search-{project.id}-onl-col?access_token={token}',
            status=200,
        )

        """Mock __02_new_task_on_query request"""
        responses.add(
            responses.POST,
            f'https://api.talkwalker.com/api/v3/stream/export?access_token={token}',
            status=200,
        )

        """Mock __03_retrieve_status_of_task request"""
        responses.add(
            responses.GET,
            f'https://api.talkwalker.com/api/v3/tasks/export/?access_token={token}',
            body=self.body2,
        )

        """Mock __04_read_collector request"""
        responses.add(
            responses.GET,
            f'https://api.talkwalker.com/api/v3/stream/c/search-{project.id}-onl-col/results?access_token=acfaad27-3948-4e13-a617-2d33fd97552a_ZStqaRbxfzpRBT7YfbIqUPJPVwa2.QUzpFqzvPtKdHdc5UNZrYlHyk03MPxVkGKfZ6n3Y4i.meiy.FNZ621ZSmhzzb.gJAlvHtslEq7PP0B3JbDC4BS1y.hwK9fPz7vMQXvSfQFXka9.gEKovum-Pu0LYzy8GSjjSLvBdA1fV5M&resume_offset=earliest&end_behaviour=stop',
            body=self.body,
        )

        """Mock _05_delete_collector request"""
        responses.add(
            responses.DELETE,
            f'https://api.talkwalker.com/api/v3/stream/c/search-{project.id}-onl-col?access_token={token}',
            status=200,
        )

        result = Asker(project.id, 'Project').run()
        self.assertTrue(result)
        self.assertEqual(project.posts.all().count(), 2)
        project = Project.objects.get(pk=project.pk)
        self.assertEqual(project.status, 'active')
