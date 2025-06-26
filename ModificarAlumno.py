import boto3

def lambda_handler(event, context):
    print(event)
    tenant_id = event['tenant_id']
    alumno_id = event['alumno_id']
    alumno_datos = event['alumno_datos']
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    alumno_actualizado = {
        'tenant_id': tenant_id,
        'alumno_id': alumno_id,
        'alumno_datos': alumno_datos
    }
    response = table.put_item(Item=alumno_actualizado)
    # Salida (json)
    return {
        'statusCode': 200,
        'message': 'Alumno modificado correctamente',
        'response': response
    }
