#!/usr/bin/python
#coding:utf-8
import urllib.request
import gzip
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

print('------Weather Forecast------')
def get_weather_data() :
    #city_name = input('name of city: ')
    city_name = '北京'
    #city_name = '长沙'
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)
    url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
    #网址1只需要输入城市名，网址2需要输入城市代码
    #print(url1)
    weather_data = urllib.request.urlopen(url1).read()
    #读取网页数据
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    #解压网页数据
    weather_dict = json.loads(weather_data)
    #将json数据转换为dict数据
    return weather_dict

def show_weather(weather_data):
    weather_dict = weather_data 
    #将json数据转换为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        print('你输入的城市名有误，或者天气中心未收录你所在城市')
    elif weather_dict.get('desc') =='OK':
        forecast = weather_dict.get('data').get('forecast')
        b_flag = '***********************************' + '\n'
        print('***********************************')
        print('城市：',weather_dict.get('data').get('city'))
        print('温度：',weather_dict.get('data').get('wendu')+'℃ ')
        print('感冒：',weather_dict.get('data').get('ganmao'))
        print('风向：',forecast[0].get('fengxiang'))
        print('风级：',forecast[0].get('fengli'))
        print('高温：',forecast[0].get('high'))
        print('低温：',forecast[0].get('low'))
        print('天气：',forecast[0].get('type'))
        print('日期：',forecast[0].get('date'))
        content0 = weather_dict.get('data').get('city') + '\n'
        content1 = weather_dict.get('data').get('wendu')+'℃ ' + '\n'
        content2 = weather_dict.get('data').get('ganmao') + '\n'
        content3 = forecast[0].get('fengxiang') + '\n'
        content4 = forecast[0].get('fengli') + '\n'
        content5 = forecast[0].get('high') + '\n'
        content6 = forecast[0].get('low') + '\n'
        content7 = forecast[0].get('type') + '\n'
        content8 = forecast[0].get('date') + '\n'
        content = b_flag+content0+content1+content2+content3+content4+content5+content6+content7+content8+b_flag
        
        #next four day
#        for i in range(1,5):
#            print('日期：',forecast[i].get('date'))
#            print('风向：',forecast[i].get('fengxiang'))
#            print('风级：',forecast[i].get('fengli'))
#            print('高温：',forecast[i].get('high'))
#            print('低温：',forecast[i].get('low'))
#            print('天气：',forecast[i].get('type'))
#            print('--------------------------')
    print('***********************************')
    return(forecast[0].get('type'), content)

def sendMail(body):
    smtp_server = 'smtp.qq.com'



    from_name = 'Weather Monitor'
    subject = "It's Raining Today!"
    mail = [
        "From: %s <%s>" % (from_name, from_mail),
        "To: %s" % ','.join(to_mail),
        "Subject: %s" % subject,
        "",
        body
        ]
    msg = '\n'.join(mail)
    print(msg)
    try:
        s = smtplib.SMTP_SSL(smtp_server,465)
        s.login(from_mail, mail_pass)
        s.sendmail(from_mail, to_mail, msg.encode('utf-8'))
        print("邮件发送成功")
        s.quit()
    except smtplib.SMTPException as e:
        print("Error: "+e)
if __name__ == "__main__":
    ww,content = show_weather(get_weather_data())
    print('ww is ' + ww)
    if '雨' in ww:
        sendMail(content)
        print("DONE!")

