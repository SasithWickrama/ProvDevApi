import re
import requests
import xml.etree.ElementTree as ET
from log import Logger
import const

logger = Logger.getLogger('huawei', 'logs/huawei')

proxies = {
    "http": None,
    "https": None,
}

class HuaweiProvision:
    def huaweiVlan(commandxml, indata, inval, inval2,ref):
        try:
            xmlfile = open('/opt/ProvDevApi/flies/nms/huawei/' + commandxml, 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]
                data = data.replace(key, str(value))

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " Input Data : "+str(inval)+" "+str(inval2))
            logger.info(ref + " command xml : "+str(commandxml))

            response = requests.request("POST", const.huawei_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))

            count = 1
            data = {}
            root = ET.fromstring(response.content)

            ResultCode=re.findall("<os:errCode>(.*?)</os:errCode>", str(response.content))
            ResultDesc=re.findall("<os:errDesc>(.*?)</os:errDesc>", str(response.content))

            logger.info(ref + " "+str(ResultCode[0])+" "+ str(ResultDesc[0]))
            logger.info(ref + " End   : =========================================================================")
            
            ulable = re.findall("<USERLABEL>(.*?)</USERLABEL>", str(response.content))
            vlan = re.findall("<VLANID>(.*?)</VLANID>", str(response.content))
            
            for i in range(len(ulable)):
                if ulable[i] == 'VOBB':
                    data['VOBB'] = vlan[i]

                if ulable[i] == 'Entree':
                    data['EVLAN'] = vlan[i]

                if ulable[i] == 'SVLAN':
                    data['SVLAN'] = vlan[i]
                    
                if ulable[i] == 'IPTV_SVLAN':
                    data['IPTVLAN'] = vlan[i]
                    
            #print(data)
            if (ResultCode[0] == '0'):
                return data
            else:
                return str(ResultCode) + '#' + str(ResultDesc)

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)

    def huaweiCreate(commandxml, indata,ref):
        try:
            xmlfile = open('/opt/ProvDevApi/flies/nms/huawei/' + commandxml, 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]
                data = data.replace(key, value)

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : "+str(commandxml))

            response = requests.request("POST", const.huawei_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))

            ResultCode=re.findall("<os:errCode>(.*?)</os:errCode>", str(response.content))
            ResultDesc=re.findall("<os:errDesc>(.*?)</os:errDesc>", str(response.content))

            logger.info(ref + " "+str(ResultCode[0])+" "+ str(ResultDesc[0]))
            logger.info(ref + " End   : =========================================================================")

            return str(ResultCode[0]) + '#' + str(ResultDesc[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)

    def huaweiDelete(commandxml, indata,ref):
        try:
            xmlfile = open('/opt/ProvDevApi/flies/nms/huawei/' + commandxml, 'r')
            data = xmlfile.read()

            for key in indata:
                value = indata[key]
                data = data.replace(key, value)

            logger.info(ref + " Start : =========================================================================")
            logger.info(ref + " Input Data : "+str(indata))
            logger.info(ref + " command xml : "+str(commandxml))

            response = requests.request("POST", const.huawei_endpoint,data=data, proxies=proxies)

            logger.info(ref +" "+str(response.request.body))
            logger.info(ref + " Response : =================================")
            logger.info(ref + str(response.text))

            ResultCode=re.findall("<os:errCode>(.*?)</os:errCode>", str(response.content))
            ResultDesc=re.findall("<os:errDesc>(.*?)</os:errDesc>", str(response.content))

            logger.info(ref + " "+str(ResultCode[0])+" "+ str(ResultDesc[0]))
            logger.info(ref + " End   : =========================================================================")

            return str(ResultCode[0]) + '#' + str(ResultDesc[0])

        except Exception as e:
            logger.error(e)
            logger.info("End   : =========================================================================")
            return '1#' + str(e)