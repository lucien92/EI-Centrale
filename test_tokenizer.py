import transformers
from transformers import AutoTokenizer

# On fait fait une segmentation par mot (voir si pareil que tokenization)

tokenizer = AutoTokenizer.from_pretrained("camembert-base") # pour la langue française
tokens = tokenizer.tokenize("rentrer une chaîne de caractères photogénèse")
print(tokens)