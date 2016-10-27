from chargehound.api_requestor import APIRequestor

requestor = APIRequestor()


class Disputes(object):
    """
    Create a dispute
    This method will return the created dispute.

    :param: str external_identifier
        The id of the dispute in your payment processor.
         For Stripe looks like `dp_XXX`. (required)
    :param: str external_charge
        The id of the disputed charge in your payment
        processor. For Stripe looks like `ch_XXX`. (required)
    :param: str external_customer
        The id of the charged customer in your payment
        processor. For Stripe looks like `cus_XXX`. (optional)
    :param: str reason
        The bank provided reason for the dispute. One
        of `general`, `fraudulent`, `duplicate`, `subscription_canceled`,
        `product_unacceptable`, `product_not_received`, `unrecognized`,
        `credit_not_processed`, `incorrect_account_details`,
        `insufficient_funds`, `bank_cannot_process`,
        `debit_not_authorized`. (required)
    :param: str charged_at
        ISO 8601 timestamp - when the charge was made.
         (required)
    :param: str disputed_at
        ISO 8601 timestamp - when the charge was disputed.
         (required)
    :param: str due_by
        ISO 8601 timestamp - when dispute evidence needs to
        be disputed by. (required)
    :param: str currency
        The currency code of the disputed charge. e.
        g. 'USD'. (required)
    :param: int amount
        The amount of the disputed charge. Amounts are
        in cents (or other minor currency unit.) (required)
    :param: str processor
        The payment processor for the charge. Currently the
        only possible value is `stripe`. (optional)
    :param: str state
        The state of the dispute. One of `needs_response`
        , `warning_needs_response`. (optional)
    :param: str reversal_currency
        The currency code of the dispute balance withdrawal.
        e.g. 'USD'. (optional)
    :param: int fee
        The amount of the dispute fee. Amounts are
        in cents (or other minor currency unit.) (optional)
    :param: int reversal_amount
        The amount of the dispute balance withdrawal (without fee)
        . Amounts are in cents (or other minor currency unit.) (optional)
    :param: int reversal_total
        The total amount of the dispute balance withdrawal (with
        fee). Amounts are in cents (or other minor currency unit.) (optional)
    :param: bool is_charge_refundable
        Is the disputed charge refundable. (optional)
    :param: int submitted_count
        How many times has dispute evidence been submitted.
        (optional)
    :param: str address_line1_check
        State of address check (if available). One
        of `pass`, `fail`, `unavailable`, `checked`. (optional)
    :param: str address_zip_check
        State of address zip check (if available).
        One of `pass`, `fail`, `unavailable`, `checked`. (optional)
    :param: str cvc_check
        State of cvc check (if available). One
        of `pass`, `fail`, `unavailable`, `checked`. (optional)
    :param: str template
        The id of the template to use. (optional)
    :param: object fields
        Key value pairs to hydrate the template's evidence
        fields. (optional)
    :param: array products
        List of products the customer purchased. (optional)
    :param: str account_id
        Set the account id for Connected accounts that are
        charged directly through Stripe. (optional)
    :param: bool submit
        Submit dispute evidence immediately after creation. (optional)
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
    A list of disputes
    This method will list all the disputes that we have synced from Stripe.
    By default the disputes will be ordered by `created`
    with the most recent dispute first.
    `has_more` will be `true` if more results are available.

    :param int limit: Maximum number of disputes to return.
        Default is 20, maximum is 100. (optional)
    :param str starting_after: A dispute id.
        Fetch disputes created after this dispute. (optional)
    :param str ending_before: A dispute id.
        Fetch disputes created before this dispute. (optional)
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
    :param str template: Set the template for this dispute. (optional)
    :param object fields:
        Key value pairs to hydrate the template's evidence fields. (optional)
    :param object products:
        List of products the customer purchased. (optional)
    :param str account_id: Set the associated Stripe account id. (optional)
    :param bool force:
        Bypass the manual review filter. (optional)
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
    :param str template: Set the template for this dispute. (optional)
    :param object fields:
        Key value pairs to hydrate the template's evidence fields. (optional)
    :param object products:
        List of products the customer purchased. (optional)
    :param str account_id: Set the associated Stripe account id. (optional)
    :return: Dispute
    """
    @classmethod
    def update(klass, dispute_id, **kwargs):
        update = kwargs

        return requestor.request('post', 'disputes/{0}'.format(dispute_id),
                                 data=update)
