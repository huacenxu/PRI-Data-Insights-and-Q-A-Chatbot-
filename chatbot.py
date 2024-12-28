from sentence_transformers import SentenceTransformer, util


class Chatbot:
    def __init__(self, knowledge_base, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.knowledge_base = knowledge_base
        self.model = SentenceTransformer(model_name)
        self.encoded_questions = self.model.encode([kb["question"] for kb in knowledge_base], convert_to_tensor=True)

    def get_response(self, user_input):
        user_embedding = self.model.encode(user_input, convert_to_tensor=True)
        similarities = util.cos_sim(user_embedding, self.encoded_questions)
        best_match = similarities.argmax().item()
        return self.knowledge_base[best_match]["answer"]
