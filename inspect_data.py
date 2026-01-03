from datasets import load_from_disk
import pandas as pd

try:
    # Load Wikitext
    print("Loading Wikitext...")
    ds = load_from_disk("datasets/wikitext_103")
    print("Type:", type(ds))
    print("DS:", ds)
    
    if hasattr(ds, 'keys'):
        print("Keys:", ds.keys())
        # Access train if available
        if 'train' in ds:
            split = ds['train']
        else:
            split = ds[list(ds.keys())[0]]
    else:
        split = ds

    print("Columns:", split.column_names)
    print("Num rows:", len(split))
    print("First item text length:", len(split[0]['text']))
    
except Exception as e:
    print(f"Error loading Wikitext: {e}")
    import traceback
    traceback.print_exc()