import logging
import azure.functions as func
import json
from confluence import process_page
from config import load_config

app = func.FunctionApp()

@app.function_name(name="ConvertPageToMarkdown")
@app.route(route="convert", auth_level=func.AuthLevel.FUNCTION)
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('⚙️ ConvertPageToMarkdown function processed a request.')

    try:
        config = load_config()
        req_body = req.get_json()
        page_id = req_body.get("page_id")

        if not page_id:
            return func.HttpResponse("Missing 'page_id' in request body", status_code=400)

        process_page(page_id, config)

        return func.HttpResponse(f"✅ Page {page_id} and subpages converted and uploaded.", status_code=200)

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
