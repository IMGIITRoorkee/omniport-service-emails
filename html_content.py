from maintainer_site.models.maintainer_group import MaintainerGroup

if isinstance(MaintainerGroup.objects.get().contact_information.get().email_address, str):
    main_email = MaintainerGroup.objects.get().contact_information.get().email_address
else:
    main_email = ''

if isinstance(MaintainerGroup.objects.get().contact_information.get().primary_phone_number, str):
    main_phone = MaintainerGroup.objects.get(
    ).contact_information.get().primary_phone_number
else:
    main_phone = ''

try:
    facebook_link = MaintainerGroup.objects.get(
    ).social_information.get().links.get(site='fac').url
    facebook_site = 'Facebook'
except Exception:
    facebook_link = ''
    facebook_site = ''

try:
    medium_link = MaintainerGroup.objects.get(
    ).social_information.get().links.get(site='med').url
    medium_site = 'Medium'
except Exception:
    medium_link = ''
    medium_site = ''

try:
    instagram_link = MaintainerGroup.objects.get(
    ).social_information.get().links.get(site='ins').url
    instagram_site = 'Instagram'
except Exception:
    instagram_link = ''
    instagram_site = ''

html_content = """
<!DOCTYPE html>
<html>

<body style="align-items: center; height: auto; position: relative; width: 100%; font-weight: normal; 
font-family: Roboto; font-style: normal; margin: 0">
    <div class='table top' style="width: 100%;
    position: relative;
    display: table; 
    background: #293B52;
    height: 48px; 
    padding: 6px 0">
        <div class='row' style="vertical-align: middle;
        display: table-cell;
        padding: 0 18px;">
            <span class='title-left white' style="position: relative;  
            color: #FFFFFF;    
            padding: 0;
            font-size: 18px;
            color: #FFFFFF; 
            float: left;">Subject/Text</span>
            
            <div class='inline-table' style="position: relative;
            height: 1.5rem;
            float: right;
            display: inline-table;">
                <span class='title-right white' style="position: relative; 
                color: #FFFFFF;
                padding: 0.15em 0;
                font-size: 14px; 
                display: table-cell; 
                vertical-align: middle;">
                    <a href='TargetURL/Text' style="color:#F8D16C; 
                    text-decoration:none;"> TargetApp/Text 
                    </a>
                </span>
            </div>
        </div>
    </div>
    <div class='table top-second' style="width: 100%;
    position: relative;
    display: table;height: 65px;
    background: #F8D16C;">
        <div class='row' style="vertical-align: middle;
        display: table-cell;
        padding: 18px;">
            <div class='post1' style='font-size: 14px;
            color: #293B52;'>
            <b>Posted By:</b> Sender/Text
            </div>
            
            <div class='post2' style="font-size: 14px;
            color: #293B52;">
            <b>Posted On:</b> Time/Text
            </div>
        </div>
    </div>
    <div class='table mid' style="width: 100%;
    position: relative;
    display: table; 
    height: auto;">
        <div class='row' style="vertical-align: middle;
        display: table-cell;
        padding: 0 2rem;">
            <div class="mail-body" style="padding: 21px 0;
            height: auto;
            font-size: 14px;
            max-width: 1400px;">Body/Text
            </div>
        </div>
    </div>
    <div class='table bottom' style="width: 100%; 
    position: relative; 
    display: table; 
    height: 100px; 
    background: #293B52; 
    font-size: 14px;">
        <div class='row white' style="vertical-align: middle; display: table-cell;
        padding: 0 18px;position: relative;
        color: #FFFFFF;
        padding: 0;">
            <div class='table bottom2' style="width: 100%; position: relative; display: table;">
                <div class='row bottom3' style="vertical-align: middle; display: table-cell; padding: 0 18px;">
                    
                    <div class='email' style="margin-top: 4px; 
                    margin-bottom: 4px;">
                        <b>Email: <a href="mailto:MaintainerMail/Text" style="color:#F8D16C; 
                        text-decoration: none;">MaintainerMail/Text</a></b>
                    </div>
                    
                    <div class='phone' style="margin-top: 4px; 
                    margin-bottom: 4px;">
                        <b>Phone: <a href="tel:+MaintainerPhone/Text" style="color:#F8D16C; 
                        text-decoration: none;">MaintainerPhone/Text</a></b>
                    </div>
                    
                    <div class='follow' style="margin-top: 4px; 
                    margin-bottom: 4px;">
                        <b>Follow us on: 
                        <a href="FacebookLink/Text" style="color:#F8D16C; 
                        text-decoration: none;">FacebookSite/Text &ensp;</a> 
                        
                        <a href="MediumLink/Text" style="color:#F8D16C; 
                        text-decoration: none;">MediumSite/Text &ensp;</a> 
                        
                        <a href="InstagramLink/Text" style="color: #F8D16C; 
                        text-decoration: none; ">InstagramSite/Text</a></b>
                    </div>
                </div>
                <div class='logo' style="position: relative; 
                float: right; 
                display: table-cell; 
                vertical-align: middle;
                padding-right: 2rem">
                    <!--<img src="data:image/svg+xml;base64," style="width: 100px; height: 100px;"/>-->
                </div>
            </div>
        </div>
    </div>
</body>

</html>


""".replace("MaintainerMail/Text", main_email).replace("MaintainerPhone/Text", main_phone).replace("MaintainerEmail"
                                                                                                   "/Text",
                                                                                                   main_email).replace(
    "FacebookLink/Text", facebook_link).replace("FacebookSite/Text", facebook_site).replace("MediumLink/Text",
                                                                                            medium_link).replace(
    "MediumSite/Text", medium_site).replace("InstagramLink/Text", instagram_link).replace("InstagramSite/Text",
                                                                                          instagram_site)
