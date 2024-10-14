import boto3
import json

client = boto3.client('s3')


def handler(event, context):
    print(json.dumps(event))
    print(type(event))
    print(event.keys())

    bucket=event["bucket"]
    chave=event["key"]

    # em-preparacao/1234-rafael
    parts = chave.split("/")
    dado_pedido = parts[1].split("-")

    pedido  = {
            "pedido" : dado_pedido[0],
            "cliente" : dado_pedido[1]
        }

    if "em-preparacao" in chave:
        sqs = SqsHandler('https://sqs.us-east-1.amazonaws.com/197771781826/em-preparacao-pizzaria')
        sqs.send(pedido)
    else :
        sqs = SqsHandler('https://sqs.us-east-1.amazonaws.com/197771781826/pronto-pizzaria')
        sqs.send(pedido)

    return ""