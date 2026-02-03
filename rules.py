import re


def rules_parser(rules_list):
    """
    Returns a list of rules, in the format of a list of lists:
    where each inner list is [input, output, environment], and each rule is an item in the outer list.
    
    :param rules_list: list of rules in the form of one rule per item, needs input output and environemnt
    """
    rules_cleaned = []
    for rule in rules_list:
        if rule.count("_") != 1:
            raise ValueError(f"Rule '{rule}' does not have exactly one '_'")
        parts = rule.split("/")
        rules_cleaned.append(parts)
    return rules_cleaned

def env_to_regex(environment, input_pattern):
    #environment = environment.replace("#", r"\b").replace("$", r"\b")
    left, right = environment.split("_")
    LEFT_BOUND  = r"(?:(?<=^)|(?<=\s))"
    RIGHT_BOUND = r"(?:(?=$)|(?=\s))"
    def replace_boundaries(left, side):
        out = []
        for char in left:
            if char == "#" or "$":
                out.append(LEFT_BOUND if side == "L" else RIGHT_BOUND)
            else:
                out.append(re.escape(char))
        return "".join(out)
    left = replace_boundaries(left, "L")
    right = replace_boundaries(right, "R")
    environment = left + "_" + right

    if input_pattern == "":
        pattern = "^" + left + r"([^\s]+)" + right + "$"
    else:    
        pattern = "^" + environment.replace("_", re.escape(input_pattern)) + "$"
    return pattern
    


def rules_applier(clean_rule_list, input_data):
    """
    Applies the rules to the input data.
    
    :param clean_rule_list: list of rules in the format returned by rules_parser
    :param input_data: the input data to be processed
    """
    output = []
    for item in input_data:
        for rule in clean_rule_list:
            input_pattern, output_pattern, environment = rule
            pattern = env_to_regex(environment, input_pattern)
            if re.match(pattern, item):
                #item = item.replace(input_pattern, output_pattern)
                item = re.sub(pattern, output_pattern, item)
        output.append(item)

    return "".join(output)