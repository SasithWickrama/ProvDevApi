import re
import requests
import xml.etree.ElementTree as ET
from log import Logger
import const

logger = Logger.getLogger('zte', 'logs/zte')

proxies = {
    "http": None,
    "https": None,
}

class ZteProvision:
    def zteVlan(commandxml, indata, inval, inval2,ref):
        try:
            xmlfile = open('/opt/ProvDevApi/flies/nms/zte/' + commandxml, 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]
                data = data.replace(key, str(value))

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " Input Data : "+str(inval)+" "+str(inval2))
            logger.info(ref + " command xml : "+str(commandxml))

            response = requests.request("POST", const.zte_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))

            count = 1
            data = {}
            root = ET.fromstring(response.content)

            for resultc in root.iter('statusCode'):
                ResultCode = resultc.text

            for resultd in root.iter('statusDesc'):
                ResultDesc = resultd.text

            logger.info(ref + " "+str(ResultCode[0])+" "+ str(ResultDesc[0]))
            logger.info(ref + " End   : =========================================================================")

            for record in root.iter('record'):
                count = count + 1
                for param in record.iter('param'):
                    count = count + 1
                    for name in param.iter('name'):
                        if name.text != 'totalrecord':
                            count = count + 1
                            name = name.text
                            for value in param.iter('value'):
                                if count == 3:
                                    value = value.text
                                    if value == inval:
                                        if inval == 'Entree':
                                            data['EVLAN'] = value2
                                        elif inval == 'IPTV_SVLAN':
                                            data['IPSV'] = value2
                                        else:
                                            data[value] = value2
                                    if value == inval2:
                                        if inval2 == 'IPTV':
                                            data['IPTVLAN'] = value2
                                        else:
                                            data[value] = value2
                                if count == 4:
                                    value2 = value.text

                                count = 1
            #print(data)
            if (ResultCode == '0'):
                return data
            else:
                return str(ResultCode) + '#' + str(ResultDesc)

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)

    def zteCreate(commandxml, indata,ref):
        try:
            xmlfile = open('/opt/ProvDevApi/flies/nms/zte/' + commandxml, 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]
                data = data.replace(key, value)

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : "+str(commandxml))

            response = requests.request("POST", const.zte_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))

            ResultCode=re.findall("<statusCode>(.*?)</statusCode>", str(response.content))
            ResultDesc=re.findall("<statusDesc>(.*?)</statusDesc>", str(response.content))

            logger.info(ref + " "+str(ResultCode[0])+" "+ str(ResultDesc[0]))
            logger.info(ref + " End   : =========================================================================")

            return str(ResultCode[0]) + '#' + str(ResultDesc[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)

    def zteDelete(commandxml, indata,ref):
        try:
            xmlfile = open('/opt/ProvDevApi/flies/nms/zte/' + commandxml, 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]
                data = data.replace(key, value)

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : "+str(commandxml))

            response = requests.request("POST", const.zte_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))

            ResultCode=re.findall("<statusCode>(.*?)</statusCode>", str(response.content))
            ResultDesc=re.findall("<statusDesc>(.*?)</statusDesc>", str(response.content))

            logger.info(ref + " "+str(ResultCode[0])+" "+ str(ResultDesc[0]))
            logger.info(ref + " End   : =========================================================================")

            return str(ResultCode[0]) + '#' + str(ResultDesc[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)