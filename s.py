#Set only can take unique elements
#1
rainfall_chennai = {120, 140, 160, 180}
rainfall_madurai = {110, 130, 150, 180}
rainfall_coimbatore = {100, 120, 180, 200}
chennai_madurai = rainfall_chennai | rainfall_madurai
print("Unique rainfall:",chennai_madurai)
#2
merged_union = rainfall_chennai | rainfall_madurai | rainfall_coimbatore
merged_update = set(rainfall_chennai)
merged_update.update(rainfall_madurai, rainfall_coimbatore)
#3
common_all = rainfall_chennai & rainfall_madurai & rainfall_coimbatore
print(common_all)
#4
unique_chennai = rainfall_chennai - rainfall_madurai - rainfall_coimbatore
print(unique_chennai)
#5
chennai_madurai = rainfall_chennai & rainfall_madurai
chennai_coimbatore = rainfall_chennai & rainfall_coimbatore
madurai_coimbatore = rainfall_madurai & rainfall_coimbatore
atleast_two = chennai_madurai | chennai_coimbatore | madurai_coimbatore
print(atleast_two)
#6
increased_chennai = {x + 10 for x in rainfall_chennai}
print(increased_chennai)