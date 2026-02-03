from rules import rules_parser, rules_applier

with open("input.txt", "r") as file:
    data = file.read()
    print(data)

with open("rules.txt", "r") as file:
    rules = [i.strip() for i in file.readlines()]
    print(rules)

clean = rules_parser(rules)

input_output = False

with open("output.txt", "w") as file:
    result = rules_applier(clean, data)
    if input_output:
        for i, x in zip(result.split(sep="\n"), data.split(sep="\n")):
            file.write(f"{x} -> {i}\n")
    else:
        for line in result:
            file.write(line)
