import wikipediaapi
from django.contrib import messages
from django.core.mail import send_mail


# write a function to fetch summary section of a wikipedia page by passing title argument and using wikipedia api.

def fetch_summary(title):
    wiki_wiki = wikipediaapi.Wikipedia('wiki_stat (you.aouali@gmail.com)', 'en')
    page_py = wiki_wiki.page('Python_(programming_language)')

    print("Page - Title: %s" % page_py.title)
    # Page - Title: Python (programming language)

    print("Page - Summary: %s" % page_py.summary[0:60])
    # Page - Summary: Python is a widely used high-level programming language for
    return page_py.summary


# write a second function to interpret the amount of 5+ letter words in the summary section. Return an alert in the second function if more than 20% of words are 5+ letter words. Send an email if an alert exists 


def interpret_summary(summary):
    words = summary.split()
    big_words = [word for word in words if len(word) >= 5 and word.isalpha()]
    if len(big_words) / len(words) > 0.2:
        send_alert()
    return big_words


def send_alert():
        send_mail(
            'Alert: High percentage of big words',
            'More than 20% of words are 5+ letters.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

