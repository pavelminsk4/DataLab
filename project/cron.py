from .models import Feedlinks, Post
import feedparser
import ssl

def feed_receiver():
  ssl._create_default_https_context = ssl._create_unverified_context #fix SSL issue
  all_feeds = Feedlinks.objects.all()
  for feed in all_feeds:
    url = feed.url
    f = feedparser.parse(url)
    fe = f.entries
    ff = f.feed
    for ent in fe:
      if not Post.objects.filter(entry_title=ent.title):
        try:
            myid = ent.id
        except:
            myid = 'None'

        try:
            myguidislink = ent.guidislink
        except:
            myguidislink = 'None'

        try:
            my_entry_content_type = ent.content[0].type
        except:
            my_entry_content_type = 'None'

        try:
            my_entry_content_language = ent.content[0].language
        except:
            my_entry_content_language = 'None'

        try:
            my_entry_content_base = ent.content[0].base
        except:
            my_entry_content_base = 'None'

        try:
            my_entry_content_value = ent.content[0].value
        except:
            my_entry_content_value = 'None'

        try:
            my_media_thumbnail_url = ent.media_thumbnail[0]['url']

        except:
            my_media_thumbnail_url = 'None'

        try:
            my_media_thumbnail_width = ent.media_thumbnail[0]['width']
        except:
            my_media_thumbnail_width = 'None'

        try:
            my_media_thumbnail_height = ent.media_thumbnail[0]['height']
        except:
            my_media_thumbnail_height = 'None'

        try:
            myhref = ent.href
        except:
            myhref = 'None'

        try:
            my_entry_media_content_type = ent.media_content[0]['type']
        except:
            my_entry_media_content_type = 'None'

        try:
            my_entry_media_content_url = ent.media_content[0]['url']
        except:
            my_entry_media_content_url = 'None'

        try:
            my_entry_media_content_height = ent.media_content[0]['height']
        except:
            my_entry_media_content_height = 'None'

        try:
            my_entry_media_content_medium = ent.media_content[0]['medium']
        except:
            my_entry_media_content_medium = 'None'

        try:
            my_entry_media_content_width = ent.media_content[0]['width']
        except:
            my_entry_media_content_width = 'None'

        try:
            my_entry_media_credit_content = ent.media_credit[0]['content']
        except:
            my_entry_media_credit_content = 'None'

        try:
            my_entry_credit = ent['credit']
        except:
            my_entry_credit = 'None'

        try:
            my_entry_authors = ent['authors'][0]['name']
        except:
            my_entry_authors = 'None'

        try:
            my_entry_author = ent['author']
        except:
            my_entry_author = 'None'

        try:
            my_entry_author_detail = ent['author_detail']
        except:
            my_entry_author_detail = 'None'

        try:
            my_entry_tags_term = ent['tags'][0]['term']
        except:
            my_entry_tags_term = 'None'

        try:
            my_entry_tags_scheme = ent['tags'][0]['scheme']
        except:
            my_entry_tags_scheme = 'None'

        try:
            my_entry_tags_label = ent['tags'][0]['label']
        except:
            my_entry_tags_label = 'None'

        try:
            my_feed_title = ff['title']
        except:
            my_feed_title = 'None'

        try:
            my_feed_title_detail_type = ff['title_detail']['type']
        except:
            my_feed_title_detail_type = 'None'

        try:
            my_feed_title_detail_language = ff['title_detail']['language']
        except:
            my_feed_title_detail_language = 'None'

        try:
            my_feed_title_detail_base = ff['title_detail']['base']
        except:
            my_feed_title_detail_base = 'None'

        try:
            my_feed_title_detail_value = ff['title_detail']['value']
        except:
            my_feed_title_detail_value = 'None'

        try:
            my_feed_links_rel = ff['links'][0]['rel']
        except:
            my_feed_links_rel = 'None'

        try:
            my_feed_links_type = ff['links'][0]['type']
        except:
            my_feed_links_type = 'None'

        try:
            my_feed_links_href = ff['links'][0]['href']
        except:
            my_feed_links_href = 'None'

        try:
            my_feed_link = ff['link']
        except:
            my_feed_link = 'None'


        try:
            my_feed_image_title = ff['image']['title']
        except:
            my_feed_image_title = 'None'

        # try:
        #     my_feed_image_title_detail_type = ff['image']['title_detail']['type']
        # except:
        #     my_feed_image_title_detail_type = 'None'

        # try:
        #     my_feed_image_title_detail_language = ff['image']['title_detail']['language']
        # except:
        #     my_feed_image_title_detail_language = 'None'

        # try:
        #     my_feed_image_title_detail_base = ff['image']['title_detail']['base']
        # except:
        #     my_feed_image_title_detail_base = 'None'

        # try:
        #     my_feed_image_title_detail_value = ff['image']['title_detail']['value']
        # except:
        #     my_feed_image_title_detail_value = 'None'


        my_feed_image_title_detail_type = 'None'
        my_feed_image_title_detail_language = 'None'
        my_feed_image_title_detail_base = 'None'
        my_feed_image_title_detail_value = 'None'

        try:
            my_feed_image_href = ff['image']['href']
        except:
            my_feed_image_href = 'None'

        try:
            my_feed_image_link = ff['image']['link']
        except:
            my_feed_image_link = 'None'

        try:
            my_feed_image_links = ff['image']['links']
        except:
            my_feed_image_links = 'None'

        try:
            my_feed_subtitle = ff['subtitle']
        except:
            my_feed_subtitle = 'None'

        try:
            my_feed_subtitle_detail = ff['subtitle_detail']
        except:
            my_feed_subtitle_detail = 'None'

        try:
            my_feed_language = ff['language']
        except:
            my_feed_language = 'None'

        try:
            my_feed_rights = ff['rights']
        except:
            my_feed_rights = 'None'

        try:
            my_feed_rights_detail = ff['rights_detail']
        except:
            my_feed_rights_detail = 'None'

        try:
            my_feed_updated = ff['updated']
        except:
            my_feed_updated = 'None'

        try:
            my_feed_updated_parsed = ff['updated_parsed']
        except:
            my_feed_updated_parsed = 'None'

        try:
            my_feed_published = ff['published']
        except:
            my_feed_published = 'None'

        try:
            my_feed_published_parsed = ff['published_parsed']
        except:
            my_feed_published_parsed = 'None'

        try:
            my_feed_tags_term = ff['tags'][0]['term']
        except:
            my_feed_tags_term = 'None'

        try:
            my_feed_tags_scheme = ff['tags'][0]['scheme']
        except:
            my_feed_tags_scheme = 'None'

        try:
            my_feed_tags_label = ff['tags'][0]['label']
        except:
            my_feed_tags_label = 'None'

        try:
            my_feed_tags_list = ff['tags']
        except:
            my_feed_tags_list = 'None'

        try:
            my_feed_ttl = ff['ttl']
        except:
            my_feed_ttl = 'None'

        try:
            my_feed_generator_detail = ff['generator_detail']
        except:
            my_feed_generator_detail = 'None'

        try:
            my_feed_docs = ff['docs']
        except:
            my_feed_docs = 'None'

        try:
            my_feed_generator = ff['generator']
        except:
            my_feed_generator = 'None'

        try:
            my_feed_publisher = ff['publisher']
        except:
            my_feed_publisher = 'None'


      Post.objects.create(entry_title=ent.title,entry_title_detail_type=ent.title_detail.type,entry_title_detail_base=ent.title_detail.base,
      entry_title_detail_value=ent.title_detail.value,
      entry_links_rel=ent.links[0].rel,
      entry_links_type=ent.links[0].type,
      entry_links_href=ent.links[0].href,
      entry_title_detail_language=ent.title_detail.language,
      entry_link=ent.link,
      entry_summary=ent.summary,
      entry_summary_detail_type=ent.title_detail.type,
      entry_summary_detail_language=ent.title_detail.language,
      entry_summary_detail_base=ent.title_detail.base,
      entry_summary_detail_value=ent.title_detail.value,
      entry_published=ent.published,
      entry_published_parsed = ent.published_parsed,
      entry_id = myid,
      entry_guidislink = myguidislink,
      entry_content_type=my_entry_content_type,
      entry_content_language=my_entry_content_language,
      entry_content_base = my_entry_content_base,
      entry_content_value = my_entry_content_value,
      entry_media_thumbnail_url= my_media_thumbnail_url,
      entry_media_thumbnail_width= my_media_thumbnail_width,
      entry_media_thumbnail_height= my_media_thumbnail_height,
      entry_href = myhref,
      entry_media_content_type = my_entry_media_content_type,
      entry_media_content_url = my_entry_media_content_url,
      entry_media_content_height = my_entry_media_content_height,
      entry_media_content_medium = my_entry_media_content_medium,
      entry_media_content_width = my_entry_media_content_width,
      entry_media_credit_content = my_entry_media_credit_content,
      entry_credit = my_entry_credit,
      entry_authors = my_entry_authors,
      entry_author = my_entry_author,
      entry_author_detail = my_entry_author_detail,
      entry_tags_term = my_entry_tags_term,
      entry_tags_scheme = my_entry_tags_scheme,
      entry_tags_label = my_entry_tags_label,
      feed_title = my_feed_title,
      feed_title_detail_type=my_feed_title_detail_type,
      feed_title_detail_language=my_feed_title_detail_language,
      feed_title_detail_base=my_feed_title_detail_base,
      feed_title_detail_value=my_feed_title_detail_value,
      feed_links_rel = my_feed_links_rel,
      feed_links_type = my_feed_links_type,
      feed_links_href=my_feed_links_href,
      feed_link = my_feed_link,
      feed_image_title = my_feed_image_title,
      feed_image_title_detail_type = my_feed_image_title_detail_type,
      feed_image_title_detail_language = my_feed_image_title_detail_language,
      feed_image_title_detail_base = my_feed_image_title_detail_base,
      feed_image_title_detail_value = my_feed_image_title_detail_value,
      feed_image_href = my_feed_image_href,
      feed_image_link = my_feed_image_link,
      feed_image_links = my_feed_image_links,
      feed_subtitle = my_feed_subtitle,
      feed_subtitle_detail=my_feed_subtitle_detail,
      feed_language=my_feed_language,
      feed_rights = my_feed_rights,
      feed_rights_detail=my_feed_rights_detail,
      feed_updated=my_feed_updated,
      feed_updated_parsed=my_feed_updated_parsed,
      feed_published=my_feed_published,
      feed_published_parsed=my_feed_published_parsed,
      feed_tags_term = my_feed_tags_term,
      feed_tags_scheme = my_feed_tags_scheme,
      feed_tags_label = my_feed_tags_label,
      feed_tags_list=my_feed_tags_list,
      feed_ttl=my_feed_ttl,
      feed_docs=my_feed_docs,
      feed_generator_detail=my_feed_generator_detail)