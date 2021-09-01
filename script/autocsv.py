import csv
import os


source_path = './label/'
save_path = './label_new/'
CsvFile = os.listdir(source_path)


if not os.path.exists(save_path):
    os.mkdir(save_path)
for leng in range(len(CsvFile)):

    with open(source_path+CsvFile[leng],'rt',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        column =[row[0] for row in reader]
        # hist_number = [row[1] for row in reader]
        # print(len(hist_number))
        for i in range(len(column)):
            if('ppm' in column[i]):
                column[i] = column[i].replace('.ppm', '')

            else:
                column[i] = column[i]

            # print(column[i])

    with open(save_path+CsvFile[leng],'wt',encoding='utf-8',newline='') as newfile:
        writer = csv.writer(newfile)
        for col in zip(column):
            writer.writerow(col)
        newfile.close()
    print(str(leng)+': Finished')
