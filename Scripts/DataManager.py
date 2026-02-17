import sys
import asyncio
import pygame
import json
import builtins
import platform

API_URL = builtins.API_BASE

dataJson = {
    'Hotkey_Up': pygame.K_w,
    'Hotkey_Down': pygame.K_s,
    'Hotkey_Left': pygame.K_a,
    'Hotkey_Right': pygame.K_d,
    'Hotkey_Boost': pygame.K_LSHIFT,
    'Hotkey_close': pygame.K_j,
    'Hotkey_Attack': pygame.K_SPACE,
    'Hotkey_HeavyAttack': pygame.K_f
}

_JS_FETCH = """
window.Fetch = {}
window.Fetch.POST = function * POST(url, data) {
    console.log('POST: ' + url, data);
    var content = 'undefined';
    fetch(new Request(url, {
        method: 'POST',
        headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
        body: data
    }))
        .then(resp => resp.text())
        .then(resp => { content = resp; })
        .catch(err => { console.log('POST error:', err); content = 'ERROR:' + String(err); });
    while (content == 'undefined') { yield; }
    yield content;
}
"""

_is_emscripten = sys.platform == "emscripten"

if _is_emscripten:
    try:
        platform.window.eval(_JS_FETCH)
    except Exception as e:
        print(f"[DataManager] JS fetch init error: {e}")
        _is_emscripten = False

if not _is_emscripten:
    import requests


async def _fetch_json(url: str, payload: dict = None):
    try:
        if _is_emscripten:
            await asyncio.sleep(0)
            text = await platform.jsiter(platform.window.Fetch.POST(url, json.dumps(payload or {})))
        else:
            text = requests.post(url, json=payload or {}).text

        if str(text).startswith('ERROR:'):
            print(f"fetch error from JS: {text}")
            return None
        return json.loads(text)
    except Exception as e:
        print(f"fetch error: {e}")
        return None


async def submitScore(score: int) -> dict:
    result = await _fetch_json(f"{API_URL}/api/scores", payload={"name": "Player", "score": score})
    return {"success": result is not None}
