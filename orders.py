import math

print("PRODUCT 1: 20$\nPRODUCT 2: 40$\nPRODUCT 3: 50$")
p1 = int(input("How many of product 1 do you need? "))
p2 = int(input("How many of product 2 do you need? "))
p3 = int(input("How many of product 3 do you need? "))
tot_quantity = p1 + p2 + p3
total = 20 * p1 + 40 * p2 + 50 * p3
d1 = d2 = d3 = wrap = flag = tot1 =tot2 =tot3 =tot4 =0

# ///////flat 10///////
if total > 200:
    tot1 = total - (total * 0.1)

# ///////bulk5///////
if p1 > 10 or p2 > 10 or p3 > 10:
    if p1 > 10 and p2 > 10 and p3 > 10:
        d1 = p1 * 20
        d2 = p2 * 40
        d3 = p3 * 50
        tot2 = d1 - (d1 * 0.05) + d2 - (d2 * 0.05) + d3 - (d3 * 0.05)
    elif p1 > 10 and p2 > 10:
        d1 = p1 * 20
        d2 = p2 * 40
        tot2 = d1 - (d1 * 0.05) + d2 - (d2 * 0.05) + p3 * 50
    elif p2 > 10 and p3 > 10:
        d2 = p2 * 20
        d3 = p3 * 40
        tot2 = p1 * 20 + d2 - (d2 * 0.05) + d3 - (d3 * 0.05)
    elif p1 > 10 and p3 > 10:
        d1 = p1 * 20
        d3 = p3 * 40
        tot2 = d1 - (d1 * 0.05) + p2 * 40 + d3 - (d3 * 0.05)
    elif p1 > 10:
        d1 = p1 * 20
        tot2 = d1 - (d1 * 0.05) + 40 * p2 + 50 * p3
    elif p2 > 10:
        d2 = p2 * 40
        d5 = d2 - (d2 * 0.05)
        tot2 = 20 * p1 + d5 + 50 * p3
    elif p3 > 10:
        d3 = p3 * 50
        d5 = d3 - (d3 * 0.05)
        tot2 = 20 * p1 + 40 * p2 + d5
# ///////bulk10///////
if tot_quantity > 20:
    tot3 = total - (total * 0.1)

# ///////tiered 50///////
if tot_quantity>30:
    if(p1>15 and p2>15 and p3>15):
        e1=p1-15
        e2=p2-15
        e3=p3-15
        tot4=(20*15 + 40*15 + 50*15 + e3*10 +e2*20 + e3*25)
    elif(p1>15 and p2>15):
        e1=p1-15
        e2=p2-15
        tot4=(20*15 + 40*15 + 50*p3 + e1*10 + e2*20)
        print(tot4)
    elif(p2>15 and p3>15):
        e2=p2-15
        e3=p3-15
        tot4=(20*p1 + 40*15 + 50*15 + e2*20 + e3*25)
        print(tot4)
    elif(p1>15 and p3>15):
        e1=p1-15
        e3=p3-15
        tot4=(20*15 + 40*p2 + 50*15 + e1*10 + e3*25)
        print(tot4)
    elif(p1>15):
        e1=p1-15
        tot4=(20*15 + 40*p2 + 50*p3 + e1*10)
        print(tot4)
    elif(p2>15):
        e2=p2-15
        tot4=(20*p1+ 40*15 + 50*p3 + e2*20)
        print(tot4)
    elif(p3>15):
        e3=p3-15
        tot4=(20*p1 + 40*p3 + 50*15 + e3*25)
        print(tot4)
benifits=min(value for value in (tot1, tot2, tot3, tot4, total) if value != 0)
if (benifits==tot1):
    flag=1
elif(benifits==tot2):
    flag=2
elif(benifits==tot3):
    flag=3
elif(benifits==tot4):
    flag=4
num_packages = math.ceil(tot_quantity / 10)
shipping_charge = num_packages * 5

gift=str(input("Do you want a gift wrap? (costs 1$) y/n : "))
if gift=="y":
    wrap=1
else:
    wrap=0
print(f"tot1: {tot1}, tot2: {tot2}, tot3: {tot3}, tot4: {tot4}")
print("Products       quantity   price ")
print(f"Product 1:  \t {p1}\t  {(p1*20)}$")
print(f"Product 2:  \t {p2}\t  {(p2*40)}$")
print(f"Product 3:  \t {p3}\t  {(p3*50)}$")
print(f"SUB TOTAL:        \t {total}\n")
if(flag==1):
    print("Flat_10_discount is applied.")
    print(f"The discount amount is  : {total-tot1}$")
elif(flag==2):
    print("Bulk_5_discount is applied.")
    print(f"The discount amount is  : {total-tot2}$")
elif(flag==3):
    print("Bulk_10_discount is applied.")
    print(f"The discount amount is  : {total-tot3}$")
elif(flag==4):
    print("Tiered_50_discount is applied.")
    print(f"The discount amount is  : {total-tot4}$")
else:
    print("Not eligible for any Discounts.")

print(f"shipping fee \t\t: {shipping_charge}$" )
print(f"Gift Wrap fee \t\t: {wrap}$")
print(f"Cost\t\t\t: {benifits+shipping_charge+wrap}$")
