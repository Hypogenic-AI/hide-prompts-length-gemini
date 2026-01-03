import pandas as pd
from datasets import load_from_disk
import tiktoken
import random

class DataManager:
    def __init__(self, wikitext_path="datasets/wikitext_103", advbench_path="datasets/advbench.csv", seed=42):
        self.wikitext_path = wikitext_path
        self.advbench_path = advbench_path
        self.seed = seed
        self.enc = tiktoken.get_encoding("cl100k_base") # Approximation for GPT models
        self.haystack_text = ""
        
        self._load_data()
        
    def _load_data(self):
        # Load AdvBench
        try:
            df = pd.read_csv(self.advbench_path)
            self.needles = df['goal'].tolist()
        except Exception as e:
            print(f"Error loading AdvBench: {e}")
            self.needles = []
            
        # Load Wikitext
        try:
            ds = load_from_disk(self.wikitext_path)
            # Flatten text
            texts = [x['text'] for x in ds if len(x['text'].strip()) > 0]
            # Join with newlines
            self.haystack_text = "\n\n".join(texts)
            # Tokenize entire massive string (this might be slow, let's optimize)
            # Instead of full tokenization, we can approximate or tokenize on demand.
            # But for precise length control, tokenization is best.
            # Let's tokenize a large chunk, say first 500k tokens.
        except Exception as e:
            print(f"Error loading Wikitext: {e}")
            self.haystack_text = ""

    def get_needles(self, n=20):
        random.seed(self.seed)
        return random.sample(self.needles, min(n, len(self.needles)))

    def get_haystack(self, length, sample_idx=0):
        """
        Get a text chunk of approximately `length` tokens.
        We use a sliding window based on sample_idx to get different chunks.
        """
        # We need a robust way to get random chunks.
        # Let's tokenize on demand.
        
        # Approximate char length (1 token ~= 4 chars)
        approx_char_len = length * 4
        
        # Total length
        total_len = len(self.haystack_text)
        if total_len == 0:
            return ""
            
        # Pick a random start position seeded by sample_idx + seed
        rng = random.Random(self.seed + sample_idx)
        start_char = rng.randint(0, max(0, total_len - approx_char_len - 10000))
        
        # Take a slice
        text_slice = self.haystack_text[start_char : start_char + approx_char_len * 2] # Grab extra
        
        # Truncate to exact tokens
        tokens = self.enc.encode(text_slice)
        if len(tokens) < length:
            # Padding if too short (repeat)
            while len(tokens) < length:
                tokens += tokens
            
        tokens = tokens[:length]
        return self.enc.decode(tokens)

    def insert_needle(self, haystack, needle, position_percent):
        """
        Insert needle at position_percent (0-100).
        """
        tokens_haystack = self.enc.encode(haystack)
        tokens_needle = self.enc.encode("\n\n" + needle + "\n\n") # Add whitespace for separation
        
        pos_idx = int(len(tokens_haystack) * (position_percent / 100.0))
        
        new_tokens = tokens_haystack[:pos_idx] + tokens_needle + tokens_haystack[pos_idx:]
        return self.enc.decode(new_tokens)
