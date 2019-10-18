# -*- coding: utf-8 -*-
#
# Electrum - lightweight Bitcoin client
# Copyright (C) 2018 The Electrum developers
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json

from .util import inv_dict
from . import bitcoin


def read_json(filename, default):
    path = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(path, 'r') as f:
            r = json.loads(f.read())
    except:
        r = default
    return r


GIT_REPO_URL = "https://github.com/syscoin/electrum"
GIT_REPO_ISSUES_URL = "https://github.com/syscoin/electrum/issues"


class AbstractNet:

    BLOCK_HEIGHT_FIRST_LIGHTNING_CHANNELS = 0

    @classmethod
    def max_checkpoint(cls) -> int:
        return max(0, len(cls.CHECKPOINTS) * net.POW_BLOCK_ADJUST - 1)

    @classmethod
    def rev_genesis_bytes(cls) -> bytes:
        return bytes.fromhex(bitcoin.rev_hex(cls.GENESIS))


class BitcoinMainnet(AbstractNet):

    TESTNET = False
    WIF_PREFIX = 0x80
    ADDRTYPE_P2PKH = 0
    ADDRTYPE_P2SH = 5
    SEGWIT_HRP = "bc"
    GENESIS = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    DEFAULT_PORTS = {'t': '50001', 's': '50002'}
    DEFAULT_SERVERS = read_json('servers.json', {})
    CHECKPOINTS = read_json('checkpoints.json', [])
    BLOCK_HEIGHT_FIRST_LIGHTNING_CHANNELS = 497000

    XPRV_HEADERS = {
        'standard':    0x0488ade4,  # xprv
        'p2wpkh-p2sh': 0x049d7878,  # yprv
        'p2wsh-p2sh':  0x0295b005,  # Yprv
        'p2wpkh':      0x04b2430c,  # zprv
        'p2wsh':       0x02aa7a99,  # Zprv
    }
    XPRV_HEADERS_INV = inv_dict(XPRV_HEADERS)
    XPUB_HEADERS = {
        'standard':    0x0488b21e,  # xpub
        'p2wpkh-p2sh': 0x049d7cb2,  # ypub
        'p2wsh-p2sh':  0x0295b43f,  # Ypub
        'p2wpkh':      0x04b24746,  # zpub
        'p2wsh':       0x02aa7ed3,  # Zpub
    }
    XPUB_HEADERS_INV = inv_dict(XPUB_HEADERS)
    BIP44_COIN_TYPE = 0
    LN_REALM_BYTE = 0
    LN_DNS_SEEDS = [
        'nodes.lightning.directory.',
        'lseed.bitcoinstats.com.',
    ]


class BitcoinTestnet(AbstractNet):

    TESTNET = True
    WIF_PREFIX = 0xef
    ADDRTYPE_P2PKH = 111
    ADDRTYPE_P2SH = 196
    SEGWIT_HRP = "tb"
    GENESIS = "000000000933ea01ad0ee984209779baaec3ced90fa3f408719526f8d77f4943"
    DEFAULT_PORTS = {'t': '51001', 's': '51002'}
    DEFAULT_SERVERS = read_json('servers_testnet.json', {})
    CHECKPOINTS = read_json('checkpoints_testnet.json', [])

    XPRV_HEADERS = {
        'standard':    0x04358394,  # tprv
        'p2wpkh-p2sh': 0x044a4e28,  # uprv
        'p2wsh-p2sh':  0x024285b5,  # Uprv
        'p2wpkh':      0x045f18bc,  # vprv
        'p2wsh':       0x02575048,  # Vprv
    }
    XPRV_HEADERS_INV = inv_dict(XPRV_HEADERS)
    XPUB_HEADERS = {
        'standard':    0x043587cf,  # tpub
        'p2wpkh-p2sh': 0x044a5262,  # upub
        'p2wsh-p2sh':  0x024289ef,  # Upub
        'p2wpkh':      0x045f1cf6,  # vpub
        'p2wsh':       0x02575483,  # Vpub
    }
    XPUB_HEADERS_INV = inv_dict(XPUB_HEADERS)
    BIP44_COIN_TYPE = 1
    LN_REALM_BYTE = 1
    LN_DNS_SEEDS = [
        'test.nodes.lightning.directory.',
        'lseed.bitcoinstats.com.',
    ]

class SyscoinMainnet(AbstractNet):

    TESTNET = False
    REGTEST = False

    WIF_PREFIX = 0x80
    ADDRTYPE_P2PKH = 0x3f
    ADDRTYPE_P2SH = 0x05

    SEGWIT_HRP = "sys"

    POW_TARGET_TIMESPAN = 21600  # 60 * 60 * 6 seconds / 6 hours
    POW_TARGET_SPACING = 60  # 60 seconds
    POW_BLOCK_ADJUST = int(POW_TARGET_TIMESPAN / POW_TARGET_SPACING)
    nBridgeStartBlock = 225000
    GENESIS = "0000022642db0346b6e01c2a397471f4f12e65d4f4251ec96c1f85367a61a7ab"
    DEFAULT_PORTS = {'t': '58881', 's': '58882'}
    DEFAULT_SERVERS = read_json('servers.json', {
        "https://127.0.0.1/": {
            "pruning": "-",
            "t": "58881",
            "s": "58882"
        }
    })
    CHECKPOINTS = read_json('checkpoints.json', [])

    XPRV_HEADERS = {
        'standard':    0x0488ade4,  # xprv XPRV_VERBYTES
        'p2wpkh-p2sh': 0x049d7878,  # yprv
        'p2wsh-p2sh':  0x0295b005,  # Yprv
        'p2wpkh':      0x04b2430c,  # zprv
        'p2wsh':       0x02aa7a99,  # Zprv
    }
    XPRV_HEADERS_INV = inv_dict(XPRV_HEADERS)
    XPUB_HEADERS = {
        'standard':    0x0488b21e,  # xpub XPUB_VERBYTES
        'p2wpkh-p2sh': 0x049d7cb2,  # ypub
        'p2wsh-p2sh':  0x0295b43f,  # Ypub
        'p2wpkh':      0x04b24746,  # zpub
        'p2wsh':       0x02aa7ed3,  # Zpub
    }
    XPUB_HEADERS_INV = inv_dict(XPUB_HEADERS)
    BIP44_COIN_TYPE = 57
    BLOCK_HEIGHT_FIRST_LIGHTNING_CHANNELS = 0
    LN_REALM_BYTE = 57
    LN_DNS_SEEDS = []


class SyscoinTestnet(SyscoinMainnet):

    TESTNET = True
    REGTEST = False

    WIF_PREFIX = 0xef
    ADDRTYPE_P2PKH = 0x41
    ADDRTYPE_P2SH = 0xc4

    SEGWIT_HRP = "tsys"

    GENESIS = "0000064430008f1fe74ba0bf54080f1cf6e73da3372df7617e33648529940fc3"
    DEFAULT_PORTS = {'t': '59991', 's': '59992'}
    DEFAULT_SERVERS = read_json('servers_testnet.json', {
        "104.248.3.80": {
            "pruning": "-",
            "t": "59991",
            "s": "59992",
            "version": "1.4"
        }
    })
    CHECKPOINTS = read_json('checkpoints_testnet.json', [])

    XPRV_HEADERS = {
        'standard':    0x04358394,  # tprv
        'p2wpkh-p2sh': 0x044a4e28,  # uprv
        'p2wsh-p2sh':  0x024285b5,  # Uprv
        'p2wpkh':      0x04358394,  # vprv
        'p2wsh':       0x02575048,  # Vprv
    }
    XPRV_HEADERS_INV = inv_dict(XPRV_HEADERS)
    XPUB_HEADERS = {
        'standard':    0x043587cf,  # tpub
        'p2wpkh-p2sh': 0x044a5262,  # upub
        'p2wsh-p2sh':  0x024289ef,  # Upub
        'p2wpkh':      0x043587cf,  # vpub
        'p2wsh':       0x02575483,  # Vpub
    }
    XPUB_HEADERS_INV = inv_dict(XPUB_HEADERS)
    BLOCK_HEIGHT_FIRST_LIGHTNING_CHANNELS = 0
    LN_REALM_BYTE = 1

class SyscoinRegtest(SyscoinTestnet):

    TESTNET = False
    REGTEST = True
    SEGWIT_HRP = "sysrt"

    GENESIS = "28a2c2d251f46fac05ade79085cbcb2ae4ec67ea24f1f1c7b40a348c00521194"
    DEFAULT_SERVERS = read_json('servers_regtest.json', {})
    CHECKPOINTS = []

class BitcoinRegtest(BitcoinTestnet):

    SEGWIT_HRP = "bcrt"
    GENESIS = "0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206"
    DEFAULT_SERVERS = read_json('servers_regtest.json', {})
    CHECKPOINTS = []
    LN_DNS_SEEDS = []


class BitcoinSimnet(BitcoinTestnet):

    WIF_PREFIX = 0x64
    ADDRTYPE_P2PKH = 0x3f
    ADDRTYPE_P2SH = 0x7b
    SEGWIT_HRP = "sb"
    GENESIS = "683e86bd5c6d110d91b94b97137ba6bfe02dbbdb8e3dff722a669b5d69d77af6"
    DEFAULT_SERVERS = read_json('servers_regtest.json', {})
    CHECKPOINTS = []
    LN_DNS_SEEDS = []


# don't import net directly, import the module instead (so that net is singleton)
net = SyscoinMainnet

def set_simnet():
    global net
    net = SyscoinSimnet

def set_mainnet():
    global net
    net = SyscoinMainnet

def set_testnet():
    global net
    net = SyscoinTestnet

def set_regtest():
    global net
    net = SyscoinRegtest
