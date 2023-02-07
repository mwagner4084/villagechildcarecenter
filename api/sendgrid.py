import json
from http.client import HTTPSConnection

from django_project import settings


class SendGridContact(dict):
    """ Serializable SendGrid Contact """

    def __init__(self, email: str, first_name: str, last_name: str):
        super().__init__()
        self['email'] = email
        self['first_name'] = first_name
        self['last_name'] = last_name


def sendgrid_add_contacts(contacts: list[SendGridContact], list_ids: list[str] | None = None) -> bool:
    """ Add contacts to SendGrid. """

    conn = HTTPSConnection("api.sendgrid.com")

    headersList = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.SENDGRID_API_KEY}"
    }

    Data = dict[str, list[str] | list[SendGridContact]]

    data: Data = {'contacts': contacts}
    if list_ids:
        data['list_ids'] = list_ids

    payload = json.dumps(data)

    conn.request("PUT", "/v3/marketing/contacts", payload, headersList)
    response = conn.getresponse()

    if response.status == 202:
        return True

    return False
