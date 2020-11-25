#------ SecretCode -------------
from random import choice

#------ EmailHandled -------------
import smtplib, ssl, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SecretCode():

    def __init__(self, longitud = 4, data = None):
        self.longitud = longitud

        if data == None:
            self.data = "0123456789"
        else :
            self.data = data

        self.cadena = ""

    def generate(self):
        self.cadena = self.cadena.join([choice(self.data) for i in range(self.longitud)])

    def getAllCadena(self):
        return self.cadena

    def getNumber1(self):
        return self.cadena[0]
    
    def getNumber2(self):
        return self.cadena[1]

    def getNumber3(self):
        return self.cadena[2]

    def getNumber4(self):
        return self.cadena[3]



def getAlternativeText(secretCode):
    return "CODIGO SECRETO ES: {0} ".format(secretCode)

def getHTMLBase(number1, number2, number3, number4):
    
    return """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1" name="viewport">
        <meta name="x-apple-disable-message-reformatting">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta content="telephone=no" name="format-detection">
        <title></title>
        <!--[if (mso 16)]>
        <style type="text/css">
        a {text-decoration: none;}
        </style>
        <![endif]-->
        <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->
        <!--[if gte mso 9]>
    <xml>
        <o:OfficeDocumentSettings>
        <o:AllowPNG></o:AllowPNG>
        <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
    <style>
    /* CONFIG STYLES Please do not delete and edit CSS styles below */
    /* IMPORTANT THIS STYLES MUST BE ON FINAL EMAIL */
    #outlook a {
        padding: 0;
    }

    .ExternalClass {
        width: 100%;
    }

    .ExternalClass,
    .ExternalClass p,
    .ExternalClass span,
    .ExternalClass font,
    .ExternalClass td,
    .ExternalClass div {
        line-height: 100%;
    }

    .box-shadow {
        box-shadow: 0 0 7px 1px #5050501f;
    }

    .es-button {
        mso-style-priority: 100 !important;
        text-decoration: none !important;
    }

    a[x-apple-data-detectors] {
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
    }

    .es-desk-hidden {
        display: none;
        float: left;
        overflow: hidden;
        width: 0;
        max-height: 0;
        line-height: 0;
        mso-hide: all;
    }

    /*
    END OF IMPORTANT
    */
    s {
        text-decoration: line-through;
    }

    html,
    body {
        width: 100%;
        font-family: arial, 'helvetica neue', helvetica, sans-serif;
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
    }

    table {
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
        border-collapse: collapse;
        border-spacing: 0px;
    }

    table td,
    html,
    body,
    .es-wrapper {
        padding: 0;
        Margin: 0;
    }

    .es-content,
    .es-header,
    .es-footer {
        table-layout: fixed !important;
        width: 100%;
    }

    img {
        display: block;
        border: 0;
        outline: none;
        text-decoration: none;
        -ms-interpolation-mode: bicubic;
    }

    table tr {
        border-collapse: collapse;
    }

    p,
    hr {
        Margin: 0;
    }

    h1,
    h2,
    h3,
    h4,
    h5 {
        Margin: 0;
        line-height: 120%;
        mso-line-height-rule: exactly;
        font-family: arial, 'helvetica neue', helvetica, sans-serif;
    }

    p,
    ul li,
    ol li,
    a {
        -webkit-text-size-adjust: none;
        -ms-text-size-adjust: none;
        mso-line-height-rule: exactly;
    }

    .es-left {
        float: left;
    }

    .es-right {
        float: right;
    }

    .es-p5 {
        padding: 5px;
    }

    .es-p5t {
        padding-top: 5px;
    }

    .es-p5b {
        padding-bottom: 5px;
    }

    .es-p5l {
        padding-left: 5px;
    }

    .es-p5r {
        padding-right: 5px;
    }

    .es-p10 {
        padding: 10px;
    }

    .es-p10t {
        padding-top: 10px;
    }

    .es-p10b {
        padding-bottom: 10px;
    }

    .es-p10l {
        padding-left: 10px;
    }

    .es-p10r {
        padding-right: 10px;
    }

    .es-p15 {
        padding: 15px;
    }

    .es-p15t {
        padding-top: 15px;
    }

    .es-p15b {
        padding-bottom: 15px;
    }

    .es-p15l {
        padding-left: 15px;
    }

    .es-p15r {
        padding-right: 15px;
    }

    .es-p20 {
        padding: 20px;
    }

    .es-p20t {
        padding-top: 20px;
    }

    .es-p20b {
        padding-bottom: 20px;
    }

    .es-p20l {
        padding-left: 20px;
    }

    .es-p20r {
        padding-right: 20px;
    }

    .es-p25 {
        padding: 25px;
    }

    .es-p25t {
        padding-top: 25px;
    }

    .es-p25b {
        padding-bottom: 25px;
    }

    .es-p25l {
        padding-left: 25px;
    }

    .es-p25r {
        padding-right: 25px;
    }

    .es-p30 {
        padding: 30px;
    }

    .es-p30t {
        padding-top: 30px;
    }

    .es-p30b {
        padding-bottom: 30px;
    }

    .es-p30l {
        padding-left: 30px;
    }

    .es-p30r {
        padding-right: 30px;
    }

    .es-p35 {
        padding: 35px;
    }

    .es-p35t {
        padding-top: 35px;
    }

    .es-p35b {
        padding-bottom: 35px;
    }

    .es-p35l {
        padding-left: 35px;
    }

    .es-p35r {
        padding-right: 35px;
    }

    .es-p40 {
        padding: 40px;
    }

    .es-p40t {
        padding-top: 40px;
    }

    .es-p40b {
        padding-bottom: 40px;
    }

    .es-p40l {
        padding-left: 40px;
    }

    .es-p40r {
        padding-right: 40px;
    }

    .es-menu td {
        border: 0;
    }

    .es-menu td a img {
        display: inline-block !important;
    }

    /* END CONFIG STYLES */
    a {
        font-family: arial, 'helvetica neue', helvetica, sans-serif;
        font-size: 14px;
        text-decoration: underline;
    }

    h1 {
        font-size: 30px;
        font-style: normal;
        font-weight: bold;
        color: #ffffff;
    }

    h1 a {
        font-size: 30px;
    }

    h2 {
        font-size: 24px;
        font-style: normal;
        font-weight: bold;
        color: #ffffff;
    }

    h2 a {
        font-size: 24px;
    }

    h3 {
        font-size: 16px;
        font-style: normal;
        font-weight: bold;
        color: #0000ff;
    }

    h3 a {
        font-size: 16px;
    }

    p,
    ul li,
    ol li {
        font-size: 14px;
        font-family: arial, 'helvetica neue', helvetica, sans-serif;
        line-height: 150%;
    }

    ul li,
    ol li {
        Margin-bottom: 15px;
    }

    .es-menu td a {
        text-decoration: none;
        display: block;
    }

    .es-wrapper {
        width: 100%;
        height: 100%;
        background-image: ;
        background-repeat: repeat;
        background-position: center top;
    }

    .es-wrapper-color {
        background-color: #f6f6f6;
    }

    .es-content-body {
        background-color: #ffffff;
    }

    .es-content-body p,
    .es-content-body ul li,
    .es-content-body ol li {
        color: #ffffff;
    }

    .es-content-body a {
        color: #0000ff;
    }

    .es-header {
        background-color: transparent;
        background-image: ;
        background-repeat: repeat;
        background-position: center top;
    }

    .es-header-body {
        background-color: #ffffff;
    }

    .es-header-body p,
    .es-header-body ul li,
    .es-header-body ol li {
        color: #333333;
        font-size: 14px;
    }

    .es-header-body a {
        color: #0000ff;
        font-size: 14px;
    }

    .es-footer {
        background-color: transparent;
        background-image: ;
        background-repeat: repeat;
        background-position: center top;
    }

    .es-footer-body {
        background-color: #ffffff;
    }

    .es-footer-body p,
    .es-footer-body ul li,
    .es-footer-body ol li {
        color: #090101;
        font-size: 14px;
    }

    .es-footer-body a {
        color: #0000ff;
        font-size: 14px;
    }

    .es-infoblock,
    .es-infoblock p,
    .es-infoblock ul li,
    .es-infoblock ol li {
        line-height: 120%;
        font-size: 12px;
        color: #cccccc;
    }

    .es-infoblock a {
        font-size: 12px;
        color: #cccccc;
    }

    a.es-button {
        border-style: solid;
        border-color: #0000ff;
        border-width: 10px 25px 10px 25px;
        display: inline-block;
        background: #0000ff;
        border-radius: 0px;
        font-size: 18px;
        font-family: arial, 'helvetica neue', helvetica, sans-serif;
        font-weight: bold;
        font-style: normal;
        line-height: 120%;
        color: #ffffff;
        text-decoration: none;
        width: auto;
        text-align: center;
    }

    .es-button-border {
        border-style: solid solid solid solid;
        border-color: #0000ff #0000ff #0000ff #0000ff;
        background: #0000ff;
        border-width: 0px 0px 0px 0px;
        display: inline-block;
        border-radius: 0px;
        width: auto;
    }

    /* RESPONSIVE STYLES Please do not delete and edit CSS styles below. If you don't need responsive layout, please delete this section. */
    @media only screen and (max-width: 600px) {

        p,
        ul li,
        ol li,
        a {
            font-size: 16px !important;
            line-height: 150% !important;
        }

        h1 {
            font-size: 25px !important;
            text-align: center;
            line-height: 120% !important;
        }

        h2 {
            font-size: 22px !important;
            text-align: center;
            line-height: 120% !important;
        }

        h3 {
            font-size: 20px !important;
            text-align: center;
            line-height: 120% !important;
        }

        h1 a {
            font-size: 25px !important;
        }

        h2 a {
            font-size: 22px !important;
        }

        h3 a {
            font-size: 20px !important;
        }

        .es-menu td a {
            font-size: 16px !important;
        }

        .es-header-body p,
        .es-header-body ul li,
        .es-header-body ol li,
        .es-header-body a {
            font-size: 13px !important;
        }

        .es-footer-body p,
        .es-footer-body ul li,
        .es-footer-body ol li,
        .es-footer-body a {
            font-size: 11px !important;
        }

        .es-infoblock p,
        .es-infoblock ul li,
        .es-infoblock ol li,
        .es-infoblock a {
            font-size: 12px !important;
        }

        *[class="gmail-fix"] {
            display: none !important;
        }

        .es-m-txt-c,
        .es-m-txt-c h1,
        .es-m-txt-c h2,
        .es-m-txt-c h3 {
            text-align: center !important;
        }

        .es-m-txt-r,
        .es-m-txt-r h1,
        .es-m-txt-r h2,
        .es-m-txt-r h3 {
            text-align: right !important;
        }

        .es-m-txt-l,
        .es-m-txt-l h1,
        .es-m-txt-l h2,
        .es-m-txt-l h3 {
            text-align: left !important;
        }

        .es-m-txt-r img,
        .es-m-txt-c img,
        .es-m-txt-l img {
            display: inline !important;
        }

        .es-button-border {
            display: block !important;
        }

        a.es-button {
            font-size: 14px !important;
            display: block !important;
            border-left-width: 0px !important;
            border-right-width: 0px !important;
        }

        .es-btn-fw {
            border-width: 10px 0px !important;
            text-align: center !important;
        }

        .es-adaptive table,
        .es-btn-fw,
        .es-btn-fw-brdr,
        .es-left,
        .es-right {
            width: 100% !important;
        }

        .es-content table,
        .es-header table,
        .es-footer table,
        .es-content,
        .es-footer,
        .es-header {
            width: 100% !important;
            max-width: 600px !important;
        }

        .es-adapt-td {
            display: block !important;
            width: 100% !important;
        }

        .adapt-img {
            width: 100% !important;
            height: auto !important;
        }

        .es-m-p0 {
            padding: 0px !important;
        }

        .es-m-p0r {
            padding-right: 0px !important;
        }

        .es-m-p10r {
            padding-right: 10px !important;
        }

        .es-m-p10l {
            padding-left: 10px !important;
        }

        .es-m-p0l {
            padding-left: 0px !important;
        }

        .es-m-p0t {
            padding-top: 0px !important;
        }

        .es-m-p0b {
            padding-bottom: 0 !important;
        }

        .es-m-p20b {
            padding-bottom: 20px !important;
        }

        .es-mobile-hidden,
        .es-hidden {
            display: none !important;
        }

        tr.es-desk-hidden,
        td.es-desk-hidden,
        table.es-desk-hidden {
            width: auto !important;
            overflow: visible !important;
            float: none !important;
            max-height: inherit !important;
            line-height: inherit !important;
        }

        tr.es-desk-hidden {
            display: table-row !important;
        }

        table.es-desk-hidden {
            display: table !important;
        }

        td.es-desk-menu-hidden {
            display: table-cell !important;
        }

        .es-menu td {
            width: 1% !important;
        }

        table.es-table-not-adapt,
        .esd-block-html table {
            width: auto !important;
        }

        table.es-social {
            display: inline-block !important;
        }

        table.es-social td {
            display: inline-block !important;
        }
    }

    /* END RESPONSIVE STYLES */
    </style>
    </head>

    <body>
        <div class="es-wrapper-color">
            <!--[if gte mso 9]>
                <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
                    <v:fill type="tile" color="#f6f6f6"></v:fill>
                </v:background>
            <![endif]-->
            <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
                <tbody>
                    <tr>
                        <td class="esd-email-paddings" valign="top">
                            <table cellpadding="0" cellspacing="0" class="es-content esd-footer-popover" align="center">
                                <tbody>
                                    <tr>
                                        <td class="esd-stripe esd-checked" align="center" style="background-color: transparent;" bgcolor="transparent">
                                            <table bgcolor="#090101" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: #EC3E7E; background-position: center top; background-repeat: no-repeat;">
                                                <tbody>
                                                    <tr>
                                                        <td class="esd-structure es-p20t es-p20r es-p20l" align="left">
                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                <tbody>
                                                                    <tr>
                                                                        <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank"><img class="adapt-img" src="https://eyncmf.stripocdn.email/content/guids/CABINET_c72901d21eb59604cd19a1d8015f0640/images/91631604999928573.png" alt style="display: block;" width="67"></a></td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="esd-structure es-p20t" align="left">
                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                <tbody>
                                                                    <tr>
                                                                        <td width="600" class="esd-container-frame" align="left">
                                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td align="left" class="esd-block-text es-p25r es-p25l es-m-txt-l">
                                                                                            <h1 style="line-height: 150%;">Restablecer la contraseña</h1>
                                                                                            <h1 style="line-height: 150%;">Su código secreto!</h1>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="esd-structure esdev-adapt-off es-p10t es-p20r es-p20l" align="left" style="background-position: center top;">
                                                            <table width="560" cellpadding="0" cellspacing="0" class="esdev-mso-table">
                                                                <tbody>
                                                                    <tr>
                                                                        <td class="esdev-mso-td" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td width="55" class="es-m-p10r esd-container-frame" align="center">
                                                                                            <table cellpadding="0" cellspacing="0" width="100%" style="border-left:2px solid #ffffff;border-right:2px solid #ffffff;border-top:2px solid #ffffff;border-bottom:2px solid #ffffff;background-position: center top; border-radius: 12px; border-collapse: separate;">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <td align="center" class="esd-block-text es-p5t es-p5b es-m-p10r es-m-p10l">
                                                                                                            <h1 style="color: #ffffff;">"""+str(number1)+ """</h1>
                                                                                                        </td>
                                                                                                    </tr>
                                                                                                </tbody>
                                                                                            </table>
                                                                                        </td>
                                                                                        <td width="15"></td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                        <td class="esdev-mso-td" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td width="55" class="esd-container-frame es-m-p10r es-m-p10l" align="center">
                                                                                            <table cellpadding="0" cellspacing="0" width="100%" style="border-left:2px solid #ffffff;border-right:2px solid #ffffff;border-top:2px solid #ffffff;border-bottom:2px solid #ffffff;background-position: center top; border-radius: 12px; border-collapse: separate;">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <td align="center" class="esd-block-text es-p5t es-p5b es-m-p10r es-m-p10l">
                                                                                                            <h1 style="color: #ffffff;">"""+str(number2)+"""</h1>
                                                                                                        </td>
                                                                                                    </tr>
                                                                                                </tbody>
                                                                                            </table>
                                                                                        </td>
                                                                                        <td width="15"></td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                        <td class="esdev-mso-td" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td width="55" class="esd-container-frame es-m-p10r es-m-p10l" align="center">
                                                                                            <table cellpadding="0" cellspacing="0" width="100%" style="border-left:2px solid #ffffff;border-right:2px solid #ffffff;border-top:2px solid #ffffff;border-bottom:2px solid #ffffff;background-position: center top; border-radius: 12px; border-collapse: separate;">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <td align="center" class="esd-block-text es-p5t es-p5b es-m-p10r es-m-p10l">
                                                                                                            <h1 style="color: #ffffff;">"""+str(number3)+"""</h1>
                                                                                                        </td>
                                                                                                    </tr>
                                                                                                </tbody>
                                                                                            </table>
                                                                                        </td>
                                                                                        <td width="15"></td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                        <td class="esdev-mso-td" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td width="55" align="center" class="esd-container-frame es-m-p10r es-m-p10l">
                                                                                            <table cellpadding="0" cellspacing="0" width="100%" style="border-left:2px solid #ffffff;border-right:2px solid #ffffff;border-top:2px solid #ffffff;border-bottom:2px solid #ffffff;background-position: center top; border-radius: 12px; border-collapse: separate;">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <td align="center" class="esd-block-text es-p5t es-p5b es-m-p10r es-m-p10l">
                                                                                                            <h1 style="color: #ffffff;">"""+str(number4)+"""</h1>
                                                                                                        </td>
                                                                                                    </tr>
                                                                                                </tbody>
                                                                                            </table>
                                                                                        </td>
                                                                                        <td width="15"></td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                        <td class="esdev-mso-td" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td width="280" align="left" class="esd-container-frame">
                                                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <td align="center" class="esd-block-spacer" height="18"></td>
                                                                                                    </tr>
                                                                                                </tbody>
                                                                                            </table>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="esd-structure es-p10t" align="left" style="background-position: center top;">
                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                <tbody>
                                                                    <tr>
                                                                        <td width="600" class="esd-container-frame" align="center" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                                <tbody>
                                                                                    <tr>
                                                                                    
                                                                                    </tr>
                                                                                    <tr>
                                                                                    
                                                                                    </tr>
                                                                                    <tr>
                                                                                        <td align="center" class="esd-block-spacer" height="58"></td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr> 
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </body>

    </html>
    """


class EmailHandled():

    def __init__(self, senderEmail, receiverEmail, password, subject, bodyMenssage, alternativeText):
        self.senderEmail = senderEmail
        self.receiverEmail = receiverEmail
        self.password = password
        self.subject = subject
        self.bodyMenssage = bodyMenssage
        self.alternativeText = alternativeText

    def sendHTMLEmail(self):
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = self.subject
        self.message["From"] = self.senderEmail
        self.message["To"] = self.receiverEmail

        self.part1 = MIMEText(self.alternativeText, "plain")
        self.part2 = MIMEText(self.bodyMenssage, "html")

        self.message.attach(self.part1)
        self.message.attach(self.part2)

        self.context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context) as server:
            server.login(self.senderEmail, self.password)
            server.sendmail(
                self.senderEmail, self.receiverEmail, self.message.as_string()
            )

