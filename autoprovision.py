import random

from log import Logger
from nmsprov import NmsProvision
from imsprov import ImsProvision
from acsprov import AcsProvision

logger = Logger.getLogger('autoprov', 'logs/autoprov')

def random_pwd(length):
    sample_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  # define the specific string
    # define the condition for random string
    return ''.join((random.choice(sample_string)) for x in range(length))

class AutoProvision:
    def autoProvCreate(req, ref):
        logger.info(ref+"  " + str(req))

        pwd = random_pwd(15)
        req['PWD'] = str(pwd)
        logger.info(ref+"  random key " + str(pwd))

        if not req['FTTH_ONT_SN'].startswith(("ALCL", "4857","HWT", "ZTE")):

            ## NMS
            resultnms = NmsProvision.acsNmsProvCreate(req, ref)
            logger.info(ref+"  ACS NMS result  " + str(resultnms))
            if resultnms['result'] == 'failed':
                return resultnms

            ## IMS
            resultudrhss = ImsProvision.udrHssCreate(req, ref)
            logger.info(ref+"  UDR HSS result  " + str(resultudrhss))
            if resultudrhss.split('#')[0] == '0':
                resultudrens = ImsProvision.udrEnsCreate(req, ref)
                logger.info(ref+"  UDR ENS result  " + str(resultudrens))
                if resultudrens.split('#')[0] == '0':
                    resultimsats = ImsProvision.imsAtsCreate(req, ref)
                    logger.info(ref+" IMS ATS result  " + str(resultimsats))
                    if resultimsats.split('#')[0] == '0':
                        resultims = {"result":"success","message": ""}
                    else:
                        resultims = {"result":"failed","message": "ADD_IMS_ATS"}
                else:
                    resultims = {"result":"failed","message": "ADD_UDR_ENS"}
            else:
                resultims = {"result":"failed","message": "ADD_UDR_HSS"}

            logger.info(ref+"  IMS result  " + str(resultims))
            if resultims['result'] == 'failed':
                return resultims

            ## ACS
            resultacs = AcsProvision.acsCreate(req, ref,pwd)
            logger.info(ref+"  ACS result" + str(resultacs))
            return resultacs
        else:
            print("OLD")
            return "success"

    def autoProvDelete(req, ref):
        logger.info(ref+"  " + str(req))

        if not req['FTTH_ONT_SN'].startswith(("ALCL","4857","HWT","ZTE")):

            ## ACS
            resultacs = AcsProvision.acsDelete(req, ref)
            logger.info(ref+"  ACS DELETE result" + str(resultacs))
            if resultacs['result'] == 'failed':
                return resultacs

            ## NMS
            resultnms = NmsProvision.acsNmsProvDelete(req, ref)
            logger.info(ref+"  ACS NMS DELETE result  " + str(resultnms))
            if resultnms['result'] == 'failed':
                return resultnms

            ## IMS
            resultudrhss = ImsProvision.udrHssDelete(req, ref)
            logger.info(ref+"  UDR HSS DELETE result  " + str(resultudrhss))
            if resultudrhss.split('#')[0] == '0':
                resultudrens = ImsProvision.udrEnsDelete(req, ref)
                logger.info(ref+"  UDR ENS DELETE result  " + str(resultudrens))
                if resultudrens.split('#')[0] == '0':
                    resultims = {"result":"success","message": "User Delete Operation Completed"}
                    #resultimsats = ImsProvision.imsAtsDelete(req, ref)
                    #logger.info(ref+" IMS ATS result  " + str(resultimsats))
                    #if resultimsats.split('#')[0] == '0':
                        #resultims = {"result":"success","message": ""}
                   # else:
                        #resultims = {"result":"failed","message": "DELETE_IMS_ATS"}
                else:
                    resultims = {"result":"failed","message": "DELETE_UDR_ENS"}
            else:
                resultims = {"result":"failed","message": "DELETE_UDR_HSS"}

            logger.info(ref+"  IMS DELETE result  " + str(resultims))
            return resultims

        else:
            ## NMS
            resultnms = NmsProvision.acsNmsProvDelete(req, ref)
            logger.info(ref+"  ACS NMS DELETE result  " + str(resultnms))
            if resultnms['result'] == 'failed':
                return resultnms

            ## IMS
            resultudrhss = ImsProvision.udrHssDelete(req, ref)
            logger.info(ref+"  UDR HSS DELETE result  " + str(resultudrhss))
            if resultudrhss.split('#')[0] == '0':
                resultudrens = ImsProvision.udrEnsDelete(req, ref)
                logger.info(ref+"  UDR ENS DELETE result  " + str(resultudrens))
                if resultudrens.split('#')[0] == '0':
                    resultims = {"result":"success","message": "User Delete Operation Completed"}
                    #resultimsats = ImsProvision.imsAtsDelete(req, ref)
                    #logger.info(ref+" IMS ATS result  " + str(resultimsats))
                    #if resultimsats.split('#')[0] == '0':
                    #resultims = {"result":"success","message": ""}
                # else:
                #resultims = {"result":"failed","message": "DELETE_IMS_ATS"}
                else:
                    resultims = {"result":"failed","message": "DELETE_UDR_ENS"}
            else:
                resultims = {"result":"failed","message": "DELETE_UDR_HSS"}

            logger.info(ref+"  IMS DELETE result  " + str(resultims))
            return resultims