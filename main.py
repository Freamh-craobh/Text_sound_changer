from rules import rules_parser, rules_applier

with open("input.txt", "r") as file:
    data = file.read()
    print(data)

with open("rules.txt", "r") as file:
    rules = [i.strip() for i in file.readlines()]
    print(rules)

clean = rules_parser(rules)
print(rules_applier(clean, data))
