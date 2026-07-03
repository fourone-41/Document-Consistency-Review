"""
Stanford 设计思维英语口语练习智能体
运行方式: python app.py
建议浏览器: Chrome 或 Edge（麦克风支持最好）
"""

import speech_recognition as sr
import gradio as gr

from scenarios import SCENARIOS
import agent
import stt
import tts

SCENARIO_KEYS = list(SCENARIOS.keys())

_WELCOME = [{"role": "assistant", "content": "👋 从左侧选择一个练习场景，AI 将用英文开场。祝练习顺利！"}]


# ── helpers ──────────────────────────────────────────────────────────────────

def _vocab_markdown(scenario_key: str) -> str:
    vocab = SCENARIOS[scenario_key]["key_vocab"]
    return "**本场景关键词**\n\n" + "\n\n".join(f"- `{v}`" for v in vocab)


def _process(user_text: str, history: list[dict], scenario_key: str):
    """Core LLM + TTS pipeline. Returns (new_history, audio_path, feedback)."""
    english, feedback = agent.chat(history, user_text, scenario_key)
    audio_path = tts.speak(english)
    new_history = history + [
        {"role": "user", "content": user_text},
        {"role": "assistant", "content": english},
    ]
    return new_history, audio_path, feedback


# ── event handlers ────────────────────────────────────────────────────────────

def on_scenario_change(scenario_key: str):
    """Reset conversation and play the AI opening line for the new scenario."""
    scenario = SCENARIOS[scenario_key]
    opening = scenario["opening_line"]
    audio_path = tts.speak(opening)
    initial_history = [{"role": "assistant", "content": opening}]
    return (
        initial_history,                    # chatbot
        audio_path,                         # ai_audio
        "",                                 # feedback_panel (clear)
        _vocab_markdown(scenario_key),      # vocab_display
        initial_history,                    # history_state
    )


def respond_voice(audio_tuple, history: list[dict], scenario_key: str):
    """Handle voice input from microphone."""
    if audio_tuple is None:
        return history, None, "", history

    try:
        user_text = stt.transcribe(audio_tuple)
    except sr.UnknownValueError:
        return history, None, "⚠️ 听不清，请重说一次，或使用下方文字输入框", history
    except sr.RequestError as exc:
        return history, None, f"⚠️ Google 语音识别网络错误: {exc}", history

    new_history, audio_path, feedback = _process(user_text, history, scenario_key)
    return new_history, audio_path, feedback, new_history


def respond_text(text: str, history: list[dict], scenario_key: str):
    """Handle text input (button or Enter)."""
    if not text.strip():
        return history, None, "", history, gr.update(value="")

    new_history, audio_path, feedback = _process(text.strip(), history, scenario_key)
    return new_history, audio_path, feedback, new_history, gr.update(value="")


# ── UI ────────────────────────────────────────────────────────────────────────

with gr.Blocks(title="Stanford 口语练习") as demo:

    gr.Markdown(
        "# 🎓 Stanford 设计思维 · 英语口语练习\n"
        "选择场景 → AI 开场 → 🎤 录音回复（或文字输入）→ 听 AI 回复 + 查看语言教练反馈"
    )

    history_state = gr.State([])

    with gr.Row():
        # ── Left panel ──────────────────────────────────────────────────────
        with gr.Column(scale=1, min_width=260):
            scenario_dropdown = gr.Dropdown(
                choices=SCENARIO_KEYS,
                value=SCENARIO_KEYS[0],
                label="🎯 练习场景",
            )
            with gr.Accordion("📚 本场景关键词", open=True):
                vocab_display = gr.Markdown("")

            gr.Markdown(
                "---\n"
                "**使用说明**\n\n"
                "1. 选择场景，AI 用英文开场\n"
                "2. 点击 🎤 录音，说完松开\n"
                "3. AI 自动回复 + 播放语音\n"
                "4. 查看下方中文教练反馈\n\n"
                "> 💡 推荐 Chrome / Edge 浏览器"
            )

        # ── Right panel ─────────────────────────────────────────────────────
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                label="对话记录",
                height=360,
                value=_WELCOME,
            )

            ai_audio = gr.Audio(
                label="🔊 AI 回复语音",
                autoplay=True,
                interactive=False,
            )

            feedback_panel = gr.Markdown("*开始对话后，这里会显示语言教练反馈...*")

            with gr.Row():
                mic_input = gr.Audio(
                    sources=["microphone"],
                    type="numpy",
                    label="🎤 语音输入（停止录音后自动提交）",
                    scale=1,
                )
                with gr.Column(scale=2):
                    text_input = gr.Textbox(
                        label="文字输入（按 Enter 或点发送）",
                        placeholder="也可以直接打字练习...",
                        lines=2,
                    )
                    send_btn = gr.Button("发送 ▶", variant="primary")

    # ── Event wiring ──────────────────────────────────────────────────────────

    scenario_dropdown.change(
        fn=on_scenario_change,
        inputs=[scenario_dropdown],
        outputs=[chatbot, ai_audio, feedback_panel, vocab_display, history_state],
    )

    mic_input.stop_recording(
        fn=respond_voice,
        inputs=[mic_input, history_state, scenario_dropdown],
        outputs=[chatbot, ai_audio, feedback_panel, history_state],
    )

    send_btn.click(
        fn=respond_text,
        inputs=[text_input, history_state, scenario_dropdown],
        outputs=[chatbot, ai_audio, feedback_panel, history_state, text_input],
    )

    text_input.submit(
        fn=respond_text,
        inputs=[text_input, history_state, scenario_dropdown],
        outputs=[chatbot, ai_audio, feedback_panel, history_state, text_input],
    )


if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        inbrowser=True,
        strict_cors=False,
    )
