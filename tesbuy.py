import MetaTrader5 as mt5

# Fungsi untuk membuka order buy
def open_buy_order(symbol, lot=0.01):
    # Inisialisasi MetaTrader 5
    if not mt5.initialize():
        print(f"Gagal menginisialisasi MetaTrader 5. Error code: {mt5.last_error()}")
        return None

    # Mendapatkan informasi simbol
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"Symbol {symbol} tidak ditemukan.")
        mt5.shutdown()
        return None

    # Pastikan simbol tersedia di MarketWatch
    if not symbol_info.visible:
        if not mt5.symbol_select(symbol, True):
            print(f"Symbol {symbol} tidak tersedia di MarketWatch.")
            mt5.shutdown()
            return None

    # Cek apakah volume lot valid
    if lot < symbol_info.volume_min or lot > symbol_info.volume_max:
        print(f"Lot tidak valid untuk {symbol}. Lot minimum: {symbol_info.volume_min}, Lot maksimum: {symbol_info.volume_max}")
        mt5.shutdown()
        return None

    # Mendapatkan harga ask terbaru untuk order buy
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"Gagal mendapatkan harga tick untuk {symbol}.")
        mt5.shutdown()
        return None

    price = tick.ask  # Harga Ask terbaru untuk order buy
    deviation = 30  # Toleransi deviasi harga

    # Mengambil balance akun untuk menghitung TP dan SL
    account_info = mt5.account_info()
    if account_info is None:
        print("Gagal mendapatkan informasi akun.")
        mt5.shutdown()
        return None

    # Tentukan SL dan TP dalam pip (gunakan jarak wajar, misal 100-200 pip untuk XAUUSD)
    sl_distance = 200 * symbol_info.point  # SL 100 pip di bawah harga Ask
    tp_distance = 800 * symbol_info.point  # TP 200 pip di atas harga Ask
    sl_price = price - sl_distance  # Stop Loss lebih rendah dari harga Ask
    tp_price = price + tp_distance  # Take Profit lebih tinggi dari harga Ask

    # Membuat request order
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,  # Tipe order buy
        "price": price,  # Gunakan harga Ask terbaru
        "sl": sl_price,  # Stop Loss (dihitung lebih rendah dari harga Ask)
        "tp": tp_price,  # Take Profit (dihitung lebih tinggi dari harga Ask)
        "deviation": deviation,
        "magic": 234000,
        "comment": "Buy order dari bot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,  # Menggunakan IOC (Immediate Or Cancel)
    }

    # Kirim request untuk membuka order buy
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Gagal membuka order buy, error code: {result.retcode}. Deskripsi error: {result}")
        mt5.shutdown()
        return None

    print(f"Order buy dibuka dengan sukses! Harga: {price}")

    # Mengambil informasi tentang order yang baru saja dibuka
    order_info = mt5.positions_get(symbol=symbol)
    if order_info:
        for pos in order_info:
            print(f"Order ID: {pos.ticket}, Symbol: {pos.symbol}, Volume: {pos.volume}, Profit: {pos.profit}")
            mt5.shutdown()
            return pos.ticket

    mt5.shutdown()
    return None


# Contoh penggunaan fungsi untuk membuka order buy di simbol XAUUSD dengan lot 0.01
open_buy_order("XAUUSD", lot=0.01)
