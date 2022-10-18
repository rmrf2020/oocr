from fastapi import FastAPI, Body, File
import ddddocr
import requests

app = FastAPI()
ocr = ddddocr.DdddOcr(show_ad=False)


@app.post("/identify/url")
async def identify_by_url(
        url: str = Body('', title='URL', embed=True)
):
    data = identify_url(url)
    return {
        "code": "0",
        "data": data
    }


@app.post("/identify/file")
async def identify_by_file(
        file: bytes = File()
):
    data = identify_file(file)
    return {
        "code": "0",
        "data": data
    }


def identify_file(file):
    return {
        "res": ocr.classification(file)
    }


def identify_url(url):
    response = requests.get(url)

    return {
        "res": ocr.classification(response.content),
        "cookie": response.cookies,
        "headers": response.headers
    }


# 在最下面加上 这一句
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
