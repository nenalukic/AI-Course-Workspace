## Lesson 1: Natural Language Processing (NLP) & Attention
Before Transformers, AI read text sequentially (word by word), which made it easily forget the beginning of a long sentence.

Transformers solved this using the Self-Attention mechanism.

Instead of reading word-by-word, the model looks at the entire sentence at once. For every single word, it calculates an "attention score" with every other word to understand context. For example, in the sentence "The bark of the tree," attention tells the model that "bark" relates to "tree" and not a dog.