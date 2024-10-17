from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings
from llama_index.core.schema import TextNode
from llama_index.core import SummaryIndex

from dotenv import load_dotenv
import logging


Settings.llm = OpenAI(temperature=0.8, model="gpt-4")
logging.basicConfig(level=logging.DEBUG)
load_dotenv()

nodes = [
    TextNode(
        text="Lionel Messi is a football player from Argentina."
        ),
    TextNode(
        text="He has won the Ballon d'Or trophy 7 times."
        ),
    TextNode(text="Lionel Messi's hometown is Rosario."),
    TextNode(text="He was born on June 24, 1987.")
]
index = SummaryIndex(nodes)
query_engine = index.as_query_engine()
response = query_engine.query(
    "What is Lionel Messi's hometown?"
)
print(response)