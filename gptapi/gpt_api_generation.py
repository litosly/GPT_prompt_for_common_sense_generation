from gpt_api_helpers import *
from constants import OBJECTS_SINGULAR, RECEPTACLES

def generate_initial_response(OBJECTS, RECEPTACLES, OUTPUT_EXAMPLE, COUNT=20, Task_specific = False, task = ""):
    """TODO: 
    1. Add mulitple times of generaetion
    2. 

    Args:
        OBJECTS (_type_): _description_
        RECEPTACLES (_type_): _description_
        OUTPUT_EXAMPLE (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    objects = ",".join(OBJECTS)
    receptacles = ",".join(RECEPTACLES)
    output_example = ",".join(OUTPUT_EXAMPLE)

    RELATIONSHIPS = ["canContain", "canHeat", "canCool"]
    relationships = ",".join(RELATIONSHIPS)

    user_content = generate_user_content_for_gpt(objects, receptacles, output_example, relationships, COUNT, task_specific=Task_specific, Task=task)

    r = generate_gpt_response(user_content)
    parsed_res = parse_concise_content(r)

    return parsed_res

def generate_refined_response(initial_response, task = ""):
    refinement_user_content = generate_user_content_for_correcting(initial_response, task)
    r = generate_gpt_response(refinement_user_content)
    parsed_res = parse_concise_content(r)

    return parsed_res

def generate_input(OBJECTS, RECEPTACLES, Task):
    objects = ",".join(OBJECTS)
    receptacles = ",".join(RECEPTACLES)
    user_input = generate_input_from_task(objects, receptacles, Task)
    res = generate_gpt_response(user_input)
    return parse_concise_content(res)

if __name__ == "__main__":
    OBJECTS = OBJECTS_SINGULAR
    # RECEPTACLES = list(RECEPTACLES)[:20] + ["MicrowaveType"]
    RECEPTACLES = list(RECEPTACLES)
    OUTPUT_EXAMPLE = ["(canContain BedType CellPhoneType)", "(canHeat MicrowaveType PlateType)"]
    Task = "Find apple"
    Task = "Heat Apple"

    # task_related_input = generate_input(OBJECTS, RECEPTACLES, Task)
    # print("task_related_input: \n", task_related_input)
    OBJECTS = "apple, knife, microwave, pot, stoveburner, countertop, bowl, spoon, fork, plate, cup, mug, water, soapbottle, dishsponge, papertowel, coffeemachine, fridge, sink, stoveknob".split(",")
    Receptacles = "microwave, pot, bowl, plate, cup, mug, sink, stoveburner, fridge, countertop".split(",")
    
    # # initial_res = generate_initial_response(OBJECTS, RECEPTACLES, OUTPUT_EXAMPLE, COUNT = 100)
    initial_res = generate_initial_response(OBJECTS, RECEPTACLES, OUTPUT_EXAMPLE, COUNT = 50, Task_specific=True, task=Task)
    # # initial_res = ['1. (canContain Shelf alarmclock)', '2. (canContain Pot apple)', '3. (canContain Sink apple)', '4. (canContain SideTable alarmclock)', '5. (canContain Shelf apple)', '6. (canContain Shelf basketball)', '7. (canContain Pan apple)', '8. (canContain SideTable armchair)', '9. (canContain Shelf armchair)', '10. (canHeat MicrowaveType apple)', '11. (canContain Shelf baseballbat)', '12. (canContain SideTable baseballbat)', '13. (canContain Pot basketball)', '14. (canHeat Pan apple)', '15. (canContain Pan basketball)', '16. (canContain SideTable basketball)', '17. (canContain Pot baseballbat)', '18. (canContain Shelf baseballbat)', '19. (canContain SideTable alarmclock)', '20. (canContain Pan baseballbat)']
    print("initial res: \n", initial_res)
    # # refined_res = generate_refined_response(initial_res)
    refined_res = generate_refined_response(initial_res, task = Task)
    print("refined res: \n", refined_res)