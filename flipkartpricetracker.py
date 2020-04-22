import requests
from bs4 import BeautifulSoup
import smtplib

url=r"https://www.flipkart.com/realme-6-comet-blue-64-gb/p/itm212944b2e7fb0?pid=MOBFPCX7F9NBPRRT&lid=LSTMOBFPCX7F9NBPRRTSHD9FQ&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_1_4.bannerX3.BANNER_mobile-phones-store_20JI2N7V980X&fm=neo%2Fmerchandising&iid=0ea6ef51-6d12-4465-8491-399f4c41fdd3.MOBFPCX7F9NBPRRT.SEARCH&ppt=browse&ppn=browse&ssid=ecwmu0xs4w0000001587584910437"
header={
    "user-agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}

def sendmail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('speaktoarivoli@gmail.com','vsmxwwopvzsbhmtl')
    subject="Hey man the price fell down !!"
    body=f"Check the amazon link  {url}"
    message=f"subject:{subject}\n\n{body}"
    server.sendmail(
        "speaktoarivoli@gmail.com",
        "speaktomrarivoli@gmail.com",
        message
    )
    print(" # Email has been sent #")

    server.quit()


def checkprice():

    page=requests.get(url,headers=header)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find('span',class_='_35KyD6').text

    flipprice=soup.find('div',class_='_1vC4OE _3qQ9m1').text
    flipprice=flipprice[1:]
    splitprice=flipprice.split(',')
    finalprice=splitprice[0]+splitprice[1]
    finalprice=int(finalprice)
    if finalprice<13998:
        sendmail()
    else:
        pass

checkprice()