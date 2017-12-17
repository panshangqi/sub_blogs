# -*- coding=utf-8 -*-
from HTMLParser import HTMLParser
# 获取文章摘要
class SummaryHTMLParser(HTMLParser):
    """Parse HTML text to get a summary
        >>> text = u'Hi guys:This is a example using SummaryHTMLParser.'
        >>> parser = SummaryHTMLParser(10)
        >>> parser.feed(text)
        >>> parser.get_summary(u'...')
        u'Higuys:Thi...'
    """

    def __init__(self, count):
        HTMLParser.__init__(self)
        self.count = count
        self.summary = u''

    def feed(self, data):
        """Only accept unicode `data`"""
        assert (isinstance(data, unicode))
        HTMLParser.feed(self, data)

    def handle_data(self, data):
        more = self.count - len(self.summary)
        if more > 0:
            # Remove possible whitespaces in `data`
            data_without_whitespace = u''.join(data.split())

            self.summary += data_without_whitespace[0:more]

    def get_summary(self, suffix=u'', wrapper=u'p'):
        return u'{1}{2}{0}'.format(wrapper, self.summary, suffix)