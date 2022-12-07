from typing import List, Optional

from fastapi import Query
from pydantic import BaseModel, Extra, validator


class UpdateSettings(BaseModel, extra=Extra.forbid):
    @validator(
        "lnbits_admin_users",
        "lnbits_allowed_users",
        "lnbits_theme_options",
        "lnbits_disabled_extensions",
        "lnbits_admin_extensions",
        pre=True,
    )
    def validate(cls, val):
        if type(val) == str:
            val = val.split(",") if val else []
        return val

    lnbits_backend_wallet_class: str = Query(None)
    lnbits_admin_users: List[str] = Query(None)
    lnbits_allowed_users: List[str] = Query(None)
    lnbits_admin_extensions: List[str] = Query(None)
    lnbits_disabled_extensions: List[str] = Query(None)
    lnbits_theme_options: List[str] = Query(None)
    lnbits_force_https: bool = Query(None)
    lnbits_reserve_fee_min: int = Query(None, ge=0)
    lnbits_reserve_fee_percent: float = Query(None, ge=0)
    lnbits_service_fee: float = Query(None, ge=0)
    lnbits_hide_api: bool = Query(None)
    lnbits_site_title: str = Query(None)
    lnbits_site_tagline: str = Query(None)
    lnbits_site_description: str = Query(None)
    lnbits_default_wallet_name: str = Query(None)
    lnbits_denomination: str = Query(None)
    lnbits_custom_logo: str = Query(None)
    lnbits_ad_space: str = Query(None)
    lnbits_ad_space_title: str = Query(None)
    lnbits_ad_space_enabled: bool = Query(None)

    # funding sources
    fake_wallet_secret: str = Query(None)
    lnbits_endpoint: str = Query(None)
    lnbits_key: str = Query(None)
    cliche_endpoint: str = Query(None)
    corelightning_rpc: str = Query(None)
    eclair_url: str = Query(None)
    eclair_pass: str = Query(None)
    lnd_rest_endpoint: str = Query(None)
    lnd_rest_cert: str = Query(None)
    lnd_rest_macaroon: str = Query(None)
    lnd_rest_macaroon_encrypted: str = Query(None)
    lnd_cert: str = Query(None)
    lnd_admin_macaroon: str = Query(None)
    lnd_invoice_macaroon: str = Query(None)
    lnd_grpc_endpoint: str = Query(None)
    lnd_grpc_cert: str = Query(None)
    lnd_grpc_port: int = Query(None, ge=0)
    lnd_grpc_admin_macaroon: str = Query(None)
    lnd_grpc_invoice_macaroon: str = Query(None)
    lnd_grpc_macaroon: str = Query(None)
    lnd_grpc_macaroon_encrypted: str = Query(None)
    lnpay_api_endpoint: str = Query(None)
    lnpay_api_key: str = Query(None)
    lnpay_wallet_key: str = Query(None)
    lntxbot_api_endpoint: str = Query(None)
    lntxbot_key: str = Query(None)
    opennode_api_endpoint: str = Query(None)
    opennode_key: str = Query(None)
    spark_url: str = Query(None)
    spark_token: str = Query(None)
    lntips_api_endpoint: str = Query(None)
    lntips_api_key: str = Query(None)
    lntips_admin_key: str = Query(None)
    lntips_invoice_key: str = Query(None)

    boltz_mempool_space_url: str = Query(None)
    boltz_mempool_space_url_ws: str = Query(None)
    boltz_network: str = Query(None)
    boltz_url: str = Query(None)


class SuperSettings(UpdateSettings):
    super_user: str


class AdminSettings(UpdateSettings):
    super_user: bool
    lnbits_allowed_funding_sources: Optional[List[str]]
