from gpt_api_helpers import *
from constants import OBJECTS_SINGULAR, RECEPTACLES

def generate_initial_response(OBJECTS, RECEPTACLES, OUTPUT_EXAMPLE, COUNT=20):
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

    RELATIONSHIPS = ["canContain", "canHeat"]
    relationships = ",".join(RELATIONSHIPS)

    user_content = generate_user_content_for_gpt(objects, receptacles, output_example, relationships, COUNT)
    r = generate_gpt_response(user_content)
    parsed_res = parse_concise_content(r)

    return parsed_res

def generate_refined_response(initial_response):
    refinement_user_content = generate_user_content_for_correcting(initial_response)
    r = generate_gpt_response(refinement_user_content)
    parsed_res = parse_concise_content(r)

    return parsed_res

if __name__ == "__main__":
    OBJECTS = OBJECTS_SINGULAR[:5] 
    RECEPTACLES = list(RECEPTACLES)[:5] + ["MicrowaveType"]
    OUTPUT_EXAMPLE = ["(canContain BedType CellPhoneType)", "(canHeat MicrowaveType PlateType)"]

    initial_res = generate_initial_response(OBJECTS, RECEPTACLES, OUTPUT_EXAMPLE, COUNT = 20)
    # initial_res = ['1. (canContain Shelf alarmclock)', '2. (canContain Pot apple)', '3. (canContain Sink apple)', '4. (canContain SideTable alarmclock)', '5. (canContain Shelf apple)', '6. (canContain Shelf basketball)', '7. (canContain Pan apple)', '8. (canContain SideTable armchair)', '9. (canContain Shelf armchair)', '10. (canHeat MicrowaveType apple)', '11. (canContain Shelf baseballbat)', '12. (canContain SideTable baseballbat)', '13. (canContain Pot basketball)', '14. (canHeat Pan apple)', '15. (canContain Pan basketball)', '16. (canContain SideTable basketball)', '17. (canContain Pot baseballbat)', '18. (canContain Shelf baseballbat)', '19. (canContain SideTable alarmclock)', '20. (canContain Pan baseballbat)']
    print("initial res: \n", initial_res)
    refined_res = generate_refined_response(initial_res)
    print("refined res: \n", refined_res)