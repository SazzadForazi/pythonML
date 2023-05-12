import csv

with open('csv1.csv') as f1, open('csv2.csv') as f2:
    csv1 = list(csv.reader(f1))
    csv2 = list(csv.reader(f2))


csv1_key_col = 1  
csv2_key_col = 0  

csv2_dict = {}
for row in csv2:
    # print(row)
    csv2_dict[row[csv2_key_col]] = row

filtered_rows = []
for row in csv1:
    if row[csv1_key_col] in csv2_dict:
        # filtered_rows.append(row + csv2_dict[row[csv1_key_col]][2:])
        filtered_rows.append(csv2_dict[row[csv1_key_col]][0:])

print(filtered_rows)
    #     for i in range(len(filtered_rows)):
    #         if(filtered_rows[i]==','):
    #             filtered_rows[i]=';'
    # print(filtered_rows)    
    
# with open('filtered2.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows(filtered_rows)
