from scraper import get_html, get_metatags
from bs4 import BeautifulSoup
from collections import Counter
import re


def analyze_meta_tags(metatags):
    missing_attrs = []
    for tag in metatags:
        # Skip charset meta tag
        # as it doesn't need 'name' or 'content'
        if tag.get('charset'):
            continue

        # Skip tags with a 'property' attribute
        if tag.get('property') and not tag.get('name'):
            continue

        # Check for tags that should have 'name' and 'content'
        if not tag.get('name') or not tag.get('content'):
            missing_attrs.append(str(tag))
    return missing_attrs


def get_text_content(soup):
    # Removing script and style elements for convenience
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()  # Remove these elements
    text = ' '.join(soup.stripped_strings)
    return text


def get_top_keywords(text, num_keywords=10):
    # A list of tuples, each containing a word and its frequency
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(num_keywords)


def keyword_meta_comparison(meta_keywords, common_words):
    # find words that are both in the meta keywords and the common words from the content
    meta_keywords_set = set(meta_keywords.lower().split(","))
    common_words_set = set(word for word, count in common_words)
    return meta_keywords_set.intersection(common_words_set)


if __name__ == "__main__":
    url = "https://hurthub.davidson.edu/"
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    metatags = get_metatags(soup)

    # Analyze missing attributes
    missing_attrs = analyze_meta_tags(metatags)
    print("Missing Attributes in Meta Tags:", missing_attrs)

    # Content and keyword analysis
    text_content = get_text_content(soup)
    common_words = get_top_keywords(text_content)

    # Find meta keywords for comparison
    meta_keywords_content = ''
    for tag in metatags:
        if tag.get('name') == 'keywords':
            meta_keywords_content = tag.get('content', '')
            break

    matching_keywords = keyword_meta_comparison(
        meta_keywords_content, common_words)
    print("Matching Keywords in Meta and Content:",
          matching_keywords)  # can hardly identify any
