import fractions

digit_cancelling_fracs = []
for i in range(1,100):
    for j in range(1,i):
        #print(repr(x))
        for k in range(1,10):
            if str(i).count(str(k)) == str(j).count(str(k)):
                i_new = str(i).replace(str(k),'')
                j_new = str(j).replace(str(k),'')
                if not((j_new == '0') or (i_new == '') or (j_new == '')):
                    if len(str(i)) == len(str(i_new)):
                        continue
                    elif i/j == int(i_new)/int(j_new):
                        digit_cancelling_fracs.append(fractions.Fraction(j,i))

print(digit_cancelling_fracs)

frac_product = 1
for frac in digit_cancelling_fracs:
    frac_product *= frac

print(frac_product)