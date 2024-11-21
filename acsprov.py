
import subprocess

import requests

import json
import const
from log import Logger

logger = Logger.getLogger('acs', 'logs/acs')
headers = {
    'Content-Type': 'application/json'
}

class AcsProvision:
    def acsCreate(data , ref,pwd):
        ##VOCIE
        try:
            voicedata ={"serialNumber": data['FTTH_ONT_SN'],
                "bbUserName": data['IMS_USERID'],
                "voicePassword": pwd}

            resultvoice = requests.request("POST", const.acs_voice_create,headers=headers, data=json.dumps(voicedata),)
            resvoice = json.loads(resultvoice.text)
            logger.info(ref+"  " + str(voicedata))
            logger.info(ref+"  " + str(resvoice))

            if resvoice['result'] == 'Success':
            
                ##BB PASSWD
                if not data['BBCOUNT'] == '0':
                    bbpwd ={"bbUserName": data['IMS_USERID'],
                            "refId":"RIBE"+str(ref)}

                    resultbbpwd = requests.request("POST", const.acs_bb_pwd,headers=headers, data=json.dumps(bbpwd))
                    resbbpwd = json.loads(resultbbpwd.text)
                    logger.info(ref+"  " + str(bbpwd))
                    logger.info(ref+"  " + str(resbbpwd))

                    if resbbpwd['status'] == 'success':
                        ##BB
                        bbdata ={"serialNumber": data['FTTH_ONT_SN'],
                                    "bbUserName": data['IMS_USERID'],
                                    "bbPassword": resbbpwd['response'],
                                    "bbStatus": "YES"}

                        resultbb = requests.request("POST", const.acs_bb_create,headers=headers, data=json.dumps(bbdata))
                        resbb = json.loads(resultbb.text)
                        logger.info(ref+"  " + str(bbdata))
                        logger.info(ref+"  " + str(resbb))

                        if resbb['result'] == 'Success':
                            responsedata = {"result":"success","message": "User Create Operation Completed"}
                        else:
                            responsedata = {"result":"failed","message": "ACS BB CREATE"}
                    else:
                        responsedata = {"result":"failed","message": "ACS BB PASSWSD"}
                else:
                    bbdata ={"serialNumber": data['FTTH_ONT_SN'],
                             "bbUserName": data['IMS_USERID'],
                             "bbPassword": "",
                             "bbStatus": "NO"}

                    resultbb = requests.request("POST", const.acs_bb_create,headers=headers, data=json.dumps(bbdata))
                    resbb = json.loads(resultbb.text)
                    logger.info(ref+"  " + str(bbdata))
                    logger.info(ref+"  " + str(resbb))

                    try:
                        if resbb['result'] == 'Success':
                            responsedata = {"result":"success","message": "User Create Operation Completed"}
                        else:
                            responsedata = {"result":"failed","message": "ACS BB CREATE"}
                    except Exception as e:
                        logger.error("acs prov BB")
                        logger.error(e)
            else:
                responsedata = {"result":"failed","message": "ACS VOICE CREATE"}

            
        except Exception as e:
            logger.error("acs prov create")
            logger.error(e)
        
        
        logger.info(ref+"  " + str(responsedata))
        return responsedata
            
    def acsDelete(data , ref):
        voicedata ={"serialNumber": data['FTTH_ONT_SN'],
                    "bbUserName": data['IMS_USERID']}

        resultvoice = requests.request("POST", const.acs_delete,headers=headers, data=json.dumps(voicedata),)
        resvoice = json.loads(resultvoice.text)
        logger.info(ref+"  " + str(voicedata))
        logger.info(ref+"  " + str(resvoice))

        if resvoice['status'] == 'success':
            responsedata = {"result":"success","message": ""}
        else:
            responsedata = {"result":"failed","message": "ACS DELETE"}

        logger.info(ref+"  " + str(responsedata))
        return responsedata