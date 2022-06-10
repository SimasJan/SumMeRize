
# AIM
From the input URL used as source, and the desired <context>, collect information from the article and provide results.
Including parsing URL sources found in the article, and them too.

## The PLAN
1. Give URL as source and ENT as entity and return entities found as ENT within the URL. (9.6.22)
2. Accept multiple ENT (9.6.22)
3. Provide output filename to store results.
4. Accept multiple sources (from a file)
5. Crawl through the hyperlinks found in the original source, to build greater search space within the relevant context.
6. Show in the result output, sentence(s) where target entity was found.
7. Replace spacy entity types as accepted entities input from the user with the free entity text matching entity explanation examples provided in the spacy library. (ORG: [])