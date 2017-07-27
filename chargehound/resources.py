from chargehound.api_requestor import APIRequestor

requestor = APIRequestor()


class Disputes(object):
    """
    Create a dispute
    This method will return the created dispute.

    :return: Dispute
    """
    @classmethod
    def create(klass, dispute_id, **kwargs):
        return requestor.request('post', 'disputes',
                                 data=kwargs)

    """
    Retrieve a dispute
    This method will return a single dispute.

    :param str dispute_id: A dispute id (required)
    :return: Dispute
    """
    @classmethod
    def retrieve(klass, dispute_id):
        return requestor.request('get', 'disputes/{0}'.format(dispute_id))

    """
    Retrieve the response for a dispute.
    :param str dispute_id: A dispute id (required)
    :return: Dispute
    """
    @classmethod
    def response(klass, dispute_id):
        return requestor.request('get',
                                 'disputes/{0}/response'.format(dispute_id))

    """
    Accept a dispute and do not submit a response.
    :param str dispute_id: A dispute id (required)
    :return: Dispute
    """
    @classmethod
    def accept(klass, dispute_id):
        return requestor.request('post',
                                 'disputes/{0}/accept'.format(dispute_id))

    """
    A list of disputes
    This method will list all the disputes that we have synced from Stripe.
    By default the disputes will be ordered by `created`
    with the most recent dispute first.
    `has_more` will be `true` if more results are available.
    :return: Disputes
    """
    @classmethod
    def list(klass, **kwargs):
        list_params = kwargs

        return requestor.request('get', 'disputes',
                                 params=list_params)

    """
    Submitting a dispute
    You will want to submit the dispute through Chargehound after you recieve
    a notification from Stripe of a new dispute.
    With one `POST` request you can update a dispute with the
    evidence fields and send the generated response to Stripe.
    The response will have a `201` status if the submit was successful.
    The dispute will also be in the submitted state.

    :param str dispute_id: A dispute id (required)
    :return: Dispute
    """
    @classmethod
    def submit(klass, dispute_id, **kwargs):
        update = kwargs

        return requestor.request('post',
                                 'disputes/{0}/submit'.format(dispute_id),
                                 data=update)

    """
    Updating a dispute
    You can update the template and the fields on a dispute.

    :param str dispute_id: A dispute id (required)
    :return: Dispute
    """
    @classmethod
    def update(klass, dispute_id, **kwargs):
        update = kwargs

        return requestor.request('post', 'disputes/{0}'.format(dispute_id),
                                 data=update)
