from math import ceil
class Cipher:
    def __init__(self, key="ddddddddddddddddd"):
        self.key = key
    
    def get_raw(string):
        return [ord(x) - 97 for x in string]
    def shift(value, key, function):
        # key needs to be extended to match the value's length
        ratio = ceil(len(value) / len(key))
        
        raw_val = Cipher.get_raw(value)
        raw_key = Cipher.get_raw(key) * ratio
        
        return "".join([chr(function(v, k)) for (v, k) in zip(raw_val, raw_key)])
    def encode(self, text):
        return Cipher.shift(text, self.key, lambda v, k: (v + k) % 26 + 97)
    def decode(self, text):
        return Cipher.shift(text, self.key, lambda v, k: (v - k) % 26 + 97)
        