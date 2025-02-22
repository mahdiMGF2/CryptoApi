from fastapi import APIRouter,Response
from pydantic import BaseModel
from app.Currency.Tron import TronManage
from tronpy.keys import PrivateKey
import json
RouterTron = APIRouter()




class TransferData(BaseModel):
    from_address:str = "TBwqzSg7e7emCeLGAjtu6Sx67aUN43stsP"
    to_address:str = "TBwqzSg7e7emCeLGAjtu6Sx67aUN43stsP"
    amount:int = 1
    private_key:str = "f829093442a1b593480321082489fd493e74379452ef9b05c1a418c83893e456"

TronManager = TronManage()
@RouterTron.post(path='/GenerateWallet',tags=['Tron'],name='Generate Wallet Tron')
async def GenerateWallet():
    WalletNew = TronManager.GenerateWallet()
    return {
            "wallet_address": WalletNew['wallet_address'],
            "private_key": str(WalletNew['private_key']),
        }



@RouterTron.get(path='/TronAccount',tags=['Tron'],name='Get Tron Account details')
async def TronDetails(address:str,response:Response):
    WalletNew = TronManager.TronAccount(address)
    if not WalletNew:
        response.status_code = 404
    return WalletNew


@RouterTron.post(path='/TransferMoney',tags=['Tron'],name='Transfer Money Tron')
async def TransferMoneyTron(data:TransferData,response:Response):
    try:
        result = TronManager.TransferMoney(from_address=data.from_address,to_address=data.to_address,amount=data.amount,private_key=PrivateKey(bytes.fromhex(data.private_key)))
    except Exception as e:
        return {"msg" : e}
    if 'msg' in result:
        return {"msg" : str(result['msg'])}

    return result