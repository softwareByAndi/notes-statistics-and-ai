# Programming LLMs From Scratch - A Comprehensive Crash Course

Welcome to this comprehensive crash course on programming Large Language Models (LLMs) from scratch. This course is designed with a unique approach - we'll start by understanding what we're ultimately building, then work backward to explore all the foundational elements needed to get there. This gives you the "why" before the "how," making your learning journey more purposeful and connected.

Large Language Models represent one of the most significant technological breakthroughs of our time. These systems can understand language, generate text, translate content, write code, and even reason about complex problems. But how do they actually work? How can you build one yourself? This course will demystify the entire process, breaking down complex concepts into understandable pieces while maintaining the technical depth needed for true mastery.

- [[course structure]]
- [[learning approach]]

Each module builds upon the previous ones, creating a comprehensive understanding of the entire LLM development process from text representation to cutting-edge applications.

- [[_Module 0 - Prerequisites and Preparation]]
- [[_Module 1 - The Big Picture - What Are We Building]]
- [[_Module 2 - Language and Text - The Foundation]]
- [[_Module 3 - Neural Networks for Language]]
- [[_Module 4 - The Transformer Revolution]]
- [[_Module 5 - Scaling Up - From Models to LLMs]]
- [[_Module 6 - Transfer Learning and Fine-tuning]]

## future modules - not yet developed


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

## learning approach

Throughout this course, I'll follow these principles:

- **Simple Language for Complex Ideas**: Technical concepts explained in plain language
- **Progressive Complexity**: Starting with the basics before diving deeper
- **Practical Examples**: Code samples and projects to reinforce learning
- **Visual Explanations**: Diagrams and visualizations to clarify abstract concepts
- **Hands-On Projects**: Milestone projects for each major section to build your portfolio
- **Real-World Applications**: Connecting theory to practical implementation

Now, let's begin with our course map and prerequisites before diving into our first module.

---

## Module 0 - Prerequisites and Preparation

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

#### Development Environment Setup

Let's set up your working environment:

1. **Install Python**: If you haven't already, download and install Python 3.8 or newer
2. **Create a virtual environment**: This keeps your project dependencies separate
``` bash
python -m venv llm-coursesource llm-course/bin/activate  # On Windows: llm-course\Scripts\activate
```
3. **Install basic libraries**:
``` bash
pip install numpy pandas matplotlib jupyter torch transformers
```
4. **Create a project folder**:
``` bash
mkdir llm-from-scratchcd llm-from-scratch
```
5. **Start Jupyter**:
``` bash
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
- **Random variables**: Values determined by chance
- **Probability distributions**: How likely different outcomes are
- **Conditional probability**: The likelihood of an event given another event occurred

Language models fundamentally work with probabilities - "what word is most likely to come next?"

#### Calculus Foundations
- **Derivatives**: Rate of change (how quickly a function's output changes)
- **Gradients**: Direction of steepest increase (critical for training neural networks)

Don't worry if these concepts aren't completely familiar - we'll explain them in context as needed.

---

## Module 1 - The Big Picture - What Are We Building

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

## Module 2 - Language and Text - The Foundation

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

#### From Human Language to Machine Numbers

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

#### ASCII: The Original Digital Alphabet

The American Standard Code for Information Interchange (ASCII) was one of the first widespread character encodings. It uses 7 bits to represent 128 different characters:

- 0-31: Control characters (non-printable)
- 32-126: Printable characters (letters, numbers, symbols)
- 127: Delete character

For example, the letter 'A' is represented as the decimal number 65, which in binary is `1000001`.

While ASCII worked well for English text, it couldn't represent the vast diversity of characters used in other languages. This limitation led to the development of more comprehensive encodings.

#### Unicode and UTF-8: A Global Digital Alphabet

Unicode was created to solve the limitations of ASCII by assigning a unique number (code point) to virtually every character used in all the world's writing systems. The most common implementation of Unicode is UTF-8, which uses a variable number of bytes to represent different characters:

- ASCII characters (English letters, numbers) use just 1 byte
- Most European and Middle Eastern scripts use 2 bytes
- East Asian scripts and emojis typically use 3 or 4 bytes

For example:

- The English letter 'A' is still 65 (1 byte): `01000001`
- The Japanese hiragana 'あ' is 12354 (3 bytes): `11100011 10000001 10000010`
- The emoji '😊' is 128522 (4 bytes): `11110000 10011111 10011000 10001010`

UTF-8 has become the dominant encoding for text on the internet because it efficiently handles multiple languages while maintaining backward compatibility with ASCII.

#### Why Character Encodings Matter for LLMs

Understanding character encodings is important for several reasons:

1. **Data preprocessing**: We need to ensure our training data uses consistent encoding
2. **Multilingual capabilities**: Different encodings affect how models handle various languages
3. **Storage efficiency**: Encoding choices impact the size of our datasets
4. **Compatibility**: Ensuring our models work with existing text systems

When building LLMs, we typically standardize on UTF-8 encoding for all text processing, ensuring our models can handle content in any language.

---

### 2.3 Tokenization - Breaking Text into Meaningful Units

Once we have text in a consistent encoding, the next challenge is breaking it into meaningful units that our models can process. This process is called tokenization.

#### Why We Need Tokenization

Consider this sentence: "The cat sat on the mat."

We could process this text in several ways:

- Character by character: ["T", "h", "e", " ", "c", "a", "t", ...]
- Word by word: ["The", "cat", "sat", "on", "the", "mat", "."]
- Subword units: ["The", "cat", "sat", "on", "the", "mat", "."]

Each approach has different trade-offs in terms of vocabulary size, meaning preservation, and computational efficiency.

#### Tokenization Strategies

There are three main approaches to tokenization:

##### 1. Character-Level Tokenization

In character-level tokenization, each character becomes a token. This approach has:

**Advantages:**

- Very small vocabulary (typically under 256 tokens for ASCII, a few thousand for Unicode)
- No out-of-vocabulary words
- Works for any language

**Disadvantages:**

- Very long sequences (a tweet might be hundreds of tokens)
- Limited semantic information in each token
- Computationally expensive for long texts

##### 2. Word-Level Tokenization

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

##### 3. Subword Tokenization

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

#### Building a Vocabulary with Byte-Pair Encoding (BPE)

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

#### Modern Tokenization in Practice

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

#### Frequency Distributions: The Building Blocks

The most basic statistical property of language is the frequency of different tokens. Some words appear much more often than others, following what's known as Zipf's Law.

Zipf's Law states that the frequency of a word is inversely proportional to its rank in the frequency table. That means:

- The most frequent word occurs approximately twice as often as the second most frequent word
- Three times as often as the third most frequent word
- And so on

In English, words like "the," "of," and "and" typically top the frequency list, while technical or specialized terms appear much less frequently.

#### N-grams: Capturing Local Patterns

While individual token frequencies tell us something about language, the real patterns emerge when we look at sequences of tokens that appear together. These sequences are called n-grams:

- **Unigrams (1-grams)**: Single tokens - "the", "cat", "sat"
- **Bigrams (2-grams)**: Pairs of adjacent tokens - "the cat", "cat sat", "sat on"
- **Trigrams (3-grams)**: Triplets of adjacent tokens - "the cat sat", "cat sat on"
- **N-grams**: Sequences of n adjacent tokens

By analyzing the frequencies of n-grams in a large corpus, we can start to capture the statistical structure of language. For example, after seeing "the cat" in English text, "sat" is more likely to follow than "elephant."

#### Conditional Probability in Language

The key insight that drives language models is conditional probability: given a sequence of words, what word is likely to come next?

Mathematically, we write this as P(next_word | previous_words) – the probability of the next word given the previous words.

For example:

- P("sat" | "the cat") = probability of "sat" given we've seen "the cat"
- P("on" | "the cat sat") = probability of "on" given we've seen "the cat sat"

These conditional probabilities form the basis of statistical language modeling.

#### Measuring Language Model Quality: Perplexity

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

#### How N-gram Models Work

An n-gram language model predicts the next word based solely on the previous n-1 words. The core idea is:

1. Count the occurrences of all n-grams in your training corpus
2. Use these counts to estimate conditional probabilities
3. Use these probabilities to predict the next word given previous words

For example, a trigram (3-gram) model would:

- Count how often "the cat sat" appears in the training data
- Count how often "the cat" appears followed by any word
- Calculate P("sat" | "the cat") = count("the cat sat") / count("the cat")

#### Implementing a Simple Bigram Model

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

#### Limitations of N-gram Models

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

---

## Module 3 - Neural Networks for Language

Welcome to Module 3 of our LLM crash course! In this module, we'll explore how neural networks revolutionized language modeling. While our previous n-gram models could capture local patterns in text, they had significant limitations that neural approaches address.

- [[3.1 From N-grams to Neural Networks]]
- [[3.2 Word Embeddings - Representing Words as Vectors]]
- [[3.3 Feed-Forward Neural Networks for Language]]
- [[3.4 Recurrent Neural Networks - Processing Sequences]]
- [[3.5 Advanced Recurrent Architectures]]
- [[3.6 Building a Character-Level Language Model]]
- [[3.7 Complete Implementation - Training and Using a Character-Level LSTM]]
- [[3.8 Evaluating Neural Language Models]]
- [[3.9 Limitations of RNN-Based Models]]
- [[3.10 Key Takeaways from Module 3]]
- [[3.11 Practice Exercises]]
- [[3.12 Preview of Module 4 - The Transformer Revolution]]

---

### 3.1 From N-grams to Neural Networks

#### The Limitations of Statistical Models

Let's briefly recap why we need to move beyond n-gram models:

1. **Limited context**: N-gram models only look at a fixed number of previous words
2. **Sparsity problem**: Many valid word combinations simply don't appear in our training data
3. **No generalization**: N-grams can't understand that "dog" and "puppy" might be used similarly
4. **Exponential growth**: The number of possible sequences grows exponentially with length

Neural networks offer solutions to these problems by learning distributed representations of words and capturing more complex patterns in language.

#### The Neural Approach to Language

Neural language models differ from n-grams in two fundamental ways:

1. **Words as vectors**: Instead of treating words as discrete symbols, neural models represent words as points in a continuous vector space
2. **Learned patterns**: Rather than counting occurrences, neural networks learn to recognize patterns through training

These differences allow neural models to generalize better, handle unseen word combinations, and capture long-range dependencies in text.

---

### 3.2 Word Embeddings - Representing Words as Vectors

#### From Symbols to Vectors

The first breakthrough in neural language models was the concept of word embeddings - representing words as dense vectors in a continuous space.

##### One-Hot Encoding: The Naive Approach

We could represent words using one-hot encoding, where each word corresponds to a vector with a single 1 and the rest 0s:

- "cat" → [1, 0, 0, 0, 0, ...]
- "dog" → [0, 1, 0, 0, 0, ...]
- "mouse" → [0, 0, 1, 0, 0, ...]

But this approach has major drawbacks:

- Vectors are extremely sparse (mostly zeros)
- All words are equally different from each other (no notion of similarity)
- Dimensions grow with vocabulary size (inefficient)

##### Dense Embeddings: Words in Meaning Space

Word embeddings solve these problems by representing words as dense vectors (typically 50-300 dimensions) where similar words have similar vectors.

For example, in a good embedding space:

- "cat" → [0.2, -0.4, 0.7, -0.2, ...]
- "dog" → [0.1, -0.3, 0.8, -0.1, ...]
- "mouse" → [0.3, -0.2, 0.5, -0.4, ...]

In this space, "cat" and "dog" might be closer to each other than either is to "computer," reflecting their semantic similarity as animals.

#### Learning Word Embeddings

How do we create these vector representations? Through training, of course! There are several approaches:

##### Word2Vec: Learning from Context

Word2Vec, introduced by Mikolov et al. in 2013, revolutionized word embeddings with two approaches:

1. **Skip-gram**: Predict surrounding words given a target word
2. **Continuous Bag of Words (CBOW)**: Predict a target word given its surrounding words

Both approaches use a simple neural network trained on a large corpus. The key insight is that words appearing in similar contexts should have similar meanings.

Let's look at the Skip-gram model more closely:

1. Start with randomly initialized embeddings for each word
2. For each word in your text, predict the words that appear nearby
3. Update the embeddings to improve these predictions
4. After training, the embedding vectors capture semantic relationships

Here's a simplified implementation of the Skip-gram training process:

```python
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class SkipGramModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(SkipGramModel, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.output_layer = nn.Linear(embedding_dim, vocab_size)
        
    def forward(self, inputs):
        embeds = self.embeddings(inputs)
        output = self.output_layer(embeds)
        return output

# Example usage
vocab_size = 10000
embedding_dim = 100
model = SkipGramModel(vocab_size, embedding_dim)

# Training setup
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# For each word in context window
for target_word, context_word in training_pairs:
    # Convert words to indices
    target_idx = word_to_idx[target_word]
    context_idx = word_to_idx[context_word]
    
    # Forward pass
    inputs = torch.tensor([target_idx])
    outputs = model(inputs)
    
    # Calculate loss
    labels = torch.tensor([context_idx])
    loss = criterion(outputs, labels)
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# After training, the embedding matrix contains our word vectors
word_embeddings = model.embeddings.weight.data
```

##### GloVe: Global Vectors for Word Representation

Another popular approach is GloVe (Pennington et al., 2014), which combines global matrix factorization with local context window methods.

GloVe works by:

1. Creating a word co-occurrence matrix from the corpus
2. Factorizing this matrix to generate embeddings
3. Weighting frequent co-occurrences more heavily

The result is embeddings that capture both global statistics and local context.

#### Fascinating Properties of Word Embeddings

Perhaps the most exciting aspect of word embeddings is that they capture meaningful semantic relationships as vector arithmetic. For example:

- king - man + woman ≈ queen
- paris - france + italy ≈ rome
- walking - walk + run ≈ running

These vector operations reveal that the embeddings have captured complex linguistic relationships like gender, country-capital pairs, and verb tenses.

#### Visualizing Word Embeddings

While embeddings typically have 100+ dimensions, we can use dimensionality reduction techniques like t-SNE or PCA to visualize them in 2D or 3D.

Here's how we might visualize a subset of word embeddings:

```python
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Get embeddings for some common words
common_words = ['king', 'queen', 'man', 'woman', 'dog', 'cat', 'mouse', 'computer', 'phone', 'car']
word_vectors = [word_embeddings[word_to_idx[word]] for word in common_words]

# Reduce to 2 dimensions with t-SNE
tsne = TSNE(n_components=2, random_state=42)
embeddings_2d = tsne.fit_transform(word_vectors)

# Plot the words
plt.figure(figsize=(10, 8))
for i, word in enumerate(common_words):
    plt.scatter(embeddings_2d[i, 0], embeddings_2d[i, 1])
    plt.annotate(word, (embeddings_2d[i, 0], embeddings_2d[i, 1]))
plt.title("Word Embeddings Visualization")
plt.show()
```

In these visualizations, we'd typically see related words clustered together - animals near other animals, objects near similar objects, etc.

---

### 3.3 Feed-Forward Neural Networks for Language

Before diving into sequence models, let's understand how a basic neural network can be used for language modeling.

#### A Simple Neural Language Model

A feed-forward neural language model works as follows:

1. Convert previous words to embeddings
2. Concatenate these embeddings into a single vector
3. Pass this vector through one or more dense layers
4. Output a probability distribution over the vocabulary for the next word

Here's a simplified implementation:

```python
class FFNLanguageModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, context_size, hidden_dim):
        super(FFNLanguageModel, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.linear1 = nn.Linear(context_size * embedding_dim, hidden_dim)
        self.linear2 = nn.Linear(hidden_dim, vocab_size)
        self.activation = nn.ReLU()
        
    def forward(self, inputs):
        # inputs shape: [batch_size, context_size]
        embeds = self.embeddings(inputs)  # [batch_size, context_size, embedding_dim]
        embeds = embeds.view(embeds.shape[0], -1)  # Flatten: [batch_size, context_size * embedding_dim]
        hidden = self.activation(self.linear1(embeds))
        output = self.linear2(hidden)  # [batch_size, vocab_size]
        return output
```

#### Limitations of Feed-Forward Models

While this approach works better than n-grams, it still has limitations:

1. **Fixed context window**: We can only consider a fixed number of previous words
2. **No parameter sharing**: Different positions in the context window have completely different weights
3. **No notion of word order**: Beyond the fixed window size

These limitations led to the development of recurrent neural networks, which handle variable-length sequences more naturally.

---

### 3.4 Recurrent Neural Networks - Processing Sequences

#### The Sequential Nature of Language

Language is inherently sequential - words occur one after another, and their meaning depends on what came before. We need a model architecture that respects this sequential nature.

#### Introducing Recurrent Neural Networks (RNNs)

Recurrent Neural Networks (RNNs) process sequences by maintaining an internal state (or "memory") that gets updated at each time step.

The key idea is simple but powerful: at each step, the RNN takes two inputs:

1. The current input token (e.g., the current word)
2. Its own internal state from the previous step

It then produces two outputs:

1. A prediction (e.g., probabilities for the next word)
2. An updated internal state to pass to the next step

This recurrent connection allows information to flow from earlier words to later predictions, regardless of distance.

#### The Mathematics of RNNs

Mathematically, an RNN cell performs this computation:

$h_t = \tanh(W_{xh} \cdot x_t + W_{hh} \cdot h_{t-1} + b_h)$ $y_t = W_{hy} \cdot h_t + b_y$

Where:

- $x_t$ is the input at time step $t$ (typically a word embedding)
- $h_t$ is the hidden state at time step $t$
- $y_t$ is the output at time step $t$
- $W_{xh}$, $W_{hh}$, and $W_{hy}$ are weight matrices
- $b_h$ and $b_y$ are bias vectors
- $\tanh$ is the hyperbolic tangent activation function

The crucial part is that the same weights ($W_{xh}$, $W_{hh}$, $W_{hy}$) are used at every time step - the RNN learns a general way to update its state regardless of position in the sequence.

#### Implementing a Simple RNN

Here's how we might implement a simple RNN language model in PyTorch:

```python
class SimpleRNN(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super(SimpleRNN, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)
        
    def forward(self, inputs, hidden=None):
        # inputs shape: [batch_size, seq_length]
        embeds = self.embeddings(inputs)  # [batch_size, seq_length, embedding_dim]
        
        # If no hidden state is provided, initialize with zeros
        if hidden is None:
            batch_size = inputs.size(0)
            hidden = torch.zeros(1, batch_size, self.rnn.hidden_size, device=inputs.device)
            
        # Process the sequence through the RNN
        output, hidden = self.rnn(embeds, hidden)
        # output shape: [batch_size, seq_length, hidden_dim]
        
        # Project to vocabulary size
        output = self.fc(output)  # [batch_size, seq_length, vocab_size]
        
        return output, hidden
```

#### Training RNNs: Backpropagation Through Time

Training RNNs involves a special form of backpropagation called Backpropagation Through Time (BPTT). The core idea is to unroll the recurrent connections over time steps and treat the network as a very deep feed-forward network with shared weights.

The process works like this:

1. Process the entire sequence forward to get predictions at each time step
2. Compute the loss at each time step (usually cross-entropy against the actual next word)
3. Sum these losses to get the total sequence loss
4. Backpropagate the gradient through the unrolled network
5. Update the weights

For efficiency, we usually process sequences in chunks rather than complete documents, a technique called truncated BPTT.

---

### 3.5 Advanced Recurrent Architectures

#### The Vanishing Gradient Problem

While simple RNNs are powerful in theory, they suffer from a serious practical limitation: the vanishing gradient problem.

As gradients flow backward through many time steps, they tend to either vanish (approach zero) or explode (become extremely large). This makes it difficult for simple RNNs to learn long-range dependencies - they struggle to connect words that are far apart in the sequence.

#### Long Short-Term Memory (LSTM) Networks

To address the vanishing gradient problem, Hochreiter and Schmidhuber introduced Long Short-Term Memory (LSTM) networks in 1997. LSTMs use gating mechanisms to control information flow, allowing them to maintain information over many time steps.

An LSTM cell has three gates:

1. **Forget gate**: Decides what information to discard from the cell state
2. **Input gate**: Decides what new information to store in the cell state
3. **Output gate**: Decides what parts of the cell state to output

These gates are controlled by sigmoid functions that output values between 0 and 1, effectively functioning as "valves" that can be fully open, fully closed, or partially open.

Mathematically:

$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$ (forget gate) $i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$ (input gate) $\tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)$ (candidate cell state) $C_t = f_t * C_{t-1} + i_t * \tilde{C}_t$ (new cell state) $o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$ (output gate) $h_t = o_t * \tanh(C_t)$ (hidden state)

Where:

- $\sigma$ is the sigmoid function
- $*$ represents element-wise multiplication
- $[h_{t-1}, x_t]$ represents the concatenation of the previous hidden state and current input

This complex mechanism allows LSTMs to learn which information is important to keep and which can be discarded, enabling them to maintain relevant context over many time steps.

#### Gated Recurrent Units (GRUs)

Gated Recurrent Units (GRUs) are a simplified version of LSTMs introduced by Cho et al. in 2014. They combine the forget and input gates into a single "update gate" and merge the cell state and hidden state.

GRUs are computationally more efficient than LSTMs while achieving similar performance on many tasks. The mathematics behind GRUs is:

$z_t = \sigma(W_z \cdot [h_{t-1}, x_t] + b_z)$ (update gate) $r_t = \sigma(W_r \cdot [h_{t-1}, x_t] + b_r)$ (reset gate) $\tilde{h}_t = \tanh(W \cdot [r_t * h_{t-1}, x_t] + b)$ (candidate hidden state) $h_t = (1 - z_t) * h_{t-1} + z_t * \tilde{h}_t$ (new hidden state)

#### Bidirectional RNNs

Another powerful extension is the bidirectional RNN, which processes the sequence in both directions:

1. A forward RNN processes the sequence from start to end
2. A backward RNN processes it from end to start
3. The outputs of both are combined (usually concatenated)

This allows the model to capture context from both past and future words, which is particularly useful for tasks like machine translation where the entire source sentence is available.

```python
class BidirectionalLSTM(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super(BidirectionalLSTM, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_dim * 2, vocab_size)  # *2 because bidirectional
        
    def forward(self, inputs):
        embeds = self.embeddings(inputs)
        output, (hidden, cell) = self.lstm(embeds)
        output = self.fc(output)
        return output
```

---

### 3.6 Building a Character-Level Language Model

Now let's put everything together and build a character-level language model using LSTMs. Character-level models have some advantages over word-level models:

- No out-of-vocabulary words (the vocabulary is just the set of characters)
- Smaller vocabulary size (typically <100 tokens vs. tens of thousands)
- Can learn to generate novel words and handle misspellings

#### Design Decisions

For our character-level model, we'll make these choices:

1. Use an LSTM architecture for long-range dependencies
2. One-hot encode characters (since the vocabulary is small)
3. Generate one character at a time, conditioned on previous characters
4. Use temperature-based sampling for text generation

#### Model Architecture

```python
class CharLSTM(nn.Module):
    def __init__(self, n_chars, hidden_dim, n_layers=2, dropout=0.2):
        super(CharLSTM, self).__init__()
        self.n_chars = n_chars  # Vocabulary size (number of unique characters)
        self.hidden_dim = hidden_dim
        self.n_layers = n_layers
        
        # Character embeddings
        self.embeddings = nn.Embedding(n_chars, hidden_dim)
        
        # LSTM layers
        self.lstm = nn.LSTM(
            input_size=hidden_dim,
            hidden_size=hidden_dim,
            num_layers=n_layers,
            dropout=dropout if n_layers > 1 else 0,
            batch_first=True
        )
        
        # Output layer
        self.fc = nn.Linear(hidden_dim, n_chars)
        
    def forward(self, inputs, hidden=None):
        # Convert character indices to embeddings
        embeds = self.embeddings(inputs)
        
        # Initialize hidden state if not provided
        if hidden is None:
            batch_size = inputs.size(0)
            hidden = self._init_hidden(batch_size)
            
        # Run through LSTM
        lstm_out, hidden = self.lstm(embeds, hidden)
        
        # Project to character space
        output = self.fc(lstm_out)
        
        return output, hidden
    
    def _init_hidden(self, batch_size):
        # Initialize hidden state with zeros
        h0 = torch.zeros(self.n_layers, batch_size, self.hidden_dim, device=self._get_device())
        c0 = torch.zeros(self.n_layers, batch_size, self.hidden_dim, device=self._get_device())
        return (h0, c0)
    
    def _get_device(self):
        return next(self.parameters()).device
```

#### Training the Model

Let's train our character-level model on a text dataset:

```python
def train_char_lstm(model, data, epochs=10, batch_size=64, seq_length=100, lr=0.001):
    model.train()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    device = next(model.parameters()).device
    
    # Prepare data
    chars = sorted(list(set(data)))
    char_to_idx = {ch: i for i, ch in enumerate(chars)}
    idx_to_char = {i: ch for i, ch in enumerate(chars)}
    data_indices = [char_to_idx[ch] for ch in data]
    
    # Training loop
    for epoch in range(epochs):
        hidden = None
        total_loss = 0
        
        # Process data in batches
        for i in range(0, len(data_indices) - seq_length - 1, batch_size * seq_length):
            # Prepare batch
            if i + batch_size * seq_length + 1 >= len(data_indices):
                continue
                
            inputs_batch = []
            targets_batch = []
            
            for j in range(batch_size):
                if i + j * seq_length + seq_length + 1 <= len(data_indices):
                    inputs = data_indices[i + j * seq_length:i + j * seq_length + seq_length]
                    targets = data_indices[i + j * seq_length + 1:i + j * seq_length + seq_length + 1]
                    inputs_batch.append(inputs)
                    targets_batch.append(targets)
            
            # Skip if not enough data for a full batch
            if len(inputs_batch) < batch_size:
                continue
                
            # Convert to tensors
            inputs_tensor = torch.tensor(inputs_batch).to(device)
            targets_tensor = torch.tensor(targets_batch).to(device)
            
            # Forward pass
            outputs, hidden = model(inputs_tensor, hidden)
            
            # Detach hidden state (for truncated BPTT)
            hidden = tuple(h.detach() for h in hidden)
            
            # Reshape for loss calculation
            outputs = outputs.view(-1, model.n_chars)
            targets = targets_tensor.view(-1)
            
            # Calculate loss
            loss = criterion(outputs, targets)
            total_loss += loss.item()
            
            # Backward pass and optimization
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 5)  # Gradient clipping
            optimizer.step()
            
        # Print progress
        print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss:.4f}")
        
        # Generate sample text
        if (epoch + 1) % 5 == 0:
            sample = generate_text(model, char_to_idx, idx_to_char, seed="The ", length=200)
            print(f"Sample: {sample}")
```

#### Generating Text

Now let's generate text with our trained model:

```python
def generate_text(model, char_to_idx, idx_to_char, seed, length=1000, temperature=0.8):
    model.eval()
    device = next(model.parameters()).device
    
    # Convert seed to indices
    chars = [char_to_idx[ch] for ch in seed]
    
    # Initialize hidden state
    hidden = None
    
    # Generate one character at a time
    with torch.no_grad():
        for _ in range(length):
            # Convert current sequence to tensor
            input_tensor = torch.tensor([chars]).to(device)
            
            # Forward pass
            output, hidden = model(input_tensor, hidden)
            
            # Get predictions for the next character
            output = output[:, -1, :]  # Take the last time step
            
            # Apply temperature
            output = output / temperature
            
            # Convert to probabilities
            probabilities = F.softmax(output, dim=1)
            
            # Sample from the distribution
            next_char_idx = torch.multinomial(probabilities, 1).item()
            
            # Add to generated sequence
            chars.append(next_char_idx)
    
    # Convert indices back to characters
    generated_text = seed + ''.join([idx_to_char[idx] for idx in chars[len(seed):]])
    return generated_text
```

#### Temperature Sampling

Notice the `temperature` parameter in our text generation function. This controls the randomness of the generated text:

- Lower temperature (e.g., 0.2) makes the model more conservative, picking the most likely characters
- Higher temperature (e.g., 1.5) makes the model more creative but potentially less coherent
- A temperature of 1.0 uses the exact probabilities from the model

This allows us to control the trade-off between coherence and creativity in the generated text.

---

### 3.7 Complete Implementation - Training and Using a Character-Level LSTM

Let's put everything together into a complete implementation that demonstrates training and using our character-level LSTM model:

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
import time

# Character-level LSTM model
class CharLSTM(nn.Module):
    def __init__(self, n_chars, hidden_dim=256, n_layers=2, dropout=0.2):
        super(CharLSTM, self).__init__()
        self.n_chars = n_chars
        self.hidden_dim = hidden_dim
        self.n_layers = n_layers
        
        self.embeddings = nn.Embedding(n_chars, hidden_dim)
        self.lstm = nn.LSTM(
            input_size=hidden_dim,
            hidden_size=hidden_dim,
            num_layers=n_layers,
            dropout=dropout if n_layers > 1 else 0,
            batch_first=True
        )
        self.fc = nn.Linear(hidden_dim, n_chars)
    
    def forward(self, inputs, hidden=None):
        embeds = self.embeddings(inputs)
        
        if hidden is None:
            batch_size = inputs.size(0)
            device = inputs.device
            h0 = torch.zeros(self.n_layers, batch_size, self.hidden_dim, device=device)
            c0 = torch.zeros(self.n_layers, batch_size, self.hidden_dim, device=device)
            hidden = (h0, c0)
            
        lstm_out, hidden = self.lstm(embeds, hidden)
        output = self.fc(lstm_out)
        
        return output, hidden

# Function to load and preprocess data
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    
    # Create character mappings
    chars = sorted(list(set(data)))
    char_to_idx = {ch: i for i, ch in enumerate(chars)}
    idx_to_char = {i: ch for i, ch in enumerate(chars)}
    
    print(f"Data has {len(data)} characters, {len(chars)} unique characters")
    return data, chars, char_to_idx, idx_to_char

# Function to create training batches
def get_batches(data_indices, batch_size, seq_length):
    n_batches = (len(data_indices) - 1) // (batch_size * seq_length)
    
    # Trim data to fit batches
    data_indices = data_indices[:n_batches * batch_size * seq_length + 1]
    
    inputs = []
    targets = []
    
    for i in range(0, len(data_indices) - seq_length, seq_length):
        inputs.append(data_indices[i:i + seq_length])
        targets.append(data_indices[i + 1:i + seq_length + 1])
    
    # Reshape into batch_size rows
    inputs = np.array(inputs).reshape(batch_size, -1)
    targets = np.array(targets).reshape(batch_size, -1)
    
    # Create batches
    for i in range(0, inputs.shape[1], seq_length):
        if i + seq_length <= inputs.shape[1]:
            yield inputs[:, i:i + seq_length], targets[:, i:i + seq_length]

# Training function
def train(model, data, chars, char_to_idx, idx_to_char, epochs=10, batch_size=64, seq_length=100, lr=0.001):
    model.train()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    device = next(model.parameters()).device
    
    # Convert data to indices
    data_indices = [char_to_idx[ch] for ch in data]
    
    # Training stats
    losses = []
    
    # Training loop
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        hidden = None
        start_time = time.time()
        
        for inputs, targets in get_batches(data_indices, batch_size, seq_length):
            # Convert to tensors
            inputs = torch.tensor(inputs, dtype=torch.long).to(device)
            targets = torch.tensor(targets, dtype=torch.long).to(device)
            
            # Reset gradients
            optimizer.zero_grad()
            
            # Forward pass
            outputs, hidden = model(inputs, hidden)
            
            # Detach hidden state
            hidden = tuple(h.detach() for h in hidden)
            
            # Reshape for loss calculation
            outputs = outputs.reshape(-1, model.n_chars)
            targets = targets.reshape(-1)
            
            # Calculate loss
            loss = criterion(outputs, targets)
            total_loss += loss.item() * inputs.size(0)
            
            # Backward pass
            loss.backward()
            
            # Clip gradients to prevent exploding gradients
            torch.nn.utils.clip_grad_norm_(model.parameters(), 5)
            
            # Update weights
            optimizer.step()
        
        # Calculate average loss
        avg_loss = total_loss / (len(data_indices) // seq_length)
        losses.append(avg_loss)
        
        # Calculate time per epoch
        elapsed_time = time.time() - start_time
        
        print(f"Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.4f}, Time: {elapsed_time:.2f}s")
        
        # Generate sample text
        if (epoch + 1) % 5 == 0 or epoch == epochs - 1:
            model.eval()
            sample = generate_text(model, char_to_idx, idx_to_char, seed="The ", length=200)
            print(f"\nSample:\n{sample}\n")
    
    # Plot training loss
    plt.figure(figsize=(10, 6))
    plt.plot(losses)
    plt.title("Training Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.show()
    
    return losses

# Text generation function
def generate_text(model, char_to_idx, idx_to_char, seed="The ", length=1000, temperature=0.7):
    model.eval()
    device = next(model.parameters()).device
    
    # Convert seed to indices
    chars = [char_to_idx.get(ch, 0) for ch in seed]  # Default to first char if not found
    
    # Generate one character at a time
    with torch.no_grad():
        hidden = None
        
        for _ in range(length):
            # Convert to tensor
            x = torch.tensor([chars], dtype=torch.long).to(device)
            
            # Forward pass
            out, hidden = model(x, hidden)
            
            # Get prediction for next character
            out = out[:, -1, :] / temperature
            
            # Convert to probabilities
            probs = F.softmax(out, dim=1).squeeze()
            
            # Sample from distribution
            char_idx = torch.multinomial(probs, 1).item()
            
            # Add to sequence
            chars.append(char_idx)
    
    # Convert to text
    text = ''.join([idx_to_char[idx] for idx in chars])
    return text

# Main function to run the model
def main():
    # Load data (assuming you have a text file)
    data, chars, char_to_idx, idx_to_char = load_data("your_text_file.txt")
    
    # Initialize model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = CharLSTM(len(chars), hidden_dim=512, n_layers=3).to(device)
    print(model)
    
    # Train model
    losses = train(model, data, chars, char_to_idx, idx_to_char, 
                   epochs=20, batch_size=128, seq_length=100, lr=0.001)
    
    # Save model
    torch.save({
        'model_state_dict': model.state_dict(),
        'char_to_idx': char_to_idx,
        'idx_to_char': idx_to_char
    }, "char_lstm_model.pth")
    
    # Generate samples with different temperatures
    print("\nSamples with different temperatures:")
    for temp in [0.2, 0.5, 1.0, 1.5]:
        sample = generate_text(model, char_to_idx, idx_to_char, seed="Once upon a time ", 
                               length=500, temperature=temp)
        print(f"\nTemperature: {temp}")
        print(sample)
        print("-" * 50)

if __name__ == "__main__":
    main()
```

This implementation includes:

- Loading and preprocessing text data
- Creating efficient batches for training
- Training the LSTM model with gradient clipping
- Generating text with temperature sampling
- Saving and loading the trained model
- Visualizing the training loss

---

### 3.8 Evaluating Neural Language Models

#### Perplexity Revisited

As with n-gram models, perplexity remains a standard metric for evaluating neural language models. For a model that assigns probability $P(x)$ to a sequence $x$, perplexity is defined as:

$\text{Perplexity}(x) = \exp\left(-\frac{1}{N} \sum_{i=1}^{N} \log P(x_i | x_1, \ldots, x_{i-1})\right)$

Lower perplexity indicates a better model. A perfect model would have a perplexity of 1, meaning it predicts each token with certainty.

#### Computing Perplexity for Neural Models

Here's how we might compute perplexity for our character-level LSTM:

```python
def calculate_perplexity(model, data, char_to_idx, batch_size=64, seq_length=100):
    model.eval()
    criterion = nn.CrossEntropyLoss(reduction='none')  # Keep per-token losses
    device = next(model.parameters()).device
    
    # Convert data to indices
    data_indices = [char_to_idx[ch] for ch in data]
    
    total_loss = 0
    n_tokens = 0
    
    with torch.no_grad():
        hidden = None
        
        for inputs, targets in get_batches(data_indices, batch_size, seq_length):
            # Convert to tensors
            inputs = torch.tensor(inputs, dtype=torch.long).to(device)
            targets = torch.tensor(targets, dtype=torch.long).to(device)
            
            # Forward pass
            outputs, hidden = model(inputs, hidden)
            
            # Detach hidden state
            hidden = tuple(h.detach() for h in hidden)
            
            # Reshape for loss calculation
            outputs = outputs.reshape(-1, model.n_chars)
            targets = targets.reshape(-1)
            
            # Calculate per-token loss
            losses = criterion(outputs, targets)
            
            total_loss += losses.sum().item()
            n_tokens += targets.numel()
    
    # Calculate average negative log-likelihood
    avg_nll = total_loss / n_tokens
    
    # Perplexity is exp(avg_nll)
    perplexity = np.exp(avg_nll)
    
    return perplexity
```

#### Comparing to Traditional Models

Neural language models generally achieve significantly lower perplexity than n-gram models, especially on test data that contains patterns not seen during training. This demonstrates their superior ability to generalize.

For example, on a typical English text corpus:

- A trigram model might achieve perplexity of 250-300
- An LSTM might achieve perplexity of 100-150
- A Transformer might achieve perplexity below 100

#### Beyond Perplexity: Human Evaluation

While perplexity provides a quantitative measure, qualitative evaluation is equally important. We can assess generated text on criteria like:

1. **Grammaticality**: Is the text grammatically correct?
2. **Coherence**: Does the text make logical sense over longer spans?
3. **Relevance**: Does the generated text stay on topic?
4. **Diversity**: Does the model produce varied and interesting text?
5. **Factuality**: Are any factual statements correct?

Human evaluation remains crucial for assessing these more subjective aspects of language model quality.

---

### 3.9 Limitations of RNN-Based Models

While RNNs and LSTMs represented a major leap forward in language modeling, they still have significant limitations:

#### Sequential Processing

RNNs process tokens one by one, which has two major drawbacks:

1. **Training is slow**: Cannot be easily parallelized
2. **Inference is slow**: Must generate each token sequentially

This makes training on massive datasets and deploying for real-time applications challenging.

#### Limited Context Window

Even with LSTMs' improved memory, they still struggle with very long-range dependencies. In practice, information beyond a certain distance tends to get "forgotten" or diluted.

#### Computation Complexity

The sequential nature of RNNs means that:

- Training time scales linearly with sequence length
- Memory usage can be inefficient
- Gradient flow can still be problematic for very long sequences

#### The Sequential Bottleneck

Perhaps the most fundamental limitation is what we call the "sequential bottleneck." Because each state depends on the previous state, we cannot parallelize the computation across the sequence. This limits both training speed and the practical length of sequences we can process.

These limitations set the stage for the Transformer architecture, which we'll explore in Module 4. Transformers replace recurrence with attention mechanisms, allowing parallel processing of the entire sequence.

---

### 3.10 Key Takeaways from Module 3

Let's summarize what we've learned in this module:

1. Neural language models represent words as continuous vectors (embeddings) rather than discrete symbols
2. Word embeddings capture semantic relationships between words
3. RNNs process sequential data by maintaining an internal state that gets updated at each step
4. LSTMs and GRUs use gating mechanisms to better capture long-range dependencies
5. Character-level models avoid vocabulary limitations but require more capacity to learn patterns
6. Neural models achieve significantly lower perplexity than traditional statistical approaches
7. Despite their power, RNNs and LSTMs face limitations due to their sequential nature

These neural approaches laid the foundation for modern language models, but the real revolution came with the Transformer architecture, which we'll explore in Module 4.

---

### 3.11 Practice Exercises

To reinforce your learning from this module, try these exercises:

1. **Word Embeddings Exploration**:
    
    - Train a Word2Vec model on a text corpus of your choice
    - Visualize the resulting embeddings using t-SNE
    - Try finding word analogies (e.g., king - man + woman = ?)
2. **RNN Implementation**:
    
    - Implement a simple RNN from scratch (without using PyTorch's RNN modules)
    - Compare its performance with PyTorch's implementation
3. **Character-Level Model Experiments**:
    
    - Train the character-level LSTM on different types of text (e.g., Shakespeare, code, news)
    - Experiment with different hyperparameters (hidden size, number of layers)
    - Try generating text with different temperature settings
    - Implement beam search for text generation instead of random sampling
4. **Model Evaluation**:
    
    - Calculate perplexity for your models on different test sets
    - Conduct a small human evaluation study comparing texts generated by different models
5. **Advanced Challenge**:
    
    - Implement a word-level LSTM language model
    - Add attention mechanisms to your LSTM (a preview of transformers!)

---

### 3.12 Preview of Module 4 - The Transformer Revolution

In our next module, we'll explore the architecture that revolutionized natural language processing: the Transformer. Introduced in the landmark "Attention Is All You Need" paper (Vaswani et al., 2017), transformers solve the key limitations of RNNs through:

1. **Attention mechanisms**: Directly modeling relationships between all words in a sequence
2. **Parallel processing**: Processing the entire sequence at once rather than token by token
3. **Position encoding**: Maintaining sequence order without recurrence
4. **Multi-head attention**: Capturing different types of relationships simultaneously

The transformer architecture enabled training on vastly larger datasets, leading to models like BERT, GPT, and eventually the modern Large Language Models we use today.

In Module 4, we'll:

- Explore attention mechanisms in depth
- Understand the complete transformer architecture
- Implement a transformer from scratch
- Train a simple transformer for next-word prediction
- Set the stage for scaling up to true LLMs

This next module represents the critical bridge from traditional neural networks to modern LLMs - the architectural innovation that made today's AI revolution possible.

---

## Module 4 - The Transformer Revolution

Welcome to Module 4 of our LLM crash course! In our previous module, we explored recurrent neural networks and their advanced variants like LSTMs for language modeling. While these models were powerful, they had fundamental limitations—particularly their sequential nature and difficulty capturing long-range dependencies.

In this module, we'll explore the architecture that revolutionized natural language processing: the Transformer. This breakthrough, introduced in the 2017 paper "Attention Is All You Need," solved the key limitations of RNNs and became the foundation for all modern Large Language Models.

- [[4.1 Attention Mechanisms - The Core Innovation]]
- [[4.2 The Complete Transformer Architecture]]
- [[4.3 Training Transformers]]
- [[4.4 Building a Small-Scale Transformer for Next-Word Prediction]]
- [[4.5 Visualizing and Understanding Transformers]]
- [[4.6 Limitations and Challenges of Transformers]]
- [[4.7 Advanced Transformer Variants]]
- [[4.8 Hands-On Project - Building a Simple Transformer for Next-Word Prediction]]
- [[4.9 Key Takeaways from Module 4]]
- [[4.10 Practice Exercises]]
- [[4.11 Preview of Module 5 - Scaling Up - From Models to LLMs]]

---

### 4.1 Attention Mechanisms - The Core Innovation

#### Why We Need a New Approach

Before diving into attention mechanisms, let's recap the core limitations of RNNs that needed solving:

1. **Sequential bottleneck**: RNNs process tokens one after another, preventing parallelization
2. **Information decay**: Information from earlier tokens gradually fades as sequences get longer
3. **Computational inefficiency**: Training RNNs on long sequences is prohibitively expensive

Attention mechanisms offer an elegant solution to these problems by allowing the model to directly connect any position in a sequence with any other position. This is like giving the model the ability to "look" at any part of the input when making a prediction, rather than relying solely on a compressed state.

#### The Intuition Behind Attention

Let's start with a simple intuition before diving into the mathematics. When we read a sentence, we naturally focus on different words depending on what we're trying to understand. For example, in the sentence "The cat sat on the mat because it was comfortable," what does "it" refer to? To answer, you might pay special attention to "cat" and "mat" to resolve the reference.

Attention mechanisms formalize this intuition, allowing models to "pay attention" to specific parts of the input when generating each part of the output.

#### Self-Attention: The Mathematical Foundation

Self-attention (sometimes called intra-attention) is the core mechanism that allows a model to weigh the importance of different words in a sequence when encoding a specific word.

Here's how it works, step by step:

1. Each token in the sequence is first converted to three vectors:
    
    - A **query** vector (Q): what the token is "looking for"
    - A **key** vector (K): what the token "offers" to others
    - A **value** vector (V): the actual content of the token
2. For each token, we compute attention scores with every other token by taking the dot product of its query vector with the key vectors of all tokens.
    
3. These scores are normalized using a softmax function to create attention weights that sum to 1.
    
4. Finally, we compute a weighted sum of all value vectors, using these attention weights.
    

Mathematically, for a single token, the self-attention operation is:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Where:

- $Q$ is the query matrix (sequence length × query dimension)
- $K$ is the key matrix (sequence length × key dimension)
- $V$ is the value matrix (sequence length × value dimension)
- $d_k$ is the dimensionality of the keys (used for scaling)

The $\frac{1}{\sqrt{d_k}}$ scaling factor prevents the dot products from growing too large in magnitude, which would push the softmax function into regions with very small gradients.

#### Visual Explanation of Self-Attention

Let's visualize this process for a simple example sentence: "The cat sat on the mat."

1. First, we convert each word to its embedding and then project it to create Q, K, and V vectors:
    
    ```
    "The"  → Q₁, K₁, V₁
    "cat"  → Q₂, K₂, V₂
    "sat"  → Q₃, K₃, V₃
    "on"   → Q₄, K₄, V₄
    "the"  → Q₅, K₅, V₅
    "mat"  → Q₆, K₆, V₆
    ```
    
2. To calculate the attention-weighted representation for "cat", we:
    
    - Compute attention scores: dot product of Q₂ with each K vector
    - Apply softmax to get weights
    - Take weighted sum of all V vectors
3. The result might look something like:
    
    - "The": 0.1 attention weight
    - "cat": 0.4 attention weight (paying most attention to itself)
    - "sat": 0.3 attention weight (closely related verb)
    - "on": 0.05 attention weight
    - "the": 0.05 attention weight
    - "mat": 0.1 attention weight
4. The final representation for "cat" would be: 0.1×V₁ + 0.4×V₂ + 0.3×V₃ + 0.05×V₄ + 0.05×V₅ + 0.1×V₆
    

This process happens simultaneously for every word in the sequence, allowing each word to gather information from the entire context.

#### Multi-Head Attention: Attending from Multiple Perspectives

In practice, a single attention mechanism might not be sufficient to capture all the different types of relationships between words. Some words might be related syntactically, others semantically, and so on.

To address this, transformers use **Multi-Head Attention**. This involves running several attention mechanisms in parallel, each with its own set of learned query, key, and value projections. The outputs of these parallel attention "heads" are then concatenated and linearly transformed.

Mathematically:

$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \text{head}_2, ..., \text{head}_h)W^O$$

Where each head is:

$$\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

And $W_i^Q$, $W_i^K$, $W_i^V$, and $W^O$ are learnable parameter matrices.

#### Implementing Self-Attention in Code

Let's implement a basic self-attention mechanism in PyTorch:

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class SelfAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(SelfAttention, self).__init__()
        self.embed_size = embed_size
        self.heads = heads
        self.head_dim = embed_size // heads
        
        assert (self.head_dim * heads == embed_size), "Embed size must be divisible by heads"
        
        # Linear transformations for Q, K, V for all heads at once
        self.q_linear = nn.Linear(embed_size, embed_size)
        self.k_linear = nn.Linear(embed_size, embed_size)
        self.v_linear = nn.Linear(embed_size, embed_size)
        
        # Output projection
        self.out = nn.Linear(embed_size, embed_size)
        
    def forward(self, q, k, v, mask=None):
        # Get batch size
        batch_size = q.size(0)
        
        # Perform linear projections and split into multiple heads
        q = self.q_linear(q).view(batch_size, -1, self.heads, self.head_dim).transpose(1, 2)
        k = self.k_linear(k).view(batch_size, -1, self.heads, self.head_dim).transpose(1, 2)
        v = self.v_linear(v).view(batch_size, -1, self.heads, self.head_dim).transpose(1, 2)
        
        # Calculate attention scores
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        
        # Apply mask if provided (useful for preventing attention to padding tokens)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        
        # Apply softmax to get attention weights
        attention = F.softmax(scores, dim=-1)
        
        # Compute weighted sum of values
        out = torch.matmul(attention, v)
        
        # Reshape back to original dimensions
        out = out.transpose(1, 2).contiguous().view(batch_size, -1, self.embed_size)
        
        # Apply final linear transformation
        out = self.out(out)
        
        return out
```

This implementation shows how self-attention computes weighted representations for each token based on the entire sequence. The multi-head approach allows the model to jointly attend to information from different representational spaces.

---

### 4.2 The Complete Transformer Architecture

Now that we understand attention mechanisms, let's explore the full Transformer architecture. The original Transformer consists of an encoder and a decoder, though many modern LLMs use only the decoder component.

#### Overall Structure

The Transformer architecture consists of:

1. **Input Embedding Layer**: Converts tokens to vectors
2. **Positional Encoding**: Adds information about token position
3. **Encoder**: Several identical layers that process the input sequence
4. **Decoder**: Several identical layers that generate the output sequence
5. **Output Linear Layer**: Projects to vocabulary size for next-token prediction

Let's examine each component in detail.

#### Embedding and Positional Encoding

Unlike RNNs, which process tokens sequentially, Transformers process all tokens in parallel. This means they have no inherent way to know the order of tokens. To address this, we add **positional encodings** to the token embeddings.

The original Transformer used sine and cosine functions of different frequencies:

$$PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}})$$ $$PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}})$$

Where:

- $pos$ is the position of the token in the sequence
- $i$ is the dimension
- $d_{model}$ is the embedding dimension

This creates a unique pattern for each position, allowing the model to learn the relative or absolute position of each token.

Here's how we might implement positional encoding:

```python
def get_positional_encoding(seq_len, d_model):
    """Create positional encoding for transformer."""
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    
    # Apply sine to even indices
    pe[:, 0::2] = torch.sin(position * div_term)
    # Apply cosine to odd indices
    pe[:, 1::2] = torch.cos(position * div_term)
    
    return pe
```

#### Encoder Layer

Each encoder layer consists of two main sub-layers:

1. **Multi-Head Self-Attention**: Processes the entire sequence using the attention mechanism
2. **Feed-Forward Network**: A simple network applied to each position independently

Each sub-layer is wrapped with **residual connections** and **layer normalization**, which helps with training stability.

```python
class EncoderLayer(nn.Module):
    def __init__(self, embed_size, heads, ff_hidden_size, dropout=0.1):
        super(EncoderLayer, self).__init__()
        
        # Self-attention layer
        self.attention = SelfAttention(embed_size, heads)
        
        # Feed-forward network
        self.feed_forward = nn.Sequential(
            nn.Linear(embed_size, ff_hidden_size),
            nn.ReLU(),
            nn.Linear(ff_hidden_size, embed_size)
        )
        
        # Layer normalization
        self.norm1 = nn.LayerNorm(embed_size)
        self.norm2 = nn.LayerNorm(embed_size)
        
        # Dropout for regularization
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, mask=None):
        # Self-attention with residual connection and normalization
        attention = self.attention(x, x, x, mask)
        x = self.norm1(x + self.dropout(attention))
        
        # Feed-forward with residual connection and normalization
        ff = self.feed_forward(x)
        x = self.norm2(x + self.dropout(ff))
        
        return x
```

The complete encoder consists of several of these layers stacked on top of each other:

```python
class Encoder(nn.Module):
    def __init__(self, vocab_size, embed_size, num_layers, heads, ff_hidden_size, dropout=0.1, max_seq_len=100):
        super(Encoder, self).__init__()
        
        # Token embedding
        self.embedding = nn.Embedding(vocab_size, embed_size)
        
        # Positional encoding
        self.pos_encoding = get_positional_encoding(max_seq_len, embed_size)
        
        # Encoder layers
        self.layers = nn.ModuleList([
            EncoderLayer(embed_size, heads, ff_hidden_size, dropout)
            for _ in range(num_layers)
        ])
        
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, mask=None):
        seq_len = x.size(1)
        
        # Add token embeddings and positional encodings
        x = self.embedding(x)
        x = x + self.pos_encoding[:seq_len, :].to(x.device)
        x = self.dropout(x)
        
        # Pass through encoder layers
        for layer in self.layers:
            x = layer(x, mask)
            
        return x
```

#### Decoder Layer

The decoder layer is similar to the encoder layer but with some key differences:

1. It uses **masked self-attention** in its first sub-layer to prevent attending to future tokens
2. It has an additional **cross-attention** layer that attends to the encoder's output

```python
class DecoderLayer(nn.Module):
    def __init__(self, embed_size, heads, ff_hidden_size, dropout=0.1):
        super(DecoderLayer, self).__init__()
        
        # Self-attention layer (masked)
        self.self_attention = SelfAttention(embed_size, heads)
        
        # Cross-attention layer
        self.cross_attention = SelfAttention(embed_size, heads)
        
        # Feed-forward network
        self.feed_forward = nn.Sequential(
            nn.Linear(embed_size, ff_hidden_size),
            nn.ReLU(),
            nn.Linear(ff_hidden_size, embed_size)
        )
        
        # Layer normalization
        self.norm1 = nn.LayerNorm(embed_size)
        self.norm2 = nn.LayerNorm(embed_size)
        self.norm3 = nn.LayerNorm(embed_size)
        
        # Dropout for regularization
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, enc_out, src_mask=None, trg_mask=None):
        # Self-attention with residual connection and normalization
        self_attention = self.self_attention(x, x, x, trg_mask)
        x = self.norm1(x + self.dropout(self_attention))
        
        # Cross-attention with encoder output
        cross_attention = self.cross_attention(x, enc_out, enc_out, src_mask)
        x = self.norm2(x + self.dropout(cross_attention))
        
        # Feed-forward with residual connection and normalization
        ff = self.feed_forward(x)
        x = self.norm3(x + self.dropout(ff))
        
        return x
```

And the complete decoder:

```python
class Decoder(nn.Module):
    def __init__(self, vocab_size, embed_size, num_layers, heads, ff_hidden_size, dropout=0.1, max_seq_len=100):
        super(Decoder, self).__init__()
        
        # Token embedding
        self.embedding = nn.Embedding(vocab_size, embed_size)
        
        # Positional encoding
        self.pos_encoding = get_positional_encoding(max_seq_len, embed_size)
        
        # Decoder layers
        self.layers = nn.ModuleList([
            DecoderLayer(embed_size, heads, ff_hidden_size, dropout)
            for _ in range(num_layers)
        ])
        
        # Final output layer
        self.fc_out = nn.Linear(embed_size, vocab_size)
        
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, enc_out, src_mask=None, trg_mask=None):
        seq_len = x.size(1)
        
        # Add token embeddings and positional encodings
        x = self.embedding(x)
        x = x + self.pos_encoding[:seq_len, :].to(x.device)
        x = self.dropout(x)
        
        # Pass through decoder layers
        for layer in self.layers:
            x = layer(x, enc_out, src_mask, trg_mask)
            
        # Project to vocabulary
        x = self.fc_out(x)
        
        return x
```

#### The Complete Transformer

Putting everything together, we get the complete Transformer model:

```python
class Transformer(nn.Module):
    def __init__(self, src_vocab_size, trg_vocab_size, embed_size=512, num_layers=6, 
                 heads=8, ff_hidden_size=2048, dropout=0.1, max_seq_len=100):
        super(Transformer, self).__init__()
        
        self.encoder = Encoder(src_vocab_size, embed_size, num_layers, heads, 
                              ff_hidden_size, dropout, max_seq_len)
        
        self.decoder = Decoder(trg_vocab_size, embed_size, num_layers, heads, 
                              ff_hidden_size, dropout, max_seq_len)
        
    def forward(self, src, trg, src_mask=None, trg_mask=None):
        enc_out = self.encoder(src, src_mask)
        out = self.decoder(trg, enc_out, src_mask, trg_mask)
        return out
    
    def create_masks(self, src, trg):
        # Source mask (to handle padding)
        src_mask = (src != 0).unsqueeze(1).unsqueeze(2)
        
        # Target mask (to handle padding and prevent looking ahead)
        trg_mask = (trg != 0).unsqueeze(1).unsqueeze(2)
        seq_len = trg.size(1)
        
        # Create look-ahead mask
        look_ahead_mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()
        look_ahead_mask = look_ahead_mask.to(trg.device)
        
        # Combine padding mask and look-ahead mask
        trg_mask = trg_mask & ~look_ahead_mask
        
        return src_mask, trg_mask
```

#### Decoder-Only Models

Many modern LLMs (like GPT) use only the decoder part of the Transformer, adapted to handle both encoding and generation. These models:

1. Use causal (masked) self-attention to predict the next token based on previous tokens
2. Eliminate the encoder entirely
3. Apply the decoder logic to the entire sequence

This simplified architecture is particularly effective for generative tasks like language modeling.

```python
class DecoderOnlyTransformer(nn.Module):
    def __init__(self, vocab_size, embed_size=768, num_layers=12, heads=12, 
                 ff_hidden_size=3072, dropout=0.1, max_seq_len=1024):
        super(DecoderOnlyTransformer, self).__init__()
        
        # Token embedding
        self.embedding = nn.Embedding(vocab_size, embed_size)
        
        # Positional encoding
        self.pos_encoding = get_positional_encoding(max_seq_len, embed_size)
        
        # Modified decoder layers (without cross-attention)
        self.layers = nn.ModuleList([
            DecoderOnlyLayer(embed_size, heads, ff_hidden_size, dropout)
            for _ in range(num_layers)
        ])
        
        # Final output layer
        self.fc_out = nn.Linear(embed_size, vocab_size)
        
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, mask=None):
        seq_len = x.size(1)
        
        # Add token embeddings and positional encodings
        x = self.embedding(x)
        x = x + self.pos_encoding[:seq_len, :].to(x.device)
        x = self.dropout(x)
        
        # Pass through layers
        for layer in self.layers:
            x = layer(x, mask)
            
        # Project to vocabulary
        x = self.fc_out(x)
        
        return x
    
    def create_causal_mask(self, seq_len):
        """Create mask to prevent attending to future tokens."""
        mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()
        return ~mask  # Invert so 1 means "can attend"
```

---

### 4.3 Training Transformers

Training a Transformer model has its own set of challenges and techniques. Let's explore the key aspects.

#### Loss Function: Cross-Entropy

For language modeling, we typically use cross-entropy loss:

```python
criterion = nn.CrossEntropyLoss(ignore_index=pad_idx)
```

This computes the loss between our predicted probability distribution over the vocabulary and the actual next token.

#### Learning Rate Scheduling

Transformers often use a special learning rate schedule called the "Noam" schedule or "warmup" schedule:

```python
def get_lr_scheduler(optimizer, d_model, warmup_steps=4000):
    """Implement the learning rate schedule from the Transformer paper."""
    def lr_lambda(step):
        # Increase linearly for warmup_steps, then decrease proportionally to sqrt(step)
        step = max(1, step)  # Avoid division by zero
        return min(step**(-0.5), step * warmup_steps**(-1.5)) * d_model**0.5
        
    return torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)
```

This schedule first increases the learning rate linearly during a warmup phase, then decreases it proportionally to the inverse square root of the step number.

#### Initialization

Proper initialization is crucial for stable training:

```python
def initialize_weights(m):
    if hasattr(m, 'weight') and m.weight.dim() > 1:
        nn.init.xavier_uniform_(m.weight.data)
```

#### Training Loop

Here's a simplified training loop for a Transformer language model:

```python
def train_epoch(model, dataloader, optimizer, criterion, device):
    model.train()
    total_loss = 0
    
    for batch in dataloader:
        src, trg = batch
        src, trg = src.to(device), trg.to(device)
        
        # Create masks
        src_mask, trg_mask = model.create_masks(src, trg)
        
        # Forward pass
        optimizer.zero_grad()
        output = model(src, trg[:, :-1], src_mask, trg_mask[:, :, :-1, :-1])
        
        # Reshape for loss computation
        output = output.contiguous().view(-1, output.shape[-1])
        trg = trg[:, 1:].contiguous().view(-1)
        
        # Compute loss
        loss = criterion(output, trg)
        
        # Backward pass
        loss.backward()
        
        # Gradient clipping
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        
        # Update weights
        optimizer.step()
        
        total_loss += loss.item()
        
    return total_loss / len(dataloader)
```

---

### 4.4 Building a Small-Scale Transformer for Next-Word Prediction

Now, let's put everything together to build a simple transformer model for next-word prediction. This will be a practical implementation that you can run on a standard GPU.

#### Project Setup

Let's define the problem and data setup:

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math
import time
from collections import Counter
import re

# Constants
BATCH_SIZE = 32
SEQ_LENGTH = 64
EMBED_SIZE = 256
NUM_HEADS = 8
NUM_LAYERS = 6
FF_HIDDEN_SIZE = 1024
DROPOUT = 0.1
EPOCHS = 10
LEARNING_RATE = 0.0001
```

#### Data Preparation

We'll use a simple text dataset for training:

```python
class TextDataset(Dataset):
    def __init__(self, text, seq_length):
        self.text = text
        self.seq_length = seq_length
        self.tokenizer = SimpleTokenizer(text)
        self.data = self.tokenizer.encode(text)
        
    def __len__(self):
        return len(self.data) - self.seq_length - 1
        
    def __getitem__(self, idx):
        # Get sequence and target
        seq = self.data[idx:idx + self.seq_length]
        target = self.data[idx + 1:idx + self.seq_length + 1]
        
        return torch.tensor(seq), torch.tensor(target)

class SimpleTokenizer:
    def __init__(self, text=None):
        # For simplicity, we'll use character-level tokenization
        if text:
            self.vocab = sorted(list(set(text)))
            self.vocab_size = len(self.vocab)
            self.char_to_idx = {ch: i for i, ch in enumerate(self.vocab)}
            self.idx_to_char = {i: ch for i, ch in enumerate(self.vocab)}
        else:
            self.vocab = []
            self.vocab_size = 0
            self.char_to_idx = {}
            self.idx_to_char = {}
    
    def encode(self, text):
        """Convert text to indices."""
        return [self.char_to_idx[ch] for ch in text]
    
    def decode(self, indices):
        """Convert indices to text."""
        return ''.join([self.idx_to_char[idx] for idx in indices])
```

#### Building a Decoder-Only Transformer

For simplicity, we'll build a decoder-only transformer similar to GPT:

```python
class DecoderOnlyLayer(nn.Module):
    def __init__(self, embed_size, heads, ff_hidden_size, dropout=0.1):
        super(DecoderOnlyLayer, self).__init__()
        
        # Self-attention layer
        self.attention = SelfAttention(embed_size, heads)
        
        # Feed-forward network
        self.feed_forward = nn.Sequential(
            nn.Linear(embed_size, ff_hidden_size),
            nn.GELU(),  # GPT uses GELU instead of ReLU
            nn.Linear(ff_hidden_size, embed_size)
        )
        
        # Layer normalization
        self.norm1 = nn.LayerNorm(embed_size)
        self.norm2 = nn.LayerNorm(embed_size)
        
        # Dropout for regularization
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, mask=None):
        # Self-attention with residual connection and normalization
        # Note: Using pre-LayerNorm as in many modern implementations
        norm_x = self.norm1(x)
        attention = self.attention(norm_x, norm_x, norm_x, mask)
        x = x + self.dropout(attention)
        
        # Feed-forward with residual connection and normalization
        norm_x = self.norm2(x)
        ff = self.feed_forward(norm_x)
        x = x + self.dropout(ff)
        
        return x

class GPTModel(nn.Module):
    def __init__(self, vocab_size, embed_size, num_layers, heads, ff_hidden_size, dropout=0.1, max_seq_len=100):
        super(GPTModel, self).__init__()
        
        # Token embedding
        self.embedding = nn.Embedding(vocab_size, embed_size)
        
        # Positional encoding
        self.register_buffer("pos_encoding", get_positional_encoding(max_seq_len, embed_size))
        
        # Decoder layers
        self.layers = nn.ModuleList([
            DecoderOnlyLayer(embed_size, heads, ff_hidden_size, dropout)
            for _ in range(num_layers)
        ])
        
        # Final layer normalization
        self.norm = nn.LayerNorm(embed_size)
        
        # Output projection
        self.fc_out = nn.Linear(embed_size, vocab_size)
        
        self.dropout = nn.Dropout(dropout)
        self.embed_size = embed_size
        
    def forward(self, x):
        seq_len = x.size(1)
        
        # Create causal attention mask
        mask = self.create_causal_mask(seq_len).to(x.device)
        
        # Add token embeddings and positional encodings
        x = self.embedding(x) * math.sqrt(self.embed_size)
        x = x + self.pos_encoding[:seq_len, :].to(x.device)
        x = self.dropout(x)
        
        # Pass through decoder layers
        for layer in self.layers:
            x = layer(x, mask)
            
        # Final layer norm
        x = self.norm(x)
        
        # Project to vocabulary
        x = self.fc_out(x)
        
        return x
    
    def create_causal_mask(self, seq_len):
        """Create mask to prevent attending to future tokens."""
        mask = torch.triu(torch.ones(1, 1, seq_len, seq_len), diagonal=1).bool()
        return ~mask  # Invert so 1 means "can attend"
    
    def generate(self, start_tokens, max_length, temperature=1.0):
        """Generate new text given starting tokens."""
        self.eval()
        current_tokens = start_tokens.clone()
        
        with torch.no_grad():
            for _ in range(max_length):
                # Get predictions
                logits = self(current_tokens)
                
                # Focus on the last token's prediction
                next_token_logits = logits[:, -1, :] / temperature
                
                # Apply softmax to get probabilities
                probabilities = F.softmax(next_token_logits, dim=-1)
                
                # Sample from the distribution
                next_token = torch.multinomial(probabilities, 1)
                
                # Add to our sequence
                current_tokens = torch.cat([current_tokens, next_token], dim=1)
        
        return current_tokens
```

#### Training and Generation

Now let's define functions for training and text generation:

```python
def train_gpt(model, dataset, epochs, batch_size, learning_rate, device):
    """Train the GPT model."""
    # Create dataloader
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    
    # Set up optimizer
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
    
    # Set up scheduler with warmup
    scheduler = get_lr_scheduler(optimizer, model.embed_size)
    
    # Loss function
    criterion = nn.CrossEntropyLoss()
    
    # Training loop
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        start_time = time.time()
        
        for batch_idx, (sequences, targets) in enumerate(dataloader):
            sequences, targets = sequences.to(device), targets.to(device)
            
            # Forward pass
            optimizer.zero_grad()
            outputs = model(sequences)
            
            # Reshape for loss calculation
            outputs = outputs.view(-1, outputs.shape[-1])
            targets = targets.view(-1)
            
            # Calculate loss
            loss = criterion(outputs, targets)
            
            # Backward pass
            loss.backward()
            
            # Gradient clipping
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            
            # Update weights
            optimizer.step()
            scheduler.step()
            
            total_loss += loss.item()
            
            # Print batch progress
            if batch_idx % 50 == 0:
                print(f"Epoch {epoch+1}/{epochs}, Batch {batch_idx}/{len(dataloader)}, Loss: {loss.item():.4f}")
        
        # Calculate average loss
        avg_loss = total_loss / len(dataloader)
        elapsed_time = time.time() - start_time
        
        print(f"Epoch {epoch+1}/{epochs}, Avg Loss: {avg_loss:.4f}, Time: {elapsed_time:.2f}s")
        
        # Generate sample text
        if (epoch + 1) % 2 == 0:
            sample_text = generate_text(model, dataset.tokenizer, "The ", 100, device)
            print(f"Sample: {sample_text}")
    
    return model

def generate_text(model, tokenizer, start_text, length, device, temperature=0.8):
    """Generate text using the trained model."""
    model.eval()
    
    # Convert start text to tensor
    start_tokens = torch.tensor([tokenizer.encode(start_text)], device=device)
    
    # Generate new tokens
    generated_tokens = model.generate(start_tokens, length, temperature)
    
    # Convert back to text
    generated_text = tokenizer.decode(generated_tokens[0].cpu().numpy())
    
    return generated_text
```

#### Complete Implementation

Now let's put everything together for a full working example:

```python
def main():
    # Check for GPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Load data (for this example, we'll use a small text corpus)
    with open("sample_text.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    # Create dataset
    dataset = TextDataset(text, SEQ_LENGTH)
    
    print(f"Vocabulary size: {dataset.tokenizer.vocab_size}")
    
    # Initialize model
    model = GPTModel(
        vocab_size=dataset.tokenizer.vocab_size,
        embed_size=EMBED_SIZE,
        num_layers=NUM_LAYERS,
        heads=NUM_HEADS,
        ff_hidden_size=FF_HIDDEN_SIZE,
        dropout=DROPOUT,
        max_seq_len=SEQ_LENGTH
    ).to(device)
    
    # Print model architecture
    print(model)
    print(f"Number of parameters: {sum(p.numel() for p in model.parameters() if p.requires_grad)}")
    
    # Train model
    model = train_gpt(model, dataset, EPOCHS, BATCH_SIZE, LEARNING_RATE, device)
    
    # Save model
    torch.save(model.state_dict(), "gpt_model.pth")
    
    # Generate samples with different temperatures
    print("\nGenerating samples with different temperatures:")
    for temp in [0.2, 0.5, 0.8, 1.2]:
        sample = generate_text(model, dataset.tokenizer, "The ", 200, device, temperature=temp)
        print(f"\nTemperature {temp}:")
        print(sample)

if __name__ == "__main__":
    main()
```

---

### 4.5 Visualizing and Understanding Transformers

One of the fascinating aspects of Transformer models is that we can visualize the attention patterns to understand what the model is learning.

#### Attention Visualization

Let's create a function to visualize attention weights:

```python
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_attention(model, text, tokenizer, device, layer_idx=0, head_idx=0):
    """Visualize attention weights for a given text."""
    model.eval()
    
    # Tokenize input
    tokens = tokenizer.encode(text)
    input_tensor = torch.tensor([tokens]).to(device)
    
    # Forward pass with attention weights
    with torch.no_grad():
        # Forward pass through embedding and positional encoding
        x = model.embedding(input_tensor) * math.sqrt(model.embed_size)
        x = x + model.pos_encoding[:input_tensor.size(1), :].to(device)
        x = model.dropout(x)
        
        # Create attention mask
        mask = model.create_causal_mask(input_tensor.size(1)).to(device)
        
        # Get attention weights from specific layer and head
        for i, layer in enumerate(model.layers):
            if i == layer_idx:
                # Run self-attention
                norm_x = layer.norm1(x)
                q = layer.attention.q_linear(norm_x)
                k = layer.attention.k_linear(norm_x)
                v = layer.attention.v_linear(norm_x)
                
                # Reshape for multi-head attention
                batch_size = q.size(0)
                q = q.view(batch_size, -1, model.layers[0].attention.heads, 
                          model.layers[0].attention.head_dim).transpose(1, 2)
                k = k.view(batch_size, -1, model.layers[0].attention.heads, 
                          model.layers[0].attention.head_dim).transpose(1, 2)
                
                # Calculate attention scores
                scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(model.layers[0].attention.head_dim)
                
                # Apply mask
                if mask is not None:
                    scores = scores.masked_fill(mask == 0, -1e9)
                
                # Apply softmax to get attention weights
                attention_weights = F.softmax(scores, dim=-1)
                
                # Extract weights for the specific head
                head_weights = attention_weights[0, head_idx].cpu().numpy()
                break
            else:
                # Just run the layer normally
                x = layer(x, mask)
    
    # Visualize
    plt.figure(figsize=(10, 8))
    sns.heatmap(head_weights, cmap="YlGnBu", 
                xticklabels=list(text), yticklabels=list(text))
    plt.title(f"Attention Weights (Layer {layer_idx}, Head {head_idx})")
    plt.xlabel("Key")
    plt.ylabel("Query")
    plt.show()
```

#### Interpreting Attention Patterns

Different attention heads often learn to focus on different linguistic patterns:

1. **Syntactic Relationships**: Some heads learn to connect subjects with verbs or articles with nouns
2. **Semantic Connections**: Other heads might focus on words with similar meanings
3. **Coreference Resolution**: Some heads learn to connect pronouns with their antecedents
4. **Positional Patterns**: Certain heads pay attention to specific relative positions

By visualizing these patterns, we can gain insights into how the model processes language.

---

### 4.6 Limitations and Challenges of Transformers

While Transformers have revolutionized NLP, they still face several challenges:

#### Quadratic Complexity

The self-attention mechanism has quadratic complexity with respect to sequence length, as it computes attention scores between every pair of tokens:

$$\text{Complexity} = O(n^2 \cdot d)$$

Where $n$ is the sequence length and $d$ is the dimension. This limits the context length that can be practically processed.

#### Memory Usage

Storing attention matrices for long sequences requires substantial memory, again limiting context length.

#### Position Encoding Limitations

The fixed positional encodings in the original Transformer don't extrapolate well to sequences longer than those seen during training.

#### Training Instability

Transformers can be challenging to train due to their depth and the complex interaction between components. Techniques like learning rate warmup, gradient clipping, and proper initialization are crucial.

---

### 4.7 Advanced Transformer Variants

Researchers have developed many variants to address Transformer limitations:

#### Efficient Attention Mechanisms

Several approaches reduce the quadratic complexity:

1. **Sparse Attention**: Only attend to a subset of tokens
2. **Local Attention**: Focus on nearby tokens
3. **Linformer**: Reduce dimensionality of key and value matrices
4. **Performer/FAVOR+**: Use kernel methods to approximate attention

#### Advanced Positional Encodings

Improvements over the original positional encoding include:

1. **Relative Positional Encodings**: Encode relative distances between tokens
2. **Rotary Position Embeddings (RoPE)**: Inject position information via rotation matrices
3. **ALiBi**: Add bias based on relative positions

#### Architecture Modifications

Other important variants include:

1. **Transformer-XL**: Enables learning dependencies beyond a fixed-length context
2. **Reformer**: Uses locality-sensitive hashing for efficient attention
3. **Longformer**: Combines local and global attention patterns
4. **Performer**: Uses fast attention via orthogonal random features

---

### 4.8 Hands-On Project - Building a Simple Transformer for Next-Word Prediction

Let's now implement a complete but trimmed-down Transformer model for next-word prediction on a small text corpus. This will cement your understanding of the architecture.

For brevity, I'll sketch the main components of the project, and you can fill in the details using the code snippets provided earlier:

1. **Data Preparation**
    
    - Select a small text corpus (e.g., a few books or articles)
    - Create a simple tokenizer (character or word-level)
    - Generate training sequences
2. **Model Implementation**
    
    - Implement a small decoder-only Transformer
    - Use the key components discussed: self-attention, feed-forward networks, layer normalization
3. **Training**
    
    - Train on next-token prediction using cross-entropy loss
    - Implement learning rate scheduling and gradient clipping
    - Monitor loss and generate samples periodically to check progress
4. **Evaluation and Generation**
    
    - Evaluate the model on a held-out test set
    - Create a text generation function with temperature control
    - Visualize attention patterns to understand what the model has learned

---

### 4.9 Key Takeaways from Module 4

Let's summarize what we've learned in this module:

1. **Attention Mechanisms**: The core innovation that allows models to focus on relevant parts of the input when making predictions
    
2. **Self-Attention**: Enables tokens to gather information from the entire sequence, overcoming the limitations of RNNs
    
3. **Multi-Head Attention**: Allows the model to attend to information from different representational subspaces
    
4. **Transformer Architecture**: Combines attention mechanisms with feed-forward networks, residual connections, and layer normalization
    
5. **Positional Encoding**: Provides sequence order information in a model that processes all tokens in parallel
    
6. **Parallel Processing**: Unlike RNNs, Transformers process all tokens simultaneously, enabling efficient training
    
7. **Scaling Properties**: The architecture scales well with more parameters and data, leading to the modern LLM revolution
    
8. **Limitations and Variants**: Various approaches to overcome the quadratic complexity and other challenges
    

The Transformer architecture represents the critical bridge from traditional neural networks to modern LLMs - the innovation that made today's AI revolution possible.

---

### 4.10 Practice Exercises

To reinforce your learning from this module, try these exercises:

1. **Implement Attention from Scratch**
    
    - Write a bare-bones implementation of self-attention without using any libraries
    - Visualize the attention weights for a simple example
2. **Experiment with Different Positional Encodings**
    
    - Implement relative positional encodings or rotary position embeddings
    - Compare their effectiveness with the original sinusoidal encodings
3. **Smaller Transformer Variants**
    
    - Implement a more efficient Transformer variant (e.g., with sparse attention)
    - Compare its performance and speed with the standard Transformer
4. **Attention Visualization Tool**
    
    - Expand the visualization function to examine all heads and layers
    - Analyze which linguistic patterns different heads capture
5. **Cross-Domain Exercise**
    
    - Adapt the Transformer for a non-text modality (e.g., simple music generation)
    - Explore how the architecture works with different types of sequential data

---

### 4.11 Preview of Module 5 - Scaling Up - From Models to LLMs

In our next module, we'll explore how to scale up from the basic Transformer architecture we've built to true Large Language Models. We'll cover:

1. **Pre-training objectives and strategies**
2. **Scaling laws and their implications**
3. **Efficient training techniques for large models**
4. **Model parallelism and distributed training**
5. **The mathematics behind model scaling**
6. **Navigating hardware constraints**
7. **Building and training a small-scale but complete LLM**

By the end of Module 5, you'll understand how modern LLMs are trained and scaled, setting the foundation for fine-tuning and specialized applications in subsequent modules.

---

## Module 5 - Scaling Up - From Models to LLMs

Welcome to Module 5 of our LLM crash course! In the previous module, we explored the revolutionary Transformer architecture that forms the foundation of modern language models. We implemented a small transformer model for next-word prediction and learned about attention mechanisms, positional encodings, and the overall architecture.

Now we're ready to tackle one of the most fascinating aspects of Large Language Models: scale. How do we go from a small transformer to a truly powerful LLM? What happens as models grow in size? How do we efficiently train models with billions of parameters?

In this module, we'll bridge the gap between the relatively small transformers that can run on a single GPU and the massive models that power today's AI revolution.

- [[5.1 The Scaling Revolution in AI]]
- [[5.2 Pre-training Objectives and Techniques]]
- [[5.3 Training Dynamics of Large Models]]
- [[5.4 Efficient Parameter Use and Model Architectures]]
- [[5.5 Scaling Infrastructure and Distributed Training]]
- [[5.6 Data Preparation and Management at Scale]]
- [[5.7 Hands-On Project - Training a Mid-Scale Language Model]]
- [[5.8 Key Takeaways from Module 5]]
- [[5.9 Practice Exercises]]
- [[5.10 Preview of Module 6 - Transfer Learning and Fine-tuning]]

---

### 5.1 The Scaling Revolution in AI

#### Understanding Scale in Language Models

When we talk about "scaling" language models, we're primarily referring to three key dimensions:

1. **Model size**: The number of parameters (weights and biases) in the neural network
2. **Dataset size**: The amount of text used for training
3. **Compute**: The computational resources used during training

The relationship between these dimensions has profound implications for model performance. Let's explore why scale matters so much in modern AI.

#### The Emergence of Scaling Laws

In 2020, researchers at OpenAI published a landmark paper on "Scaling Laws for Neural Language Models." This research revealed something remarkable: model performance improves predictably as we increase model size, dataset size, and compute.

More specifically, they found that model performance (measured by test loss) follows a power-law relationship with scale:

```
Loss ∝ (N⁻ᵃ) × (D⁻ᵇ) × (C⁻ᶜ)
```

Where:

- N is the number of model parameters
- D is the dataset size
- C is the amount of compute
- a, b, and c are scaling exponents (typically between 0.05 and 0.3)

This means that doubling the size of your model might reduce the loss by a predictable amount, even without any architectural changes.

#### Why Scaling Matters: Emergent Abilities

Perhaps the most fascinating aspect of scaling is the emergence of new capabilities that weren't explicitly programmed. As models grow larger, they don't just get better at the tasks they were already doing—they suddenly demonstrate entirely new abilities.

For example:

- Small models might struggle with basic grammar
- Medium models might handle grammar well but fail at logical reasoning
- Large models might suddenly display reasoning capabilities, humor, and creative writing skills

These "emergent abilities" often appear suddenly once models cross certain size thresholds, creating what researchers call "scaling cliffs" rather than smooth improvements.

#### The Bitter Lesson of AI Research

Computer scientist Rich Sutton's essay "The Bitter Lesson" argues that approaches leveraging computation and scale have consistently outperformed methods that try to engineer human knowledge into AI systems.

The "bitter" part is that our human intuitions about how to solve problems are often less effective than simply scaling up general methods that can learn from more data. This principle has played out dramatically in the LLM space, where scaling transformer models has yielded capabilities that surprised even their creators.

---

### 5.2 Pre-training Objectives and Techniques

Before diving into the specifics of scaling, we need to understand how we train these models in the first place. The choice of training objective significantly impacts what the model learns and how well it generalizes.

#### Autoregressive Language Modeling

The most common objective for decoder-only models like GPT is autoregressive language modeling: predicting the next token given all previous tokens.

The loss function is typically cross-entropy:

```python
def compute_language_modeling_loss(model_output, targets):
    """
    Compute cross-entropy loss for autoregressive language modeling.
    
    model_output: logits of shape [batch_size, sequence_length, vocab_size]
    targets: token ids of shape [batch_size, sequence_length]
    """
    # Reshape for loss computation
    batch_size, sequence_length, vocab_size = model_output.shape
    logits = model_output.view(-1, vocab_size)  # [batch_size*sequence_length, vocab_size]
    targets = targets.view(-1)  # [batch_size*sequence_length]
    
    # Compute cross-entropy loss
    loss = F.cross_entropy(logits, targets, ignore_index=-100)  # -100 is padding
    
    return loss
```

This approach has several advantages:

- Conceptually simple: just predict the next word
- Self-supervised: no need for labeled data
- Scales well: can use virtually any text on the internet

#### Masked Language Modeling

For encoder models like BERT, the most common objective is masked language modeling (MLM): randomly masking tokens and asking the model to predict them.

```python
def create_mlm_inputs_and_labels(input_ids, tokenizer, mask_probability=0.15):
    """
    Create inputs and labels for masked language modeling.
    
    input_ids: original token ids
    tokenizer: tokenizer with mask_token_id
    mask_probability: fraction of tokens to mask
    """
    labels = input_ids.clone()
    
    # Create a mask for tokens that will be masked
    probability_matrix = torch.full(input_ids.shape, mask_probability)
    special_tokens_mask = torch.tensor(
        [tokenizer.is_special_token(t) for t in input_ids.tolist()], 
        dtype=torch.bool
    )
    probability_matrix.masked_fill_(special_tokens_mask, value=0.0)
    masked_indices = torch.bernoulli(probability_matrix).bool()
    
    # We only compute loss on masked tokens
    labels[~masked_indices] = -100  # -100 is ignored in loss
    
    # Replace with mask token
    input_ids[masked_indices] = tokenizer.mask_token_id
    
    return input_ids, labels
```

This approach forces the model to understand bidirectional context, as it needs to consider both left and right context to predict masked tokens.

#### Hybrid Approaches

Many modern models use hybrid or novel pre-training objectives:

1. **Span-based masking**: Masking consecutive spans of tokens rather than individual tokens (e.g., T5)
2. **Prefix Language Modeling**: Combining autoregressive prediction with bidirectional attention (e.g., Prefix LM)
3. **Replaced Token Detection**: Training a discriminator to detect tokens that have been replaced by a generator (e.g., ELECTRA)

Each approach comes with its own trade-offs in terms of efficiency, downstream performance, and alignment with specific use cases.

#### Curriculum Learning for Pre-training

Rather than training on random data, curriculum learning involves structuring the training process from easier to harder examples. For LLMs, this might mean:

1. Starting with shorter, simpler texts
2. Gradually introducing longer, more complex content
3. Introducing more specialized or technical material later in training

Research suggests this can improve both training efficiency and final model quality, though implementing effective curricula remains challenging at scale.

---

### 5.3 Training Dynamics of Large Models

As models grow larger, their training dynamics change in important ways. Understanding these dynamics is crucial for successfully scaling up.

#### Optimization Challenges at Scale

Large models present unique optimization challenges:

1. **Vanishing/exploding gradients**: Deeper networks amplify gradient issues
2. **Unstable training**: Larger models are more sensitive to initialization and hyperparameters
3. **Longer convergence times**: More parameters mean more updates needed to reach convergence
4. **Memory constraints**: Model, optimizer states, and gradients must fit in available memory

#### Advanced Optimization Techniques

To address these challenges, several advanced techniques have become standard:

1. **AdamW optimizer**: A variant of Adam with improved weight decay handling
```python
optimizer = torch.optim.AdamW(
	model.parameters(),
	lr=1e-4,
	betas=(0.9, 0.999),
	eps=1e-8,
	weight_decay=0.01
)
```

2. **Learning rate schedules**: Warmup followed by decay is crucial for stable training
```python
def get_cosine_schedule_with_warmup(optimizer, num_warmup_steps, num_training_steps):
	def lr_lambda(current_step):
		if current_step < num_warmup_steps:
			return float(current_step) / float(max(1, num_warmup_steps))
		progress = float(current_step - num_warmup_steps) / float(max(1, num_training_steps - num_warmup_steps))
		return max(0.0, 0.5 * (1.0 + math.cos(math.pi * progress)))
	
	return torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)
```

3. **Gradient clipping**: Prevents exploding gradients by limiting their magnitude
```python
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
```

4. **Layer normalization placement**: "Pre-LN" (applying normalization before attention and FFN blocks) improves stability
```python
# Pre-LN architecture (more stable for training)
normalized_x = self.layer_norm(x)
attention_output = self.attention(normalized_x) + x  # Residual connection
```


#### The Challenges of Batch Size and Learning Rate

One of the most important hyper-parameter relationships is between batch size and learning rate. As we scale to larger models and distributed training, batch sizes often increase dramatically.

The relationship can be approximated as:
```
learning_rate ∝ sqrt(batch_size)
```

This means if you increase your batch size by 4x, you should roughly double your learning rate. However, this relationship breaks down at extremely large batch sizes, necessitating more careful tuning.

#### Loss Scaling for Mixed Precision Training

Training in mixed precision (using float16 for most operations) is essential for efficiency with large models, but introduces numerical stability challenges. Loss scaling helps address this:

```python
# Example of manual loss scaling
# Forward pass in float16
outputs = model(inputs)
loss = criterion(outputs, targets)

# Scale the loss to prevent underflow in gradients
scale = 128.0
scaled_loss = loss * scale

# Backward pass with scaled loss
scaled_loss.backward()

# Unscale gradients before optimizer step
for param in model.parameters():
    if param.grad is not None:
        param.grad.data = param.grad.data / scale

optimizer.step()
```

Modern frameworks like PyTorch's AMP (Automatic Mixed Precision) handle this automatically:

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

# Training loop
for inputs, targets in dataloader:
    # Forward pass with autocasting to float16 where appropriate
    with autocast():
        outputs = model(inputs)
        loss = criterion(outputs, targets)
    
    # Backward pass with gradient scaling
    scaler.scale(loss).backward()
    scaler.unscale_(optimizer)
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    scaler.step(optimizer)
    scaler.update()
    scheduler.step()
```

---

### 5.4 Efficient Parameter Use and Model Architectures

As models scale, we need to ensure parameters are used efficiently. Several architectural innovations help maximize the effectiveness of each parameter.

#### Activation Functions and Parameter Efficiency

The choice of activation function significantly impacts parameter efficiency. While ReLU was standard in earlier networks, GeLU (Gaussian Error Linear Unit) has become the dominant choice in modern LLMs:

```python
def gelu(x):
    """Gaussian Error Linear Unit."""
    return 0.5 * x * (1 + torch.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * torch.pow(x, 3))))
```

GeLU provides a smoother activation curve than ReLU and aligns well with the Gaussian noise used in training techniques like dropout.

#### Parameter Sharing and Depth vs Width

There's an ongoing debate about parameter efficiency regarding model depth versus width. Some findings include:

1. Very deep models (many layers) can be more parameter-efficient than very wide ones (large hidden dimensions)
2. However, extremely deep models become harder to train
3. Moderate depth with moderate width often provides the best balance

Some models like Albert even use parameter sharing across layers to improve efficiency:

```python
class AlbertLayer(nn.Module):
    """A single transformer layer that is shared across all layers."""
    def __init__(self, config):
        super().__init__()
        self.attention = SelfAttention(config)
        self.ffn = FeedForward(config)
        
class AlbertTransformer(nn.Module):
    """Albert transformer with shared parameters across layers."""
    def __init__(self, config):
        super().__init__()
        self.layer = AlbertLayer(config)
        self.num_layers = config.num_hidden_layers
        
    def forward(self, hidden_states, attention_mask=None):
        for i in range(self.num_layers):
            # Reuse the same layer for all transformer blocks
            hidden_states = self.layer(hidden_states, attention_mask)
        return hidden_states
```

#### Mixture of Experts

For extremely large models, Mixture of Experts (MoE) architectures have gained popularity. These models use "expert" neural networks (usually feed-forward networks) and a routing mechanism to send different inputs to different experts:

```python
class MixtureOfExperts(nn.Module):
    def __init__(self, input_size, hidden_size, num_experts, k=2):
        super().__init__()
        self.input_size = input_size
        self.num_experts = num_experts
        self.k = k  # Top-k experts to use for each token
        
        # Create experts (feed-forward networks)
        self.experts = nn.ModuleList([
            nn.Sequential(
                nn.Linear(input_size, hidden_size),
                nn.GELU(),
                nn.Linear(hidden_size, input_size)
            )
            for _ in range(num_experts)
        ])
        
        # Router network to determine which experts to use
        self.router = nn.Linear(input_size, num_experts)
        
    def forward(self, x):
        # x shape: [batch_size, seq_len, input_size]
        batch_size, seq_len, _ = x.shape
        
        # Get router logits
        router_logits = self.router(x)  # [batch_size, seq_len, num_experts]
        
        # Select top-k experts and normalize weights
        router_probs = F.softmax(router_logits, dim=-1)
        top_k_probs, top_k_indices = torch.topk(router_probs, self.k, dim=-1)
        top_k_probs = top_k_probs / top_k_probs.sum(dim=-1, keepdim=True)
        
        # Initialize output with zeros
        output = torch.zeros_like(x)
        
        # Compute weighted sum of expert outputs
        for i in range(self.k):
            # Get expert indices for this slot
            expert_indices = top_k_indices[:, :, i]  # [batch_size, seq_len]
            
            # Get probabilities for these experts
            expert_probs = top_k_probs[:, :, i]  # [batch_size, seq_len]
            
            # For each expert, compute its contribution
            for expert_idx in range(self.num_experts):
                # Create mask for tokens using this expert
                mask = (expert_indices == expert_idx).float()  # [batch_size, seq_len]
                mask = mask.unsqueeze(-1)  # [batch_size, seq_len, 1]
                
                # Apply expert to all tokens (inefficient but simple implementation)
                expert_output = self.experts[expert_idx](x)
                
                # Weight by router probability and add to output
                output += expert_output * mask * expert_probs.unsqueeze(-1)
        
        return output
```

MoE models can achieve much higher parameter counts while keeping computational costs manageable, as only a subset of parameters are activated for each input.

---

### 5.5 Scaling Infrastructure and Distributed Training

Once models grow beyond what fits on a single GPU, distributed training becomes essential.

#### Model Parallelism vs Data Parallelism

There are two primary approaches to distributed training:

1. **Data Parallelism**: Each device has a complete copy of the model but works on different data batches
```python
# Basic PyTorch DistributedDataParallel example
model = YourModel()
model = nn.parallel.DistributedDataParallel(model, device_ids=[local_rank])
```
    
2. **Model Parallelism**: The model itself is split across multiple devices
```python
# Simplified tensor parallelism example (actual implementation is more complex)
class ShardedLinear(nn.Module):
	def __init__(self, in_features, out_features, devices):
		super().__init__()
		self.devices = devices
		self.num_devices = len(devices)
		
		# Split output dimension across devices
		self.shards = nn.ModuleList([
			nn.Linear(in_features, out_features // self.num_devices).to(devices[i])
			for i in range(self.num_devices)
		])
		
	def forward(self, x):
		# Send input to all devices
		outputs = []
		for i, shard in enumerate(self.shards):
			x_i = x.to(self.devices[i])
			outputs.append(shard(x_i))
			
		# Gather and concatenate results
		outputs = [output.to(self.devices[0]) for output in outputs]
		return torch.cat(outputs, dim=-1)
```

In practice, modern frameworks implement more sophisticated approaches:

#### Pipeline Parallelism

Pipeline parallelism splits the model across devices by layer, with each device responsible for a set of consecutive layers:

```python
# Conceptual implementation of pipeline parallelism
def pipeline_forward(model_shards, input_batch, num_microbatches):
    # Split input batch into microbatches
    microbatches = torch.chunk(input_batch, num_microbatches, dim=0)
    outputs = []
    
    # Process in a pipelined fashion
    for i, microbatch in enumerate(microbatches):
        x = microbatch
        for device_id, model_shard in enumerate(model_shards):
            # Move input to the appropriate device
            x = x.to(f'cuda:{device_id}')
            # Process through this model shard
            x = model_shard(x)
        # Collect final outputs
        outputs.append(x)
    
    # Combine outputs
    return torch.cat(outputs, dim=0)
```

#### Tensor Parallelism

Tensor parallelism splits individual operations across devices. For example, a large matrix multiplication might be split such that each device computes only a portion:

```python
# Very simplified example of tensor parallelism for a self-attention layer
class DistributedSelfAttention(nn.Module):
    def __init__(self, hidden_size, num_heads, world_size):
        super().__init__()
        assert num_heads % world_size == 0, "Number of heads must be divisible by world size"
        
        # Each device gets a subset of attention heads
        self.local_num_heads = num_heads // world_size
        self.local_hidden_size = hidden_size // world_size
        self.rank = dist.get_rank()
        self.world_size = world_size
        
        # Only create parameters for our local heads
        self.q_proj = nn.Linear(hidden_size, self.local_hidden_size)
        self.k_proj = nn.Linear(hidden_size, self.local_hidden_size)
        self.v_proj = nn.Linear(hidden_size, self.local_hidden_size)
        self.o_proj = nn.Linear(self.local_hidden_size, hidden_size)
        
    def forward(self, hidden_states):
        # Each device computes attention for its subset of heads
        local_q = self.q_proj(hidden_states)
        local_k = self.k_proj(hidden_states)
        local_v = self.v_proj(hidden_states)
        
        # Compute local attention
        local_attn_output = self._attention(local_q, local_k, local_v)
        local_output = self.o_proj(local_attn_output)
        
        # All-reduce across devices to get complete output
        output = torch.zeros_like(hidden_states)
        dist.all_reduce(local_output, op=dist.ReduceOp.SUM)
        
        return output
```

#### DeepSpeed and Megatron-LM

In practice, libraries like DeepSpeed (Microsoft) and Megatron-LM (NVIDIA) provide optimized implementations of these techniques:

```python
# Using DeepSpeed for training
import deepspeed

model_engine, optimizer, _, _ = deepspeed.initialize(
    args=args,
    model=model,
    model_parameters=model.parameters()
)

# Training loop with DeepSpeed
for batch in dataloader:
    # Forward pass
    outputs = model_engine(batch)
    loss = outputs.loss
    
    # Backward pass
    model_engine.backward(loss)
    
    # Weight update
    model_engine.step()
```

These frameworks combine multiple parallelism strategies (ZeRO, pipeline, tensor) with optimized communication patterns to maximize efficiency.

---

### 5.6 Data Preparation and Management at Scale

Training massive models requires not just computational infrastructure but also sophisticated data pipelines.

#### Data Curation and Quality

High-quality training data is crucial for LLMs. Several considerations include:

1. **Deduplication**: Removing duplicated content to prevent memorization
```python
def simple_deduplication(texts):
	seen = set()
	unique_texts = []
	for text in texts:
		text_hash = hash(text)
		if text_hash not in seen:
			seen.add(text_hash)
			unique_texts.append(text)
	return unique_texts
```

2. **Content filtering**: Removing harmful, toxic, or low-quality content
```python
def basic_content_filter(text):
	# Remove texts with too many special characters
	if sum(not c.isalnum() and not c.isspace() for c in text) / len(text) > 0.3:
		return False
	
	# Filter based on length (too short texts are often not useful)
	if len(text.split()) < 10:
		return False
	
	# More sophisticated filtering would use ML models for toxicity, etc.
	return True
```

3. **Balancing**: Ensuring representation of different domains and styles
```python
def create_balanced_dataset(texts_by_domain, target_proportions):
	total_size = sum(len(texts) for texts in texts_by_domain.values())
	balanced_dataset = []
	
	for domain, target_proportion in target_proportions.items():
		texts = texts_by_domain[domain]
		target_count = int(total_size * target_proportion)
		
		if len(texts) <= target_count:
			# Use all texts from this domain
			balanced_dataset.extend(texts)
		else:
			# Sample to achieve target proportion
			sampled_texts = random.sample(texts, target_count)
			balanced_dataset.extend(sampled_texts)
			
	random.shuffle(balanced_dataset)
	return balanced_dataset
```


#### Efficient Data Loading

With terabyte-scale datasets, efficient data loading becomes critical:

```python
class StreamingDataset(torch.utils.data.IterableDataset):
    """Dataset that streams data from disk instead of loading everything to memory."""
    def __init__(self, file_paths, tokenizer, max_length=1024):
        super().__init__()
        self.file_paths = file_paths
        self.tokenizer = tokenizer
        self.max_length = max_length
        
    def __iter__(self):
        worker_info = torch.utils.data.get_worker_info()
        if worker_info is None:
            # Single worker case
            files_to_process = self.file_paths
        else:
            # Multiple workers case - split files among workers
            per_worker = int(math.ceil(len(self.file_paths) / worker_info.num_workers))
            worker_id = worker_info.id
            start = worker_id * per_worker
            end = min(start + per_worker, len(self.file_paths))
            files_to_process = self.file_paths[start:end]
        
        # Process files assigned to this worker
        for file_path in files_to_process:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if not line.strip():
                        continue
                    
                    # Tokenize text
                    tokens = self.tokenizer.encode(line.strip())
                    
                    # Yield chunks of appropriate length
                    for i in range(0, len(tokens), self.max_length):
                        chunk = tokens[i:i + self.max_length]
                        if len(chunk) == self.max_length:  # Only yield full-length chunks
                            yield torch.tensor(chunk)
```

#### WebDataset and Efficient Formats

For even larger datasets, specialized formats like WebDataset provide optimal I/O performance:

```python
import webdataset as wds

# Create a WebDataset pipeline
dataset = (
    wds.WebDataset(urls)
    .decode()
    .to_tuple("input.txt", "target.txt")
    .map(tokenize_function)
    .batched(batch_size)
)
```

---

### 5.7 Hands-On Project - Training a Mid-Scale Language Model

Now, let's put everything together in a hands-on project that trains a modest-scale language model. This won't be billions of parameters, but it will incorporate many of the scaling techniques we've discussed.

#### Project Objectives

1. Train a decoder-only transformer with ~100M parameters
2. Use advanced training techniques for stability and efficiency
3. Implement basic distributed training
4. Apply the training dynamics and optimization insights we've learned

#### Model Architecture

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class ScalableTransformer(nn.Module):
    def __init__(self, vocab_size, hidden_size=768, num_layers=12, num_heads=12, 
                 intermediate_size=3072, max_position_embeddings=1024, dropout=0.1):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.vocab_size = vocab_size
        
        # Token embeddings
        self.token_embeddings = nn.Embedding(vocab_size, hidden_size)
        
        # Position embeddings
        self.position_embeddings = nn.Embedding(max_position_embeddings, hidden_size)
        
        # Transformer layers
        self.layers = nn.ModuleList([
            TransformerBlock(hidden_size, num_heads, intermediate_size, dropout)
            for _ in range(num_layers)
        ])
        
        # Final layer norm
        self.layer_norm = nn.LayerNorm(hidden_size)
        
        # Output projection
        self.output_projection = nn.Linear(hidden_size, vocab_size, bias=False)
        
        # Tie weights between input embeddings and output projection
        self.output_projection.weight = self.token_embeddings.weight
        
        # Initialize parameters
        self.apply(self._init_weights)
        
    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            # Use scaled initialization for better training dynamics
            module.weight.data.normal_(mean=0.0, std=0.02 / math.sqrt(2 * self.num_layers))
            if module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.Embedding):
            module.weight.data.normal_(mean=0.0, std=0.02)
        elif isinstance(module, nn.LayerNorm):
            module.bias.data.zero_()
            module.weight.data.fill_(1.0)
    
    def forward(self, input_ids, return_logits=True):
        batch_size, seq_length = input_ids.size()
        device = input_ids.device
        
        # Create position indices
        position_ids = torch.arange(0, seq_length, dtype=torch.long, device=device)
        position_ids = position_ids.unsqueeze(0).expand(batch_size, -1)
        
        # Get embeddings
        token_embeds = self.token_embeddings(input_ids)
        position_embeds = self.position_embeddings(position_ids)
        
        # Combine embeddings
        hidden_states = token_embeds + position_embeds
        
        # Create casual attention mask
        attention_mask = self.create_causal_mask(seq_length).to(device)
        
        # Pass through transformer layers
        for layer in self.layers:
            hidden_states = layer(hidden_states, attention_mask)
        
        # Final layer norm
        hidden_states = self.layer_norm(hidden_states)
        
        # Project to vocabulary
        if return_logits:
            logits = self.output_projection(hidden_states)
            return logits
        else:
            return hidden_states
    
    def create_causal_mask(self, seq_length):
        """Create mask to prevent attending to future tokens."""
        mask = torch.triu(torch.ones(seq_length, seq_length), diagonal=1).bool()
        return ~mask  # Invert so 1 means "can attend"
    
    def parameter_count(self):
        """Count the number of parameters in the model."""
        return sum(p.numel() for p in self.parameters() if p.requires_grad)

class TransformerBlock(nn.Module):
    def __init__(self, hidden_size, num_heads, intermediate_size, dropout=0.1):
        super().__init__()
        # Pre-attention layer norm (Pre-LN architecture for stability)
        self.ln_1 = nn.LayerNorm(hidden_size)
        
        # Self-attention
        self.attn = MultiHeadAttention(hidden_size, num_heads, dropout)
        
        # Pre-FFN layer norm
        self.ln_2 = nn.LayerNorm(hidden_size)
        
        # Feed-forward network
        self.ffn = FeedForward(hidden_size, intermediate_size, dropout)
        
        # Dropout
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, attention_mask=None):
        # Pre-LN architecture: Apply layer norm before attention
        normalized_x = self.ln_1(x)
        attn_output = self.attn(normalized_x, attention_mask)
        x = x + self.dropout(attn_output)  # Residual connection
        
        # Apply layer norm before FFN
        normalized_x = self.ln_2(x)
        ffn_output = self.ffn(normalized_x)
        x = x + self.dropout(ffn_output)  # Residual connection
        
        return x

class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_size, num_heads, dropout=0.1):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.head_size = hidden_size // num_heads
        
        assert self.head_size * num_heads == hidden_size, "hidden_size must be divisible by num_heads"
        
        # Create query, key, value projections for all heads in a single projection
        self.query = nn.Linear(hidden_size, hidden_size)
        self.key = nn.Linear(hidden_size, hidden_size)
        self.value = nn.Linear(hidden_size, hidden_size)
        
        # Output projection
        self.output = nn.Linear(hidden_size, hidden_size)
        
        # Dropout
        self.dropout = nn.Dropout(dropout)
        
    def split_heads(self, x):
        """Split the last dimension into (num_heads, head_size)."""
        batch_size, seq_length, hidden_size = x.size()
        return x.view(batch_size, seq_length, self.num_heads, self.head_size).transpose(1, 2)
    
    def merge_heads(self, x):
        """Merge the (num_heads, head_size) back to hidden_size."""
        batch_size, num_heads, seq_length, head_size = x.size()
        return x.transpose(1, 2).reshape(batch_size, seq_length, num_heads * head_size)
    
    def forward(self, x, mask=None):
        batch_size, seq_length, _ = x.size()
        
        # Linear projections and split heads
        q = self.split_heads(self.query(x))  # (batch_size, num_heads, seq_length, head_size)
        k = self.split_heads(self.key(x))    # (batch_size, num_heads, seq_length, head_size)
        v = self.split_heads(self.value(x))  # (batch_size, num_heads, seq_length, head_size)
        
        # Scaled dot-product attention
        scale = math.sqrt(self.head_size)
        scores = torch.matmul(q, k.transpose(-2, -1)) / scale  # (batch_size, num_heads, seq_length, seq_length)
        
        # Apply mask if provided
        if mask is not None:
            # Expand mask to account for batch and num_heads dimensions
            expanded_mask = mask.unsqueeze(0).unsqueeze(0)  # (1, 1, seq_length, seq_length)
            scores = scores.masked_fill(~expanded_mask, -1e10)
        
        # Apply softmax and dropout
        attention_weights = F.softmax(scores, dim=-1)
        attention_weights = self.dropout(attention_weights)
        
        # Apply attention to values
        context = torch.matmul(attention_weights, v)  # (batch_size, num_heads, seq_length, head_size)
        
        # Merge heads and apply output projection
        context = self.merge_heads(context)  # (batch_size, seq_length, hidden_size)
        output = self.output(context)
        
        return output

class FeedForward(nn.Module):
    def __init__(self, hidden_size, intermediate_size, dropout=0.1):
        super().__init__()
        self.fc1 = nn.Linear(hidden_size, intermediate_size)
        self.fc2 = nn.Linear(intermediate_size, hidden_size)
        self.dropout = nn.Dropout(dropout)
        self.gelu = nn.GELU()
        
    def forward(self, x):
        x = self.fc1(x)
        x = self.gelu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        return x
```

#### Training Script

Here's a training script that incorporates mixed precision, gradient accumulation, and learning rate scheduling:

```python
import os
import time
import math
import torch
import torch.nn as nn
import torch.optim as optim
import torch.distributed as dist
from torch.utils.data import DataLoader
from torch.cuda.amp import autocast, GradScaler
from torch.utils.tensorboard import SummaryWriter
import numpy as np

def train_model(model, train_dataset, val_dataset, args):
    """Train a mid-scale language model with advanced techniques."""
    
    # Initialize distributed training if needed
    if args.distributed:
        dist.init_process_group(backend='nccl')
        local_rank = int(os.environ.get('LOCAL_RANK', 0))
        torch.cuda.set_device(local_rank)
        device = torch.device('cuda', local_rank)
        world_size = dist.get_world_size()
    else:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        local_rank = 0
        world_size = 1
    
    # Move model to device
    model = model.to(device)
    
    # Wrap with DDP if distributed
    if args.distributed:
        model = nn.parallel.DistributedDataParallel(
            model, device_ids=[local_rank], output_device=local_rank
        )
    
    # Create data loaders
    train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset) if args.distributed else None
    train_loader = DataLoader(
        train_dataset,
        batch_size=args.batch_size_per_gpu,
        shuffle=(train_sampler is None),
        sampler=train_sampler,
        num_workers=args.num_workers,
        pin_memory=True
    )
    
    val_loader = DataLoader(
        val_dataset,
        batch_size=args.batch_size_per_gpu,
        shuffle=False,
        num_workers=args.num_workers,
        pin_memory=True
    )
    
    # Set up optimizer
    optimizer = optim.AdamW(
        model.parameters(),
        lr=args.learning_rate,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=args.weight_decay
    )
    
    # Create learning rate scheduler
    total_steps = len(train_loader) * args.epochs // args.gradient_accumulation_steps
    warmup_steps = int(total_steps * args.warmup_ratio)
    
    lr_scheduler = get_cosine_schedule_with_warmup(
        optimizer,
        num_warmup_steps=warmup_steps,
        num_training_steps=total_steps
    )
    
    # Set up mixed precision training
    scaler = GradScaler() if args.fp16 else None
    
    # TensorBoard logging
    if local_rank == 0:
        writer = SummaryWriter(args.output_dir)
    
    # Training loop
    global_step = 0
    best_val_loss = float('inf')
    
    for epoch in range(args.epochs):
        if train_sampler:
            train_sampler.set_epoch(epoch)
        
        model.train()
        epoch_loss = 0
        epoch_start_time = time.time()
        
        for step, batch in enumerate(train_loader):
            # Move batch to device
            input_ids = batch[:, :-1].to(device)  # All but last token
            labels = batch[:, 1:].to(device)      # All but first token
            
            # Forward pass with mixed precision
            with autocast(enabled=args.fp16):
                logits = model(input_ids)
                # Calculate loss
                loss = F.cross_entropy(
                    logits.view(-1, logits.size(-1)), 
                    labels.view(-1),
                    ignore_index=-100  # Ignore padding tokens
                )
                
                # Scale loss by gradient accumulation steps
                loss = loss / args.gradient_accumulation_steps
            
            # Backward pass with gradient scaling
            if args.fp16:
                scaler.scale(loss).backward()
            else:
                loss.backward()
                
            # Update weights if we've accumulated enough gradients
            if (step + 1) % args.gradient_accumulation_steps == 0:
                if args.fp16:
                    # Unscale before gradient clipping
                    scaler.unscale_(optimizer)
                    # Clip gradients
                    torch.nn.utils.clip_grad_norm_(model.parameters(), args.max_grad_norm)
                    # Update weights with scaler
                    scaler.step(optimizer)
                    scaler.update()
                else:
                    # Clip gradients
                    torch.nn.utils.clip_grad_norm_(model.parameters(), args.max_grad_norm)
                    # Update weights
                    optimizer.step()
                
                # Update learning rate
                lr_scheduler.step()
                
                # Zero gradients
                optimizer.zero_grad()
                
                global_step += 1
                
                # Log progress
                if local_rank == 0 and global_step % args.log_steps == 0:
                    writer.add_scalar('train/loss', loss.item() * args.gradient_accumulation_steps, global_step)
                    writer.add_scalar('train/lr', lr_scheduler.get_last_lr()[0], global_step)
                    print(f"Epoch {epoch+1}/{args.epochs}, Step {global_step}, Loss: {loss.item() * args.gradient_accumulation_steps:.4f}")
            
            epoch_loss += loss.item() * args.gradient_accumulation_steps
        
        # End of epoch processing
        epoch_loss /= len(train_loader)
        epoch_time = time.time() - epoch_start_time
        
        # Validation
        model.eval()
        val_loss = 0
        
        with torch.no_grad():
            for batch in val_loader:
                input_ids = batch[:, :-1].to(device)
                labels = batch[:, 1:].to(device)
                
                with autocast(enabled=args.fp16):
                    logits = model(input_ids)
                    loss = F.cross_entropy(
                        logits.view(-1, logits.size(-1)), 
                        labels.view(-1),
                        ignore_index=-100
                    )
                
                val_loss += loss.item()
        
        val_loss /= len(val_loader)
        
        # Log validation results
        if local_rank == 0:
            writer.add_scalar('val/loss', val_loss, global_step)
            print(f"Epoch {epoch+1}/{args.epochs}, Validation Loss: {val_loss:.4f}, Time: {epoch_time:.2f}s")
            
            # Save checkpoint if validation improved
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                if hasattr(model, 'module'):
                    # Distributed training case
                    torch.save(model.module.state_dict(), os.path.join(args.output_dir, "best_model.pt"))
                else:
                    torch.save(model.state_dict(), os.path.join(args.output_dir, "best_model.pt"))
                print(f"New best model saved with validation loss: {best_val_loss:.4f}")
        
        # Save regular checkpoint
        if local_rank == 0 and (epoch + 1) % args.save_every == 0:
            checkpoint = {
                'epoch': epoch + 1,
                'global_step': global_step,
                'model_state_dict': model.module.state_dict() if hasattr(model, 'module') else model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'scheduler_state_dict': lr_scheduler.state_dict(),
                'best_val_loss': best_val_loss
            }
            torch.save(checkpoint, os.path.join(args.output_dir, f"checkpoint_epoch_{epoch+1}.pt"))
    
    # Final cleanup
    if args.distributed:
        dist.destroy_process_group()
    
    if local_rank == 0:
        writer.close()
    
    return model

def get_cosine_schedule_with_warmup(optimizer, num_warmup_steps, num_training_steps, min_lr_ratio=0.1):
    """Create a schedule with a learning rate that decreases with a warmup followed by cosine decay."""
    def lr_lambda(current_step):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1, num_warmup_steps))
        progress = float(current_step - num_warmup_steps) / float(max(1, num_training_steps - num_warmup_steps))
        return max(min_lr_ratio, 0.5 * (1.0 + math.cos(math.pi * progress)))
    
    return torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)
```

#### Text Generation

Once our model is trained, we can use it to generate text:

```python
def generate_text(model, tokenizer, prompt, max_length=100, temperature=0.8, top_k=50, top_p=0.95):
    """Generate text using various sampling strategies."""
    model.eval()
    device = next(model.parameters()).device
    
    # Tokenize the prompt
    input_ids = tokenizer.encode(prompt)
    input_ids = torch.tensor([input_ids]).to(device)
    
    # Keep track of generated tokens
    generated = input_ids.clone()
    
    with torch.no_grad():
        for _ in range(max_length):
            # Forward pass
            logits = model(generated)
            
            # Get logits for the next token
            next_token_logits = logits[:, -1, :] / temperature
            
            # Optional: Apply exponential penalty to already generated tokens
            for token_id in set(generated[0].tolist()):
                next_token_logits[0, token_id] /= 1.2
            
            # Apply top-k filtering
            if top_k > 0:
                indices_to_remove = next_token_logits < torch.topk(next_token_logits, top_k)[0][..., -1, None]
                next_token_logits[indices_to_remove] = -float("Inf")
            
            # Apply top-p (nucleus) filtering
            if top_p < 1.0:
                sorted_logits, sorted_indices = torch.sort(next_token_logits, descending=True)
                cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
                
                # Remove tokens with cumulative probability above the threshold
                sorted_indices_to_remove = cumulative_probs > top_p
                # Shift the indices to the right to keep also the first token above the threshold
                sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
                sorted_indices_to_remove[..., 0] = 0
                
                indices_to_remove = sorted_indices[sorted_indices_to_remove]
                next_token_logits[0, indices_to_remove] = -float("Inf")
            
            # Sample from the filtered distribution
            probs = F.softmax(next_token_logits, dim=-1)
            next_token = torch.multinomial(probs, num_samples=1)
            
            # Append to generated
            generated = torch.cat((generated, next_token), dim=1)
            
            # Stop if we generate an EOS token
            if next_token.item() == tokenizer.eos_token_id:
                break
    
    # Decode the generated text
    generated_text = tokenizer.decode(generated[0].tolist())
    
    return generated_text
```

---

### 5.8 Key Takeaways from Module 5

Let's summarize what we've learned in this module:

1. **Scaling Laws**: Model performance follows predictable patterns as we increase model size, dataset size, and compute resources. These scaling laws guide efficient resource allocation.
    
2. **Training Dynamics**: As models grow larger, their training dynamics change, requiring specialized optimization techniques like warmup scheduling, mixed precision, and gradient accumulation.
    
3. **Architecture Considerations**: Modern LLMs use architectures optimized for parameter efficiency, including pre-layernorm transformers, parameter sharing, and mixture of experts.
    
4. **Distributed Training**: Training large models requires sophisticated parallelism strategies, including data parallelism, pipeline parallelism, and tensor parallelism.
    
5. **Data Management**: High-quality training data requires careful curation, filtering, and efficient loading pipelines to handle terabyte-scale datasets.
    
6. **Emergent Abilities**: Perhaps most fascinatingly, as models scale, they develop new capabilities that weren't explicitly programmed, with performance discontinuities at certain scale thresholds.
    
7. **Practical Constraints**: Training truly large models requires balancing theoretical ideals with practical constraints around compute availability, memory limitations, and training time.
    

The journey from transformers to LLMs is largely a story of scale and the engineering required to achieve it. By understanding these principles, you can make informed decisions about model architecture, training configuration, and resource allocation.

---

### 5.9 Practice Exercises

To reinforce your learning from this module, try these exercises:

1. **Scaling Experiments**:
    
    - Train the same model architecture with different parameter counts (e.g., by changing hidden size)
    - Plot the relationship between parameter count and validation loss
    - Verify if it follows the predicted scaling laws
2. **Mixed Precision Implementation**:
    
    - Modify a simple transformer training loop to use mixed precision
    - Compare training speed and memory usage with and without mixed precision
    - Verify that final model quality is not compromised
3. **Distributed Data Parallelism**:
    
    - Set up a small cluster (even on a single machine with multiple GPUs)
    - Implement distributed data parallel training using PyTorch's DistributedDataParallel
    - Measure scaling efficiency as you add more GPUs
4. **Dataset Construction**:
    
    - Create a data processing pipeline for a large text corpus
    - Implement efficient tokenization, filtering, and chunking
    - Test its throughput to ensure it doesn't become a bottleneck during training
5. **Advanced Challenge - Pipeline Parallelism**:
    
    - Implement a simple version of pipeline parallelism for a transformer model
    - Split the model across multiple GPUs by layer
    - Create a microbatch scheduling system to maximize GPU utilization

---

### 5.10 Preview of Module 6 - Transfer Learning and Fine-tuning

Having explored how to scale up language models, our next module will focus on how to adapt pre-trained models for specific tasks and domains. In Module 6, we'll cover:

1. **Transfer Learning Fundamentals**: How to leverage pre-trained models for new tasks
2. **Full Fine-tuning**: Updating all parameters for downstream tasks
3. **Parameter-Efficient Fine-tuning**: Techniques like LoRA, adapters, and prompt tuning
4. **Task-Specific Adaptations**: Optimizing models for classification, generation, and more
5. **Domain Adaptation**: Specializing models for particular domains or styles
6. **Preventing Catastrophic Forgetting**: Maintaining general capabilities while specializing
7. **Quantization and Efficient Inference**: Deploying fine-tuned models efficiently

By the end of Module 6, you'll have a comprehensive understanding of how to take large pre-trained models and efficiently adapt them for specific applications, which is the most practical approach to using LLMs in most real-world scenarios.

---

## Module 6 - Transfer Learning and Fine-tuning

Welcome to Module 6 of our LLM crash course! In the previous module, we explored how to scale up language models to create truly powerful AI systems. We learned about scaling laws, distributed training, and the engineering challenges of building large models.

However, training models from scratch requires enormous computational resources that most individuals and organizations simply don't have. The good news is that we don't need to train our own models from scratch. Instead, we can leverage pre-trained models and adapt them to our specific needs - a process called transfer learning.

In this module, we'll explore how to take existing large language models and fine-tune them for specific tasks, domains, and applications. We'll learn both traditional fine-tuning approaches and cutting-edge parameter-efficient techniques that make fine-tuning accessible even with limited resources.

- [[6.1 Transfer Learning Fundamentals]]
- [[6.2 Full Fine-tuning]]
- [[6.3 Parameter-Efficient Fine-tuning Methods]]
- [[6.4 Task-Specific Adaptations]]
- [[6.5 Domain Adaptation]]
- [[6.6 Evaluating Fine-tuned Models]]
- [[6.7 Preventing Catastrophic Forgetting]]
- [[6.8 Quantization and Efficient Inference]]
- [[6.9 Hands-On Project - Fine-tuning a Model for a Specialized Task]]
- [[6.10 Key Takeaways from Module 6]]
- [[6.11 Practice Exercises]]
- [[6.12 Preview of Module 7 - Prompt Engineering and In-context Learning]]

---

### 6.1 Transfer Learning Fundamentals

#### What is Transfer Learning?

Transfer learning is the process of taking knowledge learned in one context and applying it to a different but related context. In the case of LLMs, this typically means:

1. Starting with a model pre-trained on a vast corpus of general text
2. Adapting this model to perform well on a specific task or domain

This approach leverages the fact that pre-trained models have already learned rich representations of language, including grammar, facts, and even reasoning capabilities. We can then fine-tune these models with much less data and compute than would be required for training from scratch.

#### Why Transfer Learning Works for Language Models

To understand why transfer learning works so well for language models, let's think about what these models learn during pre-training:

##### Layer-by-Layer Understanding

Language models learn different types of knowledge at different layers:

1. **Lower layers**: Capture syntactic patterns, basic grammar, and word relationships
2. **Middle layers**: Encode semantic meaning and contextual relationships
3. **Higher layers**: Represent more abstract knowledge and task-specific capabilities

When we fine-tune, we're effectively preserving the foundational knowledge in the lower and middle layers while adjusting the higher layers to specialize in our target task.

##### Foundation + Specialization

Think of pre-trained LLMs as having two components:

1. **Foundation**: General knowledge about language, facts, and reasoning
2. **Task alignment**: Specific capabilities for particular tasks

Pre-training builds the foundation, while fine-tuning aligns the model with specific tasks.

#### The Pre-training/Fine-tuning Paradigm

The standard approach to leveraging transfer learning with LLMs follows this pattern:

1. **Pre-training**: Train a large model on a diverse corpus using self-supervised objectives (like next-token prediction)
2. **Fine-tuning**: Adapt the pre-trained model to specific downstream tasks using labeled data

This paradigm has become dominant because:

- Pre-training is compute-intensive but needs to be done only once
- Fine-tuning is relatively efficient and can be done many times for different tasks
- The resulting models often perform better than those trained from scratch on the target task alone

#### What Happens During Fine-tuning?

During fine-tuning, several important things occur:

1. **Weight adjustment**: The model's parameters are updated to minimize loss on the target task
2. **Knowledge retention**: The model maintains much of its general knowledge
3. **Task specialization**: The model becomes better at the specific task
4. **Distribution shift**: The model adapts to the distribution of the fine-tuning data

The key insight is that while the weights change, they don't change dramatically - they're "fine-tuned" rather than completely relearned. This preserves the valuable knowledge from pre-training.

#### When to Fine-tune vs. When to Use Prompting

Not all use cases require fine-tuning. Here's a general guideline:

**Consider fine-tuning when**:

- You have a specific, well-defined task
- You have a moderate amount of high-quality labeled data (hundreds to thousands of examples)
- The task requires consistent, reliable outputs
- The task differs significantly from the model's pre-trained capabilities
- You need optimal performance and efficiency

**Consider prompting when**:

- You need flexibility across diverse tasks
- You have very few examples (0-100)
- The task is well-aligned with the model's existing capabilities
- You're exploring or prototyping solutions
- You don't have resources for fine-tuning

In practice, these approaches are complementary - you might use prompt engineering for exploration and initial development, then move to fine-tuning for production systems.

#### Limitations and Considerations

While transfer learning with LLMs is powerful, it has some important limitations:

1. **Bias amplification**: Fine-tuning can amplify biases present in either the pre-trained model or fine-tuning data
2. **Catastrophic forgetting**: Models can "forget" general capabilities when fine-tuned too aggressively
3. **Overfitting**: With small fine-tuning datasets, models can easily memorize rather than generalize
4. **Distribution mismatch**: If your fine-tuning data differs dramatically from the pre-training data, results may be unpredictable

We'll address strategies for mitigating these issues throughout this module.

---

### 6.2 Full Fine-tuning

Full fine-tuning is the most straightforward approach to transfer learning with LLMs. In this approach, we update all parameters of the pre-trained model using our task-specific data.

#### The Full Fine-tuning Process

Let's walk through the complete process of full fine-tuning:

##### 1. Preparing Your Dataset

The first step is to prepare a high-quality dataset for your target task. This typically involves:

- **Data collection**: Gathering examples relevant to your task
- **Preprocessing**: Cleaning and formatting the text
- **Tokenization**: Converting text to the format expected by the model
- **Train/validation split**: Creating separate sets for training and evaluation

For supervised fine-tuning, each example usually consists of an input text and a target output. However, the exact format depends on your task.

##### 2. Configuring the Pre-trained Model

Next, we load a pre-trained model and configure it for fine-tuning:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load pre-trained model and tokenizer
model_name = "gpt2-medium"  # Or any other pre-trained model
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Configure tokenizer and model for your task
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.pad_token_id
```

##### 3. Setting Up Fine-tuning Hyperparameters

Fine-tuning requires careful selection of hyperparameters:

```python
training_args = {
    "learning_rate": 5e-5,  # Typically lower than for training from scratch
    "num_train_epochs": 3,
    "per_device_train_batch_size": 4,
    "gradient_accumulation_steps": 8,  # Effectively increases batch size
    "warmup_steps": 500,
    "weight_decay": 0.01,
    "logging_steps": 100,
    "evaluation_strategy": "steps",
    "save_strategy": "steps",
    "fp16": True,  # Mixed precision training
    "max_grad_norm": 1.0,  # Gradient clipping
}
```

Some key considerations for hyperparameters:

- **Learning rate**: Usually much lower than for training from scratch (1e-5 to 5e-5)
- **Batch size**: Often smaller due to memory constraints (but can use gradient accumulation)
- **Training epochs**: Fewer epochs (2-5) to prevent overfitting
- **Weight decay**: Helps prevent overfitting (0.01 is a common value)

##### 4. Training Loop

The training process involves:

```python
from transformers import Trainer, TrainingArguments

# Set up training arguments
args = TrainingArguments(
    output_dir="./results",
    **training_args
)

# Create trainer
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
)

# Run training
trainer.train()

# Save the model
trainer.save_model("./fine-tuned-model")
```

##### 5. Evaluation and Iteration

After fine-tuning, we evaluate the model's performance:

```python
# Evaluate on validation set
metrics = trainer.evaluate()
print(f"Validation loss: {metrics['eval_loss']:.4f}")

# Try the model on some examples
input_text = "Your test input here"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs, max_length=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

Based on the evaluation, we might adjust hyperparameters and repeat the process.

#### Example: Fine-tuning for Sentiment Analysis

Let's look at a concrete example of fine-tuning for a specific task - sentiment analysis.

```python
import torch
import pandas as pd
from datasets import Dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments

# 1. Prepare data
df = pd.read_csv("sentiment_data.csv")
dataset = Dataset.from_pandas(df)

# Split into train and validation
dataset = dataset.train_test_split(test_size=0.1)

# 2. Load pre-trained model and tokenizer
model_name = "distilbert-base-uncased"
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, 
    num_labels=3  # For positive, negative, neutral
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 3. Preprocess data
def tokenize_function(examples):
    return tokenizer(
        examples["text"], 
        padding="max_length",
        truncation=True,
        max_length=128
    )

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# 4. Set up training arguments
training_args = TrainingArguments(
    output_dir="./sentiment-model",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)

# 5. Train the model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    tokenizer=tokenizer,
)

trainer.train()

# 6. Save the model
trainer.save_model("./sentiment-model-final")

# 7. Evaluate on an example
test_text = "I absolutely loved this product, it exceeded all my expectations!"
inputs = tokenizer(test_text, return_tensors="pt", padding=True, truncation=True)
outputs = model(**inputs)
predictions = torch.softmax(outputs.logits, dim=1)
print(f"Positive: {predictions[0][0]:.4f}, Neutral: {predictions[0][1]:.4f}, Negative: {predictions[0][2]:.4f}")
```

#### Advantages of Full Fine-tuning

Full fine-tuning offers several benefits:

1. **Optimal performance**: Generally achieves the best possible performance for a given task
2. **Complete adaptation**: All layers can adapt to the target domain and task
3. **Established process**: Well-understood with extensive research and tooling
4. **Flexibility**: Works for a wide range of tasks and model architectures

#### Challenges and Limitations

Despite its effectiveness, full fine-tuning has significant drawbacks:

1. **Computational requirements**: Fine-tuning large models needs substantial GPU memory
2. **Storage needs**: Each fine-tuned model requires storing a complete copy
3. **Risk of overfitting**: Especially with small datasets
4. **Catastrophic forgetting**: The model may lose general capabilities
5. **Difficult to merge**: Combining multiple fine-tuned models is challenging

These limitations have motivated the development of parameter-efficient fine-tuning methods, which we'll explore next.

---

### 6.3 Parameter-Efficient Fine-tuning Methods

As language models grow larger, full fine-tuning becomes increasingly impractical. Parameter-efficient fine-tuning (PEFT) methods address this by updating only a small subset of parameters or introducing a small number of new parameters.

These approaches offer several benefits:

1. **Lower memory requirements**: Often reducing memory needs by 90%+ during training
2. **Faster training**: Fewer parameters to update means faster iterations
3. **Better generalization**: Often less prone to overfitting on small datasets
4. **Storage efficiency**: The fine-tuned components are much smaller than the full model
5. **Modularity**: Easier to combine multiple fine-tuned models

Let's explore the most important PEFT techniques.

#### Adapter-Based Methods

Adapters insert small trainable modules into the pre-trained model while keeping the original parameters frozen.

##### How Adapters Work

1. **Architecture**: Typically a down-projection, followed by a non-linearity, then an up-projection
2. **Placement**: Usually after attention and/or feed-forward blocks in each layer
3. **Size**: Contain far fewer parameters than the original layers (reduction factor r, typically 8-64)

```python
class Adapter(nn.Module):
    def __init__(self, hidden_size, adapter_size, adapter_dropout=0.1):
        super().__init__()
        self.down_project = nn.Linear(hidden_size, adapter_size)
        self.activation = nn.GELU()
        self.up_project = nn.Linear(adapter_size, hidden_size)
        self.dropout = nn.Dropout(adapter_dropout)
        self.layer_norm = nn.LayerNorm(hidden_size)
        
    def forward(self, hidden_states):
        residual = hidden_states
        hidden_states = self.layer_norm(hidden_states)
        hidden_states = self.down_project(hidden_states)
        hidden_states = self.activation(hidden_states)
        hidden_states = self.up_project(hidden_states)
        hidden_states = self.dropout(hidden_states)
        return hidden_states + residual
```

##### Implementation Example with Transformers Library

```python
from transformers import AutoModelForCausalLM
from peft import get_peft_model, AdapterConfig

# Load pre-trained model
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Configure adapters
peft_config = AdapterConfig(
    r=16,  # Reduction factor
    lora_alpha=16,
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM"
)

# Get PEFT model for fine-tuning
peft_model = get_peft_model(model, peft_config)

# Check trainable parameters
trainable_params = sum(p.numel() for p in peft_model.parameters() if p.requires_grad)
total_params = sum(p.numel() for p in peft_model.parameters())
print(f"Trainable parameters: {trainable_params} ({trainable_params/total_params:.2%} of total)")
```

#### LoRA: Low-Rank Adaptation

LoRA is one of the most popular PEFT methods. It approximates the weight updates during fine-tuning using low-rank matrices.

##### How LoRA Works

1. **Key insight**: Weight updates during fine-tuning often have low "intrinsic rank"
2. **Implementation**: Decomposes weight updates into pairs of low-rank matrices (A×B)
3. **Application**: Usually applied to query and value projection matrices in attention
4. **Training**: Only the low-rank matrices are trained, original weights remain frozen

```python
class LoRALayer(nn.Module):
    def __init__(self, base_layer, rank=8, alpha=16):
        super().__init__()
        self.base_layer = base_layer
        self.rank = rank
        self.alpha = alpha
        
        # Initialize A with random values and B with zeros
        self.lora_A = nn.Parameter(torch.randn(base_layer.in_features, rank) * 0.01)
        self.lora_B = nn.Parameter(torch.zeros(rank, base_layer.out_features))
        
        # Freeze original weights
        for param in self.base_layer.parameters():
            param.requires_grad = False
            
    def forward(self, x):
        # Regular forward pass
        base_output = self.base_layer(x)
        
        # Add LoRA contribution, scaled by alpha/rank
        lora_output = (x @ self.lora_A) @ self.lora_B
        scaling = self.alpha / self.rank
        
        return base_output + scaling * lora_output
```

##### LoRA Implementation with PEFT Library

```python
from transformers import AutoModelForCausalLM
from peft import get_peft_model, LoraConfig, TaskType

# Load pre-trained model
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Configure LoRA
peft_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,  # Rank
    lora_alpha=16,  # Alpha scaling
    lora_dropout=0.1,
    target_modules=["q_proj", "v_proj"]  # Apply only to query and value projections
)

# Create PEFT model
peft_model = get_peft_model(model, peft_config)

# Check parameter count
trainable_params = sum(p.numel() for p in peft_model.parameters() if p.requires_grad)
total_params = sum(p.numel() for p in peft_model.parameters())
print(f"Trainable params: {trainable_params} ({trainable_params/total_params:.2%} of total)")
```

#### Prompt Tuning and Prefix Tuning

These methods add trainable tokens to the input, leaving the entire model frozen.

##### Prompt Tuning

1. **Approach**: Prepends trainable continuous "soft prompt" embeddings to the input
2. **Training**: Only the soft prompt parameters are updated
3. **Advantages**: Extremely parameter-efficient, model can be completely frozen

```python
class PromptTuningModel(nn.Module):
    def __init__(self, base_model, tokenizer, num_virtual_tokens=20):
        super().__init__()
        self.base_model = base_model
        self.tokenizer = tokenizer
        self.num_virtual_tokens = num_virtual_tokens
        
        # Freeze the base model
        for param in self.base_model.parameters():
            param.requires_grad = False
            
        # Create trainable prompt embeddings
        self.prompt_embeddings = nn.Parameter(
            torch.randn(
                1, self.num_virtual_tokens, self.base_model.config.hidden_size
            )
        )
        
    def forward(self, input_ids, attention_mask=None, **kwargs):
        batch_size = input_ids.shape[0]
        
        # Get token embeddings from the model
        token_embeds = self.base_model.get_input_embeddings()(input_ids)
        
        # Expand prompt embeddings to batch size
        prompt_embeds = self.prompt_embeddings.expand(batch_size, -1, -1)
        
        # Concatenate prompt embeddings with token embeddings
        inputs_embeds = torch.cat([prompt_embeds, token_embeds], dim=1)
        
        # Adjust attention mask if provided
        if attention_mask is not None:
            prefix_mask = torch.ones(
                batch_size, self.num_virtual_tokens, device=attention_mask.device
            )
            attention_mask = torch.cat([prefix_mask, attention_mask], dim=1)
            
        # Forward pass with extended embeddings
        outputs = self.base_model(
            inputs_embeds=inputs_embeds,
            attention_mask=attention_mask,
            **kwargs
        )
        
        return outputs
```

##### Prefix Tuning

Prefix tuning is similar to prompt tuning but inserts trainable vectors at each layer of the model instead of just the input.

```python
class PrefixTuningModel(nn.Module):
    def __init__(self, base_model, prefix_length=20):
        super().__init__()
        self.base_model = base_model
        self.prefix_length = prefix_length
        
        # Freeze the base model
        for param in self.base_model.parameters():
            param.requires_grad = False
        
        # Get configuration
        config = self.base_model.config
        hidden_size = config.hidden_size
        num_layers = config.num_hidden_layers
        num_heads = config.num_attention_heads
        head_size = hidden_size // num_heads
        
        # Create trainable prefixes for each layer
        self.prefix_keys = nn.Parameter(
            torch.randn(num_layers, prefix_length, num_heads, head_size)
        )
        
        self.prefix_values = nn.Parameter(
            torch.randn(num_layers, prefix_length, num_heads, head_size)
        )
        
    def forward(self, input_ids, **kwargs):
        # Standard forward pass with modified attention
        # (implementation would hook into the attention mechanism)
        # This is a simplified sketch - actual implementation would depend on model architecture
        
        return self.base_model(input_ids, **kwargs)
```

#### QLoRA and Other Quantized Approaches

These methods combine quantization with parameter-efficient fine-tuning to further reduce memory requirements.

##### QLoRA

QLoRA quantizes the base model (typically to 4 or 8 bits) and then applies LoRA for fine-tuning. This dramatically reduces memory usage.

```python
from transformers import AutoModelForCausalLM
from peft import get_peft_model, LoraConfig, TaskType
import bitsandbytes as bnb

# Load pre-trained model in 4-bit quantization
model = AutoModelForCausalLM.from_pretrained(
    "llama-7b",
    load_in_4bit=True,
    quantization_config=BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4"
    )
)

# Configure LoRA
peft_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,
    lora_alpha=16,
    lora_dropout=0.1,
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"]
)

# Create PEFT model
peft_model = get_peft_model(model, peft_config)

# Check memory usage
from peft.utils import get_peft_model_state_dict
print(f"Size of fine-tuned adapters: {sum(p.numel() * p.element_size() for p in get_peft_model_state_dict(peft_model).values()) / (1024 * 1024):.2f} MB")
```

#### Comparison of PEFT Methods

To help you choose the right approach, here's a comparison:

|Method|Parameter Efficiency|Memory Usage|Performance|Flexibility|Ease of Use|
|---|---|---|---|---|---|
|Full Fine-tuning|Low|High|Excellent|High|Easy|
|Adapters|Medium|Medium|Very Good|Medium|Medium|
|LoRA|High|Low|Very Good|High|Easy|
|Prompt Tuning|Very High|Very Low|Good|Limited|Medium|
|QLoRA|Very High|Very Low|Very Good|High|Medium|

#### Choosing the Right PEFT Method

Consider these factors when selecting a PEFT approach:

1. **Available compute resources**: Limited GPU memory favors more efficient methods like QLoRA
2. **Dataset size**: Smaller datasets work better with more constrained methods like LoRA
3. **Task complexity**: Complex tasks may benefit from more expressive methods like adapters
4. **Deployment constraints**: Storage or latency requirements may favor certain approaches
5. **Multi-task requirements**: Need to switch between tasks favors modular approaches

For most users just getting started with fine-tuning, LoRA or QLoRA are excellent default choices, offering a good balance of efficiency, performance, and ease of use.

---

### 6.4 Task-Specific Adaptations

Different tasks require different approaches to fine-tuning. In this section, we'll explore how to adapt pre-trained models for various common tasks.

#### Classification Tasks

Text classification involves categorizing text into predefined classes (sentiment analysis, topic classification, etc.).

##### Approach for Classification

1. **Model architecture**: Add a classification head on top of the pre-trained model
2. **Loss function**: Cross-entropy loss
3. **Output format**: Probabilities across classes

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments

# Load pre-trained model with classification head
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", 
    num_labels=4  # Number of classes
)

# Prepare classification dataset
def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length")

# Training setup
training_args = TrainingArguments(
    output_dir="./classification-model",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    num_train_epochs=3,
    evaluation_strategy="epoch"
)

# Train model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_eval_dataset
)
trainer.train()
```

##### Handling Class Imbalance

When classes aren't equally represented:

```python
# Compute class weights
from sklearn.utils.class_weight import compute_class_weight
import numpy as np

labels = [example["label"] for example in train_dataset]
class_weights = compute_class_weight(
    class_weight="balanced",
    classes=np.unique(labels),
    y=labels
)

# Convert to tensor
class_weights = torch.tensor(class_weights, dtype=torch.float)

# Create weighted loss function
class WeightedLoss(nn.Module):
    def __init__(self, class_weights):
        super().__init__()
        self.class_weights = class_weights
        
    def forward(self, outputs, targets):
        return F.cross_entropy(
            outputs.view(-1, outputs.size(-1)), 
            targets.view(-1), 
            weight=self.class_weights.to(outputs.device)
        )

# Use in training
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_eval_dataset,
    compute_loss=WeightedLoss(class_weights)
)
```

#### Sequence Tagging Tasks

Sequence tagging assigns labels to individual tokens (named entity recognition, part-of-speech tagging, etc.).

##### Approach for Sequence Tagging

1. **Model architecture**: Use a token classification head
2. **Loss function**: Token-level cross-entropy loss
3. **Output format**: Label for each token

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer

# Load pre-trained model for token classification
model = AutoModelForTokenClassification.from_pretrained(
    "distilbert-base-uncased", 
    num_labels=9  # Number of NER tags (B-PER, I-PER, etc.)
)

# Prepare NER dataset
def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(
        examples["tokens"], 
        truncation=True, 
        is_split_into_words=True
    )
    labels = []
    
    for i, label in enumerate(examples["ner_tags"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        aligned_labels = []
        
        previous_word_id = None
        for word_id in word_ids:
            if word_id is None:
                aligned_labels.append(-100)  # Special tokens
            elif word_id != previous_word_id:
                aligned_labels.append(label[word_id])
            else:
                # For tokens that are part of the same word
                # Use either the same tag or a special tag
                aligned_labels.append(label[word_id])
            previous_word_id = word_id
            
        labels.append(aligned_labels)
    
    tokenized_inputs["labels"] = labels
    return tokenized_inputs
```

#### Text Generation Tasks

Text generation involves creating coherent text based on a prompt (story generation, text completion, etc.).

##### Approach for Text Generation

1. **Model architecture**: Decoder-only or encoder-decoder models
2. **Loss function**: Next-token prediction (causal language modeling)
3. **Output format**: Generated text sequence

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

# Load pre-trained model for causal language modeling
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token  # Set pad token

# Prepare generation dataset
def preprocess_function(examples):
    return tokenizer(
        examples["text"], 
        truncation=True, 
        padding="max_length",
        max_length=512
    )

# Training setup
training_args = TrainingArguments(
    output_dir="./generation-model",
    learning_rate=5e-5,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    num_train_epochs=3,
    evaluation_strategy="steps",
    eval_steps=500
)

# Train model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_eval_dataset,
    data_collator=lambda data: {'input_ids': torch.stack([x['input_ids'] for x in data]),
                              'attention_mask': torch.stack([x['attention_mask'] for x in data]),
                              'labels': torch.stack([x['input_ids'] for x in data])}
)
trainer.train()
```

#### Question Answering Tasks

Question answering extracts answers from a context given a question.

##### Approach for Extractive QA

1. **Model architecture**: Add span prediction head (start/end positions)
2. **Loss function**: Combined loss for start and end positions
3. **Output format**: Start and end indices for the answer span

```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

# Load pre-trained model for question answering
model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# Prepare QA dataset
def preprocess_function(examples):
    questions = [q.strip() for q in examples["question"]]
    contexts = [c.strip() for c in examples["context"]]
    
    # Tokenize questions and contexts together
    inputs = tokenizer(
        questions,
        contexts,
        truncation="only_second",
        max_length=384,
        stride=128,
        padding="max_length",
        return_overflowing_tokens=True,
        return_offsets_mapping=True
    )
    
    # Map token positions to character positions
    offset_mapping = inputs.pop("offset_mapping")
    
    # Get start and end positions
    start_positions = []
    end_positions = []
    
    for i, offset in enumerate(offset_mapping):
        sample_idx = inputs["overflow_to_sample_mapping"][i]
        answer = examples["answers"][sample_idx]
        
        start_char = answer["answer_start"][0]
        end_char = start_char + len(answer["text"][0])
        
        sequence_ids = inputs.sequence_ids(i)
        
        # Find token indices that contain the answer
        token_start_index = 0
        while sequence_ids[token_start_index] != 1:
            token_start_index += 1
            
        token_end_index = len(input_ids[i]) - 1
        while sequence_ids[token_end_index] != 1:
            token_end_index -= 1
            
        # If answer not fully contained in context, use cls token
        if (offset[token_start_index][0] > end_char or 
            offset[token_end_index][1] < start_char):
            start_positions.append(0)
            end_positions.append(0)
        else:
            # Find token containing start of answer
            while (token_start_index < len(offset) and 
                  offset[token_start_index][0] <= start_char):
                token_start_index += 1
            start_positions.append(token_start_index - 1)
            
            # Find token containing end of answer
            while offset[token_end_index][1] >= end_char:
                token_end_index -= 1
            end_positions.append(token_end_index + 1)
    
    inputs["start_positions"] = start_positions
    inputs["end_positions"] = end_positions
    return inputs
```

#### Summarization Tasks

Summarization condenses a longer text into a shorter one while preserving key information.

##### Approach for Summarization

1. **Model architecture**: Encoder-decoder models (e.g., T5, BART)
2. **Loss function**: Cross-entropy on output tokens
3. **Output format**: Generated summary text

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, Seq2SeqTrainer, Seq2SeqTrainingArguments

# Load pre-trained model for summarization
model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
tokenizer = AutoTokenizer.from_pretrained("t5-base")

# Prepare summarization dataset
def preprocess_function(examples):
    # For T5, prefix the task
    inputs = ["summarize: " + doc for doc in examples["document"]]
    
    # Tokenize inputs and targets
    model_inputs = tokenizer(
        inputs, 
        max_length=1024, 
        truncation=True,
        padding="max_length"
    )
    
    # Tokenize summaries
    labels = tokenizer(
        examples["summary"], 
        max_length=128, 
        truncation=True,
        padding="max_length"
    )
    
    # Set -100 for padding tokens
    labels["input_ids"] = [
        [(l if l != tokenizer.pad_token_id else -100) for l in label]
        for label in labels["input_ids"]
    ]
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Training setup
training_args = Seq2SeqTrainingArguments(
    output_dir="./summarization-model",
    learning_rate=3e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    gradient_accumulation_steps=4,
    num_train_epochs=4,
    evaluation_strategy="epoch",
    predict_with_generate=True,
    generation_max_length=128
)

# Train model
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_eval_dataset,
)
trainer.train()
```

#### Translation Tasks

Translation converts text from one language to another.

##### Approach for Translation

1. **Model architecture**: Encoder-decoder models
2. **Loss function**: Cross-entropy on output tokens
3. **Output format**: Translated text

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, Seq2SeqTrainer, Seq2SeqTrainingArguments

# Load pre-trained model for translation
model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
tokenizer = AutoTokenizer.from_pretrained("t5-base")

# Prepare translation dataset
def preprocess_function(examples):
    # For T5, prefix with the task
    inputs = ["translate English to French: " + en for en in examples["en"]]
    
    # Tokenize inputs and targets
    model_inputs = tokenizer(
        inputs, 
        max_length=512, 
        truncation=True,
        padding="max_length"
    )
    
    # Tokenize translations
    labels = tokenizer(
        examples["fr"], 
        max_length=512, 
        truncation=True,
        padding="max_length"
    )
    
    # Set -100 for padding tokens
    labels["input_ids"] = [
        [(l if l != tokenizer.pad_token_id else -100) for l in label]
        for label in labels["input_ids"]
    ]
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs
```

#### Task-Specific Best Practices

Across all tasks, certain best practices can help improve fine-tuning outcomes:

1. **Data quality over quantity**: A smaller, high-quality dataset often outperforms a larger, noisy one
2. **Task-specific preprocessing**: Adapt preprocessing to the specific requirements of your task
3. **Evaluation metrics**: Choose metrics that align with the end-use of the model
4. **Early stopping**: Monitor validation performance and stop when it plateaus
5. **Learning rate schedules**: Warm-up followed by decay often works well
6. **Task-specific generation parameters**: Tune generation hyperparameters (temperature, top-p, etc.) for your specific use case

By adapting these approaches to your specific needs, you can effectively fine-tune models for a wide range of NLP tasks.

---

### 6.5 Domain Adaptation

Domain adaptation involves fine-tuning a pre-trained model to perform well on data from a specific domain (medical, legal, scientific, etc.). The challenge is that these domains often have specialized terminology and linguistic patterns that differ from general language.

#### Why Domain Adaptation Matters

Pre-trained LLMs typically learn from broad web corpora, which may not adequately capture the nuances of specialized domains. Domain adaptation helps models:

1. Learn domain-specific vocabulary and terminology
2. Understand specialized discourse patterns
3. Incorporate domain knowledge
4. Reduce errors on domain-specific tasks

#### Continual Pre-training

The most common approach to domain adaptation is continual pre-training - continuing the pre-training process on domain-specific data before fine-tuning for specific tasks.

##### Implementation

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling

# Load pre-trained model
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

# Create data collator for language modeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, 
    mlm=False  # Causal language modeling, not masked
)

# Set up training arguments for domain adaptation
training_args = TrainingArguments(
    output_dir="./domain-adapted-model",
    learning_rate=1e-5,  # Lower learning rate for domain adaptation
    per_device_train_batch_size=4,
    gradient_accumulation_steps=8,
    num_train_epochs=2,
    save_strategy="steps",
    save_steps=1000,
    evaluation_strategy="steps",
    eval_steps=1000,
    weight_decay=0.01,
    warmup_steps=500,
    logging_steps=100,
)

# Train on domain-specific data
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=domain_train_dataset,
    eval_dataset=domain_val_dataset,
    data_collator=data_collator,
)
trainer.train()

# Save domain-adapted model
model.save_pretrained("./domain-adapted-model-final")
tokenizer.save_pretrained("./domain-adapted-model-final")
```

#### Domain-Specific Vocabulary

Many domains have specialized terminology not well-represented in standard tokenizers. Training a domain-adapted tokenizer can significantly improve performance.

##### Extending the Vocabulary

```python
from tokenizers import ByteLevelBPETokenizer

# Train a tokenizer on domain data
tokenizer = ByteLevelBPETokenizer()

# Train from scratch
tokenizer.train(
    files=domain_text_files,
    vocab_size=50000,
    min_frequency=2,
    special_tokens=["<s>", "</s>", "<unk>", "<pad>", "<mask>"]
)
tokenizer.save_model("./domain-tokenizer")

# Alternative: Extend existing tokenizer
from transformers import AutoTokenizer

base_tokenizer = AutoTokenizer.from_pretrained("gpt2")
domain_terms = ["oncogene", "carcinoma", "metastasis", "biopsy", "chemotherapy"]

# Add new tokens to the tokenizer
num_added = base_tokenizer.add_tokens(domain_terms)
print(f"Added {num_added} tokens to the vocabulary")

# Resize token embeddings in the model
model.resize_token_embeddings(len(base_tokenizer))
```

#### Effective Domain Adaptation Strategies

##### 1. Data Curation

The quality of domain-specific data is crucial:

```python
def curate_domain_corpus(texts, domain_terms, min_term_frequency=2):
    """Filter texts to ensure domain relevance."""
    relevant_texts = []
    
    for text in texts:
        # Count domain terms in the text
        domain_term_count = sum(text.lower().count(term.lower()) for term in domain_terms)
        
        # Select texts with sufficient domain terminology
        if domain_term_count >= min_term_frequency:
            relevant_texts.append(text)
            
    return relevant_texts
```

##### 2. Staged Adaptation

For best results, use a staged approach:

1. **General pre-training**: Start with a generally pre-trained model
2. **Domain pre-training**: Continue pre-training on domain corpus
3. **Task-specific fine-tuning**: Fine-tune for specific tasks within the domain

##### 3. Domain-Specific Evaluation

Create domain-specific evaluation benchmarks:

```python
def evaluate_domain_specificity(model, tokenizer, domain_test_set, general_test_set):
    """Compare performance on domain vs. general data."""
    # Evaluate on domain data
    domain_results = evaluate_perplexity(model, tokenizer, domain_test_set)
    
    # Evaluate on general data
    general_results = evaluate_perplexity(model, tokenizer, general_test_set)
    
    # Compare results
    print(f"Domain perplexity: {domain_results['perplexity']:.2f}")
    print(f"General perplexity: {general_results['perplexity']:.2f}")
    print(f"Domain specialization (ratio): {general_results['perplexity'] / domain_results['perplexity']:.2f}")
    
    return {
        "domain_perplexity": domain_results['perplexity'],
        "general_perplexity": general_results['perplexity'],
        "specialization_ratio": general_results['perplexity'] / domain_results['perplexity']
    }
```

#### Domain Adaptation with PEFT

For efficient domain adaptation, parameter-efficient methods work well:

```python
from transformers import AutoModelForCausalLM
from peft import get_peft_model, LoraConfig, TaskType

# Load pre-trained model
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Configure LoRA for domain adaptation
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,  # Higher rank for domain adaptation
    lora_alpha=32,
    lora_dropout=0.05,
    target_modules=["c_attn"]  # Target attention layers
)

# Create PEFT model
peft_model = get_peft_model(model, lora_config)

# Training setup for domain adaptation
training_args = TrainingArguments(
    output_dir="./lora-domain-adapter",
    learning_rate=2e-4,
    num_train_epochs=3,
    per_device_train_batch_size=8,
    save_strategy="epoch",
    evaluation_strategy="epoch"
)

# Train on domain data
trainer = Trainer(
    model=peft_model,
    args=training_args,
    train_dataset=domain_train_dataset,
    eval_dataset=domain_val_dataset,
    data_collator=data_collator
)
trainer.train()

# Save the adapter weights
peft_model.save_pretrained("./lora-domain-adapter")
```

#### Domain Adaptation for Specific Industries

Let's look at adaptation strategies for particular domains:

##### Medical Domain

Medical text has unique challenges:

```python
# Medical-specific preprocessing
def preprocess_medical_text(text):
    # Standardize medical abbreviations
    text = re.sub(r'\b(?:Dx|DX)\b', 'diagnosis', text)
    text = re.sub(r'\b(?:Tx|TX)\b', 'treatment', text)
    text = re.sub(r'\b(?:Hx|HX)\b', 'history', text)
    
    # Handle numeric expressions
    text = re.sub(r'(\d+)(-|\s)(\d+)\s*(?:mg|mcg|ml|g)', r'\1-\3 \4', text)
    
    # Remove PHI (Protected Health Information)
    text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[SSN]', text)  # SSN
    text = re.sub(r'\b\d{3}-\d{3}-\d{4}\b', '[PHONE]', text)  # Phone
    
    return text
```

##### Legal Domain

Legal text requires special handling:

```python
# Legal corpus weighting
def weight_legal_corpus(texts, categories):
    """Weight training examples by legal category."""
    weights = {
        "case_law": 0.3,
        "statutes": 0.3,
        "contracts": 0.2,
        "legal_memos": 0.1,
        "legal_briefs": 0.1
    }
    
    weighted_corpus = []
    for text, category in zip(texts, categories):
        # Duplicate examples according to weights
        num_copies = max(1, int(100 * weights.get(category, 0.1)))
        weighted_corpus.extend([text] * num_copies)
        
    return weighted_corpus
```

##### Technical Documentation

For technical domains like software documentation:

```python
# Extract and retain code blocks
def process_technical_docs(text):
    # Split into text and code segments
    segments = []
    code_pattern = r'```(?:[a-z]+)?\n(.*?)```'
    
    code_blocks = re.findall(code_pattern, text, re.DOTALL)
    
    # Replace code blocks with placeholders
    placeholder_text = re.sub(code_pattern, '[CODE_BLOCK]', text, flags=re.DOTALL)
    
    # Split text on placeholders
    text_segments = placeholder_text.split('[CODE_BLOCK]')
    
    # Interleave text and code
    for i in range(max(len(text_segments), len(code_blocks))):
        if i < len(text_segments):
            segments.append({"type": "text", "content": text_segments[i]})
        if i < len(code_blocks):
            segments.append({"type": "code", "content": code_blocks[i]})
    
    return segments
```

---

### 6.6 Evaluating Fine-tuned Models

Proper evaluation is crucial to determine if fine-tuning has improved model performance for your specific task and to compare different fine-tuning approaches.

#### Setting Up a Comprehensive Evaluation Framework

A good evaluation setup should:

1. Use separate validation and test sets
2. Include multiple metrics
3. Compare to relevant baselines
4. Test for specific capabilities and limitations

```python
def evaluate_model(model, tokenizer, test_dataset, task_type):
    """Comprehensive model evaluation for different task types."""
    
    results = {}
    
    # Common setup
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()
    
    if task_type == "classification":
        # Classification metrics
        all_predictions = []
        all_references = []
        
        # Create dataloader
        dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=16)
        
        with torch.no_grad():
            for batch in dataloader:
                inputs = {k: v.to(device) for k, v in batch.items() if k != "labels"}
                labels = batch["labels"].to(device)
                
                outputs = model(**inputs)
                logits = outputs.logits
                
                predictions = torch.argmax(logits, dim=-1)
                
                all_predictions.extend(predictions.cpu().numpy())
                all_references.extend(labels.cpu().numpy())
        
        # Calculate metrics
        from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
        
        results["accuracy"] = accuracy_score(all_references, all_predictions)
        results["f1"] = f1_score(all_references, all_predictions, average="weighted")
        results["precision"] = precision_score(all_references, all_predictions, average="weighted")
        results["recall"] = recall_score(all_references, all_predictions, average="weighted")
        
    elif task_type == "generation":
        # Generation metrics
        from rouge_score import rouge_scorer
        from nltk.translate.bleu_score import corpus_bleu
        import nltk
        nltk.download('punkt')
        
        scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
        
        all_generations = []
        all_references = []
        
        # Generate text for each prompt
        for example in test_dataset:
            input_text = example["prompt"]
            reference = example["completion"]
            
            inputs = tokenizer(input_text, return_tensors="pt").to(device)
            
            # Generate text
            output_ids = model.generate(
                inputs.input_ids,
                max_length=512,
                num_beams=5,
                early_stopping=True
            )
            
            generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
            
            all_generations.append(generated_text)
            all_references.append(reference)
        
        # Calculate ROUGE scores
        rouge1_sum = rouge2_sum = rougeL_sum = 0
        for gen, ref in zip(all_generations, all_references):
            scores = scorer.score(ref, gen)
            rouge1_sum += scores['rouge1'].fmeasure
            rouge2_sum += scores['rouge2'].fmeasure
            rougeL_sum += scores['rougeL'].fmeasure
        
        n_examples = len(all_generations)
        results["rouge1"] = rouge1_sum / n_examples
        results["rouge2"] = rouge2_sum / n_examples
        results["rougeL"] = rougeL_sum / n_examples
        
        # Calculate BLEU score
        references_tokenized = [[nltk.word_tokenize(ref)] for ref in all_references]
        generations_tokenized = [nltk.word_tokenize(gen) for gen in all_generations]
        
        bleu_score = corpus_bleu(references_tokenized, generations_tokenized)
        results["bleu"] = bleu_score
    
    # Add perplexity for any text generation model
    if hasattr(model, "compute_loss"):
        # Calculate perplexity
        total_loss = 0
        total_tokens = 0
        
        dataloader = torch.utils.data.DataLoader(
            test_dataset, 
            batch_size=4, 
            collate_fn=lambda data: {
                'input_ids': torch.stack([x['input_ids'] for x in data]),
                'attention_mask': torch.stack([x['attention_mask'] for x in data]),
                'labels': torch.stack([x['input_ids'] for x in data])
            }
        )
        
        with torch.no_grad():
            for batch in dataloader:
                inputs = {k: v.to(device) for k, v in batch.items()}
                outputs = model(**inputs)
                loss = outputs.loss
                
                total_loss += loss.item() * batch["input_ids"].size(1)
                total_tokens += (batch["attention_mask"].sum()).item()
        
        avg_loss = total_loss / total_tokens
        perplexity = math.exp(avg_loss)
        results["perplexity"] = perplexity
    
    return results
```

#### Task-Specific Evaluation Metrics

Different tasks require different evaluation approaches:

##### Classification Metrics

```python
def evaluate_classification(model, eval_dataset):
    # Standard metrics
    metrics = evaluate_model(model, tokenizer, eval_dataset, "classification")
    
    # Add confusion matrix
    from sklearn.metrics import confusion_matrix
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    # Get predictions
    predictions = []
    references = []
    for batch in eval_dataloader:
        inputs = {k: v.to(device) for k, v in batch.items() if k != "labels"}
        outputs = model(**inputs)
        preds = torch.argmax(outputs.logits, dim=-1)
        
        predictions.extend(preds.cpu().numpy())
        references.extend(batch["labels"].cpu().numpy())
    
    # Create confusion matrix
    cm = confusion_matrix(references, predictions)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.savefig('confusion_matrix.png')
    
    return metrics
```

##### Generation Metrics

```python
def evaluate_generation_quality(model, tokenizer, prompts, temperature=0.7):
    """Evaluate text generation quality."""
    model.eval()
    device = next(model.parameters()).device
    
    generations = []
    
    for prompt in prompts:
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
        # Generate with different settings
        outputs_greedy = model.generate(
            inputs.input_ids, 
            max_length=200,
            do_sample=False
        )
        
        outputs_sampling = model.generate(
            inputs.input_ids, 
            max_length=200,
            do_sample=True, 
            temperature=temperature, 
            top_p=0.92
        )
        
        text_greedy = tokenizer.decode(outputs_greedy[0], skip_special_tokens=True)
        text_sampling = tokenizer.decode(outputs_sampling[0], skip_special_tokens=True)
        
        generations.append({
            "prompt": prompt,
            "greedy": text_greedy,
            "sampling": text_sampling
        })
    
    # Human evaluation is recommended for generation quality
    return generations
```

##### Domain-Specific Evaluation

```python
def evaluate_domain_accuracy(model, tokenizer, domain_test_cases):
    """Evaluate accuracy on domain-specific knowledge."""
    model.eval()
    device = next(model.parameters()).device
    
    correct = 0
    total = len(domain_test_cases)
    
    results = []
    
    for case in domain_test_cases:
        question = case["question"]
        correct_answer = case["answer"]
        
        # Format as Q&A
        prompt = f"Question: {question}\nAnswer:"
        
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
        # Generate answer
        outputs = model.generate(
            inputs.input_ids,
            max_length=100,
            num_beams=3,
            early_stopping=True
        )
        
        # Extract generated answer
        generated_answer = tokenizer.decode(outputs[0][len(inputs.input_ids[0]):], skip_special_tokens=True).strip()
        
        # Check if answer is correct (exact match or contains correct answer)
        is_correct = correct_answer.lower() in generated_answer.lower()
        if is_correct:
            correct += 1
            
        results.append({
            "question": question,
            "correct_answer": correct_answer,
            "generated_answer": generated_answer,
            "is_correct": is_correct
        })
    
    accuracy = correct / total
    print(f"Domain knowledge accuracy: {accuracy:.2f} ({correct}/{total})")
    
    return {
        "accuracy": accuracy,
        "detailed_results": results
    }
```

#### Behavioral Evaluation

Beyond task performance, it's important to evaluate behavioral aspects of fine-tuned models:

```python
def evaluate_behavioral_changes(base_model, fine_tuned_model, tokenizer, test_cases):
    """Compare responses between base and fine-tuned models."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    base_model.to(device)
    fine_tuned_model.to(device)
    
    base_model.eval()
    fine_tuned_model.eval()
    
    results = []
    
    for case in test_cases:
        prompt = case["prompt"]
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
        # Generate from base model
        base_outputs = base_model.generate(
            inputs.input_ids,
            max_length=200,
            do_sample=True,
            temperature=0.7
        )
        
        # Generate from fine-tuned model
        ft_outputs = fine_tuned_model.generate(
            inputs.input_ids,
            max_length=200,
            do_sample=True,
            temperature=0.7
        )
        
        base_text = tokenizer.decode(base_outputs[0], skip_special_tokens=True)
        ft_text = tokenizer.decode(ft_outputs[0], skip_special_tokens=True)
        
        results.append({
            "prompt": prompt,
            "base_response": base_text,
            "fine_tuned_response": ft_text,
            "category": case["category"]
        })
    
    # Analyze results by category
    category_counts = {}
    for result in results:
        category = result["category"]
        if category not in category_counts:
            category_counts[category] = {"total": 0, "different": 0}
        
        category_counts[category]["total"] += 1
        
        # Simple difference check (could be more sophisticated)
        if result["base_response"] != result["fine_tuned_response"]:
            category_counts[category]["different"] += 1
    
    # Calculate difference percentages
    for category, counts in category_counts.items():
        diff_percent = counts["different"] / counts["total"] * 100
        print(f"Category '{category}': {diff_percent:.1f}% responses changed after fine-tuning")
    
    return results, category_counts
```

#### Comparison with Baselines

Always compare your fine-tuned model against relevant baselines:

```python
def compare_with_baselines(models, tokenizer, eval_dataset, task):
    """Compare multiple models on the same evaluation set."""
    results = {}
    
    for model_name, model in models.items():
        print(f"Evaluating model: {model_name}")
        model_results = evaluate_model(model, tokenizer, eval_dataset, task)
        results[model_name] = model_results
    
    # Print comparison table
    metrics = list(results[list(results.keys())[0]].keys())
    
    print("\nComparison Table:")
    header = "Model".ljust(20) + " | " + " | ".join(metric.ljust(12) for metric in metrics)
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    
    for model_name, model_results in results.items():
        row = model_name.ljust(20) + " | "
        row += " | ".join(f"{model_results[metric]:.4f}".ljust(12) for metric in metrics)
        print(row)
    
    print("-" * len(header))
    
    return results
```

#### Interpreting Evaluation Results

Beyond the raw numbers, it's important to understand what evaluation results mean:

```python
def analyze_evaluation_results(results, baseline_results):
    """Analyze and interpret evaluation results."""
    analysis = {}
    
    # Calculate improvements
    for metric, value in results.items():
        if metric in baseline_results:
            improvement = value - baseline_results[metric]
            percent_improvement = (improvement / baseline_results[metric]) * 100
            
            analysis[metric] = {
                "value": value,
                "baseline": baseline_results[metric],
                "absolute_improvement": improvement,
                "percent_improvement": percent_improvement
            }
    
    # Print analysis
    print("\nPerformance Analysis:")
    for metric, data in analysis.items():
        print(f"{metric}:")
        print(f"  Current: {data['value']:.4f}")
        print(f"  Baseline: {data['baseline']:.4f}")
        print(f"  Improvement: {data['absolute_improvement']:.4f} ({data['percent_improvement']:.2f}%)")
    
    # Overall assessment
    avg_improvement = sum(data["percent_improvement"] for data in analysis.values()) / len(analysis)
    print(f"\nAverage improvement: {avg_improvement:.2f}%")
    
    if avg_improvement > 15:
        overall = "Significant improvement"
    elif avg_improvement > 5:
        overall = "Moderate improvement"
    elif avg_improvement > 0:
        overall = "Slight improvement"
    else:
        overall = "No improvement or regression"
    
    print(f"Overall assessment: {overall}")
    
    return analysis
```

---

### 6.7 Preventing Catastrophic Forgetting

Catastrophic forgetting occurs when a model loses previously learned capabilities after fine-tuning on a new task. This is particularly problematic with LLMs, where we want to preserve general knowledge while adding specialized capabilities.

#### Understanding Catastrophic Forgetting

When we fine-tune a model, its parameters shift to optimize for the new task. If these shifts significantly alter the representations learned during pre-training, the model may "forget" capabilities not explicitly tested in the fine-tuning objective.

Common symptoms include:

1. Degraded performance on tasks unrelated to fine-tuning
2. Loss of factual knowledge
3. Reduced generalization capabilities
4. Over-specialization to the fine-tuning domain

#### Techniques to Mitigate Catastrophic Forgetting

##### 1. Regularization Methods

Elastic Weight Consolidation (EWC) penalizes changes to important parameters:

```python
class EWCLoss(nn.Module):
    def __init__(self, model, old_model, fisher_estimation_dataset, lambda_ewc=100):
        super().__init__()
        self.model = model
        self.old_model = old_model
        self.lambda_ewc = lambda_ewc
        
        # Store old parameters
        self.old_params = {name: param.clone().detach() 
                          for name, param in old_model.named_parameters()}
        
        # Estimate Fisher Information Matrix
        self.fisher = self._estimate_fisher(fisher_estimation_dataset)
        
    def _estimate_fisher(self, dataset):
        """Estimate Fisher Information Matrix."""
        fisher = {name: torch.zeros_like(param) 
                 for name, param in self.model.named_parameters()}
        
        self.model.eval()
        for batch in dataset:
            self.model.zero_grad()
            outputs = self.model(**batch)
            loss = outputs.loss
            loss.backward()
            
            for name, param in self.model.named_parameters():
                if param.grad is not None:
                    fisher[name] += param.grad.pow(2) / len(dataset)
        
        return fisher
    
    def forward(self, outputs, targets):
        # Standard task loss
        task_loss = F.cross_entropy(outputs, targets)
        
        # EWC regularization loss
        ewc_loss = 0
        for name, param in self.model.named_parameters():
            if name in self.fisher and name in self.old_params:
                ewc_loss += torch.sum(self.fisher[name] * (param - self.old_params[name]).pow(2))
        
        # Combined loss
        loss = task_loss + self.lambda_ewc * ewc_loss
        
        return loss
```

##### 2. Replay Methods

Interleave examples from the pre-training or previous tasks:

```python
def create_mixed_dataset(new_task_dataset, general_capability_dataset, mix_ratio=0.2):
    """Create a mixed dataset with examples from both tasks."""
    
    # Determine how many general examples to include
    num_general_examples = int(len(new_task_dataset) * mix_ratio / (1 - mix_ratio))
    
    # Select samples from general dataset
    if len(general_capability_dataset) > num_general_examples:
        general_samples = random.sample(list(general_capability_dataset), num_general_examples)
    else:
        general_samples = list(general_capability_dataset)
    
    # Combine datasets
    mixed_dataset = list(new_task_dataset) + general_samples
    random.shuffle(mixed_dataset)
    
    return mixed_dataset
```

##### 3. Multitask Learning

Train on multiple tasks simultaneously:

```python
def create_multitask_dataset(task_datasets, task_prefixes):
    """Create a multitask dataset with task prefixes."""
    combined_dataset = []
    
    for task_name, dataset in task_datasets.items():
        prefix = task_prefixes[task_name]
        
        # Add task prefix to each example
        prefixed_dataset = []
        for example in dataset:
            prefixed_example = example.copy()
            prefixed_example["input_text"] = prefix + " " + example["input_text"]
            prefixed_dataset.append(prefixed_example)
        
        combined_dataset.extend(prefixed_dataset)
    
    # Shuffle the combined dataset
    random.shuffle(combined_dataset)
    
    return combined_dataset
```

##### 4. Parameter-Efficient Fine-tuning

PEFT methods naturally mitigate catastrophic forgetting by keeping most parameters frozen:

```python
from transformers import AutoModelForCausalLM
from peft import get_peft_model, LoraConfig

# Load pre-trained model
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Configure LoRA
peft_config = LoraConfig(
    task_type="CAUSAL_LM",
    r=8,
    lora_alpha=16,
    lora_dropout=0.1,
    target_modules=["c_attn"]
)

# Create PEFT model - base weights are frozen
peft_model = get_peft_model(model, peft_config)
```

##### 5. Knowledge Distillation

Use the original model to guide the fine-tuned model:

```python
class DistillationLoss(nn.Module):
    def __init__(self, teacher_model, temperature=2.0, alpha=0.5):
        super().__init__()
        self.teacher_model = teacher_model
        self.temperature = temperature
        self.alpha = alpha
        
        # Freeze teacher model
        for param in teacher_model.parameters():
            param.requires_grad = False
            
    def forward(self, student_logits, labels, inputs):
        # Standard cross-entropy loss
        ce_loss = F.cross_entropy(student_logits, labels)
        
        # Get teacher predictions
        with torch.no_grad():
            teacher_logits = self.teacher_model(**inputs).logits
            
        # Distillation loss
        distill_loss = F.kl_div(
            F.log_softmax(student_logits / self.temperature, dim=-1),
            F.softmax(teacher_logits / self.temperature, dim=-1),
            reduction='batchmean'
        ) * (self.temperature ** 2)
        
        # Combined loss
        loss = (1 - self.alpha) * ce_loss + self.alpha * distill_loss
        
        return loss
```

#### Measuring and Monitoring Forgetting

It's important to track if your fine-tuning is causing catastrophic forgetting:

```python
def evaluate_forgetting(base_model, fine_tuned_model, tokenizer, general_eval_datasets):
    """Evaluate how much general capability has been lost."""
    
    results = {}
    
    for dataset_name, dataset in general_eval_datasets.items():
        print(f"Evaluating on {dataset_name}...")
        
        # Evaluate base model
        base_metrics = evaluate_model(base_model, tokenizer, dataset, task_type="generation")
        
        # Evaluate fine-tuned model
        ft_metrics = evaluate_model(fine_tuned_model, tokenizer, dataset, task_type="generation")
        
        # Calculate changes
        changes = {}
        for metric, value in base_metrics.items():
            change = ft_metrics[metric] - value
            percent_change = (change / value) * 100 if value != 0 else float('inf')
            
            changes[metric] = {
                "base": value,
                "fine_tuned": ft_metrics[metric],
                "absolute_change": change,
                "percent_change": percent_change
            }
        
        results[dataset_name] = changes
    
    # Print summary
    print("\nForgetting Analysis:")
    for dataset_name, changes in results.items():
        print(f"\n{dataset_name}:")
        for metric, data in changes.items():
            change_str = f"{data['absolute_change']:.4f} ({data['percent_change']:.2f}%)"
            change_type = "Improvement" if data['percent_change'] > 0 else "Regression"
            print(f"  {metric}: {change_str} - {change_type}")
    
    return results
```

#### Practical Strategy for Preventing Forgetting

In practice, a combination of techniques works best:

1. Use PEFT methods as a first line of defense
2. Include a small amount of diverse "replay" data in fine-tuning
3. Apply lightweight regularization like knowledge distillation
4. Continuously monitor for forgetting on general tasks
5. Use multi-stage fine-tuning with decreasing learning rates

---

### 6.8 Quantization and Efficient Inference

After fine-tuning a model, deploying it efficiently becomes the next challenge. Quantization reduces the precision of model weights, significantly decreasing memory usage and increasing inference speed with minimal impact on quality.

#### Understanding Quantization

Quantization converts high-precision weights (usually FP32 or FP16) to lower precision (INT8, INT4, or even lower):

- **FP32**: 32-bit floating point (standard precision)
- **FP16**: 16-bit floating point (half precision)
- **INT8**: 8-bit integer (quantized)
- **INT4**: 4-bit integer (highly quantized)

#### Types of Quantization

##### Post-Training Quantization (PTQ)

PTQ applies quantization after training without further fine-tuning:

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

# Configure quantization
quantization_config = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_threshold=6.0
)

# Load model with quantization
model = AutoModelForCausalLM.from_pretrained(
    "your-fine-tuned-model",
    quantization_config=quantization_config,
    device_map="auto"
)

# Model is now loaded in 8-bit precision
print(f"Model size in memory: {model.get_memory_footprint() / 1e9:.2f} GB")
```

##### Quantization-Aware Training (QAT)

QAT incorporates quantization during the training process:

```python
import torch.quantization as quantization

# Define quantization configuration
qconfig = quantization.get_default_qconfig('fbgemm')  # For x86 CPUs
model.qconfig = qconfig

# Prepare model for QAT
quantization.prepare_qat(model, inplace=True)

# Train with quantization awareness
for epoch in range(num_epochs):
    train_one_epoch(model, criterion, optimizer, data_loader, device)
    
    # Adjust learning rate
    scheduler.step()

# Convert to quantized model
quantization.convert(model, inplace=True)
```

##### Dynamic Quantization

Applied at runtime without calibration data:

```python
import torch

# Apply dynamic quantization
quantized_model = torch.quantization.quantize_dynamic(
    model,  # Model to quantize
    {torch.nn.Linear},  # Layers to quantize
    dtype=torch.qint8  # Quantization data type
)

# Compare model sizes
fp32_size = sum(p.numel() * 4 for p in model.parameters())  # 4 bytes per param for fp32
q_size = sum(p.numel() * (1 if isinstance(p, torch.qint8) else 4) for p in quantized_model.parameters())

print(f"FP32 model size: {fp32_size / 1e6:.2f} MB")
print(f"Quantized model size: {q_size / 1e6:.2f} MB")
print(f"Compression ratio: {fp32_size / q_size:.2f}x")
```

#### GPTQ and Other Advanced Quantization Techniques

GPTQ is a state-of-the-art quantization method specifically designed for LLMs:

```python
from transformers import AutoModelForCausalLM, GPTQConfig

# Configure GPTQ
gptq_config = GPTQConfig(
    bits=4,  # 4-bit quantization
    group_size=128,  # Group size for quantization
    dataset="c4",  # Calibration dataset
    desc_act=False  # Whether to quantize activations
)

# Load and quantize model
model = AutoModelForCausalLM.from_pretrained(
    "your-fine-tuned-model",
    quantization_config=gptq_config,
    device_map="auto"
)
```

#### Evaluating Quantized Models

Always evaluate quantization impact on model quality:

```python
def compare_quantized_models(original_model, quantized_model, tokenizer, eval_dataset):
    """Compare original and quantized model performance."""
    
    print("Evaluating original model...")
    original_results = evaluate_model(original_model, tokenizer, eval_dataset, "generation")
    
    print("Evaluating quantized model...")
    quantized_results = evaluate_model(quantized_model, tokenizer, eval_dataset, "generation")
    
    # Compare results
    print("\nPerformance Comparison:")
    print("Metric".ljust(15) + "Original".ljust(15) + "Quantized".ljust(15) + "Difference".ljust(15) + "% Change")
    print("-" * 75)
    
    for metric in original_results:
        orig_val = original_results[metric]
        quant_val = quantized_results[metric]
        difference = quant_val - orig_val
        percent = (difference / orig_val) * 100 if orig_val != 0 else float('inf')
        
        print(
            f"{metric}".ljust(15) + 
            f"{orig_val:.4f}".ljust(15) + 
            f"{quant_val:.4f}".ljust(15) + 
            f"{difference:.4f}".ljust(15) + 
            f"{percent:.2f}%"
        )
    
    # Speed comparison
    print("\nSpeed Comparison:")
    original_speed = measure_inference_speed(original_model, tokenizer, prompt="Your test prompt here")
    quantized_speed = measure_inference_speed(quantized_model, tokenizer, prompt="Your test prompt here")
    
    speedup = quantized_speed / original_speed if original_speed > 0 else float('inf')
    print(f"Original model: {original_speed:.2f} tokens/sec")
    print(f"Quantized model: {quantized_speed:.2f} tokens/sec")
    print(f"Speedup: {speedup:.2f}x")
    
    # Memory usage
    import torch
    original_memory = torch.cuda.max_memory_allocated() / 1e9 if torch.cuda.is_available() else "N/A"
    torch.cuda.reset_peak_memory_stats()
    
    # Run inference with quantized model
    inputs = tokenizer("Test prompt", return_tensors="pt").to(next(quantized_model.parameters()).device)
    quantized_model.generate(**inputs, max_length=50)
    
    quantized_memory = torch.cuda.max_memory_allocated() / 1e9 if torch.cuda.is_available() else "N/A"
    
    print(f"\nMemory Usage:")
    print(f"Original model: {original_memory:.2f} GB")
    print(f"Quantized model: {quantized_memory:.2f} GB")
    if isinstance(original_memory, float) and isinstance(quantized_memory, float):
        print(f"Memory reduction: {original_memory/quantized_memory:.2f}x")
    
    return {
        "performance": {
            "original": original_results,
            "quantized": quantized_results
        },
        "speed": {
            "original": original_speed,
            "quantized": quantized_speed,
            "speedup": speedup
        },
        "memory": {
            "original": original_memory,
            "quantized": quantized_memory
        }
    }

def measure_inference_speed(model, tokenizer, prompt, max_length=100, num_runs=5):
    """Measure inference speed in tokens per second."""
    device = next(model.parameters()).device
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    
    # Warm-up run
    _ = model.generate(**inputs, max_length=max_length)
    
    # Timed runs
    start_time = time.time()
    for _ in range(num_runs):
        generated = model.generate(**inputs, max_length=max_length)
    end_time = time.time()
    
    # Calculate tokens per second
    total_time = end_time - start_time
    num_tokens_generated = generated.shape[1] - inputs.input_ids.shape[1]
    tokens_per_second = (num_tokens_generated * num_runs) / total_time
    
    return tokens_per_second
```

#### Optimizing Inference with ONNX and TensorRT

Convert models to optimized formats for faster inference:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from optimum.onnxruntime import ORTModelForCausalLM

# Load model and tokenizer
model_id = "your-fine-tuned-model"
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Convert to ONNX with Optimum
ort_model = ORTModelForCausalLM.from_pretrained(
    model_id,
    from_transformers=True,
    provider="CUDAExecutionProvider"
)

# Save ONNX model
ort_model.save_pretrained("./onnx-model")

# Inference with ONNX model
inputs = tokenizer("Generate a story about:", return_tensors="pt")
outputs = ort_model.generate(**inputs, max_length=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

#### Pruning: Removing Unnecessary Weights

Pruning removes less important weights, further reducing model size:

```python
import torch.nn.utils.prune as prune

def apply_weight_pruning(model, pruning_rate=0.3):
    """Apply magnitude pruning to model weights."""
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            prune.l1_unstructured(module, name='weight', amount=pruning_rate)
            
    # Calculate sparsity after pruning
    total_params = 0
    zero_params = 0
    
    for name, param in model.named_parameters():
        if 'weight' in name:
            total_params += param.numel()
            zero_params += (param == 0).sum().item()
    
    sparsity = 100.0 * zero_params / total_params
    print(f"Model sparsity after pruning: {sparsity:.2f}%")
    
    return model

# Apply pruning
pruned_model = apply_weight_pruning(model, pruning_rate=0.3)

# Make pruning permanent
for module in pruned_model.modules():
    if isinstance(module, torch.nn.Linear):
        prune.remove(module, 'weight')
```

#### Distillation: Creating Smaller, Faster Models

Knowledge distillation creates a smaller model that mimics the behavior of a larger one:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

# Load teacher (large) and student (small) models
teacher_model = AutoModelForCausalLM.from_pretrained("your-fine-tuned-model")
student_model = AutoModelForCausalLM.from_pretrained("gpt2")  # Smaller model

tokenizer = AutoTokenizer.from_pretrained("your-fine-tuned-model")

# Freeze teacher model
for param in teacher_model.parameters():
    param.requires_grad = False

# Custom distillation training loop
class DistillationTrainer(Trainer):
    def compute_loss(self, model, inputs, return_outputs=False):
        # Student forward pass
        student_outputs = model(**inputs)
        student_logits = student_outputs.logits
        
        # Teacher forward pass
        with torch.no_grad():
            teacher_outputs = self.teacher_model(**inputs)
            teacher_logits = teacher_outputs.logits
        
        # Standard language modeling loss
        loss_ce = student_outputs.loss
        
        # Distillation loss
        temperature = 2.0
        loss_kd = F.kl_div(
            F.log_softmax(student_logits / temperature, dim=-1),
            F.softmax(teacher_logits / temperature, dim=-1),
            reduction="batchmean"
        ) * (temperature ** 2)
        
        # Combined loss
        alpha = 0.5  # Weight between CE and KD loss
        loss = alpha * loss_ce + (1 - alpha) * loss_kd
        
        return (loss, student_outputs) if return_outputs else loss

# Set up distillation trainer
distill_trainer = DistillationTrainer(
    model=student_model,
    teacher_model=teacher_model,
    args=TrainingArguments(
        output_dir="./distilled-model",
        learning_rate=5e-5,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        evaluation_strategy="steps",
        eval_steps=500,
        save_strategy="steps",
        save_steps=500,
        logging_dir="./logs"
    ),
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)

# Train distilled model
distill_trainer.train()

# Save distilled model
distill_trainer.save_model("./distilled-model-final")
```

---

### 6.9 Hands-On Project - Fine-tuning a Model for a Specialized Task

Let's put everything we've learned into practice with a complete project to fine-tune a model for a specialized task: creating a technical documentation assistant.

#### Project Overview

We'll fine-tune a model to:

1. Answer questions about programming concepts
2. Generate code examples in various languages
3. Explain technical concepts clearly
4. Follow a consistent style for documentation

#### Step 1: Define Requirements

```python
# Project Requirements
project = {
    "name": "TechDocGPT",
    "description": "A specialized assistant for technical documentation",
    "base_model": "gpt2-medium",
    "fine_tuning_method": "LoRA",
    "target_tasks": ["question-answering", "code-generation", "explanation"],
    "evaluation_metrics": ["accuracy", "code_correctness", "clarity"]
}
```

#### Step 2: Prepare Training Data

```python
import pandas as pd
from datasets import Dataset

# Load and prepare training data
def prepare_training_data():
    # Sample data structure (in practice, you'd have a larger dataset)
    data = {
        "instruction": [
            "Explain how HTTP requests work",
            "Write a Python function to sort a list of numbers",
            "What is the difference between REST and GraphQL?",
            "Create a React component for a login form"
        ],
        "response": [
            "HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the web. Here's how HTTP requests work:\n\n1. The client (browser) sends an HTTP request to a server\n2. This request includes a method (GET, POST, etc.), headers, and sometimes a body\n3. The server processes the request and sends back an HTTP response\n4. The response contains a status code, headers, and usually a body with the requested data\n\nThe most common HTTP methods are:\n- GET: Retrieve data\n- POST: Submit data\n- PUT: Update existing data\n- DELETE: Remove data",
            
            "```python\ndef sort_numbers(numbers):\n    \"\"\"\n    Sort a list of numbers in ascending order.\n    \n    Args:\n        numbers: List of integers or floats\n        \n    Returns:\n        A new list with the numbers sorted\n    \"\"\"\n    # Using Python's built-in sorted function\n    return sorted(numbers)\n    \n    # Alternatively, we could use the list.sort() method\n    # This modifies the original list instead of returning a new one\n    # numbers.sort()\n    # return numbers\n```\n\nThis function takes a list of numbers and returns a new sorted list. The built-in `sorted()` function handles both integers and floats, and can even sort strings or other comparable objects.",
            
            "REST (Representational State Transfer) and GraphQL are both approaches for building APIs, but they differ in several key ways:\n\n1. **Data Fetching**:\n   - REST: Typically utilizes multiple endpoints, each returning fixed data structures\n   - GraphQL: Uses a single endpoint where clients specify exactly what data they need\n\n2. **Over/Under-fetching**:\n   - REST: Often returns too much data or requires multiple requests to get all needed data\n   - GraphQL: Clients request precisely the data they need, no more, no less\n\n3. **Versioning**:\n   - REST: Often requires explicit versioning (e.g., /api/v1/)\n   - GraphQL: Can add fields without breaking existing queries\n\n4. **Error Handling**:\n   - REST: Uses HTTP status codes\n   - GraphQL: Always returns 200 OK with errors in the response body\n\nChoose REST for simpler APIs with well-defined resources. Choose GraphQL for complex applications where clients need flexible data fetching.",
            
            "```jsx\nimport React, { useState } from 'react';\n\nconst LoginForm = () => {\n  const [email, setEmail] = useState('');\n  const [password, setPassword] = useState('');\n  const [error, setError] = useState('');\n\n  const handleSubmit = (e) => {\n    e.preventDefault();\n    setError('');\n    \n    if (!email || !password) {\n      setError('Please enter both email and password');\n      return;\n    }\n    \n    // Here you would typically call an authentication API\n    console.log('Logging in with:', email, password);\n    // Example: authService.login(email, password)\n  };\n\n  return (\n    <div className=\"login-form-container\">\n      <h2>Log In</h2>\n      \n      {error && <div className=\"error-message\">{error}</div>}\n      \n      <form onSubmit={handleSubmit}>\n        <div className=\"form-group\">\n          <label htmlFor=\"email\">Email:</label>\n          <input\n            type=\"email\"\n            id=\"email\"\n            value={email}\n            onChange={(e) => setEmail(e.target.value)}\n            required\n          />\n        </div>\n        \n        <div className=\"form-group\">\n          <label htmlFor=\"password\">Password:</label>\n          <input\n            type=\"password\"\n            id=\"password\"\n            value={password}\n            onChange={(e) => setPassword(e.target.value)}\n            required\n          />\n        </div>\n        \n        <button type=\"submit\" className=\"login-button\">\n          Log In\n        </button>\n      </form>\n    </div>\n  );\n};\n\nexport default LoginForm;\n```\n\nThis React component creates a simple login form with email and password fields. It uses React Hooks (useState) to manage the form state and includes basic validation to ensure both fields are filled before submission."
        ]
    }
    
    # Convert to DataFrame and then to Hugging Face Dataset
    df = pd.DataFrame(data)
    dataset = Dataset.from_pandas(df)
    
    # Split into train and validation
    dataset = dataset.train_test_split(test_size=0.1)
    
    return dataset

# Format data for instruction-based fine-tuning
def format_instruction_dataset(example):
    return {
        "text": f"### Instruction:\n{example['instruction']}\n\n### Response:\n{example['response']}\n"
    }
```

#### Step 3: Set Up LoRA Fine-tuning

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import get_peft_model, LoraConfig, TaskType, PeftModel
import torch

def setup_fine_tuning():
    # Load base model and tokenizer
    model_name = "gpt2-medium"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Add padding token if it doesn't exist
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = tokenizer.pad_token_id
    
    # Configure LoRA
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=16,  # Rank
        lora_alpha=32,
        lora_dropout=0.05,
        target_modules=["c_attn", "c_proj"],  # Target attention components
        bias="none",
    )
    
    # Create PEFT model
    peft_model = get_peft_model(model, lora_config)
    
    # Print trainable parameters info
    trainable_params = sum(p.numel() for p in peft_model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in peft_model.parameters())
    print(f"Trainable parameters: {trainable_params} ({trainable_params/total_params:.2%} of total)")
    
    return peft_model, tokenizer

# Tokenization function
def tokenize_function(examples, tokenizer, max_length=512):
    return tokenizer(
        examples["text"],
        truncation=True,
        padding="max_length",
        max_length=max_length,
        return_tensors="pt"
    )

# Data collator for causal language modeling (continued)
class CustomDataCollator:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        
    def __call__(self, examples):
        # Extract input_ids and create batch
        batch = {
            "input_ids": torch.stack([example["input_ids"] for example in examples]),
            "attention_mask": torch.stack([example["attention_mask"] for example in examples]),
        }
        
        # Set up labels for causal language modeling (shifted input_ids)
        batch["labels"] = batch["input_ids"].clone()
        
        # Return the batch
        return batch
```


#### Step 4: Training Process

```python
from transformers import Trainer

def train_model(model, tokenizer, dataset):
    # Tokenize datasets
    tokenized_dataset = dataset.map(
        lambda examples: tokenize_function(examples, tokenizer),
        batched=True,
        remove_columns=dataset["train"].column_names  # Remove original columns
    )
    
    # Set up training arguments
    training_args = TrainingArguments(
        output_dir="./techdoc-assistant",
        learning_rate=1e-4,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        gradient_accumulation_steps=8,  # Effectively increases batch size
        warmup_steps=100,
        weight_decay=0.01,
        logging_dir="./logs",
        logging_steps=10,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        save_total_limit=3,
        report_to="tensorboard",
        fp16=True,  # Mixed precision training for efficiency
    )
    
    # Create data collator
    data_collator = CustomDataCollator(tokenizer)
    
    # Initialize trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["test"],
        data_collator=data_collator,
    )
    
    # Train the model
    print("Starting training...")
    trainer.train()
    
    # Save the fine-tuned model
    model.save_pretrained("./techdoc-assistant-final")
    tokenizer.save_pretrained("./techdoc-assistant-final")
    
    return model, tokenizer
```

#### Step 5: Evaluation Functions

```python
def evaluate_technical_documentation(model, tokenizer, test_prompts):
    """Evaluate the model on technical documentation tasks."""
    model.eval()
    device = next(model.parameters()).device
    
    results = []
    
    for prompt in test_prompts:
        # Format prompt as instruction
        formatted_prompt = f"### Instruction:\n{prompt}\n\n### Response:\n"
        
        # Tokenize
        inputs = tokenizer(formatted_prompt, return_tensors="pt").to(device)
        
        # Generate response
        output_ids = model.generate(
            inputs.input_ids,
            max_length=512,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            num_return_sequences=1,
        )
        
        # Decode generated text, skipping the input prompt
        prompt_length = len(inputs.input_ids[0])
        generated_text = tokenizer.decode(output_ids[0][prompt_length:], skip_special_tokens=True)
        
        # Add to results
        results.append({
            "prompt": prompt,
            "response": generated_text.strip(),
        })
    
    return results

def analyze_code_correctness(responses):
    """Basic analysis of code snippets in responses."""
    import re
    
    code_results = []
    code_pattern = r'```(?:python|javascript|jsx|java|cpp|c\+\+|rust|go)?\n(.*?)```'
    
    for response in responses:
        # Extract code blocks
        code_blocks = re.findall(code_pattern, response["response"], re.DOTALL)
        
        # Analyze each code block
        for code in code_blocks:
            # Check for syntax errors (this is a simplified check)
            has_syntax_error = False
            has_comments = '"""' in code or "'''" in code or '#' in code or '//' in code
            
            # Count lines and estimate complexity
            lines = code.strip().split('\n')
            line_count = len(lines)
            complexity = "Simple" if line_count < 15 else "Moderate" if line_count < 40 else "Complex"
            
            # Add to results
            code_results.append({
                "prompt": response["prompt"],
                "code_length": line_count,
                "has_comments": has_comments,
                "complexity": complexity,
                "has_syntax_error": has_syntax_error,
            })
    
    # Print summary
    if code_results:
        print(f"Found {len(code_results)} code snippets")
        print(f"Average length: {sum(r['code_length'] for r in code_results) / len(code_results):.1f} lines")
        print(f"With comments: {sum(1 for r in code_results if r['has_comments'])} ({sum(1 for r in code_results if r['has_comments']) / len(code_results):.1%})")
    
    return code_results
```

#### Step 6: Put It All Together

```python
def run_complete_project():
    """Run the complete fine-tuning project."""
    # Prepare data
    dataset = prepare_training_data()
    dataset = dataset.map(format_instruction_dataset)
    print(f"Dataset prepared with {len(dataset['train'])} training examples")
    
    # Set up model and tokenizer
    model, tokenizer = setup_fine_tuning()
    
    # Train model
    trained_model, tokenizer = train_model(model, tokenizer, dataset)
    
    # Evaluate on test prompts
    test_prompts = [
        "Explain how RESTful APIs work",
        "Write a Python class to represent a simple bank account",
        "What's the difference between synchronous and asynchronous programming?",
        "Create a function to calculate the Fibonacci sequence in JavaScript"
    ]
    
    evaluation_results = evaluate_technical_documentation(trained_model, tokenizer, test_prompts)
    
    # Analyze code snippets
    code_analysis = analyze_code_correctness(evaluation_results)
    
    # Print sample responses
    print("\nSample Responses:")
    for i, result in enumerate(evaluation_results[:2]):  # Show first 2 examples
        print(f"\nPrompt {i+1}: {result['prompt']}")
        print("-" * 40)
        print(result['response'])
        print("=" * 80)
    
    return {
        "model": trained_model,
        "tokenizer": tokenizer,
        "evaluation_results": evaluation_results,
        "code_analysis": code_analysis
    }

# Call this function to execute the entire project
if __name__ == "__main__":
    project_results = run_complete_project()
```

#### Step 7: Save and Load the Fine-tuned Model

```python
def save_and_load_model():
    """Demonstrate how to save and load a LoRA fine-tuned model."""
    from peft import PeftModel, PeftConfig
    
    # Save model adapter weights separately
    def save_lora_model(model, path):
        model.save_pretrained(path)
        print(f"LoRA adapter saved to {path}")
    
    # Load model for inference
    def load_for_inference(base_model_name, adapter_path):
        # Load base model
        base_model = AutoModelForCausalLM.from_pretrained(base_model_name)
        
        # Load adapter
        model = PeftModel.from_pretrained(base_model, adapter_path)
        tokenizer = AutoTokenizer.from_pretrained(base_model_name)
        
        # Set model to evaluation mode
        model.eval()
        
        return model, tokenizer
    
    # Example: Save model after training
    # save_lora_model(project_results["model"], "./techdoc-lora-adapter")
    
    # Example: Load model for inference
    model, tokenizer = load_for_inference("gpt2-medium", "./techdoc-lora-adapter")
    
    # Test the loaded model
    prompt = "Explain how garbage collection works in programming languages"
    formatted_prompt = f"### Instruction:\n{prompt}\n\n### Response:\n"
    
    inputs = tokenizer(formatted_prompt, return_tensors="pt").to(next(model.parameters()).device)
    outputs = model.generate(**inputs, max_length=512, temperature=0.7)
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Prompt: {prompt}\n\nResponse: {response}")
    
    return model, tokenizer
```

#### Step 8: Apply Quantization for Deployment

```python
def prepare_for_deployment():
    """Demonstrate quantization and preparation for deployment."""
    from peft import PeftModel, PeftConfig
    import torch
    
    # Load LoRA weights with base model
    base_model = AutoModelForCausalLM.from_pretrained("gpt2-medium")
    model = PeftModel.from_pretrained(base_model, "./techdoc-lora-adapter")
    tokenizer = AutoTokenizer.from_pretrained("gpt2-medium")
    
    # Merge weights (optional, combines adapter with base model)
    merged_model = model.merge_and_unload()
    
    # Apply 8-bit quantization 
    try:
        import bitsandbytes as bnb
        from transformers import BitsAndBytesConfig
        
        # Configure quantization
        quantization_config = BitsAndBytesConfig(
            load_in_8bit=True,
            llm_int8_enable_fp32_cpu_offload=True
        )
        
        # Load model with quantization
        quantized_model = AutoModelForCausalLM.from_pretrained(
            "gpt2-medium",
            quantization_config=quantization_config,
            device_map="auto"
        )
        
        # Load adapter onto quantized model
        quantized_model = PeftModel.from_pretrained(
            quantized_model, 
            "./techdoc-lora-adapter"
        )
        
        print("Model quantized successfully")
        
        # Compare memory usage
        def get_model_size(model):
            """Estimate model size in memory."""
            return sum(p.numel() * p.element_size() for p in model.parameters()) / (1024 * 1024)
        
        original_size = get_model_size(model)
        quantized_size = get_model_size(quantized_model)
        
        print(f"Original model size: {original_size:.2f} MB")
        print(f"Quantized model size: {quantized_size:.2f} MB")
        print(f"Compression ratio: {original_size / quantized_size:.2f}x")
        
        return quantized_model, tokenizer
        
    except ImportError:
        print("Quantization libraries not available. Install bitsandbytes for quantization.")
        return merged_model, tokenizer
```

#### Step 9: Create a Simple Inference API

```python
def create_inference_api(model, tokenizer):
    """Create a simple FastAPI endpoint for model inference."""
    try:
        from fastapi import FastAPI, HTTPException
        from pydantic import BaseModel
        import uvicorn
        
        app = FastAPI(title="TechDoc Assistant API")
        
        class DocumentationRequest(BaseModel):
            prompt: str
            max_length: int = 512
            temperature: float = 0.7
            top_p: float = 0.9
        
        class DocumentationResponse(BaseModel):
            prompt: str
            response: str
        
        @app.post("/generate", response_model=DocumentationResponse)
        async def generate_documentation(request: DocumentationRequest):
            try:
                # Format prompt
                formatted_prompt = f"### Instruction:\n{request.prompt}\n\n### Response:\n"
                
                # Tokenize
                inputs = tokenizer(formatted_prompt, return_tensors="pt").to(
                    next(model.parameters()).device
                )
                
                # Generate response
                outputs = model.generate(
                    inputs.input_ids,
                    max_length=request.max_length,
                    temperature=request.temperature,
                    top_p=request.top_p,
                    do_sample=True
                )
                
                # Decode
                response = tokenizer.decode(outputs[0], skip_special_tokens=True)
                
                # Extract just the response part
                response_text = response.split("### Response:\n")[-1].strip()
                
                return DocumentationResponse(
                    prompt=request.prompt,
                    response=response_text
                )
            
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Generation error: {str(e)}")
        
        # Return the app instance (would normally be run with uvicorn)
        return app
        
    except ImportError:
        print("API libraries not available. Install fastapi and uvicorn for API deployment.")
        return None
```

This comprehensive project demonstrates a complete workflow for fine-tuning a language model for a specific task. By following these steps, you can create specialized models for various applications while efficiently using computational resources through techniques like LoRA fine-tuning and quantization.

The project illustrates several key concepts:

1. **Data preparation**: Formatting data for instruction fine-tuning
2. **Parameter-efficient fine-tuning**: Using LoRA to adapt models efficiently
3. **Evaluation**: Assessing model performance on technical content
4. **Deployment considerations**: Quantizing and serving the model

In a real-world scenario, you would want to expand the training dataset significantly, add more comprehensive evaluation metrics, and potentially incorporate techniques to prevent catastrophic forgetting of general knowledge while specializing in technical documentation.

---

### 6.10 Key Takeaways from Module 6

In this module, we've explored the powerful paradigm of transfer learning and fine-tuning for large language models. Let's summarize the key points:

#### The Power of Transfer Learning

Transfer learning allows us to leverage knowledge from pre-trained models rather than starting from scratch. This approach:

1. **Drastically reduces computational requirements** for developing specialized models
2. **Minimizes data needs** by building on existing language knowledge
3. **Enables rapid adaptation** to new domains and tasks
4. **Preserves general capabilities** while adding specialized skills

#### Fine-tuning Approaches

We explored several approaches to fine-tuning:

1. **Full fine-tuning**: Updates all parameters of the pre-trained model
    
    - Provides optimal performance but requires significant resources
    - Most suitable when computational resources are plentiful
2. **Parameter-efficient fine-tuning (PEFT)**: Updates a small subset of parameters
    
    - LoRA: Low-rank adaptation of weight matrices
    - Adapters: Small modules inserted between layers
    - Prompt tuning: Trainable continuous prompt embeddings
    - Significantly reduces memory requirements and training time
    - Often performs nearly as well as full fine-tuning
3. **Quantization and optimization**: Reduces model precision after training
    
    - Enables deployment on resource-constrained devices
    - Maintains most of model quality with substantial efficiency gains

#### Task Adaptation Strategies

Different tasks require different adaptation strategies:

1. **Classification tasks**: Add classification heads and use cross-entropy loss
2. **Generation tasks**: Use autoregressive fine-tuning with carefully formatted data
3. **Sequence tagging**: Employ token-level classification with aligned labels
4. **Question answering**: Specialize in extracting information from context
5. **Domain adaptation**: Continue pre-training on domain-specific corpora before task-specific fine-tuning

#### Mitigating Catastrophic Forgetting

Fine-tuning can cause models to "forget" their general capabilities. We learned techniques to prevent this:

1. **Regularization methods**: Constrain weight updates to preserve original knowledge
2. **Replay methods**: Mix in general-domain examples during fine-tuning
3. **Parameter-efficient methods**: Naturally preserve original capabilities by keeping most weights frozen
4. **Knowledge distillation**: Use the original model to guide the fine-tuned model
5. **Continual learning**: Gradually adapt the model while maintaining performance on previous tasks

#### Evaluation Best Practices

Proper evaluation ensures that fine-tuned models meet requirements:

1. **Task-specific metrics**: Different tasks require different evaluation approaches
2. **Behavioral evaluation**: Assess changes in model behavior beyond just task performance
3. **Comparison with baselines**: Always benchmark against relevant baseline models
4. **Domain-specific testing**: Create specialized test sets for your particular application
5. **General capability retention**: Check that general abilities haven't degraded

#### Deployment Considerations

Moving from fine-tuning to production requires additional steps:

1. **Quantization**: Reduce precision to improve inference speed and reduce memory usage
2. **Pruning**: Remove unnecessary weights to shrink model size
3. **Distillation**: Create smaller, faster models that mimic larger ones
4. **Optimization frameworks**: Convert models to optimized formats like ONNX
5. **Inference APIs**: Create standardized interfaces for model access

#### Practical Recommendations

Based on all we've covered, here are some practical recommendations:

1. **Start with PEFT**: Begin with parameter-efficient methods like LoRA before trying full fine-tuning
2. **Quality data matters more than quantity**: Focus on high-quality, diverse examples
3. **Consistent formatting**: Use consistent instruction formats across training examples
4. **Test general capabilities**: Always verify that fine-tuning hasn't degraded important general abilities
5. **Consider compute trade-offs**: Balance training efficiency with inference requirements
6. **Iterate quickly**: Use efficient methods to test multiple approaches before committing resources

By applying these principles, you can effectively adapt large language models to specialized tasks and domains, creating powerful AI systems tailored to your specific needs.

---

### 6.11 Practice Exercises

To reinforce your learning from this module, here are some hands-on exercises to try:

#### Exercise 1: Comparative Fine-tuning

Try fine-tuning the same base model using different methods and compare the results:

1. **Setup**:
    
    - Choose a small base model (e.g., GPT-2 small or DistilGPT2)
    - Select a simple task (e.g., sentiment classification)
    - Prepare a small dataset (a few hundred examples)
2. **Implement and compare**:
    
    - Fine-tune using full fine-tuning
    - Fine-tune using LoRA
    - Fine-tune using adapters
    - Fine-tune using prompt tuning
3. **Analyze**:
    
    - Compare performance metrics across methods
    - Measure training time and memory usage
    - Evaluate model size and inference speed
    - Determine the best approach for your specific use case

#### Exercise 2: Domain Adaptation

Adapt a pre-trained model to a specialized domain:

1. **Data collection**:
    
    - Gather text from a specialized domain (legal, medical, technical, etc.)
    - Create a corpus of at least 1,000 documents
    - Split into training and evaluation sets
2. **Adaptation process**:
    
    - Continue pre-training a small language model on your domain corpus
    - Compare different learning rates and training durations
    - Evaluate domain-specific knowledge before and after adaptation
3. **Extension**:
    
    - Fine-tune for a specific task within the domain
    - Compare performance with and without domain adaptation
    - Analyze which domain-specific terms and concepts the model has learned

#### Exercise 3: Preventing Catastrophic Forgetting

Experiment with techniques to maintain general capabilities:

1. **Baseline evaluation**:
    
    - Select a pre-trained model
    - Evaluate its performance on general language tasks (e.g., grammar, world knowledge)
    - Fine-tune for a specialized task without any forgetting mitigation
    - Re-evaluate general capabilities to measure forgetting
2. **Apply mitigation techniques**:
    
    - Implement EWC (Elastic Weight Consolidation)
    - Create a mixed dataset with replay examples
    - Try LoRA with different configurations
    - Apply knowledge distillation
3. **Comparative analysis**:
    
    - Measure forgetting across different techniques
    - Analyze the trade-off between task performance and general capability retention
    - Determine the most effective approach for your specific scenario

#### Exercise 4: Efficient Deployment Pipeline

Build a complete pipeline from fine-tuning to deployment:

1. **Fine-tuning**:
    
    - Fine-tune a model for a practical application (e.g., customer support responses)
    - Use parameter-efficient methods for training efficiency
2. **Optimization**:
    
    - Apply quantization to the fine-tuned model
    - Compare FP32, FP16, INT8, and mixed precision
    - Measure the impact on performance metrics
3. **Deployment**:
    
    - Create a simple REST API for model inference
    - Implement caching for frequent requests
    - Measure throughput and latency
    - Optimize for production use

#### Exercise 5: Multi-task Fine-tuning

Adapt a model for multiple related tasks simultaneously:

1. **Task selection**:
    
    - Choose 3-4 related NLP tasks (e.g., sentiment analysis, topic classification, named entity recognition)
    - Prepare small datasets for each task
2. **Multi-task setup**:
    
    - Format inputs with task-specific prefixes
    - Create a combined dataset with examples from all tasks
    - Fine-tune a single model on the combined dataset
3. **Evaluation and comparison**:
    
    - Compare with single-task fine-tuned models
    - Analyze performance trade-offs across tasks
    - Test for knowledge transfer between related tasks

#### Exercise 6: Fine-tuning for Code Generation

Create a specialized code assistant:

1. **Data preparation**:
    
    - Collect pairs of natural language descriptions and code implementations
    - Focus on a specific programming language or framework
    - Format as instruction-response pairs
2. **Fine-tuning process**:
    
    - Use a pre-trained code model (e.g., CodeGen, StarCoder) or a general LLM
    - Apply LoRA for efficient fine-tuning
    - Train with appropriate learning rate and epochs
3. **Evaluation**:
    
    - Create test prompts for code generation
    - Evaluate syntactic correctness of generated code
    - Test functional correctness where possible
    - Compare with general, non-fine-tuned models

By completing these exercises, you'll gain hands-on experience with the full spectrum of fine-tuning techniques and applications, deepening your understanding of how to effectively adapt language models for specialized purposes.

---

### 6.12 Preview of Module 7 - Prompt Engineering and In-context Learning

In our next module, we'll explore an alternative approach to adapting language models: using the power of prompts to guide model behavior without changing any parameters. This approach, known as prompt engineering or in-context learning, has become increasingly important as models grow larger and more capable.

Module 7 will cover:

#### 1. Fundamentals of Prompt Engineering

- The theory and principles behind effective prompts
- How modern LLMs interpret and respond to different prompt formats
- The relationship between model size and prompt sensitivity
- The conceptual differences between fine-tuning and prompting

#### 2. Zero-shot and Few-shot Learning

- Leveraging a model's existing knowledge without examples
- Using demonstrations to guide model behavior
- Techniques for selecting effective examples
- When to use zero-shot vs. few-shot approaches

#### 3. Chain-of-Thought and Reasoning Techniques

- Prompting models to think step-by-step
- Techniques for improved reasoning and problem-solving
- Self-consistency and verification methods
- Combining reasoning with external tools and knowledge

#### 4. Advanced Prompting Strategies

- Role-playing and personas in prompts
- System prompts and instruction formats
- Template engineering for consistent outputs
- Combining prompts with structured data

#### 5. Prompt Optimization and Tuning

- Automated methods for prompt improvement
- A/B testing prompts for optimal performance
- Measuring and comparing prompt effectiveness
- Soft prompts and continuous prompt optimization

#### 6. Building Robust Prompt-based Applications

- Creating reliable systems with unreliable components
- Error handling and recovery strategies
- Combining prompting with retrieval and tools
- Designing for prompt-based workflows

#### 7. Hybrid Approaches: Combining Fine-tuning and Prompting

- When to fine-tune vs. when to prompt
- Using fine-tuned models with carefully crafted prompts
- Instruction fine-tuning for better prompt following
- The future of model adaptation techniques

In Module 7, we'll see how the careful crafting of inputs can unlock capabilities in models without modifying their parameters. This complementary approach to fine-tuning is especially valuable when working with the latest frontier models or when computational resources for fine-tuning are limited.

By the end of Modules 6 and 7, you'll have a comprehensive understanding of both parameter-based adaptation (fine-tuning) and input-based adaptation (prompting), allowing you to choose the most appropriate approach for any given scenario.

---

