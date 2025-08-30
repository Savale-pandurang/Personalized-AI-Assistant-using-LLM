import os
import time
import webbrowser
import pyttsx3
import speech_recognition as sr
from openai import OpenAI
import requests

# ------------------- CONFIG -------------------
DEEPSEEK_API_KEY = "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"
SERPAPI_KEY = "ced70450dd45419ca20f0140b1aed7bf5d5c16a088502a26857e8fc9f6b0fbf2"
# Initialize DeepSeek client
client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com/v1"
)

# ------------------- SPEAK FUNCTION -------------------
def speak(text):
    """Roz speaks aloud the given text (only clean text)."""
    engine = pyttsx3.init()
    clean_text = "".join(ch for ch in text if ch.isalnum() or ch.isspace() or ch in ".,!?")
    engine.say(clean_text)
    engine.runAndWait()

# ------------------- LISTEN FUNCTION -------------------
def listen():
    """Listen to the microphone and return recognized speech."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    try:
        text = recognizer.recognize_google(audio)
        print(f"👉 You said: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

# ------------------- SEARCH LOGIC -------------------
def search_web(query):
    """Fetch results from SerpAPI (Google Search)."""
    url = f"https://serpapi.com/search?q={query}&api_key={SERPAPI_KEY}"
    response = requests.get(url).json()
    results = response.get("organic_results", [])
    return results

def handle_search_results(results):
    """Print full results but speak only clean titles (no emoji/snippet)."""
    if not results:
        speak("I could not find anything.")
        return ""

    context_texts = []
    for idx, item in enumerate(results, 1):
        title = item.get("title", "No title")
        link = item.get("link", "")
        snippet = item.get("snippet", "")

        # Print full details in terminal
        print(f"🔍 {idx}. {title}\n   {snippet}\n   {link}\n")

        # Speak only the clean title
        speak(f"Result {idx}: {title}")

        # Collect text for DeepSeek context
        context_texts.append(f"{idx}. {title} - {snippet}")

    # Return combined context
    return "\n".join(context_texts)

# ------------------- AI RESPONSE -------------------
def ask_deepseek(user_text, context=""):
    """Send query to DeepSeek for a proper AI explanation with retry logic."""
    prompt = f"User asked: {user_text}\n\nHere are search results:\n{context}\n\nGive a clear helpful answer."

    for attempt in range(3):  # retry up to 3 times
        try:
            response = client.chat.completions.create(
                model="deepseek/deepseek-r1-0528-qwen3-8b:free",
                messages=[{"role": "user", "content": prompt}],
            )
            answer = response.choices[0].message.content
            print(f"\n🤖 Roz: {answer}\n")
            speak(answer)
            return
        except Exception as e:
            print(f"⚠️ Error (attempt {attempt+1}):", e)
            time.sleep(2)  # wait before retry
    speak("Sorry, something went wrong while answering.")

# ------------------- MAIN LOOP -------------------
def main():
    speak("Hello, I am Roz. How can I help you today?")
    while True:
        user_text = listen().lower()
        if not user_text:
            continue

        if "stop" in user_text or "exit" in user_text or "quit" in user_text:
            speak("Goodbye!")
            break

        if "search" in user_text or "find" in user_text or "google" in user_text:
            print("🔍 Searching the web...")
            search_results = search_web(user_text)
            if search_results:
                search_context = handle_search_results(search_results)
                ask_deepseek(user_text, search_context)
        else:
            # Normal query → just use AI
            ask_deepseek(user_text)

# ------------------- RUN -------------------
if __name__ == "__main__":
    main()
