# TL;DR - 2 - Language and Text: Foundation of Language Models

Module 2 covers how computers represent and process text, forming the basis for language modeling.

## Character Encodings

Computers store text as binary numbers using standards like ASCII (English only) and UTF-8 (supports all languages). UTF-8 uses variable bytes per character to efficiently represent global scripts.

## Tokenization

Language models break text into meaningful units (tokens) using three main approaches:

- Character-level: Each character is a token (small vocabulary but very long sequences)
- Word-level: Each word is a token (semantic meaning but huge vocabulary)
- Subword tokenization: Balance between the two (handles unseen words by combining subword pieces)

Modern LLMs primarily use subword methods like BPE (used by GPT) and WordPiece (used by BERT).

## Statistical Patterns in Language

The module explores how words follow statistical distributions (Zipf's Law) and how n-grams (sequences of n words) capture local patterns in text.

## N-gram Language Models

The first approach to language modeling:

- Count occurrences of word sequences in training data
- Use these counts to predict probability of next words
- Limited by sparsity and inability to generalize to unseen combinations

## Perplexity

The standard evaluation metric for language models, measuring how "surprised" a model is by new text. Lower perplexity means better prediction.

This foundation of text representation sets the stage for neural approaches to language modeling in Module 3.