#ai #machinelearning #database #computerscience 

O que é e quando usar um vector database?

Vector databases são bem recentes e estão ficando mais populares com esse hype das AIs. Mas quando é útil utilizar esse tipo de DB?

--------------------

Search engines como o Google utilizam full-text search, porém NLPs como o ChatGPT e o Bing AI usam semantic search ou similarity search, um tipo de busca que considera não só a semelhança dos caracteres, mas tbm o significado das palavras

--------------------

Como isso funciona? Uma NLP recebe um texto como entrada e retorna um texto como saída. Isso envolve várias etapas de processamento, uma delas é a vetorização.

------------------------------

No processo de vetorização, os tokens do texto de entrada são convertidos em vetores usando  operações de álgebra linear. Simplificando:

Um texto vira um array com valores numéricos, por ex.:

"aprendendo NLP" ---> [0.9, 0.02, 0.88, 0.1, 0.3]

----------------------------------

E é agora q entra o vector database. Já temos um monte de vetores, mas esses vetores são basicamente números, matrizes, eles não significam nada isoladamente. Então o vector database é usado para indexar esses vetores.

----------------------------------

O vector database vai indexar os vetores, deixando próximos os vetores com valores parecidos, isso possibilita que aconteça uma busca por semelhança no banco de dados (similarity search), se você buscar por

------------------------------------

"What was the Great Depression?"

Se essa frase não existir no seu banco de dados, você consegue obter resultados mesmo assim, por causa da similaridade.

----------------------------------

E com isso, pode ser feita também uma busca semântica (semantic search), um tipo de busca que leva em consideração o significado das palavras também. Porém, muitas vezes a busca semântica não é necessária, porque uma vetorização bem feita já leva em consideração o significado das palavras