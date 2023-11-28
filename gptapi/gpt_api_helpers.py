from openai import OpenAI

# client = OpenAI(api_key='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')
client = OpenAI(api_key='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')

system_content_example = "You are a common-sense generator, skilled in generating common sense knowledge with restricted objects and perceptacles. You are to given concise output without explanation."
user_content_example = "Use the list of Objects = Background, 'AlarmClock','Apple','ArmChair', 'BaseballBat', 'BasketBall and the a list of RECEPTACLES_EXPLORE = [ 'BathtubBasin',        'Drawer',        'Shelf',        'Sink',        'Cabinet',        'CounterTop'] to generate can-contain relationship, e.g.: (canContain BedType CellPhoneType) (canContain CounterTopType PotatoType), please give concise response without explanation"

def generate_user_content_for_gpt(OBJECTS, RECEPTACLES, OUTPUT_EXAMPLE, RELATIONSHIPS, COUNT=20, print_input=True):
    if print_input:
        print("OBJECTS: ", OBJECTS)
        print("RECEPTACLES: ", RECEPTACLES)
        print("RELATIONSHIPS: ", RELATIONSHIPS)
        print("")

    user_content = ("Use the list of Objects = " + OBJECTS 
    + " and the the list of RECEPTACLES = " + RECEPTACLES 
    + " to generate common-sense knowledge with list of RELATIONSHIPS = " + RELATIONSHIPS
    + ", in the form of (RELATIONSHIPS RECEPTACLESType OBJECTSType) e.g.: " + OUTPUT_EXAMPLE 
    + ", please give " + str(COUNT)
    + "concise response without explanation")

    return user_content


def generate_gpt_response(user_content, gpt_model = "gpt-4-1106-preview", system_content = "") -> str:
    """Generate GPT API response with specified model, system content (optional) and user content

    Args:
        gpt_model (str, optional): _description_. Defaults to "gpt-4-1106-preview" (other:"gpt-3.5-turbo").

    Returns:
        str: string output
    """
    if system_content:
        content_generation = client.chat.completions.create(
            model=gpt_model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ]
        )
    else:
        content_generation = client.chat.completions.create(
            model=gpt_model,
            messages=[
                {"role": "user", "content": user_content}
            ]
        )
    response_content = content_generation.choices[0].message.content
    return response_content


def parse_concise_content(content, parser = "\n"):
    """Parse concise gpt api response content.

    Args:
        content (_type_): api generated content
    """
    return content.split(parser)

def generate_user_content_for_correcting(initial_result):
    """Ask Chatgpt to refine its answer so that it only include practical result 

    Args:
        initial_result (_type_): _description_
    """
    user_content = "pick the correct common sense knowledge from below and respond with copy of the correct ones without explanation:"
    return user_content + str(initial_result)
