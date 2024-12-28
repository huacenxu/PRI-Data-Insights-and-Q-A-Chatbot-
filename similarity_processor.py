import time
from sentence_transformers import SentenceTransformer, util


class SimilarityProcessor:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        """
        Initialize the SimilarityProcessor with a specific embedding model.
        """
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

    def compute_similarity(self, data, text_col1, text_col2, similarity_col='similarity_score'):
        """
        Compute similarity scores between two text columns and add them to the DataFrame.

        Args:
            data (pd.DataFrame): The input DataFrame.
            text_col1 (str): The name of the first text column.
            text_col2 (str): The name of the second text column.
            similarity_col (str): The name of the new column for similarity scores.
        
        Returns:
            pd.DataFrame: The DataFrame with the similarity scores added.
        """
        # Fill missing values with an empty string
        texts1 = data[text_col1].fillna("").tolist()
        texts2 = data[text_col2].fillna("").tolist()

        # Compute embeddings and similarity scores
        start_time = time.time()
        print("Generating embeddings...")
        embeddings1 = self.model.encode(texts1, convert_to_tensor=True)
        embeddings2 = self.model.encode(texts2, convert_to_tensor=True)

        print("Computing cosine similarity scores...")
        similarity_scores = util.cos_sim(embeddings1, embeddings2).diagonal().cpu().numpy()

        # Add similarity scores to the DataFrame
        data[similarity_col] = similarity_scores

        elapsed_time = time.time() - start_time
        print(f"Processed {len(data)} rows in {elapsed_time:.2f} seconds.")
        return data
