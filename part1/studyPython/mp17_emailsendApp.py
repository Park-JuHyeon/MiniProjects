# 이메일 보내기 앱
import smtplib  # 메일전송 프로토콜 (simple mail transfer protocol)
from email.mime.text import MIMEText  

send_email = '' # 보내는 이메일
send_pass = ''  # 비밀번호

recv_email = 'wngus2tp@gmail.com'

smtp_name = 'smtp.naver.com'
smtp_port = 587  # 포트번호

text = '''메일 내용입니다 => 주현아 공부좀 하자 진짜 이번주부터..
진짜 할때 됐다 하..
'''

msg = MIMEText(text)
msg['Subject'] = '메일 제목입니다'
msg['From'] = send_email  # 보내는 사람
msg['to'] = recv_email  # 받는사람
print(msg.as_string())

mail = smtplib.SMTP(smtp_name, smtp_port)  # SMTP 객체 생성
mail.starttls()  # 전송계층 
mail.login(send_email, send_pass)
mail.sendmail(send_email, recv_email, msg = msg.as_string())
mail.quit()
print('전송 완료')



