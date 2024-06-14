from STO.stock_df import df
import yfinance as yf

class stockScreener(df):
    def stock_screener(self, market_cap_min=None, market_cap_max=None, pe_min=None, pe_max=None):
        data = yf.download(self.ticker, period='1d')
        info = yf.Ticker(self.ticker).info
        market_cap = info['marketCap']
        pe_ratio = info['trailingPE']
        if market_cap_min is not None and market_cap < market_cap_min:
            error = True
        if market_cap_max is not None and market_cap > market_cap_max:
            error = True
        if pe_min is not None and pe_ratio < pe_min:
            error = True
        if pe_max is not None and pe_ratio > pe_max:
            error = True
        
        return info if error != True else None