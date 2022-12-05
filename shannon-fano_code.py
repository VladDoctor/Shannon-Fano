message = "Уинстон вынул из кармана монету в двадцать пять центов. " \
          "И на ней мелкими, но четкими буквами выбиты те же три лозунга, " \
          "а на другой стороне лик Старшего Брата. Даже с монеты его глаза следят за тобой. " \
          "Эти глаза везде — на деньгах, марках, обложках книг, транспаран- тах, " \
          "плакатах, сигаретных пачках. Они наблюдают, а голос обволакивает. " \
          "Во сне и наяву, на работе и за едой, дома и на улице, в ванне или в постели " \
          "— не скрыться. Нет ничего своего, лишь несколько кубических сантиметров " \
          "внутри черепной коробки."

ensemble = {}

for m in message:
    if not m.lower() in ensemble.keys():
        ensemble[m.lower()] = 0
    else:
        ensemble[m.lower()] += 1

for key in ensemble.keys():
    ensemble[key] = round(ensemble[key] / len(message),3)

three = {}

ensemble = dict(sorted(ensemble.items(), key=lambda item: item[1]))

def binary_group(sub_ensemble, code):
    sub_ensemble = dict(sorted(sub_ensemble.items(), key=lambda item: item[1]))
    if len(list(sub_ensemble.values())) > 2:
        sum_v = sum(list(sub_ensemble.values()))
        barrier = round(sum_v/2,3)

        sum1_gr = 0
        groups = [{},{}]

        for key in sub_ensemble.keys():
            sum1_gr += sub_ensemble[key]
            if sum1_gr <= barrier:
                groups[1][key] = sub_ensemble[key]
            else:
                groups[0][key] = sub_ensemble[key]

        for group in groups:
            three[len(list(three.keys())) + 1] = groups
            if len(list(group.keys())) == 2:
                for key in group.keys():
                    three[len(list(three.keys())) + 1] = {key : group[key]}
            else:
                binary_group(group)
    else:
        return sub_ensemble



binary_group(ensemble, 0)

for key in three.keys():
    print(key, '=', three[key])
