import MetaTrader5 as mt5

def open_sell_order(symbol, lot=0.01):
    # Inisialisasi MetaTrader 5
    if not mt5.initialize():
        print(f"Gagal menginisialisasi MetaTrader 5. Error code: {mt5.last_error()}")
        return None

    # Mendapatkan informasi simbol
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"Symbol {symbol} tidak ditemukan.")
        return None

    # Pastikan simbol tersedia di MarketWatch
    if not symbol_info.visible:
        if not mt5.symbol_select(symbol, True):
            print(f"Symbol {symbol} tidak tersedia di MarketWatch.")
            return None

    # Cek apakah volume lot valid
    if lot < symbol_info.volume_min or lot > symbol_info.volume_max:
        print(f"Lot tidak valid untuk {symbol}. Lot minimum: {symbol_info.volume_min}, Lot maksimum: {symbol_info.volume_max}")
        return None

    # Mendapatkan harga bid terbaru untuk order sell
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"Gagal mendapatkan harga tick untuk {symbol}.")
        return None

    price = tick.bid  # Harga Bid terbaru untuk order sell
    deviation = 30  # Toleransi deviasi harga

    # Mengambil balance akun untuk menghitung TP dan SL
    account_info = mt5.account_info()
    if account_info is None:
        print("Gagal mendapatkan informasi akun.")
        return None

    # Tentukan SL dan TP dalam pip (gunakan jarak wajar, misal 100-200 pip untuk XAUUSD)
    sl_distance = 500 * symbol_info.point  # SL 100 pip di atas harga Bid
    tp_distance = 1000 * symbol_info.point  # TP 200 pip di bawah harga Bid
    sl_price = price + sl_distance
    tp_price = price - tp_distance

    # Membuat request order
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL,
        "price": price,  # Gunakan harga Bid terbaru
        "sl": sl_price,  # Stop Loss (dihitung lebih tinggi dari harga Bid)
        "tp": tp_price,  # Take Profit (dihitung lebih rendah dari harga Bid)
        "deviation": deviation,
        "magic": 234000,
        "comment": "Sell order dari bot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,  # Menggunakan IOC (Immediate Or Cancel)
    }

    # Kirim request untuk membuka order sell
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Gagal membuka order sell, error code: {result.retcode}. Deskripsi error: {result}")
        return None

    print(f"Order sell dibuka dengan sukses! Harga: {price}")

    # Mengambil informasi tentang order yang baru saja dibuka
    order_info = mt5.positions_get(symbol=symbol)
    if order_info:
        for pos in order_info:
            print(f"Order ID: {pos.ticket}, Symbol: {pos.symbol}, Volume: {pos.volume}, Profit: {pos.profit}")
            return pos.ticket

    return None

# Contoh penggunaan fungsi untuk membuka order sell di simbol XAUUSD dengan lot 0.01
open_sell_order("XAUUSD", lot=0.01)
