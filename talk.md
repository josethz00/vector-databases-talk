---
marp: true
math: mathjax
style: |
 section.split {
    overflow: visible;
    display: grid;
    grid-template-columns: 500px 500px;
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

## A split slide
<!-- _class: split -->

<div class=ldiv>

#### Title for the left panel
- listed item
- listed item
- listed item
</div>
<div class=rdiv>

#### Title for the right panel
- listed item
- listed item
- listed item
</div>