def get_mask_card_number(card):
    card = str(card)
    return card[:4] + ' ' + card[4:6] + '**' + ' ' + '****' + ' ' + card[12:]
def get_mask_account(mask):
    mask = str(mask)
    return '**' + mask[16:]
f = 12341234123412341234
print(get_mask_account(f))


C = input()
counter = 0
spl = C.split()
for i in spl:
    if i.isalpha():
        counter += 1
print(counter)
