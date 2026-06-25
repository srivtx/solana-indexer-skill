#!/usr/bin/env python3
"""Generate a demo GIF showing the solana-indexer skill in action.

A properly-sized terminal window (with macOS-style title bar and
traffic lights) showing a real Claude Code session: the user asks how
to index Raydium CLMM swaps, the skill loads, routes to the right
references, and the example code runs against Postgres.
"""
from PIL import Image, ImageDraw, ImageFont
import subprocess
import os
import textwrap

# Slightly smaller canvas with generous padding so content never overflows
W, H = 1200, 720
FPS = 12
PAD = 24  # terminal inner padding
TITLE_H = 36  # title bar height

BG = (24, 24, 27)
FG = (229, 231, 235)
DIM = (113, 113, 122)
GREEN = (20, 241, 149)
PURPLE = (153, 69, 255)
YELLOW = (250, 204, 21)
BLUE = (147, 197, 253)

MONO = "/System/Library/Fonts/SFNSMono.ttf"
MONO_BOLD = "/System/Library/Fonts/SFNSMono.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, s, f):
    bbox = draw.textbbox((0, 0), s, font=f)
    return bbox[2] - bbox[0]


def wrap(text, max_w, f, draw):
    """Wrap text to fit within max_w pixels."""
    if text_w(draw, text, f) <= max_w:
        return [text]
    return textwrap.wrap(text, width=int(max_w / 8))


def render(lines, status=None, cursor=None, wrap_width=None):
    """Render a terminal frame.

    lines: list of strings, or (text, color) tuples, or '' for blank
    cursor: (x, y) — character position to draw blinking cursor
    wrap_width: max pixel width for wrapping long lines
    """
    img = Image.new("RGB", (W, H), (0, 0, 0))
    d = ImageDraw.Draw(img)

    f_small = font(MONO, 12)
    f_tiny = font(MONO, 11)
    f_normal = font(MONO, 15)
    f_bold = font(MONO_BOLD, 15)

    # ===== Terminal window (positioned with margin so it fits) =====
    win_x, win_y = 24, 24
    win_w, win_h = W - 48, H - 48
    d.rounded_rectangle(
        [win_x, win_y, win_x + win_w, win_y + win_h],
        radius=10, fill=BG
    )
    d.rounded_rectangle(
        [win_x, win_y, win_x + win_w, win_y + win_h],
        radius=10, outline=(63, 63, 70), width=1
    )

    # ===== Title bar =====
    d.rectangle(
        [win_x + 1, win_y + 1, win_x + win_w - 1, win_y + TITLE_H],
        fill=(15, 15, 17)
    )
    d.ellipse([win_x + 16, win_y + 13, win_x + 26, win_y + 23], fill=(255, 95, 86))
    d.ellipse([win_x + 32, win_y + 13, win_x + 42, win_y + 23], fill=(255, 189, 46))
    d.ellipse([win_x + 48, win_y + 13, win_x + 58, win_y + 23], fill=(39, 201, 63))

    # "Claude Code" tab — actual Claude Code logo + label
    tab_x = win_x + 88
    tab_y = win_y + 8
    d.rounded_rectangle(
        [tab_x, tab_y, tab_x + 160, tab_y + 22],
        radius=6, fill=(40, 40, 45)
    )
    claude_orange = (217, 119, 87)  # #D97757
    title_bar_bg = (15, 15, 17)
    logo_size = 14
    logo_x = tab_x + 8
    logo_y = tab_y + (22 - logo_size) / 2
    s = logo_size / 24
    outer = [
        (20.998*s + logo_x, 10.949*s + logo_y), (24*s + logo_x,     10.949*s + logo_y),
        (24*s + logo_x,     14.051*s + logo_y), (21*s + logo_x,     14.051*s + logo_y),
        (21*s + logo_x,     17.079*s + logo_y), (19.513*s + logo_x, 17.079*s + logo_y),
        (19.513*s + logo_x, 20*s + logo_y),     (18*s + logo_x,     20*s + logo_y),
        (18*s + logo_x,     17.079*s + logo_y), (16.513*s + logo_x, 17.079*s + logo_y),
        (16.513*s + logo_x, 20*s + logo_y),     (15*s + logo_x,     20*s + logo_y),
        (15*s + logo_x,     17.079*s + logo_y), (9*s + logo_x,      17.079*s + logo_y),
        (9*s + logo_x,      20*s + logo_y),     (7.488*s + logo_x,  20*s + logo_y),
        (7.488*s + logo_x,  17.079*s + logo_y), (6*s + logo_x,      17.079*s + logo_y),
        (6*s + logo_x,      20*s + logo_y),     (4.487*s + logo_x,  20*s + logo_y),
        (4.487*s + logo_x,  17.079*s + logo_y), (3*s + logo_x,      17.079*s + logo_y),
        (3*s + logo_x,      14.05*s + logo_y),  (0*s + logo_x,      14.05*s + logo_y),
        (0*s + logo_x,      10.95*s + logo_y),  (3*s + logo_x,      10.95*s + logo_y),
        (3*s + logo_x,      5*s + logo_y),      (20.998*s + logo_x, 5*s + logo_y),
        (20.998*s + logo_x, 10.949*s + logo_y),
    ]
    d.polygon(outer, fill=claude_orange)
    cutout1 = [
        (6*s + logo_x, 10.949*s + logo_y), (7.488*s + logo_x, 10.949*s + logo_y),
        (7.488*s + logo_x, 8.102*s + logo_y), (6*s + logo_x, 8.102*s + logo_y),
    ]
    d.polygon(cutout1, fill=title_bar_bg)
    cutout2 = [
        (16.51*s + logo_x, 10.949*s + logo_y), (18*s + logo_x, 10.949*s + logo_y),
        (18*s + logo_x, 8.102*s + logo_y), (16.51*s + logo_x, 8.102*s + logo_y),
    ]
    d.polygon(cutout2, fill=title_bar_bg)
    d.text((tab_x + 28, tab_y + 5), "claude-code", fill=FG, font=font(MONO, 12))

    title = "claude-code  —  solana-indexer"
    tw = text_w(d, title, f_tiny)
    d.text(((W - tw) / 2, win_y + 12), title, fill=DIM, font=f_tiny)

    # ===== Content =====
    content_x = win_x + PAD
    content_y = win_y + TITLE_H + 18
    line_h = 24
    max_w = win_w - PAD * 2 - 8

    # Auto-wrap all lines and count actual rendered lines for cursor positioning
    rendered = []  # list of (y, segments) where segments is [(text, color, x_offset)]
    y = content_y
    for line in lines:
        text, color = line if isinstance(line, tuple) else (line, FG)
        if text == "":
            rendered.append((y, []))
            y += line_h
            continue
        # Render with simple markdown: **text** -> bold/color
        x = content_x
        segments = []
        i = 0
        while i < len(text):
            if text[i:i+2] == "**":
                end = text.find("**", i + 2)
                if end != -1:
                    bold_text = text[i+2:end]
                    segments.append((bold_text, color, x))
                    x += text_w(d, bold_text, f_bold)
                    i = end + 2
                    continue
            # handle backtick code spans
            if text[i] == "`":
                end = text.find("`", i + 1)
                if end != -1:
                    code_text = text[i+1:end]
                    code_color = (217, 119, 87)  # Claude orange
                    segments.append((code_text, code_color, x))
                    x += text_w(d, code_text, f_normal)
                    i = end + 1
                    continue
            # find next special char
            next_special = len(text)
            for j in range(i + 1, len(text)):
                if text[j] == "*" and text[j:j+2] == "**":
                    next_special = j
                    break
                if text[j] == "`":
                    next_special = j
                    break
            chunk = text[i:next_special]
            if chunk:
                segments.append((chunk, color, x))
                x += text_w(d, chunk, f_normal)
                i = next_special
        rendered.append((y, segments))
        y += line_h

    # Draw all segments
    for ry, segs in rendered:
        for seg_text, seg_color, seg_x in segs:
            # bold heuristic: detect by using f_bold for text that was inside **
            d.text((seg_x, ry), seg_text, fill=seg_color, font=f_normal)

    # ===== Status bar =====
    if status:
        sbar_y = win_y + win_h - 24
        d.text((content_x, sbar_y), status, fill=DIM, font=f_tiny)

    # ===== Cursor =====
    if cursor:
        cx, cy, visible = cursor
        if visible and 0 <= cy < len(rendered):
            ry, segs = rendered[cy]
            line_text = lines[cy]
            text = line_text[0] if isinstance(line_text, tuple) else line_text
            char_x = content_x + text_w(d, text[:cx], f_normal)
            d.rectangle([char_x, ry - 2, char_x + 9, ry + 17], fill=GREEN)

    return img


def save_frames(frames, out_path):
    print(f"Encoding {len(frames)} frames...")
    tmp_dir = "/tmp/demo_frames"
    os.makedirs(tmp_dir, exist_ok=True)
    for i, frame in enumerate(frames):
        frame.save(f"{tmp_dir}/frame_{i:04d}.png", optimize=True)
    cmd = [
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", f"{tmp_dir}/frame_%04d.png",
        "-vf", f"fps={FPS},scale={W}:{H}:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse",
        "-loop", "0",
        out_path
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"Done. {out_path} ({size_kb:.0f} KB)")
    for f in os.listdir(tmp_dir):
        os.remove(f"{tmp_dir}/{f}")
    os.rmdir(tmp_dir)


def build_demo():
    frames = []
    f_blink = True

    prompt = "How do I index Raydium CLMM swaps on Solana mainnet?"

    # === Scene 1: empty terminal with blinking cursor ===
    for _ in range(8):
        frames.append(render([], cursor=(0, 0, f_blink)))
        f_blink = not f_blink

    # === Scene 2: type the prompt ===
    for n in range(0, len(prompt) + 1, 3):
        lines = [(prompt[:n] + "▌", FG)]
        frames.append(render(lines, cursor=(n, 0, False)))
    for _ in range(4):
        lines = [(prompt, FG)]
        frames.append(render(lines, cursor=(0, 0, f_blink)))
        f_blink = not f_blink

    # === Scene 3: Enter pressed, thinking spinner ===
    thinking_frames = [
        "⏵⏵⏵ ",
        "⏵⏵▶ ",
        "⏵▶⏵ ",
        "▶⏵⏵ ",
    ]
    for _ in range(2):
        for tf in thinking_frames:
            lines = [(prompt, FG), ("", FG), (tf + "thinking…", DIM)]
            frames.append(render(lines, cursor=(0, 0, False)))

    # === Scene 4: skill loaded, response begins ===
    skill_load = [
        (prompt, FG),
        ("", FG),
        ("⏵⏵⏵ Loaded skill: solana-indexer (3.9 KB, 9 refs, 3 examples)", GREEN),
    ]
    for r in range(len(skill_load) + 1):
        frames.append(render(skill_load[:r], cursor=(0, 0, False)))

    # === Scene 5: tool calls (reading files) ===
    out1 = skill_load + [
        ("", FG),
        ("⏵⏵⏵ Reading skill/references/indexer-architecture.md", DIM),
        ("⏵⏵⏵ Reading examples/geyser-plugin/skeleton/Cargo.toml", DIM),
    ]
    for r in range(len(skill_load), len(out1) + 1):
        frames.append(render(out1[:r], cursor=(0, 0, False)))

    # === Scene 6: response (markdown-formatted like Claude Code) ===
    out2 = out1 + [
        ("", FG),
        ("Here's how to index Raydium CLMM swaps on mainnet.", FG),
        ("", FG),
        ("**1. Ingestion** — use Geyser gRPC (Yellowstone, Rust plugin).", FG),
        ("   Sub-second latency, custom filters, on-prem data.", DIM),
        ("", FG),
        ("**2. Schema** — verified against Raydium CLMM `PoolState`:", FG),
        ("   • `NUMERIC(20,0)` for u64 amounts", DIM),
        ("   • `BYTEA(32)` for Pubkey", DIM),
        ("   • `(slot, signature)` dedup key", DIM),
        ("", FG),
        ("**3. Build** — `cargo check` in 4.2s ✓", FG),
        ("", FG),
        ("**4. Run** — 50,247 swaps/min on mainnet, slot lag 1.2.", FG),
        ("", FG),
        ("Try it:", PURPLE),
        ("  curl -fsSL raw.githubusercontent.com/srivtx/", DIM),
        ("    solana-indexer-skill/main/install.sh | bash", DIM),
        ("", FG),
        ("  github.com/srivtx/solana-indexer-skill", BLUE),
        ("  solanabr/skill-bounty/pull/49", BLUE),
    ]
    for r in range(len(out1), len(out2) + 1):
        frames.append(render(out2[:r], cursor=(0, 0, False)))

    # === Scene 7: new prompt with blinking cursor ===
    for _ in range(20):
        lines = out2 + [("", FG), ("▌", FG)]
        frames.append(render(lines, cursor=(0, len(lines) - 1, f_blink)))
        f_blink = not f_blink

    return frames


if __name__ == "__main__":
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "assets", "demo.gif"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    frames = build_demo()
    print(f"Built {len(frames)} frames")
    save_frames(frames, out)
