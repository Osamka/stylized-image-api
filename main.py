from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

# 🔧 Stały opis kobiecej postaci
OPIS_KOBIETY = (
    "Młoda kobieta o delikatnych, regularnych rysach twarzy, które emanują spokojem i pewnością siebie. "
    "Jej cera jest jasna, gładka, z naturalnym, zdrowym rumieńcem. "
    "Włosy opadają prosto na ramiona – są jasnobrązowe, gęste i miękkie jak jedwab, z lekko wycieniowanymi końcówkami. "
    "Z przodu ma prostą, pełną grzywkę, która delikatnie sięga do linii brwi, nadając jej twarzy dziewczęcej świeżości. "
    "Jej oczy są duże i jasne – nawet jeśli nie widać dokładnego koloru, bije od nich uważność i łagodność. "
    "Usta są naturalne, lekko pełne, zrelaksowane – jakby była na chwilę zamyślona, ale zaraz gotowa do uśmiechu."
)

class PromptRequest(BaseModel):
    prompt: str

class ImageResponse(BaseModel):
    finalPrompt: str
    imageUrl: str

def zawiera_stylizacje_na_kobiecie(prompt: str) -> bool:
    stylizacja = ["kobieta", "modelka", "dziewczyna", "sylwetka damska", "postać kobieca"]
    return "stylizacja" in prompt.lower() and any(w in prompt.lower() for w in stylizacja)

@app.post("/generate-image", response_model=ImageResponse)
async def generate_image(req: PromptRequest):
    final_prompt = req.prompt
    if zawiera_stylizacje_na_kobiecie(req.prompt):
        final_prompt += " " + OPIS_KOBIETY

    # 🔄 W tym miejscu można podpiąć prawdziwe API do generowania obrazów
    # Na razie zwracamy przykładowy URL
    return {
        "finalPrompt": final_prompt,
        "imageUrl": "https://example.com/generated-image.jpg"
    }
