import re
from log import Logger
import requests
from requests.auth import HTTPBasicAuth
logger = Logger.getLogger('nokia', 'logs/nokia')
import const

proxies = {
    "http": None,
    "https": None,
}
class NokiaProvision:
    def acsCreate(commandxml, indata,ref):
        try:
            xmlfile = open('/opt/ProvDevApi/flies/nms/nokia/' + commandxml, 'r')
            #xmlfile = open('D:\\DevOps\\Python\\ProvDevApi\\flies\\nms\\nokia\\' + commandxml, 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]

                data = data.replace(key, value)
                # print(key, value)

            # print(data)
            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : "+str(commandxml))

            response = requests.request("POST", const.nokia_endpoint,
                                        data=data, proxies=proxies, auth=HTTPBasicAuth('nbiuser', 'nbiuser'))

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))


            ResultCode=re.findall("<ResultIndicator>(.*?)</ResultIndicator>", str(response.content))

            if len(ResultCode) > 0:
                logger.info(ref + ' 0#' + str(ResultCode[0]))
                logger.info(ref + " End   : =========================================================================")
                return '0#' + str(ResultCode[0])
            else:
                ResultCode = re.findall("<message>(.*?)</message>", str(response.content))
                logger.info(ref + ' 1#' + str(ResultCode[0]))
                logger.info(ref + " End   : =========================================================================")
                return '1#' + str(ResultCode[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)


    def nmsDelete(commandxml, indata,ref):
        try:
            xmlfile = open('/opt/ProvDevApi/flies/nms/nokia/' + commandxml, 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]

                data = data.replace(key, value)
                # print(key, value)

            # print(data)
            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : "+str(commandxml))

            response = requests.request("POST", const.nokia_endpoint,
                                        data=data, proxies=proxies, auth=HTTPBasicAuth('nbiuser', 'nbiuser'))

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))


            ResultCode=re.findall("<ResultIndicator>(.*?)</ResultIndicator>", str(response.content))

            if len(ResultCode) > 0:
                logger.info(ref + ' 0#' + str(ResultCode[0]))
                logger.info(ref + " End   : =========================================================================")
                return '0#' + str(ResultCode[0])
            else:
                ResultCode = re.findall("<message>(.*?)</message>", str(response.content))
                logger.info(ref + ' 1#' + str(ResultCode[0]))
                logger.info(ref + " End   : =========================================================================")
                return '1#' + str(ResultCode[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)
