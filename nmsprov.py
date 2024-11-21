from log import Logger
from nokia import NokiaProvision as nc
from zte import ZteProvision as zc
from huawei import HuaweiProvision as hc

logger = Logger.getLogger('nms', 'logs/nms')
class NmsProvision:
    def acsNmsProvCreate (data, ref):
        ## NOKIA NMS PROVISION
        try:
            if data["OLT_NAME"] == "NOKIA":
                ##ONT
                logger.info(ref+"  " + "command xml : ADD_ONT_NOKIA_ACS")
                resultont = nc.acsCreate("ADD_ONT_NOKIA_ACS.xml", data, ref)
                logger.info(ref+"  " + str(resultont))
                if resultont.split('#')[0] == '0':
                    ##BB
                    logger.info(ref+"  " + "command xml : ADD_NK_INTERNET_ACS")
                    resultbb = nc.acsCreate("ADD_NK_INTERNET_ACS.xml", data, ref)
                    logger.info(ref+"  " + str(resultbb))
                    if resultbb.split('#')[0] == '0':
                        ##VOICE
                        logger.info(ref+"  " + "command xml : ADD_VOICE_NOKIA_ACS")
                        resultvoice = nc.acsCreate("ADD_VOICE_NOKIA_ACS.xml", data, ref)
                        logger.info(ref+"  " + str(resultvoice))
                        if resultvoice.split('#')[0] == '0':
                            if not data["IPTVCOUNT"] == "0":
                                ##IPTV
                                logger.info(ref+"  " + "command xml : ADD_NK_IPTV_ACS")
                                resultiptv = nc.acsCreate("ADD_NK_IPTV_ACS.xml", data, ref)
                                logger.info(ref+"  " + str(resultiptv))
                                if resultiptv.split('#')[0] == '0':
                                    responsedata = {"result":"success","message": ""}

                                else:
                                    responsedata = {"result":"failed","message": "ADD_NK_IPTV_ACS"}
                            else:
                                responsedata = {"result":"success","message": ""}
                        else:
                            responsedata = {"result":"failed","message": "ADD_VOICE_NOKIA_ACS"}
                    else:
                        responsedata = {"result":"failed","message": "ADD_NK_INTERNET_ACS"}
                else:
                    responsedata = {"result":"failed","message": "ADD_ONT_NOKIA_ACS"}

            ## ZTE NMS PROVISION
            if data["OLT_NAME"] == "ZTE":
                #GET VLAN VOICE
                logger.info(ref+"  " + "command xml : GET_LIST_VLAN_VOICE")
                resultvlan = zc.zteVlan('lst_vlan.xml', data, 'VOBB', '',ref)
                logger.info(ref+"  " + str(resultvlan))
                data.update(resultvlan)

                #GET VLAN BB
                logger.info(ref+"  " + "command xml : GET_LIST_VLAN_BB")
                resultvlanbb = zc.zteVlan('lst_vlan.xml', data, 'Entree', 'SVLAN',ref)
                logger.info(ref+"  " + str(resultvlanbb))
                data.update(resultvlanbb)

                #GET VLAN IPTV
                if not data["IPTVCOUNT"] == "0":
                    logger.info(ref+"  " + "command xml : GET_LIST_VLAN_IPTV")
                    resultvlanpeo = zc.zteVlan('lst_vlan.xml', data, 'IPTV_SVLAN', 'IPTV',ref)
                    logger.info(ref+"  " + str(resultvlanpeo))
                    data.update(resultvlanpeo)

                ##ONT
                logger.info(ref+"  " + "command xml : ADD_ONT_ZTE_ACS")
                resultont = zc.zteCreate("ADD_ONT_ZTE_ACS.xml", data, ref)
                logger.info(ref+"  " + str(resultont))
                if resultont.split('#')[0] == '0':
                    if  data['ADSL_ZTE_DNAME'].split('_')[1].startswith(("C300", "C350", "C320")):
                        ##ONT PROFILE
                        logger.info(ref+"  " + "command xml : ADD_ONT_ZTE_C300PROF")
                        resultont = zc.zteCreate("ADD_ONT_ZTE_C300PROF.xml", data, ref)
                        logger.info(ref+"  " + str(resultont))
                        if resultont.split('#')[0] == '0':
                            ##BB
                            logger.info(ref+"  " + "command xml : ADD_INT_ZTE_C300")
                            resultont = zc.zteCreate("ADD_INT_ZTE_C300.xml", data, ref)
                            logger.info(ref+"  " + str(resultont))
                            if resultont.split('#')[0] == '0':
                                ##VOICE
                                logger.info(ref+"  " + "command xml : ADD_VOICE_ZTE_C300")
                                resultont = zc.zteCreate("ADD_VOICE_ZTE_C300.xml", data, ref)
                                logger.info(ref+"  " + str(resultont))
                                if resultont.split('#')[0] == '0':
                                    if not data["IPTVCOUNT"] == "0":
                                        ##IPTV PORT
                                        logger.info(ref+"  " + "command xml : ADD_IPTV_ZTE_C300")
                                        resultont = zc.zteCreate("ADD_IPTV_ZTE_C300.xml", data, ref)
                                        logger.info(ref+"  " + str(resultont))
                                        if resultont.split('#')[0] == '0':
                                            ##IPTV MULTICAST
                                            logger.info(ref+"  " + "command xml : ADD_IPTV_ZTE_MULTICAST_C300")
                                            resultont = zc.zteCreate("ADD_IPTV_ZTE_MULTICAST_C300.xml", data, ref)
                                            logger.info(ref+"  " + str(resultont))
                                            if resultont.split('#')[0] == '0':
                                                ##IPTV UNICAST
                                                logger.info(ref+"  " + "command xml : ADD_IPTV_ZTE_UNICAST_C300")
                                                resultont = zc.zteCreate("ADD_IPTV_ZTE_UNICAST_C300.xml", data, ref)
                                                logger.info(ref+"  " + str(resultont))
                                                if resultont.split('#')[0] == '0':
                                                    ##IPTV RECEIVE30
                                                    logger.info(ref+"  " + "command xml : ADD_IPTV_ZTE_RECEIVE30_C300")
                                                    resultont = zc.zteCreate("ADD_IPTV_ZTE_RECEIVE30_C300.xml", data, ref)
                                                    logger.info(ref+"  " + str(resultont))
                                                    if resultont.split('#')[0] == '0':
                                                        ##IPTV RECEIVE50
                                                        logger.info(ref+"  " + "command xml : ADD_IPTV_ZTE_RECEIVE50_C300")
                                                        resultont = zc.zteCreate("ADD_IPTV_ZTE_RECEIVE50_C300.xml", data, ref)
                                                        logger.info(ref+"  " + str(resultont))
                                                        if resultont.split('#')[0] == '0':
                                                            responsedata = {"result":"success","message": ""}
                                                        else:
                                                            responsedata = {"result":"failed","message": "ADD_IPTV_ZTE_RECEIVE50_C300"}
                                                    else:
                                                        responsedata = {"result":"failed","message": "ADD_IPTV_ZTE_RECEIVE30_C300"}
                                                else:
                                                    responsedata = {"result":"failed","message": "ADD_IPTV_ZTE_UNICAST_C300"}
                                            else:
                                                responsedata = {"result":"failed","message": "ADD_IPTV_ZTE_MULTICAST_C300"}
                                        else:
                                            responsedata = {"result":"failed","message": "ADD_IPTV_ZTE_C300"}
                                    else:
                                        responsedata = {"result":"success","message": ""}
                                else:
                                    responsedata = {"result":"failed","message": "ADD_VOICE_ZTE_C300"}
                            else:
                                responsedata = {"result":"failed","message": "ADD_INT_ZTE_C300"}
                        else:
                            responsedata = {"result":"failed","message": "ADD_ONT_ZTE_C300PROF"}

                    if  data['ADSL_ZTE_DNAME'].split('_')[1].startswith(("C600")):
                        ##ONT PROFILE
                        logger.info(ref+"  " + "command xml : ADD_ONT_ZTE_C600PROF")
                        resultont = zc.zteCreate("ADD_ONT_ZTE_C600PROF.xml", data, ref)
                        logger.info(ref+"  " + str(resultont))
                        if resultont.split('#')[0] == '0':
                            ##BB
                            logger.info(ref+"  " + "command xml : ADD_INT_ZTE_C600")
                            resultont = zc.zteCreate("ADD_INT_ZTE_C600.xml", data, ref)
                            logger.info(ref+"  " + str(resultont))
                            if resultont.split('#')[0] == '0':
                                ##VOICE
                                logger.info(ref+"  " + "command xml : ADD_VOICE_ZTE_C600")
                                resultont = zc.zteCreate("ADD_VOICE_ZTE_C600.xml", data, ref)
                                logger.info(ref+"  " + str(resultont))
                                if resultont.split('#')[0] == '0':
                                    if not data["IPTVCOUNT"] == "0":
                                        ##IPTV PORT
                                        logger.info(ref+"  " + "command xml : ADD_IPTV_ZTE_C600")
                                        resultont = zc.zteCreate("ADD_IPTV_ZTE_C600.xml", data, ref)
                                        logger.info(ref+"  " + str(resultont))
                                        if resultont.split('#')[0] == '0':
                                            ##IPTV MULTICAST
                                            logger.info(ref+"  " + "command xml : ADD_IPTV_ZTE_MULTICAST_600")
                                            resultont = zc.zteCreate("ADD_IPTV_ZTE_MULTICAST_C600.xml", data, ref)
                                            logger.info(ref+"  " + str(resultont))
                                            if resultont.split('#')[0] == '0':
                                                ##IPTV RECEIVE
                                                logger.info(ref+"  " + "command xml : ADD_IPTV_ZTE_RECEIVE_C600")
                                                resultont = zc.zteCreate("ADD_IPTV_ZTE_RECEIVE_C600.xml", data, ref)
                                                logger.info(ref+"  " + str(resultont))
                                                if resultont.split('#')[0] == '0':
                                                    responsedata = {"result":"success","message": ""}
                                                else:
                                                    responsedata = {"result":"failed","message": "ADD_IPTV_ZTE_RECEIVE_C600"}
                                            else:
                                                responsedata = {"result":"failed","message": "ADD_IPTV_ZTE_MULTICAST_C600"}
                                        else:
                                            responsedata = {"result":"failed","message": "ADD_IPTV_ZTE_C600"}
                                    else:
                                        responsedata = {"result":"success","message": ""}
                                else:
                                    responsedata = {"result":"failed","message": "ADD_VOICE_ZTE_C600"}
                            else:
                                responsedata = {"result":"failed","message": "ADD_INT_ZTE_C600"}

                        else:
                            responsedata = {"result":"failed","message": "ADD_ONT_ZTE_C600PROF"}
                else:
                    responsedata = {"result":"failed","message": "ADD_ONT_ZTE_ACS"}

            if data["OLT_NAME"] == "HUAWEI":

                temp = data['FTTH_ZTE_PID'].split("-")

                data['FTTH_HUW_FN'] = str(temp[0])
                data['FTTH_HUW_SN'] = str(temp[1])
                data['FTTH_HUW_PN'] = str(temp[2])

                #GET VLAN VOICE
                logger.info(ref+"  " + "command xml : GET_LIST_VLAN_VOICE")
                resultvlan = hc.huaweiVlan('lst_vlan_huawei.xml', data, 'VOBB', '',ref)
                logger.info(ref+"  " + str(resultvlan))
                data.update(resultvlan)

                #GET VLAN BB
                logger.info(ref+"  " + "command xml : GET_LIST_VLAN_BB")
                resultvlanbb = hc.huaweiVlan('lst_vlan_huawei.xml', data, 'Entree', 'SVLAN',ref)
                logger.info(ref+"  " + str(resultvlanbb))
                data.update(resultvlanbb)

                #GET VLAN IPTV
                if not data["IPTVCOUNT"] == "0":
                    logger.info(ref+"  " + "command xml : GET_LIST_VLAN_IPTV")
                    resultvlanpeo = hc.huaweiVlan('lst_vlan_huawei.xml', data, 'IPTV_SVLAN', 'IPTV',ref)
                    logger.info(ref+"  " + str(resultvlanpeo))
                    data.update(resultvlanpeo)
                ##ONT
                logger.info(ref+"  " + "command xml : ADD_ONT_HUAWEI_ACS")
                resultont = hc.huaweiCreate("ADD_ONT_HUAWEI_ACS.xml", data, ref)
                logger.info(ref+"  " + str(resultont))
                if resultont.split('#')[0] == '0':
                    ##BB
                    logger.info(ref+"  " + "command xml : ADD_INT_HUAWEI")
                    resultbb = hc.huaweiCreate("ADD_INT_HUAWEI.xml", data, ref)
                    logger.info(ref+"  " + str(resultbb))
                    if resultbb.split('#')[0] == '0':
                        ##VOICE
                        logger.info(ref+"  " + "command xml : ADD_VOICE_HUAWEI")
                        resultvoice = hc.huaweiCreate("ADD_VOICE_HUAWEI.xml", data, ref)
                        logger.info(ref+"  " + str(resultvoice))
                        if resultvoice.split('#')[0] == '0':
                            if not data["IPTVCOUNT"] == "0":
                                ##IPTV
                                logger.info(ref+"  " + "command xml : ADD_IPTV_HUAWEI")
                                resultiptv = hc.huaweiCreate("ADD_IPTV_HUAWEI.xml", data, ref)
                                logger.info(ref+"  " + str(resultiptv))
                                if resultiptv.split('#')[0] == '0':
                                    ##IPTV JOINT
                                    logger.info(ref+"  " + "command xml : ADD_JOINT_NTV_HUAWEI")
                                    resultiptvjoint = hc.huaweiCreate("ADD_JOINT_NTV_HUAWEI.xml", data, ref)
                                    logger.info(ref+"  " + str(resultiptvjoint))
                                    if resultiptvjoint.split('#')[0] == '0':
                                        responsedata = {"result":"success","message": ""}
                                    else:
                                        responsedata = {"result":"failed","message": "resultiptvjoint"}
                                else:
                                    responsedata = {"result":"failed","message": "ADD_IPTV_HUAWEI"}
                            else:
                                responsedata = {"result":"success","message": ""}
                        else:
                            responsedata = {"result":"failed","message": "ADD_VOICE_HUAWEI"}
                    else:
                        responsedata = {"result":"failed","message": "ADD_INT_HUAWEI"}
                else:
                    responsedata = {"result":"failed","message": "ADD_ONT_HUAWEI_ACS"}
        except Exception as e:
            logger.error("nms prov")
            logger.error(e)

        logger.info(ref+"  " + str(responsedata))
        return responsedata

    def acsNmsProvDelete (data, ref):
        try:
            if data["OLT_NAME"] == "NOKIA":
                logger.info(ref+"  " + "command xml : DEL_ONT_NOKIA")
                resultont = nc.nmsDelete("DEL_ONT_NOKIA.xml", data, ref)
                logger.info(ref+"  " + str(resultont))
                if resultont.split('#')[0] == '0':
                    responsedata = {"result":"success","message": ""}

                else:
                    responsedata = {"result":"failed","message": "DEL_ONT_NOKIA"}

            if data["OLT_NAME"] == "ZTE":
                logger.info(ref+"  " + "command xml : DEL_ONT_ZTE")
                resultont = zc.zteDelete("DEL_ONT_ZTE.xml", data, ref)
                logger.info(ref+"  " + str(resultont))
                if resultont.split('#')[0] == '0':
                    responsedata = {"result":"success","message": ""}

                else:
                    responsedata = {"result":"failed","message": "DEL_ONT_ZTE"}
                    
            if data["OLT_NAME"] == "HUAWEI":
            
                temp = data['FTTH_ZTE_PID'].split("-")

                data['FTTH_HUW_FN'] = str(temp[0])
                data['FTTH_HUW_SN'] = str(temp[1])
                data['FTTH_HUW_PN'] = str(temp[2])
                
                logger.info(ref+"  " + "command xml : DEL_ONT_HUAWEI")
                resultont = hc.huaweiDelete("DEL_ONT_HUAWEI.xml", data, ref)
                logger.info(ref+"  " + str(resultont))
                if resultont.split('#')[0] == '0':
                    responsedata = {"result":"success","message": ""}

                else:
                    responsedata = {"result":"failed","message": "DEL_ONT_HUAWEI"}        
        except Exception as e:
            logger.error("nms prov delete")
            logger.error(e)

        logger.info(ref+"  " + str(responsedata))
        return responsedata