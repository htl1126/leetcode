# Ref: https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/1110529/Python-Use-two-dictionaries-explained

class Codec:
    def __init__(self):
        self.short_long = {}
        self.long_short = {}
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.long_short:
            code = "".join(random.choices(self.alphabet, k=6))
            if code not in self.short_long:
                self.long_short[longUrl] = code
                self.short_long[code] = longUrl
        return "http://tinyurl.com/" + self.long_short[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_long[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
