import logging
import azure.functions as func
import json
from confluence import process_page, get_space_homepage
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
        space_key = req_body.get("space_key")

        if not page_id and not space_key:
            return func.HttpResponse(
                "Missing 'page_id' or 'space_key' in request body",
                status_code=400
            )
        
        if space_key:
            logging.info(f"Fetching homepage for space: {space_key}")
            page_id = get_space_homepage(space_key, config)
            if not page_id:
                return func.HttpResponse(
                    f"Could not find homepage for space '{space_key}'",
                    status_code=404
                )

        process_page(page_id, config)

        return func.HttpResponse(
            f"✅ Page {page_id} and subpages converted and uploaded.",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
