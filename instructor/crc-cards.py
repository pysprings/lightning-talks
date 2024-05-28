import sys
import argparse
import logging
from jinja2 import Template
import textwrap
from pprint import pprint
import instructor
from openai import OpenAI
from pydantic import BaseModel
from graphviz import Digraph

# Configure logging
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Collaborator(BaseModel):
    name: str
    description: str


class Card(BaseModel):
    name: str
    responsibilities: str
    collaborators: list[Collaborator]


class CardStack(BaseModel):
    cards: list[Card]


def process_file(file_path):
    """
    Process a single file, render it using the Jinja2 template, and extract entities using instructor.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()

    with open("prompt.txt", "r", encoding="utf-8") as f:
        template_content = f.read()

    template = Template(template_content)
    rendered_prompt = template.render(FILENAME=file_path, CODE=file_content)

    client = instructor.patch(OpenAI())
    response = client.chat.completions.create(
        model="gpt-4o",
        response_model=CardStack,
        messages=[
            {"role": "user", "content": rendered_prompt},
        ],
        temperature=0,
    )
    return response


def cardstack_to_dot(cardstack: CardStack) -> str:
    """
    Convert a CardStack to a Graphviz dot graph.
    """
    dot = Digraph()

    for card in cardstack.cards:
        wrapped_responsibilities = textwrap.fill(card.responsibilities, width=30)
        wrapped_responsibilities = wrapped_responsibilities.replace("\n", "\\n")
        collaborators_list = "\\n".join(
            [collaborator.name for collaborator in card.collaborators]
        )
        dot.node(
            card.name,
            label=f"{{ {card.name} | {{ {wrapped_responsibilities} | {collaborators_list} }} }}",
            shape="record",
        )

        card_names = {card.name for card in cardstack.cards}
        for collaborator in card.collaborators:
            if collaborator.name in card_names:
                wrapped_description = textwrap.fill(collaborator.description, width=30)
                wrapped_description = wrapped_description.replace("\n", "\\n")
                dot.edge(card.name, collaborator.name)

    return dot.source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a CRC card diagram from a source file."
    )
    parser.add_argument("file", help="The source file to process.")
    parser.add_argument(
        "-o",
        "--output",
        help="The output file for the Graphviz dot graph.",
        default=None,
    )
    args = parser.parse_args()

    file_path = args.file
    output_path = args.output

    if not file_path:
        print("Usage: python crcgen.py <file> [-o output]")
        sys.exit(1)

    cards = process_file(file_path)
    dot_graph = cardstack_to_dot(cards)
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(dot_graph)
    else:
        print(dot_graph)
