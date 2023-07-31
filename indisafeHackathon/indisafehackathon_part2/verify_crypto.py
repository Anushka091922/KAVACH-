import bitcoin




def detect_cryptocurrency(public_key, private_key):
    # Bitcoin
    try:
        # Check if public key is valid for Bitcoin
        if public_key.startswith('02') or public_key.startswith('03') or public_key.startswith('04'):
            # Check if private key is valid for Bitcoin
            if private_key.startswith('5') or private_key.startswith('K') or private_key.startswith('L'):
                return "Bitcoin"
    except Exception:
        pass

    # Ethereum
    try:
        # Check if public key is valid for Ethereum
        if public_key.startswith('0x'):
            # Check if private key is valid for Ethereum
            if private_key.startswith('0x'):
                return "Ethereum"
    except Exception:
        pass

    # Tether
    try:
        # Check if public key is valid for Tether
        if public_key.startswith('1') and len(public_key) == 34:
            # Check if private key is valid for Tether
            if private_key.startswith('5') or private_key.startswith('K') or private_key.startswith('L'):
                return "Tether"
    except Exception:
        pass

    # Monero
    try:
        # Check if public key is valid for Monero
        if public_key.startswith('4'):
            # Check if private key is valid for Monero
            if private_key.startswith('4'):
                return "Monero"
    except Exception:
        pass

    # Dogecoin
    try:
        # Check if public key is valid for Dogecoin
        if public_key.startswith('D') or public_key.startswith('9'):
            # Check if private key is valid for Dogecoin
            if private_key.startswith('Q') or private_key.startswith('6'):
                return "Dogecoin"
    except Exception:
        pass

    # Dutchcoin
    try:
        # Check if public key is valid for Dutchcoin
        if public_key.startswith('D') or public_key.startswith('9'):
            # Check if private key is valid for Dutchcoin
            if private_key.startswith('Q') or private_key.startswith('6'):
                return "Dutchcoin"
    except Exception:
        pass

    # Binance Coin
    try:
        # Check if public key is valid for Binance Coin
        if public_key.startswith('bnb') and len(public_key) == 42:
            # Check if private key is valid for Binance Coin
            if private_key.startswith('5') or private_key.startswith('K') or private_key.startswith('L'):
                return "Binance Coin"
    except Exception:
        pass

    # Cardano
    try:
        # Check if public key is valid for Cardano
        if public_key.startswith('addr') and len(public_key) == 59:
            # Check if private key is valid for Cardano
            if private_key.startswith('ed25519'):
                return "Cardano"
    except Exception:
        pass

    # Polkadot
    try:
        # Check if public key is valid for Polkadot
        if public_key.startswith('1'):
            # Check if private key is valid for Polkadot
            if private_key.startswith('0x'):
                return "Polkadot"
    except Exception:
        pass

    return "No"


def verify_tx(tex):
    try:
        bitcoin.fetchtx(tex)
        return("a real transaction")
    except:
        return("not a real transaction")
