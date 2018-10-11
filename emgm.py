import smtplib


s = smtplib.SMTP("smtp.gmail.com", 587)


s.starttls()


s.login("adityasingh33378@gmail.com","aditya1718"


message = 'hii'


s.sendmail("adityasingh33378@gmail.com","tharunmuduru@gmail.com",message)


s.quit()