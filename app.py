import MetaTrader5 as mt5
import pandas as pd
import time
import numpy as np



#          _____                    _____                    _____                    _____                    _____                    _____          
#         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
#        /::\    \                /::\    \                /::\    \                /::\____\                /::\    \                /::\____\        
#       /::::\    \              /::::\    \               \:::\    \              /:::/    /               /::::\    \              /::::|   |        
#      /::::::\    \            /::::::\    \               \:::\    \            /:::/    /               /::::::\    \            /:::::|   |        
#     /:::/\:::\    \          /:::/\:::\    \               \:::\    \          /:::/    /               /:::/\:::\    \          /::::::|   |        
#    /:::/__\:::\    \        /:::/__\:::\    \               \:::\    \        /:::/____/               /:::/__\:::\    \        /:::/|::|   |        
#   /::::\   \:::\    \      /::::\   \:::\    \              /::::\    \      /::::\    \              /::::\   \:::\    \      /:::/ |::|   |        
#  /::::::\   \:::\    \    /::::::\   \:::\    \    ____    /::::::\    \    /::::::\    \   _____    /::::::\   \:::\    \    /:::/  |::|   | _____  
# /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /\   \  /:::/\:::\    \  /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \ 
#/:::/  \:::\   \:::|    |/:::/  \:::\   \:::\____\/::\   \/:::/  \:::\____\/:::/  \:::\    /::\____\/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\
#\::/   |::::\  /:::|____|\::/    \:::\  /:::/    /\:::\  /:::/    \::/    /\::/    \:::\  /:::/    /\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /
# \/____|:::::\/:::/    /  \/____/ \:::\/:::/    /  \:::\/:::/    / \/____/  \/____/ \:::\/:::/    /  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    / 
#       |:::::::::/    /            \::::::/    /    \::::::/    /                    \::::::/    /            \::::::/    /           |::|/:::/    /  
#       |::|\::::/    /              \::::/    /      \::::/____/                      \::::/    /              \::::/    /            |::::::/    /   
#       |::| \::/____/               /:::/    /        \:::\    \                      /:::/    /               /:::/    /             |:::::/    /    
#       |::|  ~|                    /:::/    /          \:::\    \                    /:::/    /               /:::/    /              |::::/    /     
#       |::|   |                   /:::/    /            \:::\    \                  /:::/    /               /:::/    /               /:::/    /      
#       \::|   |                  /:::/    /              \:::\____\                /:::/    /               /:::/    /               /:::/    /       
#        \:|   |                  \::/    /                \::/    /                \::/    /                \::/    /                \::/    /        
#         \|___|                   \/____/                  \/____/                  \/____/                  \/____/                  \/____/  


#            ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  
#           ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
#            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
#            ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
#            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
#            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
#            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  


#                                uuuuuuuuuuuuuuuuuuuuu.
#                            .u$$$$$$$$$$$$$$$$$$$$$$$$$$W.
#                            u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Wu.
#                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
#                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                    `    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                    .i$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
#                    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$W
#                    .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$W
#                    .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
#                    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
#                    W$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#            $u       #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$~
#            $#      `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#            $i        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#            $$        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#            $$         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#            #$.        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#            $$      $iW$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$!
#            $$i      $$$$$$$#"" `"""#$$$$$$$$$$$$$$$$$#""""""#$$$$$$$$$$$$$$$W
#            #$$W    `$$$#"            "       !$$$$$`           `"#$$$$$$$$$$#
#            $$$     ``                 ! !iuW$$$$$                 #$$$$$$$#
#            #$$    $u                  $   $$$$$$$                  $$$$$$$~
#            "#    #$$i.               #   $$$$$$$.                 `$$$$$$
#                    $$$$$i.                """#$$$$i.               .$$$$#
#                    $$$$$$$$!         .   `    $$$$$$$$$i           $$$$$
#                    `$$$$$  $iWW   .uW`        #$$$$$$$$$W.       .$$$$$$#
#                        "#$$$$$$$$$$$$#`          $$$$$$$$$$$iWiuuuW$$$$$$$$W
#                        !#""    ""             `$$$$$$$##$$$$$$$$$$$$$$$$
#                    i$$$$    .                   !$$$$$$ .$$$$$$$$$$$$$$$#
#                    $$$$$$$$$$`                    $$$$$$$$$Wi$$$$$$#"#$$`
#                   #$$$$$$$$$W.                   $$$$$$$$$$$#   ``
#                    `$$$$##$$$$!       i$u.  $. .i$$$$$$$$$#""
#                        "     `#W       $$$$$$$$$$$$$$$$$$$`      u$#
#                                        W$$$$$$$$$$$$$$$$$$      $$$$W
#                                        $$`!$$$##$$$$``$$$$      $$$$!
#                                    i$" $$$$  $$#"`  """     W$$$$
#                                                            W$$$$!
#                                uW$$  uu  uu.  $$$  $$$Wu#   $$$$$$
#                                ~$$$$iu$$iu$$$uW$$! $$$$$$i .W$$$$$$
#                        ..  !   "#$$$$$$$$$$##$$$$$$$$$$$$$$$$$$$$#"
#                        $$W  $     "#$$$$$$$iW$$$$$$$$$$$$$$$$$$$$$W
#                        $#`   `       ""#$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                        !$$$$$$$$$$$$$$$$$$$$$#`
#                                        $$$$$$$$$$$$$$$$$$$$$$!
#                                        $$$$$$$$$$$$$$$$$$$$$$$`
#                                        $$$$$$$$$$$$$$$$$$$$"
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                                                                                                                                                                

#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
# Path ke MetaTrader 5 terminal
terminal_path = "C:\\Program Files\\MetaTrader 5\\terminal64.exe"

# Inisialisasi MetaTrader 5
if not mt5.initialize(terminal=terminal_path):
    print(f"Gagal menginisialisasi MetaTrader 5, error: {mt5.last_error()}")
    exit()

# Login ke akun MetaTrader 5
account_number = ""
password = ""
server = ""

login_status = mt5.login(account_number, password=password, server=server)

if login_status:
    print(f"Berhasil login ke akun {account_number}")
else:
    print(f"Gagal login ke akun {account_number}, error code: {mt5.last_error()}")
    mt5.shutdown()
    exit()

# Mengambil informasi akun
account_info = mt5.account_info()
if account_info is not None:
    print(f"Nama Akun: {account_info.name}")
    print(f"Balance: {account_info.balance}")
else:
    print("Gagal mendapatkan informasi akun.")
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def open_buy_order(symbol, lot=0.01):
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

    # Mendapatkan harga ask terbaru untuk order buy
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"Gagal mendapatkan harga tick untuk {symbol}.")
        return None

    price = tick.ask  # Harga Ask terbaru untuk order buy
    deviation = 30  # Toleransi deviasi harga

    # Mengambil balance akun untuk menghitung TP dan SL
    account_info = mt5.account_info()
    if account_info is None:
        print("Gagal mendapatkan informasi akun.")
        return None

    # Tentukan SL dan TP dalam pip (gunakan jarak wajar, misal 100-200 pip untuk XAUUSD)
    sl_distance = 500 * symbol_info.point  # SL 200 pip di bawah harga Ask
    tp_distance = 1000 * symbol_info.point  # TP 800 pip di atas harga Ask
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
        return None

    print(f"Order buy dibuka dengan sukses! Harga: {price}")

    # Mengambil informasi tentang order yang baru saja dibuka
    order_info = mt5.positions_get(symbol=symbol)
    if order_info:
        for pos in order_info:
            print(f"Order ID: {pos.ticket}, Symbol: {pos.symbol}, Volume: {pos.volume}, Profit: {pos.profit}")
            return pos.ticket

    return None
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

def open_buy_order_m5(symbol, lot=0.01):
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

    # Mendapatkan harga ask terbaru untuk order buy
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"Gagal mendapatkan harga tick untuk {symbol}.")
        return None

    price = tick.ask  # Harga Ask terbaru untuk order buy
    deviation = 30  # Toleransi deviasi harga

    # Mengambil balance akun untuk menghitung TP dan SL
    account_info = mt5.account_info()
    if account_info is None:
        print("Gagal mendapatkan informasi akun.")
        return None

    # Tentukan SL dan TP dalam pip (gunakan jarak wajar, misal 100-200 pip untuk XAUUSD)
    sl_distance = 800 * symbol_info.point  # SL 200 pip di bawah harga Ask
    tp_distance = 1600 * symbol_info.point  # TP 800 pip di atas harga Ask
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
        return None

    print(f"Order buy dibuka dengan sukses! Harga: {price}")

    # Mengambil informasi tentang order yang baru saja dibuka
    order_info = mt5.positions_get(symbol=symbol)
    if order_info:
        for pos in order_info:
            print(f"Order ID: {pos.ticket}, Symbol: {pos.symbol}, Volume: {pos.volume}, Profit: {pos.profit}")
            return pos.ticket

    return None

#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def open_buy_order_m15(symbol, lot=0.01):
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

    # Mendapatkan harga ask terbaru untuk order buy
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"Gagal mendapatkan harga tick untuk {symbol}.")
        return None

    price = tick.ask  # Harga Ask terbaru untuk order buy
    deviation = 30  # Toleransi deviasi harga

    # Mengambil balance akun untuk menghitung TP dan SL
    account_info = mt5.account_info()
    if account_info is None:
        print("Gagal mendapatkan informasi akun.")
        return None

    # Tentukan SL dan TP dalam pip (gunakan jarak wajar, misal 100-200 pip untuk XAUUSD)
    sl_distance = 1600 * symbol_info.point  # SL 200 pip di bawah harga Ask
    tp_distance = 3200 * symbol_info.point  # TP 800 pip di atas harga Ask
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
        return None

    print(f"Order buy dibuka dengan sukses! Harga: {price}")

    # Mengambil informasi tentang order yang baru saja dibuka
    order_info = mt5.positions_get(symbol=symbol)
    if order_info:
        for pos in order_info:
            print(f"Order ID: {pos.ticket}, Symbol: {pos.symbol}, Volume: {pos.volume}, Profit: {pos.profit}")
            return pos.ticket

    return None
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def open_buy_order_m30(symbol, lot=0.01):
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

    # Mendapatkan harga ask terbaru untuk order buy
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"Gagal mendapatkan harga tick untuk {symbol}.")
        return None

    price = tick.ask  # Harga Ask terbaru untuk order buy
    deviation = 30  # Toleransi deviasi harga

    # Mengambil balance akun untuk menghitung TP dan SL
    account_info = mt5.account_info()
    if account_info is None:
        print("Gagal mendapatkan informasi akun.")
        return None

    # Tentukan SL dan TP dalam pip (gunakan jarak wajar, misal 100-200 pip untuk XAUUSD)
    sl_distance = 1600 * symbol_info.point  # SL 200 pip di bawah harga Ask
    tp_distance = 3200 * symbol_info.point  # TP 800 pip di atas harga Ask
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
        return None

    print(f"Order buy dibuka dengan sukses! Harga: {price}")

    # Mengambil informasi tentang order yang baru saja dibuka
    order_info = mt5.positions_get(symbol=symbol)
    if order_info:
        for pos in order_info:
            print(f"Order ID: {pos.ticket}, Symbol: {pos.symbol}, Volume: {pos.volume}, Profit: {pos.profit}")
            return pos.ticket

    return None
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def open_buy_order_h1(symbol, lot=0.01):
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

    # Mendapatkan harga ask terbaru untuk order buy
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"Gagal mendapatkan harga tick untuk {symbol}.")
        return None

    price = tick.ask  # Harga Ask terbaru untuk order buy
    deviation = 30  # Toleransi deviasi harga

    # Mengambil balance akun untuk menghitung TP dan SL
    account_info = mt5.account_info()
    if account_info is None:
        print("Gagal mendapatkan informasi akun.")
        return None

    # Tentukan SL dan TP dalam pip (gunakan jarak wajar, misal 100-200 pip untuk XAUUSD)
    sl_distance = 1600 * symbol_info.point  # SL 200 pip di bawah harga Ask
    tp_distance = 3200 * symbol_info.point  # TP 800 pip di atas harga Ask
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
        return None

    print(f"Order buy dibuka dengan sukses! Harga: {price}")

    # Mengambil informasi tentang order yang baru saja dibuka
    order_info = mt5.positions_get(symbol=symbol)
    if order_info:
        for pos in order_info:
            print(f"Order ID: {pos.ticket}, Symbol: {pos.symbol}, Volume: {pos.volume}, Profit: {pos.profit}")
            return pos.ticket

    return None
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

def open_buy_order_h4(symbol, lot=0.01):
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

    # Mendapatkan harga ask terbaru untuk order buy
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"Gagal mendapatkan harga tick untuk {symbol}.")
        return None

    price = tick.ask  # Harga Ask terbaru untuk order buy
    deviation = 30  # Toleransi deviasi harga

    # Mengambil balance akun untuk menghitung TP dan SL
    account_info = mt5.account_info()
    if account_info is None:
        print("Gagal mendapatkan informasi akun.")
        return None

    # Tentukan SL dan TP dalam pip (gunakan jarak wajar, misal 100-200 pip untuk XAUUSD)
    sl_distance = 300 * symbol_info.point  # SL 200 pip di bawah harga Ask
    tp_distance = 800 * symbol_info.point  # TP 800 pip di atas harga Ask
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
        return None

    print(f"Order buy dibuka dengan sukses! Harga: {price}")

    # Mengambil informasi tentang order yang baru saja dibuka
    order_info = mt5.positions_get(symbol=symbol)
    if order_info:
        for pos in order_info:
            print(f"Order ID: {pos.ticket}, Symbol: {pos.symbol}, Volume: {pos.volume}, Profit: {pos.profit}")
            return pos.ticket

    return None
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def is_bullish_engulfing(df):
    # Memastikan bahwa kita memiliki setidaknya 2 candlestick untuk analisis
    if len(df) < 2:
        return False

    # Ambil candlestick terakhir dan candlestick sebelumnya
    last_candle = df.iloc[-1]
    previous_candle = df.iloc[-2]

    # Memeriksa apakah pola bullish engulfing terbentuk
    if (previous_candle['close'] < previous_candle['open'] and  # Candlestick sebelumnya bearish
        last_candle['close'] > last_candle['open'] and        # Candlestick terakhir bullish
        last_candle['open'] < previous_candle['close'] and    # Open candlestick terakhir lebih rendah dari close candlestick sebelumnya
        last_candle['close'] > previous_candle['open']):       # Close candlestick terakhir lebih tinggi dari open candlestick sebelumnya
        return True

    return False

#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def get_total_profit():
    """
    Menghitung total profit dari semua posisi terbuka.
    """
    positions = mt5.positions_get()  # Ambil semua posisi yang terbuka
    if positions is None:
        print("Tidak ada posisi terbuka saat ini.")
        return 0

    total_profit = sum(pos.profit for pos in positions)  # Hitung total profit
    return total_profit
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

def is_bearish_engulfing(df):
    # Memastikan bahwa kita memiliki setidaknya 2 candlestick untuk analisis
    if len(df) < 2:
        return False

    # Ambil candlestick terakhir dan candlestick sebelumnya
    last_candle = df.iloc[-1]
    previous_candle = df.iloc[-2]

    # Memeriksa apakah pola bearish engulfing terbentuk
    if (previous_candle['close'] > previous_candle['open'] and  # Candlestick sebelumnya bullish
        last_candle['close'] < last_candle['open'] and        # Candlestick terakhir bearish
        last_candle['open'] > previous_candle['close'] and    # Open candlestick terakhir lebih tinggi dari close candlestick sebelumnya
        last_candle['close'] < previous_candle['open']):       # Close candlestick terakhir lebih rendah dari open candlestick sebelumnya
        return True

    return False
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def calculate_support_resistance(df, period=1000):
    if len(df) < period:
        return None, None  # Tidak cukup data untuk menghitung support/resistance
    
    support = df['low'].tail(period).min()
    resistance = df['high'].tail(period).max()
    return support, resistance
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def get_candlestick_data(symbol, timeframe, number_of_candles):
    # Mengambil data candlestick dari MT5
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, number_of_candles)
    if rates is None:
        print(f"Gagal mengambil data candlestick untuk simbol {symbol} di timeframe {timeframe}.")
        return None

    # Mengonversi data ke DataFrame
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')  # Konversi timestamp
    return df
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
# Fungsi untuk mendeteksi pola Hammer setelah candlestick terakhir sudah close
def is_hammer(df):
    """
    Mendeteksi pola hammer pada candlestick yang sudah close.
    """
    # Pastikan ada setidaknya satu candle yang sudah close
    if len(df) < 2:
        return False  # Tidak cukup data untuk mendeteksi pola

    # Ambil candlestick yang sudah tertutup (candle sebelumnya)
    last_candle = df.iloc[-2]  # Mengambil candle terakhir yang sudah close (candle ke-2 dari belakang)

    # Perhitungan komponen candlestick
    body_size = abs(last_candle['close'] - last_candle['open'])  # Ukuran body dari candle
    lower_wick = last_candle['open'] - last_candle['low'] if last_candle['open'] > last_candle['close'] else last_candle['close'] - last_candle['low']  # Ukuran sumbu bawah
    upper_wick = last_candle['high'] - last_candle['close'] if last_candle['close'] > last_candle['open'] else last_candle['high'] - last_candle['open']  # Ukuran sumbu atas

    # Syarat pola hammer:
    # - Sumbu bawah lebih panjang dari 2x ukuran body
    # - Sumbu atas lebih pendek dari ukuran body
    # - Badan yang kecil
    if lower_wick > 2 * body_size and upper_wick < body_size:
        return True

    return False
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

# Fungsi untuk menutup semua posisi terbuka
def close_all_positions():
    """
    Menutup semua posisi yang terbuka.
    """
    positions = mt5.positions_get()  # Ambil semua posisi yang terbuka
    if positions is None:
        print("Tidak ada posisi terbuka yang perlu ditutup.")
        return False

    success = True
    for pos in positions:
        # Tentukan apakah posisi adalah BUY atau SELL dan atur tipe order penutup
        close_type = mt5.ORDER_TYPE_SELL if pos.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
        
        # Request untuk menutup posisi
        close_request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": pos.symbol,
            "volume": pos.volume,  # Tutup seluruh volume posisi
            "type": close_type,
            "position": pos.ticket,  # ID posisi yang akan ditutup
            "price": mt5.symbol_info_tick(pos.symbol).bid if close_type == mt5.ORDER_TYPE_SELL else mt5.symbol_info_tick(pos.symbol).ask,
            "deviation": 20,  # Toleransi deviasi harga
            "magic": 234000,
            "comment": "Menutup semua posisi dari bot",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        # Kirim request untuk menutup posisi
        result = mt5.order_send(close_request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"Gagal menutup posisi {pos.ticket}. Error code: {result.retcode}")
            success = False
        else:
            print(f"Posisi {pos.ticket} berhasil ditutup! Symbol: {pos.symbol}, Profit: {pos.profit}")

    return success

# Fungsi utama untuk mengecek apakah total profit sudah mencapai target, dan menutup semua posisi jika iya
def check_and_close_positions_if_profit_reached(target_profit=100000):
    """
    Mengecek apakah total profit dari semua posisi sudah mencapai target,
    dan menutup semua posisi jika target tercapai.
    """
    total_profit = get_total_profit()
    print(f"Total profit saat ini: {total_profit:.2f}")

    # Jika total profit sudah mencapai atau melebihi target, tutup semua posisi
    if total_profit >= target_profit:
        print(f"Target profit {target_profit} tercapai! Menutup semua posisi...")
        if close_all_positions():
            print("Semua posisi berhasil ditutup.")
        else:
            print("Gagal menutup beberapa posisi.")
    else:
        print(f"Profit belum mencapai target {target_profit}. Menunggu...")

# Contoh penggunaan fungsi dalam loop utama
def trading_bot(symbol):
    """
    Fungsi utama trading bot untuk mendeteksi pola dan menutup posisi ketika profit mencapai target.
    """
    ticket = None  # Menyimpan ID posisi terbukaading...")

#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def detect_order_block(df, period=10):
    """
    Mendeteksi Order Block dari data candlestick.
    Order block ditentukan dengan menemukan candle besar dalam periode tertentu.
    
    Parameters:
    df (DataFrame): Data candlestick dengan kolom ['open', 'high', 'low', 'close']
    period (int): Jumlah candle yang dianalisis untuk mendeteksi order block.

    Returns:
    Tuple: (support_level, resistance_level) dari order block.
    """
    # Menemukan candle terbesar dalam periode terakhir
    df['body_size'] = abs(df['close'] - df['open'])
    largest_candle = df.tail(period).nlargest(1, 'body_size').iloc[0]

    if largest_candle['close'] > largest_candle['open']:
        # Candle bullish -> Order block di low
        support_level = largest_candle['low']
        resistance_level = largest_candle['high']
    else:
        # Candle bearish -> Order block di high
        support_level = largest_candle['low']
        resistance_level = largest_candle['high']

    return support_level, resistance_level

#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def detect_liquidity_grab(df, period=20):
    """
    Mendeteksi Liquidity Grab.
    Likuiditas diambil jika high/low terbaru melampaui high/low periode sebelumnya, namun harga kembali dalam range.

    Parameters:
    df (DataFrame): Data candlestick dengan kolom ['high', 'low', 'close']
    period (int): Jumlah candle yang dianalisis untuk mendeteksi likuiditas.

    Returns:
    Bool: True jika likuiditas terambil.
    """
    recent_high = df['high'].tail(period).max()
    recent_low = df['low'].tail(period).min()
    
    last_candle = df.iloc[-1]

    if last_candle['high'] > recent_high or last_candle['low'] < recent_low:
        return True  # Likuiditas terambil
    return False
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
# Fungsi untuk mengecek apakah posisi sudah ditutup karena TP atau SL
def check_if_position_closed(ticket):
    # Ambil informasi posisi berdasarkan ticket
    position = mt5.positions_get(ticket=ticket)
    if not position:
        print(f"Posisi dengan ticket {ticket} sudah ditutup (TP atau SL mungkin sudah tercapai).")
        return True  # Posisi sudah ditutup
    return False  # Posisi masih terbuka
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def get_data_for_timeframe(symbol, timeframe, num_candles):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_candles)
    if rates is None or len(rates) == 0:
        print(f"Gagal mengambil data candlestick untuk time frame {timeframe}.")
        return None
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def detect_market_structure(df):
    """
    Mendeteksi perubahan struktur pasar (Higher Highs, Lower Lows).
    
    Parameters:
    df (DataFrame): Data candlestick dengan kolom ['high', 'low']

    Returns:
    String: 'Bullish', 'Bearish', atau 'Range'
    """
    highs = df['high'].values
    lows = df['low'].values
    
    # Deteksi tren dengan membandingkan high dan low sebelumnya
    if highs[-1] > highs[-2] and lows[-1] > lows[-2]:
        return 'Bullish'  # Tren naik
    elif highs[-1] < highs[-2] and lows[-1] < lows[-2]:
        return 'Bearish'  # Tren turun
    else:
        return 'Range'  # Konsolidasi
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
# Fungsi untuk menutup posisi
def close_position(ticket):
    position = mt5.positions_get(ticket=ticket)
    if not position:
        print(f"Tidak ada posisi dengan ticket {ticket}.")
        return False
    
    position = position[0]
    close_price = mt5.symbol_info_tick(position.symbol).bid  # Gunakan harga Bid terbaru

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "position": position.ticket,
        "symbol": position.symbol,
        "volume": position.volume,
        "type": mt5.ORDER_TYPE_SELL if position.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY,
        "price": close_price,
        "deviation": 30,  # Meningkatkan deviasi untuk penutupan
        "magic": 234000,
        "comment": "Close order dari bot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Gagal menutup posisi {ticket}, error code: {result.retcode}")
        return False
    print(f"Posisi {ticket} berhasil ditutup.")
    return True
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
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
    sl_distance = 300 * symbol_info.point  # SL 100 pip di atas harga Bid
    tp_distance = 800 * symbol_info.point  # TP 200 pip di bawah harga Bid
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
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

def open_sell_order_m5(symbol, lot=0.01):
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
    sl_distance = 1600 * symbol_info.point  # SL 100 pip di atas harga Bid
    tp_distance = 3200 * symbol_info.point  # TP 200 pip di bawah harga Bid
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
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

def open_sell_order_m15(symbol, lot=0.01):
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
    sl_distance = 1600 * symbol_info.point  # SL 100 pip di atas harga Bid
    tp_distance = 3200 * symbol_info.point  # TP 200 pip di bawah harga Bid
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
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def open_sell_order_m30(symbol, lot=0.01):
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
    sl_distance = 300 * symbol_info.point  # SL 100 pip di atas harga Bid
    tp_distance = 800 * symbol_info.point  # TP 200 pip di bawah harga Bid
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
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def open_sell_order_h1(symbol, lot=0.01):
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
    sl_distance = 300 * symbol_info.point  # SL 100 pip di atas harga Bid
    tp_distance = 800 * symbol_info.point  # TP 200 pip di bawah harga Bid
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
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
def open_sell_order_h4(symbol, lot=0.01):
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
    sl_distance = 300 * symbol_info.point  # SL 100 pip di atas harga Bid
    tp_distance = 800 * symbol_info.point  # TP 200 pip di bawah harga Bid
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
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
# Fungsi utama untuk loop trading
symbol = "XAUUSD"
ticket = None
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
while True:
    check_and_close_positions_if_profit_reached(target_profit=100000)
    # Ambil data candlestick dari berbagai time frame
    data_m1 = get_data_for_timeframe(symbol, mt5.TIMEFRAME_M1, 1000)
    data_m5 = get_data_for_timeframe(symbol, mt5.TIMEFRAME_M5, 1000)
    data_m15 = get_data_for_timeframe(symbol, mt5.TIMEFRAME_M15, 1000)
    data_m30 = get_data_for_timeframe(symbol, mt5.TIMEFRAME_M30, 1000)
    data_h1 = get_data_for_timeframe(symbol, mt5.TIMEFRAME_H1, 1000)
    data_h4 = get_data_for_timeframe(symbol, mt5.TIMEFRAME_H4, 1000)
    data_d1 = get_data_for_timeframe(symbol, mt5.TIMEFRAME_D1, 1000)
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
    data_m1 = get_candlestick_data(symbol, mt5.TIMEFRAME_M1, 100)
    data_m5 = get_candlestick_data(symbol, mt5.TIMEFRAME_M5, 100)
    data_m15 = get_candlestick_data(symbol, mt5.TIMEFRAME_M15, 100)
    data_m30 = get_candlestick_data(symbol, mt5.TIMEFRAME_M30, 100)
    data_h1 = get_candlestick_data(symbol, mt5.TIMEFRAME_H1, 100)
#--------------------------------------------------------------------------------------------------------------------------------------------    
#--------------------------------------------------------------------------------------------------------------------------------------------
    # Pastikan data candlestick berhasil diambil
    if data_m5 is not None:
        print("Data Candlestick M5 Terbaru:")
        print(data_m5.tail())

        # Hitung level support dan resistance untuk M5 (contoh)
        support, resistance = calculate_support_resistance(data_m5, period=500)
        if support is not None and resistance is not None:
            print(f"Support Level (M5): {support}")
            print(f"Resistance Level (M5): {resistance}")

        
        # Mendeteksi liquidity grab di M5
        if detect_liquidity_grab(data_m5, period=500):
            print("Liquidity Grab terdeteksi di M5!")
        
        # Mendeteksi struktur pasar (market structure) di M5
        market_structure_m5 = detect_market_structure(data_m5)
        print(f"Market Structure (M5): {market_structure_m5}")
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
    # Menganalisis data dari time frame lainnya:
    if data_m15 is not None:
        print("Data Candlestick M15 Terbaru:")
        print(data_m15.tail())

        # Hitung level support dan resistance untuk M15
        support_m15, resistance_m15 = calculate_support_resistance(data_m15, period=400)
        if support_m15 is not None and resistance_m15 is not None:
            print(f"Support Level (M15): {support_m15}")
            print(f"Resistance Level (M15): {resistance_m15}")
        
        # Mendeteksi market structure di M15
        market_structure_m15 = detect_market_structure(data_m15)
        print(f"Market Structure (M15): {market_structure_m15}")
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
    if data_m30 is not None:
        print("Data Candlestick M30 Terbaru:")
        print(data_m30.tail())

        # Hitung level support dan resistance untuk M30
        support_m30, resistance_m30 = calculate_support_resistance(data_m30, period=300)
        if support_m30 is not None and resistance_m30 is not None:
            print(f"Support Level (M30): {support_m30}")
            print(f"Resistance Level (M30): {resistance_m30}")
        
        # Mendeteksi market structure di M30
        market_structure_m30 = detect_market_structure(data_m30)
        print(f"Market Structure (M30): {market_structure_m30}")
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
    if data_h1 is not None:
        print("Data Candlestick H1 Terbaru:")
        print(data_h1.tail())

        # Hitung level support dan resistance untuk H1
        support_h1, resistance_h1 = calculate_support_resistance(data_h1, period=200)
        if support_h1 is not None and resistance_h1 is not None:
            print(f"Support Level (H1): {support_h1}")
            print(f"Resistance Level (H1): {resistance_h1}")
        
        # Mendeteksi market structure di H1
        market_structure_h1 = detect_market_structure(data_h1)
        print(f"Market Structure (H1): {market_structure_h1}")
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
    if data_h4 is not None:
        print("Data Candlestick H4 Terbaru:")
        print(data_h4.tail())

        # Hitung level support dan resistance untuk H4
        support_h4, resistance_h4 = calculate_support_resistance(data_h4, period=100)
        if support_h4 is not None and resistance_h4 is not None:
            print(f"Support Level (H4): {support_h4}")
            print(f"Resistance Level (H4): {resistance_h4}")
        
        # Mendeteksi market structure di H4
        market_structure_h4 = detect_market_structure(data_h4)
        print(f"Market Structure (H4): {market_structure_h4}")
#--------------------------------------------------------------------------------------------------------------------------------------------        
#--------------------------------------------------------------------------------------------------------------------------------------------
    if data_d1 is not None:
        print("Data Candlestick D1 Terbaru:")
        print(data_d1.tail())

        # Hitung level support dan resistance untuk D1
        support_d1, resistance_d1 = calculate_support_resistance(data_d1, period=50)
        if support_d1 is not None and resistance_d1 is not None:
            print(f"Support Level (D1): {support_d1}")
            print(f"Resistance Level (D1): {resistance_d1}")
        
        # Mendeteksi market structure di D1
        market_structure_d1 = detect_market_structure(data_d1)
        print(f"Market Structure (D1): {market_structure_d1}")
#--------------------------------------------------------------------------------------------------------------------------------------------        
#--------------------------------------------------------------------------------------------------------------------------------------------
    # Keputusan trading berdasarkan analisis multi-time frame
    if market_structure_m5 == 'Bullish' and market_structure_m15 == 'Bullish' and market_structure_h1 == 'Bullish':
        print("Market Bullish di M5, M15, dan H1. Membuka order buy...")
        ticket = open_buy_order(symbol)
    elif market_structure_m5 == 'Bearish' and market_structure_m15 == 'Bearish' and market_structure_h1 == 'Bearish':
        print("Market Bearish di M5, M15, dan H1. Membuka order sell...")
        ticket = open_sell_order(symbol)
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------        
            # Deteksi likuiditas dan lakukan order di Timeframe M5, M15, M30, H1
        if market_structure_m5 == 'Bullish' and detect_liquidity_grab(data_m5):
            print("Market M5 bullish dan likuiditas terambil. Membuka order buy...")
            ticket = open_buy_order(symbol)
        elif market_structure_m5 == 'Bearish' and detect_liquidity_grab(data_m5):
            print("Market M5 bearish dan likuiditas terambil. Membuka order sell...")
            ticket = open_sell_order(symbol)

        # Timeframe M15
        elif market_structure_m15 == 'Bullish' and detect_liquidity_grab(data_m15):
            print("Market M15 bullish dan likuiditas terambil. Membuka order buy...")
            ticket = open_buy_order(symbol)
        elif market_structure_m15 == 'Bearish' and detect_liquidity_grab(data_m15):
            print("Market M15 bearish dan likuiditas terambil. Membuka order sell...")
            ticket = open_sell_order(symbol)

        # Timeframe M30
        elif market_structure_m30 == 'Bullish' and detect_liquidity_grab(data_m30):
            print("Market M30 bullish dan likuiditas terambil. Membuka order buy...")
            ticket = open_buy_order(symbol)
        elif market_structure_m30 == 'Bearish' and detect_liquidity_grab(data_m30):
            print("Market M30 bearish dan likuiditas terambil. Membuka order sell...")
            ticket = open_sell_order(symbol)

        # Timeframe H1
        elif market_structure_h1 == 'Bullish' and detect_liquidity_grab(data_h1):
            print("Market H1 bullish dan likuiditas terambil. Membuka order buy...")
            ticket = open_buy_order(symbol)
        elif market_structure_h1 == 'Bearish' and detect_liquidity_grab(data_h1):
            print("Market H1 bearish dan likuiditas terambil. Membuka order sell...")
            ticket = open_sell_order(symbol)
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------           
   # Loop untuk mendeteksi pola bullish engulfing atau hammer dan membuka posisi buy
    if data_m1 is not None and (is_bullish_engulfing(data_m1) or is_hammer(data_m1)):
        print("Pola bullish engulfing atau hammer terdeteksi di timeframe M1.")
    elif data_m5 is not None and (is_bullish_engulfing(data_m5) or is_hammer(data_m5)):
        print("Pola bullish engulfing atau hammer terdeteksi di timeframe M5.")
        ticket = open_buy_order_m5(symbol)
    elif data_m15 is not None and (is_bullish_engulfing(data_m15) or is_hammer(data_m15)):
        print("Pola bullish engulfing atau hammer terdeteksi di timeframe M15.")
        ticket = open_buy_order_m15(symbol)
    elif data_m30 is not None and (is_bullish_engulfing(data_m30) or is_hammer(data_m30)):
        print("Pola bullish engulfing atau hammer terdeteksi di timeframe M30.")
        ticket = open_buy_order_m30(symbol)
    elif data_h1 is not None and (is_bullish_engulfing(data_h1) or is_hammer(data_h1)):
        print("Pola bullish engulfing atau hammer terdeteksi di timeframe H1.")
        ticket = open_buy_order_h1(symbol)
    else:
        print("Tidak ada pola bullish engulfing atau hammer yang terdeteksi pada timeframe yang dipilih.")

#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
    # Cek pola bearish engulfing pada setiap timeframe
    if data_m1 is not None and is_bearish_engulfing(data_m1):
        print("Pola bearish engulfing terdeteksi di timeframe M1.")
    elif data_m5 is not None and is_bearish_engulfing(data_m5):
        print("Pola bearish engulfing terdeteksi di timeframe M5.")
        ticket = open_sell_order_m5(symbol)
    elif data_m15 is not None and is_bearish_engulfing(data_m15):
        print("Pola bearish engulfing terdeteksi di timeframe M15.")
        ticket = open_sell_order_m15(symbol)
    elif data_m30 is not None and is_bearish_engulfing(data_m30):
        print("Pola bearish engulfing terdeteksi di timeframe M30.")
        ticket = open_sell_order_m30(symbol)
    elif data_h1 is not None and is_bearish_engulfing(data_h1):
        print("Pola bearish engulfing terdeteksi di timeframe H1.")
        ticket = open_sell_order_h1(symbol)
    else:
        print("Tidak ada pola bearish engulfing yang terdeteksi pada timeframe yang dipilih.")

#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

    # Jika ada posisi terbuka, cek apakah sudah ditutup karena TP atau SL
    if ticket is not None:
        if check_if_position_closed(ticket):
            print(f"Posisi dengan ticket {ticket} telah ditutup.")
            ticket = None  # Set ticket ke None jika posisi sudah ditutup
        else:
            print(f"Posisi dengan ticket {ticket} masih terbuka. Menunggu...")
            
            
    

    time.sleep(60)  # Tunggu 1 menit sebelum iterasi berikutnya
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

#          _____                    _____            _____                    _____                    _____                    _____                    _____                _____          
#         /\    \                  /\    \          /\    \                  /\    \                  /\    \                  /\    \                  /\    \              /\    \         
#        /::\    \                /::\____\        /::\    \                /::\    \                /::\____\                /::\____\                /::\    \            /::\    \        
#       /::::\    \              /:::/    /       /::::\    \              /::::\    \              /:::/    /               /:::/    /               /::::\    \           \:::\    \       
#      /::::::\    \            /:::/    /       /::::::\    \            /::::::\    \            /:::/    /               /:::/    /               /::::::\    \           \:::\    \      
#     /:::/\:::\    \          /:::/    /       /:::/\:::\    \          /:::/\:::\    \          /:::/    /               /:::/    /               /:::/\:::\    \           \:::\    \     
#    /:::/__\:::\    \        /:::/    /       /:::/__\:::\    \        /:::/  \:::\    \        /:::/____/               /:::/____/               /:::/__\:::\    \           \:::\    \    
#   /::::\   \:::\    \      /:::/    /       /::::\   \:::\    \      /:::/    \:::\    \      /::::\    \              /::::\    \              /::::\   \:::\    \          /::::\    \   
#  /::::::\   \:::\    \    /:::/    /       /::::::\   \:::\    \    /:::/    / \:::\    \    /::::::\____\________    /::::::\    \   _____    /::::::\   \:::\    \        /::::::\    \  
# /:::/\:::\   \:::\ ___\  /:::/    /       /:::/\:::\   \:::\    \  /:::/    /   \:::\    \  /:::/\:::::::::::\    \  /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \      /:::/\:::\    \ 
#/:::/__\:::\   \:::|    |/:::/____/       /:::/  \:::\   \:::\____\/:::/____/     \:::\____\/:::/  |:::::::::::\____\/:::/  \:::\    /::\____\/:::/  \:::\   \:::\____\    /:::/  \:::\____\
#\:::\   \:::\  /:::|____|\:::\    \       \::/    \:::\  /:::/    /\:::\    \      \::/    /\::/   |::|~~~|~~~~~     \::/    \:::\  /:::/    /\::/    \:::\  /:::/    /   /:::/    \::/    /
# \:::\   \:::\/:::/    /  \:::\    \       \/____/ \:::\/:::/    /  \:::\    \      \/____/  \/____|::|   |           \/____/ \:::\/:::/    /  \/____/ \:::\/:::/    /   /:::/    / \/____/ 
#  \:::\   \::::::/    /    \:::\    \               \::::::/    /    \:::\    \                    |::|   |                    \::::::/    /            \::::::/    /   /:::/    /          
#   \:::\   \::::/    /      \:::\    \               \::::/    /      \:::\    \                   |::|   |                     \::::/    /              \::::/    /   /:::/    /           
#    \:::\  /:::/    /        \:::\    \              /:::/    /        \:::\    \                  |::|   |                     /:::/    /               /:::/    /    \::/    /            
#     \:::\/:::/    /          \:::\    \            /:::/    /          \:::\    \                 |::|   |                    /:::/    /               /:::/    /      \/____/             
#      \::::::/    /            \:::\    \          /:::/    /            \:::\    \                |::|   |                   /:::/    /               /:::/    /                           
#       \::::/    /              \:::\____\        /:::/    /              \:::\____\               \::|   |                  /:::/    /               /:::/    /                            
#        \::/____/                \::/    /        \::/    /                \::/    /                \:|   |                  \::/    /                \::/    /                             
#         ~~                       \/____/          \/____/                  \/____/                  \|___|                   \/____/                  \/____/                              
                                                                                                                                                                                            
