from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from prompt import EXPERT_PROMPT_ENGINEER
from langchain_core.output_parsers import StrOutputParser


class PromptEngine:
    def __init__(self, model_name: str = "qwen2.5:latest"):
        
        self.llm = ChatOllama(model=model_name)
        self.parser = StrOutputParser()

        # Build the prompt template with placeholders
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", EXPERT_PROMPT_ENGINEER + """
            
            Additional Guidelines:
            - Use a **{tone}** tone in the final output.
            - Generate a **{length}** style prompt.
            """),
            ("user", "{user_input}")
        ])

        # Create the chain
        self.chain = self.prompt | self.llm | self.parser


    def ask(self, user_input: str, tone: str = "Professional", length: str = "Detailed") -> str:
        """
        Takes raw user input and returns the optimized prompt.
        """
        result = self.chain.invoke({
            "user_input": user_input,
            "tone": tone,
            "length": length
        })
        return result
