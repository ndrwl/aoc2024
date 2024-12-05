from sys import stdin

rules = []
updates = []

loading_rules = True

for line in stdin:
    if len(line.strip()) == 0:
        loading_rules = False
        continue

    if loading_rules:
        x_str, y_str = line.split('|')
        rules.append([int(x_str), int(y_str)])
    else:
        update_str = line.split(',')
        updates.append([int(page_str) for page_str in update_str])

def mid_page(update):
    return update[int(len(update) / 2)]

def make_page_to_order_map(update):
    map = {}
    for page_number in range(len(update)):
        map[update[page_number]] = page_number
    return map

def follows_rules(update):
    global rules

    page_map = make_page_to_order_map(update)

    for (rule_page1, rule_page2) in rules:
        if not rule_page1 in page_map or not rule_page2 in page_map:
             continue
        if page_map[rule_page1] > page_map[rule_page2]:
            return False
    return True

def fix(update):
    global rules

    page_map = make_page_to_order_map(update)
    changes_made = True

    while changes_made:
        changes_made = False

        for (rule_page1, rule_page2) in rules:
            if not rule_page1 in page_map or not rule_page2 in page_map:
                 continue

            rule_page1_pos = page_map[rule_page1]
            rule_page2_pos = page_map[rule_page2]

            if rule_page1_pos > rule_page2_pos:
                update[rule_page2_pos] = rule_page1
                update[rule_page1_pos] = rule_page2

                page_map[rule_page1] = rule_page2_pos
                page_map[rule_page2] = rule_page1_pos

                changes_made = True

    return update

sum_follows = 0
sum_fixed = 0

for update in updates:
    if follows_rules(update):
        sum_follows += mid_page(update)
    else:
        sum_fixed += mid_page(fix(update))

print(sum_follows)
print(sum_fixed)
