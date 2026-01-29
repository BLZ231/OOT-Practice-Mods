from pathlib import Path

INPUT = Path("build/ntsc-1.2/assets/text/message_data.enc.nes.h")
OUTPUT = Path("dumped_messages.txt")

def extract_msg_blocks(text):
    blocks = []
    i = 0
    while True:
        start = text.find("MSG(", i)
        if start == -1:
            break

        depth = 1
        j = start + 4
        while j < len(text) and depth > 0:
            if text[j] == "(":
                depth += 1
            elif text[j] == ")":
                depth -= 1
            j += 1

        blocks.append(text[start + 4 : j - 1])
        i = j

    return blocks

def decode(block):
    out = []
    i = 0
    while i < len(block):
        if block.startswith("ITEM_ICON(", i):
            end = block.find(")", i)
            icon = block[i+10:end]
            out.append(f"[Item Icon {icon}]")
            i = end + 1
        elif block.startswith("COLOR(", i):
            end = block.find(")", i)
            color = block[i+6:end]
            out.append(f"[Color {color}]")
            i = end + 1
        elif block.startswith("0x", i):
            val = int(block[i+2:i+4], 16)
            if val == 0x01:
                out.append("\n")
            elif 0x20 <= val <= 0x7E:
                out.append(chr(val))
            i += 4
        else:
            i += 1
    return "".join(out).strip()

text = INPUT.read_text(errors="ignore")
chunks = text.split("DEFINE_MESSAGE(")[1:]

with OUTPUT.open("w") as f:
    for chunk in chunks:
        msg_id = chunk.split(",", 1)[0].strip()

        msgs = extract_msg_blocks(chunk)
        if len(msgs) < 2:
            continue

        english = decode(msgs[1])

        f.write(f"{msg_id}\n")
        f.write(english)
        f.write("\n\n")

print("Dump complete.")
