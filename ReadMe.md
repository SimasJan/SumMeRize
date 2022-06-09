
# AIM
From the input URL used as source, and the desired <context>, collect information from the article and provide results.
Including parsing URL sources found in the article, and them too.

## The PLAN
Phase 1:
[x] 1. Give URL as source and ENT as entity and return entities found as ENT within the URL. 
[x] 2. Accept multiple ENT
3. Provide output filename to store results.
4. Accept multiple sources (from a file)

Phase 2:
1. Crawl through the hyperlinks found in the original source, to build greater search space within the relevant context.
2. Show in the result output, sentence(s) where target entity was found.
