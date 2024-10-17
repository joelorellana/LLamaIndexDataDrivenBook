from llama_index.readers.wikipedia import WikipediaReader
loader = WikipediaReader() 
documents = loader.load_data(pages=['Nayib Bukele', 'Donald Trump']) 
print(f"loaded {len(documents)} documents")