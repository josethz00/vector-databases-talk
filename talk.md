---
marp: true
math: mathjax
style: |
 section.split {
    overflow: visible;
    display: grid;
    grid-template-columns: 600px 600px;
    grid-template-rows: 100px auto;
    grid-template-areas: 
        "slideheading slideheading"
        "leftpanel rightpanel";
    }

    section.split .ldiv { grid-area: leftpanel; }
    section.split .rdiv { grid-area: rightpanel; }
---

# Vector Databases

![bg right 99%](./vector-db-banner.png)

<i style="font-size: 22px; font-weight: bold; color: #666">With the rise of AI, vector databases are becoming more popular. But what exactly is a vector database and when should you use it? </i>

---

## What is a vector database?

Traditional search engines use full-text search, but NLPs like ChatGPT and Bing AI use semantic search or similarity search, a type of search that considers not only the characters match, but also the meaning of the words

* Recently Google also started using semantic search

---

<!-- _class: split -->

<div class=ldiv>

### Full-text search

- Search for a word or phrase in large amounts of text
- The search engine returns a list of documents that contain the search term

</div>


<div class=rdiv>

### Semantic search

- Search for a word or phrase in large amounts of text
- The search engine will return a list of documents that contain the search term or have a similar meaning

</div>

---

## Full-text search

```sql
SELECT title, content
FROM documents
WHERE search_vector @@ plainto_tsquery('english', 'example search');
```

---

## Semantic search

![width:900px](./semantic-search.png)