must create your own .env file, with this format
CONFLUENCE_API_TOKEN=
CONFLUENCE_BASE_URL=
AZURE_STORAGE_CONNECTION_STRING=
AZURE_CONTAINER_NAME= (this one is not implemented yet, must be added through azure_blob.py, should not be difficult at all.

terminal 1:

cd

source .venv/bin/activate

func start

terminal 2:

cd

source .venv/bin/activate

curl -X POST http://localhost:7071/api/convert \
     -H "Content-Type: application/json" \
     -d '{"space_key": "INFRA"}'

Have tested with python 3.13 and it did not work, but 3.9.x should be fully compatible.
To do : make sure when the program is re-run through functions, it does not re-do the entire process aka do not duplicate data
