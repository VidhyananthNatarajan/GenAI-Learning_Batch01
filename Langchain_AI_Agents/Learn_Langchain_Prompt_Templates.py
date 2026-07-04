
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# Simple String Based Prompt Template
simple_prompt = PromptTemplate(
     input_variables=["word1","word2"],
     template="Merge these 2 words into a single word.word1:{word1}.word2:{word2}",
    )

print(simple_prompt.format(word1="Hello",word2="World"))

# ChatPrompt Template - from_template
prompt_template =ChatPromptTemplate.from_template(
      template="Merge these 2 words into a single word.word1:{word1}.word2:{word2}")

print(prompt_template.format(word1="Hello",word2="World"))


# ChatPromptTemplate- from_messages
prompt_messages = ChatPromptTemplate.from_messages([
    ("system","Provide me the best Answers always"),
    ("human","Merge these 2 sentences into a single sentences.sentence1:{sent1}.sentence2:{sent2}")])


print(prompt_messages.format(sent1="What is the capital of USA?",sent2="Washingtion"))


# Using the chain - Prompt template +LLM

prompt_template =ChatPromptTemplate.from_template(
      ##template="Merge these 2 words into a single word.word1:{word1}.word2:{word2}")
        template="Answer the questions.Question1:{qn1}.Question2:{qn2}")

## invoke the model
llm =ChatGroq( model ="openai/gpt-oss-120b",temperature=0,max_tokens=1024)

chain = prompt_template|llm

response = chain.invoke({"qn1":"Where is Newzland located?","qn2":"What is the current temperature"})

print(response.content)

