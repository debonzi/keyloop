import arrow
import sqlalchemy as sa
from pyramid.threadlocal import get_current_request
from sqlalchemy_utils import ArrowType, IPAddressType


def current_ip(*args, **kwargs):
    req = get_current_request()
    if req and hasattr(req, "remote_addr"):
        return req.client_addr
    else:
        return None


def return_now():
    return arrow.utcnow()


class CreatedUpdatedMixin(object):
    """Provides created and updated attributes"""

    created = sa.Column(ArrowType, default=return_now, index=True)
    updated = sa.Column(
        ArrowType, default=return_now, onupdate=arrow.utcnow, index=True
    )
    created_ip = sa.Column(IPAddressType, default=current_ip, nullable=True, index=True)
    updated_ip = sa.Column(
        IPAddressType,
        default=current_ip,
        onupdate=current_ip,
        nullable=True,
        index=True,
    )


class WhiteLabelMixin(object):

    # referencia ao partner (e.g. `loan uuid`)
    partner_slug = sa.Column(sa.String(50), nullable=False, index=True)

    # referencia ao parterner (e.g. `loan uuid`)
    partner_customer_key = sa.Column(sa.String(200), nullable=False, index=True)
