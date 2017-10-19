



import datetime as dt
import pandas as pd
time = "2013-05-08T10:00:00"
# con = dt.datetime.strptime(time,"%d/%m/%Y %H:%M").strftime("%Y%m%d%H%M%S000")
# con = dt.datetime.strptime(time,"%d/%m/%Y %H:%M").timestamp()
con = dt.datetime.strptime(time,"%Y-%m-%dT%H:%M:%S").timestamp()


print(con)
post = pd.read_csv("Votes.csv")
time = post["CreationDate"]



for i in range(len(time)):
	if len(time[i])<23:
		con = dt.datetime.strptime(time[i],"%d/%m/%Y %H:%M").timestamp()
		# post.CreationDate[post.CreationDate=="time[i]"] = con
		post.set_value(i,'CreationDate',con) 
	elif len(time[i])==23:
		con = dt.datetime.strptime(time[i][:-4],"%Y-%m-%dT%H:%M:%S").timestamp()
		post.set_value(i,'CreationDate',con) 

post.to_csv('v_time.csv')