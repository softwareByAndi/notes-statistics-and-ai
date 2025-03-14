# TL;DR - 3 - Neural Networks for Language

Module 3 explains how neural networks revolutionized language modeling by overcoming limitations of earlier statistical approaches (like n-grams).

## Word Embeddings

Neural networks represent words as vectors (lists of numbers) in a continuous space where similar words have similar vectors. This allows the model to understand relationships between words (like "king - man + woman ≈ queen").

## RNNs (Recurrent Neural Networks)

RNNs process text sequentially, maintaining a "memory" of previous words through an internal state that gets updated with each new word. This helps them capture context in ways n-grams couldn't.

## LSTMs and GRUs

Regular RNNs struggle with longer sequences due to the "vanishing gradient problem." LSTMs (Long Short-Term Memory) and GRUs (Gated Recurrent Units) solve this using special "gates" that control what information to remember or forget, allowing them to maintain relevant context over longer distances.

## Character-Level Language Models

The module demonstrates building a character-level LSTM model that:

- Takes one character as input
- Predicts the next character
- Can generate text character by character

## Limitations of RNN-Based Models

While powerful, RNNs and LSTMs have drawbacks:

- Sequential processing makes them slow (can't be parallelized)
- Still struggle with very long-range dependencies
- Computationally inefficient for long sequences

These limitations led to the development of Transformer models (covered in Module 4), which would eventually enable modern LLMs by processing entire sequences in parallel rather than sequentially.