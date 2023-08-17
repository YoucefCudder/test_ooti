import wikipediaapi
from django.contrib import messages
from django.core.mail import send_mail



def fetch_summary(title):
    wiki_wiki = wikipediaapi.Wikipedia('wiki_stat (you.aouali@gmail.com)', 'en')
    page_py = wiki_wiki.page('Python_(programming_language)')

    print("Page - Title: %s" % page_py.title)

    print("Page - Summary: %s" % page_py.summary[0:60])
    return page_py.summary




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

