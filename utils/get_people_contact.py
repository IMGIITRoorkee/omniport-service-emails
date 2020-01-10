from formula_one.models import ContactInformation


def get_people_contact(people, use_custom_email, check_if_verified):
    """
    fetch email addresses of people
    :param people: list of person ids
    :param use_custom_email: boolean for whether to use custom email address
    :param check_if_verified: boolean for whether to check email verification
    :return: email address of the person to whom it is sent
    """
    all_contact_info = list()
    for person in people:
        all_contact_info.append(ContactInformation.objects.filter(
            person__in=[person],
        ).first())
    emails = list()
    for contact_info in all_contact_info:
        email = contact_info.institute_webmail_address
        if use_custom_email:
            if check_if_verified:
                if contact_info.email_address_verified:
                    email = contact_info.email_address
                else:
                    return ''
            else:
                email = contact_info.email_address
        emails.append(email)

    return emails
