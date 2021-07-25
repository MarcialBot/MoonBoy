import numpy as np
import pandas as pd
import ccxt

class Exchange(server):

    _config: Dict = {}
    _ccxt_config: Dict = {}
    _params: Dict = {}
    _ft_has_default: Dict = {
        "stoploss_on_exchange": False,
        "order_time_in_force": ["gtc"],
        "ohlcv_params": {},
        "ohlcv_candle_limit": 500,
        "ohlcv_partial_candle": True,
        "trades_pagination": "time", # 'time' or 'id'
        "trades_pagination_arg": "since",
        "l2_limit_range": None,
        "l2_limit_range_required": True,
    }
    _ft_has: Dict = {}

    def __init__(self, config: Dict[str, Any]) -> None:
        self.name = name


