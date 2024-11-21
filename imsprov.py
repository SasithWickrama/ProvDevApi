from datetime import datetime
import re
import subprocess
from requests.auth import HTTPBasicAuth
import requests

import const
from log import Logger

logger = Logger.getLogger('ims', 'logs/ims')

proxies = {
    "http": None,
    "https": None,
}

class ImsProvision:
    ##UDR HSS CREATE
    def udrHssCreate(indata, ref):
        try:
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dt2 = datetime.now().strftime('%Y%m%d%H%M%S')

            indata['DT']= str(dt)
            indata['DSERIAL']= str(dt)

            xmlfile = open('/opt/ProvDevApi/flies/ims/UDR_ADDFTTH_HSS.xml', 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]

                data = data.replace(key, value)

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : UDR_ADDFTTH_HSS.xml")

            response = requests.request("POST", const.udr_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))

            ResultCode=re.findall("<ResultCode>(.*?)</ResultCode>", str(response.content))
            ResultDescr=re.findall("<ResultDescr>(.*?)</ResultDescr>", str(response.content))

            if ResultCode[0] == '0':
                logger.info(ref + ' 0#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '0#' + str(ResultDescr[0])
            else:
                logger.info(ref + ' 1#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '1#' + str(ResultDescr[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)


    ##UDR ENS CREATE
    def udrEnsCreate(indata, ref):
        try:
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dt2 = datetime.now().strftime('%Y%m%d%H%M%S')

            indata['DT']= str(dt)
            indata['DSERIAL']= str(dt)

            xmlfile = open('/opt/ProvDevApi/flies/ims/ADDENS.xml', 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]

                data = data.replace(key, value)

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : ADDENS.xml")

            response = requests.request("POST", const.udr_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))

            ResultCode=re.findall("<ResultCode>(.*?)</ResultCode>", str(response.content))
            ResultDescr=re.findall("<ResultDescr>(.*?)</ResultDescr>", str(response.content))

            if ResultCode[0] == '0':
                logger.info(ref + ' 0#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '0#' + str(ResultDescr[0])
            else:
                logger.info(ref + ' 1#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '1#' + str(ResultDescr[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)


    ##IMS ATS CREATE
    def imsAtsCreate(indata, ref):
        try:
            xmlfile = open('/opt/ProvDevApi/flies/ims/ADDATS.xml', 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]

                data = data.replace(key, value)

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : ADDATS.xml")

            response = requests.request("POST", const.ims_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.url))
            logger.info(ref + str(response.text))

            ResultCode=re.findall("<ns1:ResultCode>(.*?)</ns1:ResultCode>", str(response.content))
            ResultDescr=re.findall("<ns1:ResultDesc>(.*?)</ns1:ResultDesc>", str(response.content))

            if ResultCode[0] == '0':
                logger.info(ref + ' 0#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '0#' + str(ResultDescr[0])
            else:
                logger.info(ref + ' 1#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '1#' + str(ResultDescr[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)


    ##IMS ATS DELETE
    def imsAtsDelete(indata, ref):
        try:
            xmlfile = open('/opt/ProvDevApi/flies/ims/DELATS.xml', 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]

                data = data.replace(key, value)

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : DELATS.xml")

            response = requests.request("POST", const.ims_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.url))
            logger.info(ref + str(response.text))

            ResultCode=re.findall("<ns1:ResultCode>(.*?)</ns1:ResultCode>", str(response.content))
            ResultDescr=re.findall("<ns1:ResultDesc>(.*?)</ns1:ResultDesc>", str(response.content))

            if ResultCode[0] == '0':
                logger.info(ref + ' 0#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '0#' + str(ResultDescr[0])
            else:
                logger.info(ref + ' 1#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '1#' + str(ResultDescr[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)

    ##UDR HSS DELETE
    def udrHssDelete(indata, ref):
        try:

            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dt2 = datetime.now().strftime('%Y%m%d%H%M%S')

            indata['DT']= str(dt)
            indata['DSERIAL']= str(dt)

            xmlfile = open('/opt/ProvDevApi/flies/ims/UDR_DEL_HSS.xml', 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]

                data = data.replace(key, value)

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : UDR_DEL_HSS.xml")

            response = requests.request("POST", const.udr_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))

            ResultCode=re.findall("<ResultCode>(.*?)</ResultCode>", str(response.content))
            ResultDescr=re.findall("<ResultDescr>(.*?)</ResultDescr>", str(response.content))

            if ResultCode[0] == '0':
                logger.info(ref + ' 0#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '0#' + str(ResultDescr[0])
            else:
                logger.info(ref + ' 1#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '1#' + str(ResultDescr[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)

    ##UDR ENS DELETE
    def udrEnsDelete(indata, ref):
        try:
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dt2 = datetime.now().strftime('%Y%m%d%H%M%S')

            indata['DT']= str(dt)
            indata['DSERIAL']= str(dt)

            xmlfile = open('/opt/ProvDevApi/flies/ims/DELENS.xml', 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]

                data = data.replace(key, value)

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : DELENS.xml")

            response = requests.request("POST", const.udr_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))

            ResultCode=re.findall("<ResultCode>(.*?)</ResultCode>", str(response.content))
            ResultDescr=re.findall("<ResultDescr>(.*?)</ResultDescr>", str(response.content))

            if ResultCode[0] == '0':
                logger.info(ref + ' 0#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '0#' + str(ResultDescr[0])
            else:
                logger.info(ref + ' 1#' + str(ResultDescr[0]))
                logger.info(ref + " End   : =========================================================================")
                return '1#' + str(ResultDescr[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)