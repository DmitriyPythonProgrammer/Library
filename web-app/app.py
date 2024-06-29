from fastapi import FastAPI, applications
from fastapi.openapi.docs import get_swagger_ui_html
import os
from dotenv import load_dotenv
from routing.books import router as router_book
from routing.authors import router as router_authors


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdn.staticfile.net/swagger-ui/5.1.0/swagger-ui-bundle.min.js",
        swagger_css_url="https://cdn.staticfile.net/swagger-ui/5.1.0/swagger-ui.min.css")


def get_application() -> FastAPI:
    application = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")
    applications.get_swagger_ui_html = swagger_monkey_patch
    application.include_router(router_book)
    application.include_router(router_authors)
    return application


app = get_application()








