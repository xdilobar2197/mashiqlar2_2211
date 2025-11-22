# mashiqlar2_2211

#2 - masala 1 ji iwlanishi
def bmi_hisoblay(boy, vazn):
    if boy <= 0 or vazn <= 0:
        print('Xato: boy yoki vazn notogri.')
        return
    bmi = vazn / (boy * boy)

    if bmi < 18.5:
        holat = 'Ozganlik'
    elif  bmi < 25:
        holat = 'Norm'
    elif 25 < bmi < 30:
        holat = 'Ortacha vazn'
    else:
        holat = 'semizlik'

        print(f' BMI = {bmi: 2f}, {holat}')

# 2 - masalani 2ji iwlaniwi
def bmi_hisobla(boy, vazn):
    if boy <= 0:
        print('Xato boy')
    else:
        bmi = vazn / (boy * boy)

    if bmi < 18.5:
        print('Ozganlik')
    elif 18.5 <= bmi < 25:
        print('No\'rmal')
    elif 25 <= bmi < 30:
        print('Ortacha vazn')
    elif bmi >= 30:
        print('Semizlik')

bmi_hisobla(1.75, 60)

bmi_hisobla(1.21, 70)

bmi_hisobla(1.35, 30)

bmi_hisobla(1.8, 90)
