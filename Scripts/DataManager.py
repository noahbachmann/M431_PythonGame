from typing import List
import sys
import asyncio
import pygame
import json
import platform

API_URL = "space-fighter-web.vercel.app"

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
window.Fetch.GET = function * GET(url) {
    console.log('GET: ' + url);
    var content = 'undefined';
    fetch(new Request(url, { method: 'GET' }))
        .then(resp => resp.text())
        .then(resp => { content = resp; })
        .catch(err => { console.log('GET error:', err); content = 'ERROR:' + String(err); });
    while (content == 'undefined') { yield; }
    yield content;
}
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


async def _fetch_json(url: str, method: str = 'GET', payload: dict = None):
    try:
        if _is_emscripten:
            await asyncio.sleep(0)
            if method == 'GET':
                text = await platform.jsiter(platform.window.Fetch.GET(url))
            else:
                text = await platform.jsiter(platform.window.Fetch.POST(url, json.dumps(payload or {})))
        else:
            if method == 'GET':
                text = requests.get(url).text
            else:
                text = requests.post(url, json=payload or {}).text
            print(f"[DataManager] response: {text}")

        if str(text).startswith('ERROR:'):
            print(f"fetch error from JS: {text}")
            return None
        return json.loads(text)
    except Exception as e:
        print(f"fetch error: {e}")
        return None


class DataManager:
    def __init__(self):
        self.hi_scores: List[int] = []

    async def fetchScores(self) -> List[int]:
        data = await _fetch_json(f"{API_URL}/api/scores")
        if data is not None:
            self.hi_scores = [s["score"] for s in data]
        return self.hi_scores

    async def submitScore(self, score: int) -> dict:
        result = await _fetch_json(f"{API_URL}/api/scores", method='POST', payload={"name": "Player", "score": score})
        return {"success": result is not None}

    def isHighScore(self, score: int) -> bool:
        if score <= 99:
            return False
        if len(self.hi_scores) < 10:
            return True
        return score > min(self.hi_scores)


_manager = DataManager()


async def loadData():
    scores = await _manager.fetchScores()
    print(f"Loaded scores: {scores}")

def isHighScore(score: int) -> bool:
    return _manager.isHighScore(score)

async def submitScore(score: int) -> dict:
    return await _manager.submitScore(score)
