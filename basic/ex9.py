from datetime import datetime

exam_st_date = (11, 12, 2014)
str1=str(exam_st_date[0]) + "/" + str(exam_st_date[1]) + "/" + str(exam_st_date[2])

print(exam_st_date)

exam_date=datetime.strptime(str1,"%d/%m/%Y")
print(exam_date)

