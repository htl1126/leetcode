# Ref: https://leetcode.com/problems/web-crawler/discuss/450325/Python-BFS-straightforward
# Algo: BFS

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

import collections

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        visited = {startUrl}
        ans = [startUrl]
        queue = collections.deque([startUrl])
        domain = startUrl.split("http://")[1].split('/')[0]
        while queue:
            url = queue.popleft()
            check = htmlParser.getUrls(url)
            for new_url in check:
                if new_url in visited:
                    continue
                if new_url.split("http://")[1].split('/')[0] != domain:
                    continue
                visited.add(new_url)
                ans.append(new_url)
                queue.append(new_url)
        return ans
