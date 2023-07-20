import os
import openai

from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

#Initial Data
content_system = 'You will be provided the description of Element in the List of Atribites, also you will provided the List of Groups, your task is to define the right Group for Element.'
intro_element = 'Element has the following attributes: '
element_atributes = 'Type Name: A_WL_Brick_Plast2_Cem15_Brick100_Cem15_Plast2-134mm, Category: Basic Wall, Finish Material: Beige Limewash Paint, Description: Brick Wall w/ Beige Limewash Fin (Ex) and Beige Limewash Fin (Int) 134mm'
intro_groups = 'List of Groups: '
main_groups = 'Walls & Finishing, Floors and finishing,   Ceilings,  Doors,  Windows, Facade, Roof, Stairs, Railings'

content_user = intro_element + element_atributes + '.' + intro_groups + main_groups + '.'

subgroup_1 = []
subgroup_2 = []

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": content_system
    },
    {
      "role": "user",
      "content": content_user
    }
  ],
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

response_content = response.choices[0].message.content.strip()

def search_elements_in_text(text, elements_to_search):
  text = text.replace(".", "")
  text_list = text.split()
  found_elements = []
  elements_to_search = elements_to_search.replace(",", "")
  group_list = elements_to_search.split()
  for element in group_list:
    if element in text_list:
      found_elements.append(element)
  found_group = " ".join(found_elements)
  return found_group

response_result = search_elements_in_text(response_content, main_groups)

print(response)
print(response_result)