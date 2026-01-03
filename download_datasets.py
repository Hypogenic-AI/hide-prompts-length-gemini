import os
from datasets import load_dataset

def download_datasets():
    print("Downloading Wikitext-103...")
    try:
        # Wikitext-103 has long articles
        dataset = load_dataset("wikitext", "wikitext-103-raw-v1", split="test") 
        
        save_path = "datasets/wikitext_103"
        dataset.save_to_disk(save_path)
        print(f"Successfully saved to {save_path}")
        
        # Save a sample
        with open(os.path.join(save_path, "sample.txt"), "w") as f:
            f.write(str(dataset[0]))
            
    except Exception as e:
        print(f"Error downloading Wikitext: {e}")

if __name__ == "__main__":
    os.makedirs("datasets", exist_ok=True)
    download_datasets()