from typing import List, Optional, Union

from lnbits.helpers import urlsafe_short_hash

from . import db
from .models import createLnurlpos, lnurlpospayment, lnurlposs

###############lnurlposS##########################


async def create_lnurlpos(data: createLnurlpos,) -> lnurlposs:
    lnurlpos_id = urlsafe_short_hash()
    lnurlpos_key = urlsafe_short_hash()
    await db.execute(
        """
        INSERT INTO lnurlpos.lnurlposs (
            id,
            key,
            title,
            wallet,
            currency
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (lnurlpos_id, lnurlpos_key, data.title, data.wallet, data.currency),
    )
    return await get_lnurlpos(lnurlpos_id)


async def update_lnurlpos(lnurlpos_id: str, **kwargs) -> Optional[lnurlposs]:
    q = ", ".join([f"{field[0]} = ?" for field in kwargs.items()])
    await db.execute(
        f"UPDATE lnurlpos.lnurlposs SET {q} WHERE id = ?",
        (*kwargs.values(), lnurlpos_id),
    )
    row = await db.fetchone(
        "SELECT * FROM lnurlpos.lnurlposs WHERE id = ?", (lnurlpos_id,)
    )
    return lnurlposs(**row) if row else None


async def get_lnurlpos(lnurlpos_id: str) -> lnurlposs:
    row = await db.fetchone(
        "SELECT * FROM lnurlpos.lnurlposs WHERE id = ?", (lnurlpos_id,)
    )
    return lnurlposs(**row) if row else None


async def get_lnurlposs(wallet_ids: Union[str, List[str]]) -> List[lnurlposs]:
    wallet_ids = [wallet_ids]
    q = ",".join(["?"] * len(wallet_ids[0]))
    rows = await db.fetchall(
        f"""
        SELECT * FROM lnurlpos.lnurlposs WHERE wallet IN ({q})
        ORDER BY id
        """,
        (*wallet_ids,),
    )

    return [lnurlposs(**row) if row else None for row in rows]


async def delete_lnurlpos(lnurlpos_id: str) -> None:
    await db.execute("DELETE FROM lnurlpos.lnurlposs WHERE id = ?", (lnurlpos_id,))

    ########################lnulpos payments###########################


async def create_lnurlpospayment(
    posid: str,
    payload: Optional[str] = None,
    pin: Optional[str] = None,
    payhash: Optional[str] = None,
    sats: Optional[int] = 0,
) -> lnurlpospayment:
    lnurlpospayment_id = urlsafe_short_hash()
    await db.execute(
        """
        INSERT INTO lnurlpos.lnurlpospayment (
            id,
            posid,
            payload,
            pin,
            payhash,
            sats
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (lnurlpospayment_id, posid, payload, pin, payhash, sats),
    )
    return await get_lnurlpospayment(lnurlpospayment_id)


async def update_lnurlpospayment(
    lnurlpospayment_id: str, **kwargs
) -> Optional[lnurlpospayment]:
    q = ", ".join([f"{field[0]} = ?" for field in kwargs.items()])
    await db.execute(
        f"UPDATE lnurlpos.lnurlpospayment SET {q} WHERE id = ?",
        (*kwargs.values(), lnurlpospayment_id),
    )
    row = await db.fetchone(
        "SELECT * FROM lnurlpos.lnurlpospayment WHERE id = ?", (lnurlpospayment_id,)
    )
    return lnurlpospayment(**row) if row else None


async def get_lnurlpospayment(lnurlpospayment_id: str) -> lnurlpospayment:
    row = await db.fetchone(
        "SELECT * FROM lnurlpos.lnurlpospayment WHERE id = ?", (lnurlpospayment_id,)
    )
    return lnurlpospayment(**row) if row else None