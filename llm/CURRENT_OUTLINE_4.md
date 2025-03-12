# outline

- [[introduction]]
- [[course structure]]
- [[learning_approach]]

---

Each module builds upon the previous ones, creating a comprehensive understanding of the entire LLM development process from text representation to cutting-edge applications.

- [[_mod 0 - Prerequisites and Preparation]]
- [[_mod 1 - The Big Picture - What Are We Building]]
- [[_mod 2 - Language and Text - The Foundation]]

## future modules - not yet developed

**Module 3: Neural Networks for Language**

- Word embeddings and vector representations
- Recurrent neural networks for sequences
- Building a character-level RNN language model

**Module 4: The Transformer Revolution**

- Attention mechanisms explained
- The complete transformer architecture
- Building a simple transformer for next-word prediction

**Module 5: Scaling Up - From Models to LLMs**

- Training dynamics of large models
- Pre-training objectives and techniques
- Building and training a small-scale transformer

**Module 6: Transfer Learning and Fine-tuning**

- Utilizing pre-trained models
- Fine-tuning strategies and techniques
- Advanced fine-tuning with parameter-efficient methods

**Module 7: Prompt Engineering and In-context Learning**

- The art and science of effective prompting
- Few-shot and zero-shot techniques
- Building prompt-based applications

**Module 8: Alignment and Safety**

- Addressing biases in language models
- Reinforcement Learning from Human Feedback (RLHF)
- Techniques for responsible AI development

**Module 9: Deployment and Production**

- Model optimization and quantization
- Inference systems and scaling
- Building production-ready LLM applications

**Module 10: Cutting-Edge Applications and Research**

- Multimodal capabilities
- Tool use and augmented models
- Future directions in LLM research

---

## introduction

Welcome to this comprehensive crash course on programming Large Language Models (LLMs) from scratch. This course is designed with a unique approach - we'll start by understanding what we're ultimately building, then work backward to explore all the foundational elements needed to get there. This gives you the "why" before the "how," making your learning journey more purposeful and connected.

Large Language Models represent one of the most significant technological breakthroughs of our time. These systems can understand language, generate text, translate content, write code, and even reason about complex problems. But how do they actually work? How can you build one yourself? This course will demystify the entire process, breaking down complex concepts into understandable pieces while maintaining the technical depth needed for true mastery.

---

## course structure

This course is organized as a set of interconnected modules that form a knowledge network:

1. **End-to-End Overview**: Understanding what we're building and why
2. **Foundational Elements**: The mathematical and programming fundamentals
3. **Core Building Blocks**: Key technologies and techniques
4. **Integration and Scaling**: Putting it all together and making it powerful
5. **Optimization and Deployment**: Making it efficient and usable
6. **Cutting Edge Applications**: Exploring the frontiers of what's possible

Each module builds upon previous ones, with clear references to prerequisite knowledge. You can follow the course linearly, or navigate based on your specific interests or projects.

---

## learning_approach

Throughout this course, I'll follow these principles:

- **Simple Language for Complex Ideas**: Technical concepts explained in plain language
- **Progressive Complexity**: Starting with the basics before diving deeper
- **Practical Examples**: Code samples and projects to reinforce learning
- **Visual Explanations**: Diagrams and visualizations to clarify abstract concepts
- **Hands-On Projects**: Milestone projects for each major section to build your portfolio
- **Real-World Applications**: Connecting theory to practical implementation

Now, let's begin with our course map and prerequisites before diving into our first module.

---

## mod 0 - Prerequisites and Preparation

Before we start building language models, let's ensure you have the right foundation:
- [[Knowledge Prerequisites]]
- [[Recommended Setup]]
- [[Quick Mathematics Review]]

Don't worry if you don't have extensive machine learning experience - we'll build that knowledge together from the ground up.

---

### Knowledge Prerequisites

- **Programming**: You should be comfortable with Python programming
- **Mathematics**: Basic algebra knowledge is required; we'll review other math concepts as needed
- **Development Environment**: Access to a computer where you can run Python code

---

### Recommended Setup

- Python 3.8+ installed on your system
- Basic familiarity with Jupyter notebooks
- Understanding of pip for package installation

### Development Environment Setup

Let's set up your working environment:

1. **Install Python**: If you haven't already, download and install Python 3.8 or newer
2. **Create a virtual environment**: This keeps your project dependencies separate
    
    ```bash
    python -m venv llm-coursesource llm-course/bin/activate  # On Windows: llm-course\Scripts\activate
    ```
    
3. **Install basic libraries**:
    
    ```bash
    pip install numpy pandas matplotlib jupyter torch transformers
    ```
    
4. **Create a project folder**:
    
    ```bash
    mkdir llm-from-scratchcd llm-from-scratch
    ```
    
5. **Start Jupyter**:
    
    ```bash
    jupyter notebook
    ```
    

This will give you a solid starting point to work through the course examples and projects.

---

### Quick Mathematics Review

While we'll explain mathematical concepts as we encounter them, here's a brief refresher on some key areas that will appear throughout the course:

#### Linear Algebra Essentials
#linear-algebra 

- **Vectors**: Ordered lists of numbers with magnitude and direction
- **Matrices**: 2D arrays of numbers with rows and columns
- **Operations**: Addition, multiplication, transpose

For example, a vector might represent a word in our language model, while a matrix might represent a transformation we apply to that word.

#### Probability Basics
[[probability.ipynb]]
- **Random variables**: Values determined by chance
- **Probability distributions**: How likely different outcomes are
- **Conditional probability**: The likelihood of an event given another event occurred

Language models fundamentally work with probabilities - "what word is most likely to come next?"

#### Calculus Foundations
- **Derivatives**: Rate of change (how quickly a function's output changes)
- **Gradients**: Direction of steepest increase (critical for training neural networks)

Don't worry if these concepts aren't completely familiar - we'll explain them in context as needed.

---

#### probability.ipynb

``` md
[<< home](../home.md)

# probability

- probability - chance or likelihood of something happening
- event - something that happens / the outcome of an experiment
- experiment - a process that is performed to observe possible outcomes
- sample space - the set of all outcomes of an experiment

**note that most of this is generated from github copilot AI... it needs to be double checked**

**equation:**  
- probability of an event = number of favorable outcomes / total number of possible outcomes

### mutually exclusive events
- two events are mutually exclusive if they cannot occur at the same time
- the probability of two mutually exclusive events occurring at the same time is 0

### independent events
- two events are independent if the occurrence of one event does not affect the probability of the other event
- the probability of two independent events occurring at the same time is the product of their individual probabilities

### dependent events
- two events are dependent if the occurrence of one event affects the probability of the other event
- the probability of two dependent events occurring at the same time is the product of their individual probabilities

### conditional probability: P(A|B)
the probability of an event occurring **given** that another event has already occurred
- **mutually exclusive events**: `P(A|B) = 0`
- **non-mutually exclusive events**: `P(A|B) = P(A and B) / P(B)`
    - We divide by P(B) because we are only considering the probability of A occurring given that B has already occurred. 
    - We are not considering the probability of B occurring given that A has already occurred.

### multiplication rule: P(A and B)
both occurring at the same time
- **mutually exclusive events**: `P(A and B) = 0`
- **non-mutually exclusive events**: `P(A and B) = P(A) * P(B|A)`

### addition rule: P(A or B)
one or the other or both occurring
- **mutually exclusive events**: `P(A or B) = P(A) + P(B)`
- **non-mutually exclusive events**: `P(A or B) = P(A) + P(B) - P(A and B)`
    - We subtract P(A and B) because these entries are duplicates. 
    - Entries that intersect are counted once from A and again from B, so we need to subtract one of them.

### permutations
- the number of ways to arrange a set of objects in a specific order
- n objects taken r at a time is `n! / (n - r)!`
- n objects taken all at a time is `n!`

### combinations
- the number of ways to select a subset of objects from a larger set of objects
- the number of combinations of n objects taken r at a time is `n! / (r! * (n - r)!)`
- the number of combinations of n objects taken all at a time is `1`

### binomial probability
- the probability of exactly x successes in n trials
- `P(r) = (n! / (r! * (n - r)!)) * prob_success^r * prob_failure^(n - r)`


### bayes rule
- [see bayes rule](./bayes_rule.ipynb)

### marginal probability / joint probability table
this is a table view that shows both marginal and joint probabilities for two events
- marginal probability: the probability of a single event occurring
- joint probability: the probability of two events occurring at the same time
- [see marginal and joint probability](./marginal_and_joint_probability.ipynb)




```

---

## mod 1 - The Big Picture - What Are We Building

Before diving into the technical details, let's understand what a Large Language Model actually is and what we're working toward building.

- [[1.1 What is a Large Language Model]]
- [[1.2 The Evolution of Language Models]]
- [[1.3 Key Components of Modern LLMs]]
- [[1.4 The Journey of a Prompt]]
- [[1.5 Understanding Model Scale]]
- [[1.6 Hands-On Project - Using an Existing LLM via API]]
- [[1.7 Key Takeaways from Module 1]]
- [[1.8 Preview of Module 2 - Text Representation]]

---

### 1.1 What is a Large Language Model

At its core, a Large Language Model is a system that learns patterns in language from vast amounts of text data, then uses those patterns to generate new text that's coherent, relevant, and sometimes surprisingly insightful.

**Simple Definition**: A Large Language Model is a computer program that predicts what words should come next in a sequence, based on patterns it learned from reading billions of documents.

Imagine having read every book, article, and website ever published, and developing an intuition for how language works. LLMs attempt to capture that intuition mathematically.

---

### 1.2 The Evolution of Language Models

Language models have evolved dramatically over time:

1. **Statistical Models (1980s-2000s)**
    
    - Simple probability-based models (n-grams)
    - Limited by sparse data and lack of generalization
2. **Neural Network Models (2010-2017)**
    
    - Word embeddings (Word2Vec, GloVe)
    - Recurrent Neural Networks (RNNs, LSTMs)
    - Better generalization but struggled with long contexts
3. **Transformer Revolution (2017-Present)**
    
    - Attention mechanisms replaced recurrence
    - Enabled efficient training on massive datasets
    - Opened the door to truly large models
4. **Scaling Era (2019-Present)**
    
    - GPT, BERT, T5, and other massive models
    - Emergent capabilities appearing with scale
    - Continued improvements in architecture and training

We'll work through this evolution throughout the course, building our understanding layer by layer.

---

### 1.3 Key Components of Modern LLMs

A modern Large Language Model system consists of several critical components:

1. **Tokenization System**: Converting text to numbers and back
2. **Neural Network Architecture**: Typically transformer-based
3. **Training Infrastructure**: Hardware and software for learning
4. **Fine-tuning System**: Specializing models for specific tasks
5. **Inference Engine**: Running the model efficiently
6. **Application Layer**: Integrating the model into useful tools

Each of these components involves fascinating engineering and research challenges that we'll explore in detail.

---

### 1.4 The Journey of a Prompt

To understand how LLMs work, let's follow what happens when you provide a prompt:

1. **Tokenization**: Your text gets split into tokens (pieces of words or characters)
2. **Embedding**: Tokens are converted to numerical vectors
3. **Processing**: These vectors flow through the neural network's layers
4. **Attention**: The model focuses on relevant parts of your input
5. **Prediction**: The model predicts probability distributions for the next token
6. **Sampling**: A specific token is chosen based on these probabilities
7. **Repetition**: Steps 3-6 repeat to generate each subsequent token
8. **Detokenization**: Tokens are converted back to readable text

This process happens incredibly quickly, with modern models generating thousands of tokens per second on appropriate hardware.

---

### 1.5 Understanding Model Scale

Modern LLMs are defined by their scale:

- **Parameter Count**: The number of adjustable values in the model (ranging from millions to trillions)
- **Training Data**: The amount of text the model learns from (trillions of words)
- **Compute Resources**: The computational power used for training (thousands of GPUs for weeks or months)

While we won't be able to train truly massive models in this course, we'll understand the principles that enable scaling and build smaller models that demonstrate the core concepts.

---

### 1.6 Hands-On Project - Using an Existing LLM via API

Let's get practical with our first project - using an existing LLM through an API. This helps us understand what we're ultimately building toward.

```python
import json
import anthropic

client = anthropic.Anthropic(
	# defaults to os.environ.get("ANTHROPIC_API_KEY")
)
message = client.messages.create(
	model="claude-3-5-haiku-20241022",
	max_tokens=1024,
	messages=[ 
		{
			"role": "user", 
			"content": "Hello, Claude."
		}
	]
)
print(message.to_json())
```

This gives us a taste of what's possible with LLMs, and sets our target for what we'll build toward throughout this course.


#### example - summarize and classify wiki articles
``` python
from claude_models import Models
import anthropic
import wikipedia
import json

client = anthropic.Anthropic()

#tool definition
tools = [
    {
        "name": "print_article_classification",
        "description": "Prints the classification results.",
        "input_schema": {
            "type": "object",
            "properties": {
                "subject": {
                    "type": "string",
                    "description": "The overall subject of the article",
                },
                "summary": {
                    "type": "string",
                    "description": "A paragaph summary of the article"
                },
                "keywords": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "description": "List of keywords and topics in the article"
                    }
                },
                "categories": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "The category name."},
                            "score": {"type": "number", "description": "The classification score for the category, ranging from 0.0 to 1.0."}
                        },
                        "required": ["name", "score"]
                    }
                }
            },
            "required": ["subject","summary", "keywords", "categories"]
        }
    }
]

#The function that generates the json for a given article subject
def generate_json_for_article(subject):
    page = wikipedia.page(subject, auto_suggest=True)
    query = f"""
    <document>
    {page.content}
    </document>

    Use the print_article_classification tool. Example categories are Politics, Sports, Technology, Entertainment, Business.
    """

    response = client.messages.create(
        model=Models.haiku.value,
        max_tokens=4096,
        tools=tools,
        messages=[{"role": "user", "content": query}]
    )

    json_classification = None
    for content in response.content:
        if content.type == "tool_use" and content.name == "print_article_classification":
            json_classification = content.input
            break

    if json_classification:
        print("Text Classification (JSON):")
        print(json.dumps(json_classification, indent=2))
    else:
        print("No text classification found in the response.")

# generate_json_for_article("Transformer (deep learning architecture)")
generate_json_for_article("Jeff Goldblum")
```

---

### 1.7 Key Takeaways from Module 1

- LLMs are pattern recognition systems trained on vast text data
- They evolved from simple statistical models to complex neural networks
- Modern LLMs use transformer architectures and attention mechanisms
- The scale of models has grown exponentially in recent years
- LLMs convert text to numbers, process those numbers, and convert back to text
- Using existing LLMs via APIs provides a reference point for our learning

---

### 1.8 Preview of Module 2 - Text Representation

In our next module, we'll dive deeper into how computers represent text - the foundation of language modeling. We'll explore:

- Character encodings and how text is stored digitally
- Tokenization strategies for breaking text into manageable pieces
- Creating vocabularies and embedding spaces
- Statistical patterns in language and how to measure them

By the end of Module 2, you'll understand how to convert raw text into a format that neural networks can process, setting the stage for our exploration of neural language models.

---

## mod 2 - Language and Text - The Foundation

Welcome to Module 2 of our LLM crash course! In this module, we'll explore the fundamental question: how do computers understand and process text? Before we can build neural networks that work with language, we need to understand how to represent text in a format that machines can work with.

- [[llm/modules/mod 2/2.1 The Text Representation Challenge]]
- [[2.2 Character Encodings - The Digital Alphabet]]
- [[2.3 Tokenization - Breaking Text into Meaningful Units]]
- [[2.4 Statistical Patterns in Language]]
- [[2.5 Building Your First Language Model - N-gram Models]]
- [[2.6 Hands-On Project - Building an N-gram Language Model]]
- [[2.7 Beyond N-grams - The Path Forward]]
- [[2.8 Key Takeaways from Module 2]]
- [[2.9 Practice Exercises]]
- [[2.10 Preview of Module 3 - Neural Networks for Language]]

---

### 2.1 The Text Representation Challenge

Computers don't inherently understand text the way humans do. While we see meaningful words and sentences, computers ultimately work with numbers. The first challenge in building language models is bridging this gap – converting human language into numerical representations that preserve meaning and can be manipulated mathematically.

### From Human Language to Machine Numbers

Think about how you're reading these words right now. Your brain processes visual symbols (letters), combines them into words, and extracts meaning based on your prior knowledge of language. Computers need a similar pipeline, but built explicitly through code.

The journey from raw text to a format usable by language models involves several transformations:

1. **Character encoding**: Converting raw characters to binary
2. **Tokenization**: Breaking text into meaningful units
3. **Numerical representation**: Converting tokens to vectors
4. **Statistical processing**: Capturing patterns and relationships

Let's explore each of these steps in detail.

---

### 2.2 Character Encodings - The Digital Alphabet

At the most fundamental level, computers store everything as binary data – sequences of 0s and 1s. Character encodings provide the rules for converting between human-readable characters and their binary representations.

### ASCII: The Original Digital Alphabet

The American Standard Code for Information Interchange (ASCII) was one of the first widespread character encodings. It uses 7 bits to represent 128 different characters:

- 0-31: Control characters (non-printable)
- 32-126: Printable characters (letters, numbers, symbols)
- 127: Delete character

For example, the letter 'A' is represented as the decimal number 65, which in binary is `1000001`.

While ASCII worked well for English text, it couldn't represent the vast diversity of characters used in other languages. This limitation led to the development of more comprehensive encodings.

### Unicode and UTF-8: A Global Digital Alphabet

Unicode was created to solve the limitations of ASCII by assigning a unique number (code point) to virtually every character used in all the world's writing systems. The most common implementation of Unicode is UTF-8, which uses a variable number of bytes to represent different characters:

- ASCII characters (English letters, numbers) use just 1 byte
- Most European and Middle Eastern scripts use 2 bytes
- East Asian scripts and emojis typically use 3 or 4 bytes

For example:

- The English letter 'A' is still 65 (1 byte): `01000001`
- The Japanese hiragana 'あ' is 12354 (3 bytes): `11100011 10000001 10000010`
- The emoji '😊' is 128522 (4 bytes): `11110000 10011111 10011000 10001010`

UTF-8 has become the dominant encoding for text on the internet because it efficiently handles multiple languages while maintaining backward compatibility with ASCII.

### Why Character Encodings Matter for LLMs

Understanding character encodings is important for several reasons:

1. **Data preprocessing**: We need to ensure our training data uses consistent encoding
2. **Multilingual capabilities**: Different encodings affect how models handle various languages
3. **Storage efficiency**: Encoding choices impact the size of our datasets
4. **Compatibility**: Ensuring our models work with existing text systems

When building LLMs, we typically standardize on UTF-8 encoding for all text processing, ensuring our models can handle content in any language.

---

### 2.3 Tokenization - Breaking Text into Meaningful Units

Once we have text in a consistent encoding, the next challenge is breaking it into meaningful units that our models can process. This process is called tokenization.

### Why We Need Tokenization

Consider this sentence: "The cat sat on the mat."

We could process this text in several ways:

- Character by character: ["T", "h", "e", " ", "c", "a", "t", ...]
- Word by word: ["The", "cat", "sat", "on", "the", "mat", "."]
- Subword units: ["The", "cat", "sat", "on", "the", "mat", "."]

Each approach has different trade-offs in terms of vocabulary size, meaning preservation, and computational efficiency.

### Tokenization Strategies

There are three main approaches to tokenization:

#### 1. Character-Level Tokenization

In character-level tokenization, each character becomes a token. This approach has:

**Advantages:**

- Very small vocabulary (typically under 256 tokens for ASCII, a few thousand for Unicode)
- No out-of-vocabulary words
- Works for any language

**Disadvantages:**

- Very long sequences (a tweet might be hundreds of tokens)
- Limited semantic information in each token
- Computationally expensive for long texts

#### 2. Word-Level Tokenization

Word-level tokenization splits text at word boundaries (usually spaces and punctuation). This approach has:

**Advantages:**

- More semantic meaning in each token
- Shorter sequences (that tweet might be 20-30 tokens)
- Intuitive alignment with how humans understand language

**Disadvantages:**

- Very large vocabulary (potentially millions of words)
- Cannot handle new or rare words (out-of-vocabulary problem)
- Different rules needed for different languages

Here's a simple example of word-level tokenization in Python:

```python
def simple_word_tokenize(text):
    # Split on spaces and keep punctuation separate
    words = []
    for word in text.split():
        # Handle case where punctuation is attached to word
        if word[-1] in ".,:;!?":
            words.append(word[:-1])
            words.append(word[-1])
        else:
            words.append(word)
    return words

sample_text = "Hello, world! This is a simple tokenizer."
tokens = simple_word_tokenize(sample_text)
print(tokens)
# Output: ['Hello', ',', 'world', '!', 'This', 'is', 'a', 'simple', 'tokenizer', '.']
```

#### 3. Subword Tokenization

Subword tokenization is a hybrid approach that breaks common words into single tokens but splits rare or complex words into meaningful subword pieces. This offers the best of both worlds:

**Advantages:**

- Moderate vocabulary size (typically 10,000-50,000 tokens)
- Can handle new words by combining subword pieces
- Preserves most semantic information
- Works well across languages

**Disadvantages:**

- More complex to implement
- Words can be split in unintuitive ways
- Still longer sequences than word-level tokenization

Modern LLMs primarily use subword tokenization methods like:

- **Byte-Pair Encoding (BPE)**: Used by GPT models
- **WordPiece**: Used by BERT
- **SentencePiece**: Used by T5 and many multilingual models

### Building a Vocabulary with Byte-Pair Encoding (BPE)

Let's understand how BPE works as it's one of the most common subword tokenization methods:

1. Start with a vocabulary of individual characters
2. Count the frequency of character pairs in your training data
3. Merge the most frequent pair to create a new token
4. Update the text with this new merged token
5. Repeat steps 2-4 until you reach your desired vocabulary size

Here's a simplified example:

```python
def train_bpe(text, num_merges):
    # Start with character-level tokens
    tokens = [[char for char in word] for word in text.split()]
    
    # Initialize vocabulary with unique characters
    vocab = set(char for word in tokens for char in word)
    
    for i in range(num_merges):
        # Count pairs
        pairs = {}
        for word in tokens:
            for j in range(len(word) - 1):
                pair = (word[j], word[j + 1])
                pairs[pair] = pairs.get(pair, 0) + 1
        
        if not pairs:
            break
            
        # Find most frequent pair
        best_pair = max(pairs, key=pairs.get)
        
        # Create new merged token
        new_token = best_pair[0] + best_pair[1]
        vocab.add(new_token)
        
        # Replace pairs in all words
        new_tokens = []
        for word in tokens:
            i = 0
            new_word = []
            while i < len(word):
                if i < len(word) - 1 and (word[i], word[i + 1]) == best_pair:
                    new_word.append(new_token)
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1
            new_tokens.append(new_word)
        tokens = new_tokens
        
    return vocab, tokens

# Example usage
text = "low lower lowest lowering lowered"
vocab, tokenized = train_bpe(text, 10)
print(f"Vocabulary: {vocab}")
print(f"Tokenized: {tokenized}")
```

In a real BPE implementation, you would train on millions of documents to build a robust vocabulary, then use that vocabulary to tokenize new text.

### Modern Tokenization in Practice

Modern LLMs use sophisticated tokenizers that handle:

- Multiple languages
- Special tokens (like [START], [END], [PAD])
- Whitespace and formatting
- Rare characters and emojis

Here's how you might use a pre-trained tokenizer from the Hugging Face transformers library:

```python
from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

text = "Hello, world! This is GPT-2 tokenization in action."
tokens = tokenizer.encode(text)
print(f"Token IDs: {tokens}")
print(f"Decoded tokens: {[tokenizer.decode([token]) for token in tokens]}")
```

This would output something like:

```
Token IDs: [15496, 11, 995, 0, 428, 318, 8105, 8, 10394, 290, 3155, 13]
Decoded tokens: ['Hello', ',', ' world', '!', ' This', ' is', ' GPT', '-', '2', ' token', 'ization', ' in action.']
```

Notice how "tokenization" gets split into "token" and "ization" – this is the subword nature of BPE at work!

---

### 2.4 Statistical Patterns in Language

Now that we can represent text as sequences of tokens, let's explore the statistical patterns that emerge in language. These patterns form the foundation of language modeling.

### Frequency Distributions: The Building Blocks

The most basic statistical property of language is the frequency of different tokens. Some words appear much more often than others, following what's known as Zipf's Law.

Zipf's Law states that the frequency of a word is inversely proportional to its rank in the frequency table. That means:

- The most frequent word occurs approximately twice as often as the second most frequent word
- Three times as often as the third most frequent word
- And so on

In English, words like "the," "of," and "and" typically top the frequency list, while technical or specialized terms appear much less frequently.

### N-grams: Capturing Local Patterns

While individual token frequencies tell us something about language, the real patterns emerge when we look at sequences of tokens that appear together. These sequences are called n-grams:

- **Unigrams (1-grams)**: Single tokens - "the", "cat", "sat"
- **Bigrams (2-grams)**: Pairs of adjacent tokens - "the cat", "cat sat", "sat on"
- **Trigrams (3-grams)**: Triplets of adjacent tokens - "the cat sat", "cat sat on"
- **N-grams**: Sequences of n adjacent tokens

By analyzing the frequencies of n-grams in a large corpus, we can start to capture the statistical structure of language. For example, after seeing "the cat" in English text, "sat" is more likely to follow than "elephant."

### Conditional Probability in Language

The key insight that drives language models is conditional probability: given a sequence of words, what word is likely to come next?

Mathematically, we write this as P(next_word | previous_words) – the probability of the next word given the previous words.

For example:

- P("sat" | "the cat") = probability of "sat" given we've seen "the cat"
- P("on" | "the cat sat") = probability of "on" given we've seen "the cat sat"

These conditional probabilities form the basis of statistical language modeling.

### Measuring Language Model Quality: Perplexity

How do we know if our language model is capturing these patterns effectively? The standard metric is called perplexity.

Perplexity measures how "surprised" a model is by new text. Lower perplexity means the model is less surprised, indicating it has better learned the patterns in the language.

Mathematically, perplexity is defined as:

$\text{Perplexity} = 2^{-\frac{1}{N} \sum_{i=1}^{N} \log_2 P(w_i | w_1, \ldots, w_{i-1})}$

Where:

- N is the number of tokens in the test data
- P(w_i | w_1, ..., w_{i-1}) is the probability our model assigns to word w_i given all previous words

In simpler terms, perplexity is the inverse of the average probability the model assigns to each word in the test data, raised to the power of how many words there are. A perfect model would have a perplexity of 1.

---

### 2.5 Building Your First Language Model - N-gram Models

With our understanding of tokens and language statistics, we can now build a simple but powerful language model: the n-gram model.

### How N-gram Models Work

An n-gram language model predicts the next word based solely on the previous n-1 words. The core idea is:

1. Count the occurrences of all n-grams in your training corpus
2. Use these counts to estimate conditional probabilities
3. Use these probabilities to predict the next word given previous words

For example, a trigram (3-gram) model would:

- Count how often "the cat sat" appears in the training data
- Count how often "the cat" appears followed by any word
- Calculate P("sat" | "the cat") = count("the cat sat") / count("the cat")

### Implementing a Simple Bigram Model

Let's implement a basic bigram (2-gram) language model in Python:

```python
import random
from collections import defaultdict, Counter

class BigramLanguageModel:
    def __init__(self):
        self.bigram_counts = defaultdict(Counter)
        self.context_counts = Counter()
        
    def train(self, corpus):
        # Split the corpus into tokens (here we're using simple word tokenization)
        tokens = corpus.split()
        
        # Count bigrams and contexts
        for i in range(len(tokens) - 1):
            current_word = tokens[i]
            next_word = tokens[i + 1]
            
            self.bigram_counts[current_word][next_word] += 1
            self.context_counts[current_word] += 1
    
    def probability(self, word, context):
        """Calculate P(word|context)"""
        if context not in self.context_counts:
            return 0.0
        
        return self.bigram_counts[context][word] / self.context_counts[context]
    
    def generate_next_word(self, context):
        """Generate the next word given the context word"""
        if context not in self.context_counts:
            # If we haven't seen this context, choose a random word
            return random.choice(list(self.context_counts.keys()))
        
        # Get all possible next words and their counts
        possible_words = self.bigram_counts[context]
        
        # Create weighted distribution
        words = list(possible_words.keys())
        weights = [count / self.context_counts[context] for count in possible_words.values()]
        
        return random.choices(words, weights=weights)[0]
    
    def generate_text(self, start_word, length=10):
        """Generate a sequence of text starting with start_word"""
        if start_word not in self.context_counts:
            start_word = random.choice(list(self.context_counts.keys()))
            
        text = [start_word]
        current_word = start_word
        
        for _ in range(length):
            next_word = self.generate_next_word(current_word)
            text.append(next_word)
            current_word = next_word
            
        return " ".join(text)

# Example usage
corpus = """
The cat sat on the mat. The dog chased the cat.
The cat ran up the tree. The dog barked at the cat.
The bird flew over the tree. The cat watched the bird.
"""

model = BigramLanguageModel()
model.train(corpus)

# Generate text
print(model.generate_text("The", 10))
```

This simple model demonstrates the core concepts behind language modeling:

1. Learning the statistical patterns in text
2. Using those patterns to predict what comes next
3. Generating new text by repeatedly predicting the next word

### Limitations of N-gram Models

While n-gram models are easy to understand and implement, they have several important limitations:

1. **Limited context**: They only consider the previous n-1 words, ignoring longer-range dependencies
2. **Sparsity problem**: Many valid n-grams might never appear in the training data
3. **Memory requirements**: Storing counts for all n-grams becomes prohibitively expensive as n increases
4. **No semantic understanding**: They operate purely on token sequences without understanding meaning

To address these limitations, researchers developed techniques like:

- **Smoothing**: Assigning some probability to unseen n-grams
- **Backoff**: Using shorter n-grams when longer ones aren't available
- **Interpolation**: Combining predictions from multiple n-gram models

While these techniques improved n-gram models, their fundamental limitations led to the development of neural network-based approaches, which we'll explore in Module 3.

---

### 2.6 Hands-On Project - Building an N-gram Language Model

Now let's put everything together in a more comprehensive project. We'll build a trigram language model that includes smoothing to handle unseen n-grams.

```python
import re
import random
from collections import defaultdict, Counter

class NgramLanguageModel:
    def __init__(self, n=3, smoothing=0.01):
        self.n = n  # n-gram size
        self.smoothing = smoothing  # Add-k smoothing factor
        self.ngram_counts = defaultdict(Counter)
        self.context_counts = defaultdict(int)
        self.vocabulary = set()
        
    def preprocess(self, text):
        """Clean and tokenize text"""
        # Convert to lowercase and replace newlines with spaces
        text = text.lower().replace('\n', ' ')
        # Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text)
        # Split into tokens (simple word tokenization)
        tokens = text.split()
        return tokens
    
    def train(self, corpus):
        """Train the model on a text corpus"""
        tokens = self.preprocess(corpus)
        self.vocabulary.update(tokens)
        
        # Add special start and end tokens
        tokens = ['<s>'] * (self.n - 1) + tokens + ['</s>']
        
        # Count n-grams
        for i in range(len(tokens) - self.n + 1):
            ngram = tuple(tokens[i:i + self.n])
            context = ngram[:-1]
            word = ngram[-1]
            
            self.ngram_counts[context][word] += 1
            self.context_counts[context] += 1
    
    def probability(self, word, context):
        """Calculate smoothed probability P(word|context)"""
        # Add-k smoothing
        numerator = self.ngram_counts[context][word] + self.smoothing
        denominator = self.context_counts[context] + self.smoothing * len(self.vocabulary)
        return numerator / denominator
    
    def generate_next_word(self, context):
        """Generate the next word given the context"""
        context = tuple(context)
        
        if context not in self.context_counts or self.context_counts[context] == 0:
            # Backoff to a shorter context or choose random word
            if len(context) > 1:
                return self.generate_next_word(context[1:])
            else:
                return random.choice(list(self.vocabulary))
        
        # Get all possible next words and their probabilities
        candidates = []
        weights = []
        
        for word in self.vocabulary:
            prob = self.probability(word, context)
            candidates.append(word)
            weights.append(prob)
        
        # Add the end token
        candidates.append('</s>')
        weights.append(self.probability('</s>', context))
        
        return random.choices(candidates, weights=weights)[0]
    
    def generate_text(self, max_length=30):
        """Generate a sequence of text"""
        # Start with the special start tokens
        text = ['<s>'] * (self.n - 1)
        
        # Generate words until we hit the end token or max length
        while text[-1] != '</s>' and len(text) < max_length + (self.n - 1):
            context = tuple(text[-(self.n - 1):])
            next_word = self.generate_next_word(context)
            text.append(next_word)
        
        # Remove the special tokens before returning
        return ' '.join([t for t in text if t not in ['<s>', '</s>']])
    
    def calculate_perplexity(self, test_corpus):
        """Calculate perplexity on test data"""
        tokens = self.preprocess(test_corpus)
        tokens = ['<s>'] * (self.n - 1) + tokens + ['</s>']
        
        log_prob_sum = 0
        count = 0
        
        for i in range(len(tokens) - self.n + 1):
            ngram = tuple(tokens[i:i + self.n])
            context = ngram[:-1]
            word = ngram[-1]
            prob = self.probability(word, context)
            log_prob_sum += -1 * (1 / len(tokens)) * (1 if prob > 0 else 0) * (
                0 if prob == 0 else (
                    1 / (len(tokens) - self.n + 1)) * (
                        0 if prob == 0 else (
                            2 if prob == 1 else 2**(1 / (len(tokens) - self.n + 1)) * 2**log2(prob))))
            count += 1
            
        perplexity = 2 ** log_prob_sum
        return perplexity

# Example usage
training_corpus = """
The quick brown fox jumps over the lazy dog. A fox is a wild animal.
Dogs are domestic animals. The lazy dog sleeps all day.
The brown fox is quick and clever. Dogs chase cats. Cats chase mice.
"""

test_corpus = "The quick fox jumps. Dogs sleep all day."

model = NgramLanguageModel(n=3, smoothing=0.1)
model.train(training_corpus)

# Generate some text
print("Generated text:")
for _ in range(3):
    print(model.generate_text())

# Calculate perplexity
perplexity = model.calculate_perplexity(test_corpus)
print(f"Perplexity on test corpus: {perplexity:.2f}")
```

This more advanced model includes several important features:

- Proper text preprocessing
- Add-k smoothing to handle unseen n-grams
- Context backoff for unseen contexts
- Special tokens for sequence starts and ends
- Perplexity calculation for model evaluation

---

### 2.7 Beyond N-grams - The Path Forward

While our n-gram model captures basic language patterns, it has fundamental limitations. Modern language models overcome these limitations through:

1. **Dense vector representations**: Instead of sparse n-gram counts, modern models use dense vectors (embeddings) to represent words and contexts
2. **Neural architectures**: Neural networks can learn complex patterns that go far beyond simple n-gram statistics
3. **Long-range dependencies**: Attention mechanisms help models capture relationships between words far apart in a sequence
4. **Transfer learning**: Pre-training on vast text datasets before fine-tuning for specific tasks

In Module 3, we'll dive into neural network approaches to language modeling, starting with word embeddings and recurrent neural networks. These techniques lay the groundwork for the transformer revolution that powers modern LLMs.

---

### 2.8 Key Takeaways from Module 2

Let's summarize what we've learned in this module:

1. Computers represent text through character encodings like UTF-8
2. Tokenization converts text into discrete units that models can process
3. Subword tokenization methods like BPE offer the best balance of vocabulary size and handling unknown words
4. Language follows statistical patterns that can be captured through n-gram analysis
5. N-gram models predict the next word based on previous words
6. Perplexity measures how well a language model captures these patterns
7. While n-gram models are simple and interpretable, they have significant limitations that neural approaches address

In our next module, we'll explore how neural networks revolutionized language modeling by overcoming many of the limitations of traditional statistical approaches.

---

### 2.9 Practice Exercises

To reinforce your learning from this module, try these exercises:

1. Implement a character-level n-gram model and compare its generated text to our word-level model
2. Experiment with different values of n and smoothing to see how they affect text generation quality
3. Calculate the perplexity of your model on different test datasets
4. Implement a simple BPE tokenizer from scratch and use it to tokenize some example text
5. Analyze the frequency distribution of words in a large text corpus and verify Zipf's Law

These exercises will help solidify your understanding of the foundational concepts before we move on to neural approaches in Module 3.

---

### 2.10 Preview of Module 3 - Neural Networks for Language

In our next module, we'll explore how neural networks transformed language modeling. We'll cover:

- Word embeddings that capture semantic relationships between words
- Recurrent Neural Networks (RNNs) for sequence modeling
- Long Short-Term Memory (LSTM) networks that handle long-range dependencies
- Training neural language models with backpropagation
- Building a character-level RNN language model

These neural approaches address many limitations of n-gram models and set the stage for the transformer revolution that powers modern LLMs.

Would you like me to explain any part of this module in more detail before we move on to Module 3?

---

