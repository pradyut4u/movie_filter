import csv

with open('mov.csv',encoding = "utf8")as f:
    csvreader = csv.reader(f)
    movielist = list(csvreader)
    headers = movielist[0]
    datamov = movielist[1:]

headers.append("movie_poster")

print(len(headers))
            

with open("finalmovie.csv","a+",encoding = "utf8")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open('movie_links.csv', encoding = "utf8")as f:
    csvreader = csv.reader(f)
    movielist2 = list(csvreader)
    datamov2 = movielist[1:]

for i in datamov:
    posterfound = any(i[8] in j for j in datamov2)
    if posterfound == True:
        for j in datamov2:
            if j[0] == i[8]:
                i.append(j[1])
                if len(i) == 28:
                    with open("finalmovie.csv","a+",encoding = "utf8")as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(i)