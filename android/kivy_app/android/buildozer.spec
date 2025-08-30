

```ini
[app]
title = Roz
package.name = roz
package.domain = org.example
source.dir = kivy_app
source.include_exts = py
version = 0.1
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
# ```

# ---

# ## Notes & Tips

# * macOS voices: run `say -v ?` in Terminal to list voices (e.g., **Alex** en, **Karen** en‑AU, **Ting‑Ting** zh‑CN, **Yuna** ko, **Kyoko** ja, **Javier** es‑MX, **Monica** es‑ES, **Milena** ru‑RU, **Lekha** hi‑IN).
# * Add or remove allowed apps in `mac_control.py` → `SAFE_APPS` map.
# * For **streaming** tokens, enable `stream=True` and use EventSource/Server‑Sent Events (out of scope here for simplicity).
# * The DeepSeek API is **OpenAI‑compatible** (`base_url=https://api.deepseek.com`), models: `deepseek-reasoner` (R1‑0528) and `deepseek-chat` (V3‑0324). See official docs.

# ```
# ```
