````md
# Android client (optional)
This is a **very small Kivy app** that talks to your Mac Roz server over Wi‑Fi.

## Steps
1. Install build tools
```bash
# Prefer running in a Python 3.10 virtualenv
pip install buildozer==1.5.0 Cython==0.29.36 kivy==2.3.0 requests==2.32.3
# For the first build, Buildozer downloads the Android SDK/NDK (~1–2 GB)
````

2. Put files:

```
android/
  buildozer.spec
  kivy_app/
    main.py
```

3. Edit `buildozer.spec` → set `package.name`, `package.domain`.

4. Start your Mac server (`python app.py`) and ensure phone and Mac are on the same network. Note the Mac **IP** (e.g., 192.168.1.25).

5. In `main.py`, set `SERVER_BASE = "http://<YOUR_MAC_IP>:8000"`.

6. Build and deploy:

```bash
cd android
buildozer android debug deploy run
```

````

---
