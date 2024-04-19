from dotenv import load_dotenv
import os
from ftplib import FTP, FTP_TLS
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse

app = FastAPI()

# Load variables from .env file
load_dotenv()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/download/{fileDownload}")
async def ftpDownload(fileDownload):

    FTP_HOST=os.getenv('FTP_HOST')
    FTP_USER=os.getenv('FTP_USER')
    FTP_PASS=os.getenv('FTP_PASS')

    # Conectando-se ao servidor FTP
    ftps = FTP_TLS(host=FTP_HOST, user=FTP_USER, passwd=FTP_PASS)
    ftps.set_debuglevel(1)
    ftps.set_pasv(True)
    ftps.prot_p()

    # Configura a pasta padrão de download
    ftps.cwd('/CMP')
    # Fazendo download de um arquivo do servidor
    with open(f'/tmp/{fileDownload}.gz', 'wb') as arquivo:
        ftps.retrbinary(f'RETR {fileDownload}', arquivo.write)

    # Fechando a conexão
    ftps.quit()

    pathFile = f'/tmp/{fileDownload}.gz'
    fileName = f'{fileDownload}.gz'
    
    try:
        print("Return file...")
        # return send_from_directory('/tmp', f'{fileDownload}.gz')
        return FileResponse(path=pathFile, filename=fileName)
        
    except:
        print("ERROR: Return file...")
        return {"msg": "Error, try again!!"}
