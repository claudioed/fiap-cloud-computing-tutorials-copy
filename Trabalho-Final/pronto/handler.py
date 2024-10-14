import boto3
import json
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table_name = 'pedidos-pizzaria'
table = dynamodb.Table(table_name)

def handler(event, context):
    print(json.dumps(event))
    print(type(event))
    print(event.keys())

    pedido = {
             "pedido": "1234",
             "datetime": datetime.now(),
             "cliente": "rafael",
             "status": "pronto"

    }
    table.put_item(Item=pedido)

    return {
        'statusCode': 200,
        'body': json.dumps('Pedido incluido no dynamoDB')
    }