---
marp: true
math: mathjax
---

# Vector Databases

![bg right 99%](./vector-db-banner.png)

<i style="font-size: 22px; font-weight: bold; color: #666">With the rise of AI, vector databases are becoming more popular. But what exactly is a vector database and when should you use it? </i>

---

## What is a vector database?

Traditional search engines use full-text search, but NLPs like ChatGPT and Bing AI use semantic search or similarity search, a type of search that considers not only the characters match, but also the meaning of the words

* Recently Google also started using semantic search

---



```sql
SELECT title, content
FROM documents
WHERE search_vector @@ plainto_tsquery('english', 'example search');
```
