from sentence_transformers import SentenceTransformer
from celery import shared_task
import numpy as np
from project.models import Post
from datetime import datetime

@shared_task
def calculate_summary_vector():
    start_time = datetime.now()
    posts = Post.objects.filter(summary_vector=[]).order_by('-creationdate')[:100000]
    i = 0
    multilingual_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    for p in posts:
        i += 1
        small_sum_emb = multilingual_model.encode(p.entry_summary, convert_to_tensor=True)
        vector = np.array(small_sum_emb.cpu())
        p.summary_vector = [vector]
        p.save()
    end_time = datetime.now()
    print(end_time - start_time)
