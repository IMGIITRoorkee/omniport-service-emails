import re
from maintainer_site.models.maintainer_group import MaintainerGroup


def get_html_content():
    maintainer = MaintainerGroup.objects.filter().first()
    if maintainer is None:
        return None
    else:
        contact_info = maintainer.contact_information.filter()
        social_info = maintainer.social_information.filter()
        replacements = {
            'MaintainerMail': contact_info.get().email_address,
            'MaintainerPhone': contact_info.get().primary_phone_number,
        }

        content = """
<!DOCTYPE html>
<html>
   <body style="align-items: center; height: auto; position: relative; 
      width: 100%; font-weight: normal; font-family: Roboto; font-style: 
      normal; margin: 0">
      <div class='table top' style="width: 100%; 
         position: relative; display: table; background: #293B52; height: 
         48px; padding: 6px 0">
         <div class='row' style="vertical-align: 
            middle; display: table-cell; padding: 0 18px;">
            <span 
               class='title-left white' style="position: relative; color: #FFFFFF; 
               padding: 0; font-size: 18px; color: #FFFFFF; float: 
               left;">Subject</span> 
            <div class='inline-table' style="position: relative; 
               height: 1.5rem; float: right; display: inline-table;"> 
               <span class='title-right white' style="position: 
                  relative; color: #FFFFFF; padding: 0.15em 0; font-size: 
                  14px; display: table-cell; vertical-align: middle;"> <a 
                  href='TargetURL' style="color:#F8D16C; 
                  text-decoration:none;"> TargetApp </a> </span> 
            </div>
         </div>
      </div>
      <div class='table top-second' style="width: 
         100%; position: relative; display: table;height: 65px; 
         background: #F8D16C;">
         <div class='row' 
            style="vertical-align: middle; display: table-cell; 
            padding: 18px;">
            <div class='post1' style='font-size: 
               14px; color: #293B52;'> <b>Posted By:</b> Sender </div>
            <div class='post2' style="font-size: 14px; color: 
               #293B52;"> <b>Posted On:</b> Time </div>
         </div>
      </div>
      <div class='table mid' style="width: 100%; position: 
         relative; display: table; height: auto;">
         <div 
            class='row' style="vertical-align: middle; display: 
            table-cell; padding: 0 2rem;">
            <div class="mail-body" 
               style="padding: 21px 0; height: auto; font-size: 14px; 
               max-width: 1400px;">Body </div>
         </div>
      </div>
      <div 
         class='table bottom' style="width: 100%; position: 
         relative; display: table; height: 100px; background: 
         #293B52; font-size: 14px;">
         <div class='row white' 
            style="vertical-align: middle; display: table-cell; 
            padding: 0 18px;position: relative; color: #FFFFFF; 
            padding: 0;">
            <div class='table bottom2' style="width: 
               100%; position: relative; display: table;">
               <div 
                  class='row bottom3' style="vertical-align: middle; 
                  display: table-cell; padding: 0 18px;">
                  <div class='email' style="margin-top: 4px; 
                     margin-bottom: 4px;"> <b>Email: <a 
                     href="mailto:MaintainerMail" 
                     style="color:#F8D16C; text-decoration: 
                     none;">MaintainerMail</a></b> </div>
                  <div class='phone' style="margin-top: 4px; 
                     margin-bottom: 4px;"> <b>Phone: <a 
                     href="tel:+MaintainerPhone" style="color:#F8D16C; 
                     text-decoration: none;">MaintainerPhone</a></b> 
                  </div>
                  <div class='follow' style="margin-top: 4px; 
                     margin-bottom: 4px;">
                     <b>Follow us on: 
                     <a href='FacebookLink' style="color:#F8D16C; 
                        text-decoration: none;">FacebookSite</a> &ensp; 
                     <a href='MediumLink' style="color:#F8D16C; 
                        text-decoration: none;">MediumSite</a> &ensp; 
                     <a href='InstagramLink' style="color: 
                        #F8D16C; text-decoration: none; 
                        ">InstagramSite</a></b> 
                  </div>
               </div>
               <div 
                  class='logo' style="position: relative; 
                  float: right; display: table-cell; 
                  vertical-align: middle; padding: 22px 32px"> 
                  <img src="cid:logo" style="width: 66px; 
                     height: 66px;"/> 
               </div>
            </div>
         </div>
      </div>
   </body>
</html>
        """

        def remove_link(link):
            bit = "<a href='" + link + "[\s\S]*?</a>"
            clean = re.compile(bit)
            return re.sub(clean, '', content)

        try:
            replacements['FacebookLink'] = social_info.first().links.filter(
                site='fac').first().url
            replacements['FacebookSite'] = 'Facebook'
        except AttributeError:
            content = remove_link('Facebook')
        try:
            replacements['MediumLink'] = social_info.first().links.filter(
                site='med').first().url
            replacements['MediumSite'] = 'Medium'
        except AttributeError:
            content = remove_link('Medium')

        try:
            replacements['InstagramLink'] = social_info.first().links.filter(
                site='ins').first().url
            replacements['InstagramSite'] = 'Instagram'
        except AttributeError:
            content = remove_link('Instagram')

        for to_replace, replace_by in replacements.items():
            content = content.replace(to_replace, replace_by)
        return content
