import smtplib  
from email.mime.text import MIMEText  
mailto_list=['1187816874@qq.com']          
mail_host="smtp.163.com"             
mail_user="13937134284@163.com"                       
mail_pass="psqandzpm.com"                            
mail_postfix="163.com"                    
def send_mail(to_list,sub,content):  
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)                
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)                             
        server.login(mail_user,mail_pass)         
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  
for i in range(1):                          
    if send_mail(mailto_list,"iphone","iphone is 152652152415"):
        print "done!"  
    else:  
        print "failed!"  
