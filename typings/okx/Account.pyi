"""
This type stub file was generated by pyright.
"""

from .consts import *
from .okxclient import OkxClient

class AccountAPI(OkxClient):
    def __init__(
        self,
        api_key=...,
        api_secret_key=...,
        passphrase=...,
        use_server_time=...,
        flag=...,
        domain=...,
        debug=...,
        proxy=...,
    ) -> None: ...
    def get_position_risk(self, instType=...):  # -> Any:
        ...
    def get_account_balance(self, ccy=...):  # -> Any:
        ...
    def get_positions(self, instType=..., instId=...):  # -> Any:
        ...
    def position_builder(
        self,
        inclRealPosAndEq=...,
        spotOffsetType=...,
        greeksType=...,
        simPos=...,
        simAsset=...,
    ):  # -> Any:
        ...
    def get_account_bills(
        self,
        instType=...,
        ccy=...,
        mgnMode=...,
        ctType=...,
        type=...,
        subType=...,
        after=...,
        before=...,
        limit=...,
    ):  # -> Any:
        ...
    def get_account_bills_archive(
        self,
        instType=...,
        ccy=...,
        mgnMode=...,
        ctType=...,
        type=...,
        subType=...,
        after=...,
        before=...,
        limit=...,
        begin=...,
        end=...,
    ):  # -> Any:
        ...
    def get_account_config(self):  # -> Any:
        ...
    def set_position_mode(self, posMode):  # -> Any:
        ...
    def set_leverage(self, lever, mgnMode, instId=..., ccy=..., posSide=...):  # -> Any:
        ...
    def get_max_order_size(self, instId, tdMode, ccy=..., px=...):  # -> Any:
        ...
    def get_max_avail_size(
        self,
        instId,
        tdMode,
        ccy=...,
        reduceOnly=...,
        unSpotOffset=...,
        quickMgnType=...,
    ):  # -> Any:
        ...
    def adjustment_margin(self, instId, posSide, type, amt, loanTrans=...):  # -> Any:
        ...
    def get_leverage(self, mgnMode, ccy=..., instId=...):  # -> Any:
        ...
    def get_instruments(
        self, instType=..., ugly=..., instFamily=..., instId=...
    ):  # -> Any:
        ...
    def get_max_loan(self, instId, mgnMode, mgnCcy=...):  # -> Any:
        ...
    def get_fee_rates(
        self, instType, instId=..., uly=..., category=..., instFamily=...
    ):  # -> Any:
        ...
    def get_interest_accrued(
        self, instId=..., ccy=..., mgnMode=..., after=..., before=..., limit=...
    ):  # -> Any:
        ...
    def get_interest_rate(self, ccy=...):  # -> Any:
        ...
    def set_greeks(self, greeksType):  # -> Any:
        ...
    def set_isolated_mode(self, isoMode, type):  # -> Any:
        ...
    def get_max_withdrawal(self, ccy=...):  # -> Any:
        ...
    def borrow_repay(self, ccy=..., side=..., amt=..., ordId=...):  # -> Any:
        ...
    def get_borrow_repay_history(
        self, ccy=..., after=..., before=..., limit=...
    ):  # -> Any:
        ...
    def get_interest_limits(self, type=..., ccy=...):  # -> Any:
        ...
    def get_simulated_margin(
        self, instType=..., inclRealPos=..., spotOffsetType=..., simPos=...
    ):  # -> Any:
        ...
    def get_greeks(self, ccy=...):  # -> Any:
        ...
    def get_account_position_risk(self):  # -> Any:
        ...
    def get_positions_history(
        self,
        instType=...,
        instId=...,
        mgnMode=...,
        type=...,
        posId=...,
        after=...,
        before=...,
        limit=...,
    ):  # -> Any:
        ...
    def get_account_position_tiers(
        self, instType=..., uly=..., instFamily=...
    ):  # -> Any:
        ...
    def get_VIP_interest_accrued_data(
        self, ccy=..., ordId=..., after=..., before=..., limit=...
    ):  # -> Any:
        ...
    def get_VIP_interest_deducted_data(
        self, ccy=..., ordId=..., after=..., before=..., limit=...
    ):  # -> Any:
        ...
    def get_VIP_loan_order_list(
        self, ordId=..., state=..., ccy=..., after=..., before=..., limit=...
    ):  # -> Any:
        ...
    def get_VIP_loan_order_detail(
        self, ccy=..., ordId=..., after=..., before=..., limit=...
    ):  # -> Any:
        ...
    def set_risk_offset_typel(self, type=...):  # -> Any:
        ...
    def set_auto_loan(self, autoLoan=...):  # -> Any:
        ...
    def activate_option(self):  # -> Any:
        ...
    def get_fix_loan_borrowing_limit(self):  # -> Any:
        ...
    def get_fix_loan_borrowing_quote(
        self, type=..., ccy=..., amt=..., maxRate=..., term=..., ordId=...
    ):  # -> Any:
        ...
    def place_fix_loan_borrowing_order(
        self, ccy=..., amt=..., maxRate=..., term=..., reborrow=..., reborrowRate=...
    ):  # -> Any:
        ...
    def amend_fix_loan_borrowing_order(
        self, ordId=..., reborrow=..., renewMaxRate=...
    ):  # -> Any:
        ...
    def fix_loan_manual_reborrow(self, ordId=..., maxRate=...):  # -> Any:
        ...
    def repay_fix_loan_borrowing_order(self, ordId=...):  # -> Any:
        ...
    def get_fix_loan_borrowing_orders_list(
        self, ordId=..., ccy=..., state=..., after=..., before=..., limit=...
    ):  # -> Any:
        ...
    def spot_manual_borrow_repay(self, ccy=..., side=..., amt=...):  # -> Any:
        ...
    def set_auto_repay(self, autoRepay=...):  # -> Any:
        ...
    def spot_borrow_repay_history(
        self, ccy=..., type=..., after=..., before=..., limit=...
    ):  # -> Any:
        ...
