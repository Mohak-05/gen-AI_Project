from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model = 'llama2')

prompt = PromptTemplate(
    input_variables=["name", "genre", "traits"],
    template="""
You are a master character creator. Generate a rich backstory (max 150 words)
and a vivid physical description for:

Name: {name}
Genre: {genre}
Traits: {traits}

Respond in this format:
Story: <story>
Appearance: <appearance>
"""
)
llm_chain = LLMChain(llm=llm, prompt=prompt)

def generate_story(name, genre, traits):
    return llm_chain.run({"name": name, "genre": genre, "traits": traits})