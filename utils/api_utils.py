import json
import logging
from collections import namedtuple

from newsapi import NewsApiClient

logger = logging.getLogger(__name__)
SourceAttributes = namedtuple("SourceAttributes", ["id", "name"])

def get_top_headlines(news_api: NewsApiClient,
                      q=None,
                      qintitle=None,
                      sources=None,
                      language="en",
                      country=None,
                      category=None,
                      page_size=None,
                      page=None) -> json:
    try:
        logger.info(f"[get_top_headlines] - Start - "
                    f"q={q} "
                    f"qintitle={qintitle} "
                    f"sources={sources} "
                    f"language={language} "
                    f"country={country} "
                    f"category={category} "
                    f"page_size={page_size} "
                    f"page={page}")

        top_headlines = news_api.get_top_headlines(q=q,
                                                   qintitle=qintitle,
                                                   sources=sources,
                                                   category=category,
                                                   language=language,
                                                   country=country,
                                                   page_size=page_size,
                                                   page=page).get('articles')
        logger.info("[get_top_headlines] - End processing")
        return top_headlines
    except Exception as ex:
        logger.error(repr(ex))



def get_sources_id(news_api: NewsApiClient,
                   category=None,
                   language=None,
                   country=None) -> SourceAttributes:
    try:
        logger.info(f"[get_sources_id] - Start - "
                    f"category={category} "
                    f"language={language} "
                    f"country={country}")
        source_json = news_api.get_sources(category=category,
                                           language=language,
                                           country=country).get("sources")

        for source_dic in source_json:
            yield SourceAttributes(source_dic.get("id"), source_dic.get("name"))
        logger.info("[get_sources_id] - End processing")
    except Exception as ex:
        logger.error(repr(ex))
