from dotenv import load_dotenv
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex

load_dotenv()

parser = LlamaParse(result_type="text")
file_extractor = {".pdf": parser}
reader = SimpleDirectoryReader('./files/pdf',
                               file_extractor=file_extractor)
docs = reader.load_data()

index = VectorStoreIndex.from_documents(docs)
qe = index.as_query_engine()

response = qe.query("List all large dog breeds mentiones in Table 2.")

print(response)