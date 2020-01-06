
def get_person_contact(person, use_custom_email, check_if_verified):
    """
    :param person:
    :param use_custom_email:
    :param check_if_verified:
    :return: email address of the person to whom it is sent
    """

    email = ''
    contact_info = person.contact_information.first()
    if contact_info:
        try:
            email = contact_info.institute_webmail_address
        except:
            pass
        if use_custom_email:
            try:
                if check_if_verified:
                    if contact_info.email_address_verified:
                        email = contact_info.email_address
                else:
                    email = contact_info.email_address
            except:
                pass
    return email
