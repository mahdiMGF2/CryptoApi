from tronpy import Tron
from tronpy.keys import PrivateKey
import secrets,requests,json,logging,os,dotenv
from tronpy.providers import HTTPProvider


#load env file
dotenv.load_dotenv()


class TronManage():
    def __init__(self):
        self.key = os.getenv('ApiKeyTronpy')
        self.tron = Tron(provider=HTTPProvider("https://api.trongrid.io", api_key=self.key))
        self.private_key = PrivateKey
        self.secret = secrets
    def __repr__(self):
        return "Wallet Info Api"
    def GenerateWallet(self):
        private_key = self.private_key(self.secret.token_bytes(32))
        wallet_address = private_key.public_key.to_base58check_address()
        return {
            "wallet_address": wallet_address,
            "private_key": private_key,
        }
    def TronAccount(self,address:str):
        url = f"https://api.trongrid.io/v1/accounts/{address}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()["data"]
            if data:
                return data[0]
            return None
        return None
    def TransferMoney(self,from_address:str,to_address:str,amount:int,private_key:PrivateKey):
        try:
            txn = (
                self.tron.trx.transfer(
                    from_=from_address,
                    to=to_address,
                    amount=amount*1000000
                ).build().sign(private_key)
            )
            result = txn.broadcast()
            return result
        except Exception as e:
            logging.error(e)
            return {"msg" : e}
