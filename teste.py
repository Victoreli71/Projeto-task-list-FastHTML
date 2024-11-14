from fasthtml.common import FastHTML, serve

app = FastHTML()

@app.get("/")
def homepage():
    return "<h1>bem vindo ao meu site </h1>"

serve()
