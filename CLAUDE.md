# Project Guidance

This file provides context and guidance for working with the Python Space Shooter project.

## Project Overview

**Python Space Shooter** is a Pygame-based space shooter game with dual deployment modes:, Desktop: Standalone pygame application, can be packaged with PyInstaller
- **Web**: Runs in browser via pygbag (WebAssembly/Emscripten) This is where we will work 100% of the time. Dont mind the Desktop version much.

The codebase uses an asyncio-based game loop and syncs scores to a **Nuxt server API** that manages the Neon PostgreSQL database for global leaderboards.

### Build & Packaging
- For web deployment: pygbag handles packaging and WASM compilation

## Core Commands

```bash
# Run the game locally
python main.py

# Install dependencies
pip install -r Requirements.txt

#run the game in web mode (most important part)
python -m pygbag main.py

```
## Project Architecture

### Game Loop Structure (main.py)
The game follows a state machine: `MainMenu → Round → EndGameMenu → repeat`

All game states use asyncio for web compatibility. The main rendering pipeline:
1. **screen** (full window) ← background image + cameraSurface
2. **cameraSurface** (1024x1024 viewport) ← sprite rendering with offset

Key pattern: `await asyncio.sleep(0)` in all loops yields control for web compatibility

### API Communication
Both desktop and web versions use **httpx** for async HTTP requests to the Nuxt API:
- DataManager.fetchScores() → GET /api/hiscores
- DataManager.submitScore(score) → POST /api/hiscores
- Credentials: `x-api-key` header for authentication

### Key Components

| File | Role |
|------|------|
| **Scripts/Round.py** | Main game loop, manages player/enemies/HUD, handles pause/game events |
| **Scripts/Player.py** | Player entity with shooting, boosting, and health mechanics |
| **Scripts/Enemy.py** | Enemy entity with AI movement and attack behavior |
| **Scripts/EnemySpawner.py** | Controls enemy spawning based on round difficulty |
| **Scripts/HUDController.py** | UI overlay: health bar, score, pause menu, wave counter |
| **Scripts/Groups.py** | Custom `AllSprites` group with camera offset management for infinite scrolling |
| **Scripts/DataManager.py** | Leaderboard sync via Nuxt API using httpx |
| **Scripts/GameMenus.py** | Main menu and EndGameMenu UI |

### Data Management Architecture

**DataManager** (Scripts/DataManager.py) handles all leaderboard communication via Nuxt server API:

**Both Desktop & Web Modes**:
- DataManager calls Nuxt `/api/hiscores` endpoint over HTTPS
- Uses httpx for async HTTP requests (works universally)
- Cached top 10 scores stored locally

**Database Setup**:
- Simple schema: `hiscores` table with `player_name` (varchar) and `score` (bigint)
- Nuxt server route: `server/api/hiscores.ts`
- Environment variables: `API_BASE` (Nuxt URL), `API_KEY` (shared secret for auth)

See **SETUP_DATABASE.md** for database setup.

### Sprite Offset System
**Scripts/Groups.py** implements camera-relative rendering:
- `AllSprites` group tracks position offset
- Sprites render relative to camera position
- Enables infinite scrolling without world boundary wrapping

## Important File Paths

```
main.py                           # Entry point, game state machine
Scripts/Round.py                  # Main game loop logic
Scripts/Player.py                 # Player mechanics
Scripts/DataManager.py            # Leaderboard sync via Nuxt API
SETUP_DATABASE.md                 # Database setup instructions
```

## Development Notes

### Async-First Design
All game loops and event handlers use asyncio:
- Every loop must have `await asyncio.sleep(0)` to yield control
- This is **critical for web (pygbag) compatibility** - without it the browser will freeze
- Desktop also benefits from responsive event handling

### API Configuration
Set environment variables before running the game:
```bash
export API_BASE=https://your-nuxt-site.com     # Your Nuxt deployment URL
export API_KEY=your-secret-key                  # Shared secret key (must match Nuxt env)
python main.py
```

### Database Setup
1. Create Neon PostgreSQL project
2. Add Nuxt server route: `server/api/hiscores.ts` (see architecture example)
3. Set `API_BASE` and `API_KEY` environment variables in your Nuxt `.env`
4. See **SETUP_DATABASE.md** for detailed instructions



### Common Patterns

**Fetch Leaderboard**:
```python
# In any async context
scores = await DataManager.fetchScores()  # Returns list of top 10 scores
```

**Submit Score**:
```python
result = await DataManager.submitScore(1500)
if result["success"]:
    print("Score submitted!")
```

**Sprite Rendering with Offset**:
```python
# Groups.py handles offset automatically
all_sprites.add(enemy)  # Sprite renders at position - group.offset
```

## Recent Changes

- **Refactored to Nuxt API**: Uses httpx for universal async HTTP requests
- **Simplified DataManager**: Removed platform-specific logic, cleaner API
- **Environment variables**: API_BASE and API_KEY for configuration

## Debugging Tips

- Use `print()` statements; they appear in console (desktop) or browser console (web)
- Verify `API_BASE` and `API_KEY` environment variables are set correctly
- Check Nuxt server route `server/api/hiscores.ts` is deployed and accessible
- Verify asyncio.sleep(0) is present in all game loops for web compatibility
- Test API locally: `curl -H "x-api-key: your-key" http://localhost:3000/api/hiscores`
