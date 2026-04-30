import whisper

VALID_COMMANDS = {
    "I'm an idiot",
    "I'm little puppy for you",
    "I like eating poop",
    "I like losing in everything",
    "I'm would do that you say",
    "I'm your slave",
    "I'm the worst person in the world",
    "I'm stupid makaka",
    "ya dibil",
}

def run(prog, inp=""):
    try:
        cells = [0] * 30000
        ptr = 0
        iptr = 0
        out = ""
        code = prog.split(" ya kaka ")
        i = 0

        # Validate all commands upfront
        for cmd in code:
            if cmd not in VALID_COMMANDS:
                return "Error"

        while i < len(code):
            cmd = code[i]
            if cmd == "I'm an idiot":
                cells[ptr] = (cells[ptr] + 1) % 256
            elif cmd == "I'm little puppy for you":
                cells[ptr] = (cells[ptr] - 1) % 256
            elif cmd == "I like eating poop":
                out += chr(cells[ptr])
            elif cmd == "I like losing in everything":
                if iptr < len(inp):
                    cells[ptr] = ord(inp[iptr]) % 256
                    iptr += 1
                else:
                    cells[ptr] = 0
            elif cmd == "I'm would do that you say":
                ptr = (ptr + 1) % 30000
            elif cmd == "I'm your slave":
                ptr = (ptr - 1) % 30000
            elif cmd == "I'm the worst person in the world":
                if cells[ptr] == 0:
                    depth = 1
                    while depth > 0:
                        i += 1
                        if code[i] == "I'm the worst person in the world":
                            depth += 1
                        elif code[i] == "I'm stupid makaka":
                            depth -= 1
            elif cmd == "I'm stupid makaka":
                if cells[ptr] != 0:
                    depth = 1
                    while depth > 0:
                        i -= 1
                        if code[i] == "I'm stupid makaka":
                            depth += 1
                        elif code[i] == "I'm the worst person in the world":
                            depth -= 1
            elif cmd == "ya dibil":
                cells[:] = [0] * 30000
            i += 1
        return out
    except:
        return "Error"


if __name__ == "__main__":
    src = input("Файл или код: ").strip()
    if src[-4:] == ".mp3" or src[-4:] == ".wav":
        model = whisper.load_model("base")
        trans = model.transcribe(src)["text"]
        print(f"Код:\n{trans}")
        prog = trans
    else:
        prog = src
    print(run(prog, input("Инпут: ")))
