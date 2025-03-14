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